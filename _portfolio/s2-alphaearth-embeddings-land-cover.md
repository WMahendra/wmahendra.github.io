---
title: "Comparing Sentinel-2 Spectral Features and AlphaEarth Satellite Embeddings for Land-Cover Classification"
excerpt: "Comparison of conventional Sentinel-2 spectral features and AlphaEarth learned satellite embeddings for three-class land-cover classification using the same training labels and Random Forest setup."
collection: portfolio
category: technical
featured: false
date: 2026-09-01   # September 2026; day set only so Jekyll can sort - not a factual day
date_precision: month   # only the month is confirmed; suppresses day-level date metadata
gee_url: "https://code.earthengine.google.com/67790a3f5d72a8c9a3c523bd1d9cd1eb"
earth_engine_app_url:   # left empty on purpose - no public Earth Engine App exists yet
---

**Technical exploration · September 2026 · Google Earth Engine · Sentinel-2 and Google Satellite Embedding V1, 2024**

## Research question

How does a land-cover classification built from selected Sentinel-2 spectral features
compare with one built from AlphaEarth Satellite Embeddings, when the same training
samples, the same three-class scheme and the same Random Forest classifier are used?

The question is deliberately narrow. It asks what changes when only the *feature
representation* changes, and it does not ask which dataset is better.

## Why compare these representations?

Supervised land-cover classification usually begins with feature engineering. An analyst
selects spectral bands, adds indices that are known to separate the target classes, and
hands that stack to a classifier. The choice is interpretable and cheap, but it is also a
decision made in advance about which parts of the signal matter.

Geospatial foundation models offer a different starting point. AlphaEarth Foundations
learns a compact representation of Earth-observation information and distributes it as an
annual embedding field, in which each pixel is described by many learned dimensions rather
than by measured reflectance (Brown et al., 2025). The practical question that follows is
whether such a representation can be dropped into an otherwise conventional supervised
workflow, replacing manually designed spectral features without changing anything else.

This exploration tests that substitution directly. It is not a sensor-versus-sensor
comparison: one side is a set of selected spectral measurements and two explicitly
constructed indices, the other is a set of learned geospatial features. The two are also
not fully independent, because the broader AlphaEarth representation is derived from
multiple Earth-observation sources that include optical observations. Any difference
between the two classifications therefore reflects how the information is *encoded*, not a
contest between two instruments.

## Data

**Sentinel-2.** The optical branch uses `COPERNICUS/S2_SR_HARMONIZED` surface reflectance
for 2024, filtered to the study geometry (Google Earth Engine, n.d.-a). Cloud and cirrus
are removed with the QA60 bitmask, reflectance is rescaled by dividing by 10,000, and the
filtered collection is reduced to an annual median composite clipped to the geometry.
Two indices are added to the composite:

- NDVI = (B8 − B4) / (B8 + B4), after Rouse et al. (1974)
- NDWI = (B3 − B8) / (B3 + B8), after McFeeters (1996)

The classification feature set is B2, B3, B4, B8, B11, B12, NDVI and NDWI — eight features
in total.

**Satellite embeddings.** The learned branch uses `GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL`
(Google Earth Engine, n.d.-b), filtered to 2024 and to the same geometry, mosaicked across
the annual collection and clipped. Every band returned by `bandNames()` is used as a
classification feature, so the classifier receives the full embedding rather than a
selected subset. These bands are embedding dimensions, not spectral measurements: they
carry no wavelength and no direct physical unit.

A note on spatial resolution is needed here. Both branches are sampled at 10 m, but that
scale is a sampling choice, not a property of every input. B2, B3, B4 and B8 are native
10 m Sentinel-2 bands, whereas B11 and B12 are native 20 m bands resampled to the sampling
scale. The Sentinel-2 feature stack is therefore a mixed-resolution stack presented at 10 m,
and fine detail in the SWIR features is not genuinely 10 m information.

## Comparison design

Three classes are mapped: forest (0), water (1) and bare soil (2). Three labelled
FeatureCollections — `forest`, `water` and `baresoil` — are each assigned the matching class
value and merged into one collection.

That merged collection is the single point of control in the experiment. The *same* labels
train both classifiers, both use `smileRandomForest` with 100 trees, and both sample their
predictors at 10 m. The only substantive difference between the two runs is what the
classifier sees: eight spectral and index features on one side, all available embedding
dimensions on the other.

Holding the labels and the classifier family constant makes the feature representation the
main methodological variable. It does not, however, make this a benchmark. The script
implements no train/test separation and no independent validation, so the design supports a
qualitative comparison of two outputs and nothing stronger.

## Classification workflow

<figure>
  <img src="/images/diagrams/s2-alphaearth-workflow.svg" alt="Two parallel branches. Left: Sentinel-2 SR Harmonized for 2024 is cloud and cirrus masked with QA60, reduced to an annual median composite, and reduced to the features B2, B3, B4, B8, B11, B12 plus NDVI and NDWI. Right: AlphaEarth Satellite Embeddings for 2024 are mosaicked into an annual embedding image and all embedding dimensions are kept. Both branches take the same merged training samples, train a Random Forest with 100 trees, and produce a forest, water and bare soil classification. The two classifications converge on a qualitative comparison of the outputs.">
  <figcaption>Method-only workflow. Both branches share the training samples and the classifier; only the feature representation differs. No accuracy assessment is part of this workflow.</figcaption>
</figure>

Random Forest is used on both sides because it tolerates high-dimensional, correlated
inputs without feature selection (Breiman, 2001) — a property that matters more on the
embedding side, where the feature count is large and the dimensions are not independently
meaningful. The whole workflow runs in the Earth Engine Code Editor (Gorelick et al.,
2017).

## Outputs

The script produces four layers:

1. a Sentinel-2 false-colour composite, B8 / B4 / B3, stretched 0.0–0.3, which renders
   vegetation in red and makes vegetated and non-vegetated surfaces easy to separate
   visually;
2. a visualisation of three selected embedding dimensions, A20 / A50 / A30, stretched
   −0.5 to 0.5. This is a view of the embedding feature space, not a spectral image: the
   colours show where the three chosen dimensions differ, and no wavelength or physical
   interpretation should be read into them;
3. a three-class Sentinel-2 classification, and
4. a three-class embedding classification,

both rendered with forest in green, water in blue and bare soil in brown.

No exported output from this workflow was available when this page was written, and no
figures of the classified maps are shown. The description above is therefore limited to
what the workflow generates. Nothing is claimed here about how the two classifications
differ spatially — that requires inspecting genuine outputs, and any such observation will
be added only once the exports exist.

## Interpretation

The comparison indicates what kind of question this design can and cannot answer.

The Sentinel-2 branch is fully interpretable. Each feature has a physical meaning, the two
indices encode known contrasts — vegetation vigour and open water — and a misclassification
can usually be traced back to a specific part of the spectrum or to the compositing step.
The embedding branch, in contrast, offers no comparable diagnostic path. Its dimensions
summarise spatial and temporal information learned from multiple sources, so a
misclassification cannot be attributed to a band or an index.

What the workflow does show is that the substitution is mechanically straightforward: an
annual embedding image can be passed to a conventional supervised classifier in place of a
hand-built spectral stack, with no change to the labels, the classifier or the sampling
scale. Whether that substitution is *worth* making is a separate question, and this
exploration does not answer it. Demonstrating that a foundation-model representation is
superior would require independent evaluation, and none is implemented here. The value of
the exercise is methodological: it isolates the feature representation as a variable and
sets up the comparison that a validated experiment would then measure.

## Limitations

These bound what the current workflow can support.

- Only three classes are evaluated: forest, water and bare soil.
- No independent validation dataset is implemented.
- The labelled collection used for training is not separated into a hold-out evaluation
  set.
- Quantitative classification performance therefore cannot be compared between the two
  branches, and no accuracy figure is reported or implied.
- Sentinel-2 and AlphaEarth represent fundamentally different feature spaces, so the two
  models are not competing on equal footing in any statistical sense.
- The Sentinel-2 branch uses six selected bands and two engineered indices, whereas the
  embedding branch uses all available learned dimensions — the feature counts and their
  construction are not comparable.
- The Sentinel-2 input is an annual median composite; the embedding is an annual learned
  representation. The two summarise the year in different ways.
- Embedding dimensions are not physically interpretable in the way optical bands are.
- This is not a fully independent sensor-to-sensor comparison, because the AlphaEarth
  representation incorporates optical observations among its sources.
- The experiment covers only the supplied study geometry; nothing here should be
  generalised to other landscapes without further testing.

## Next step

A quantitative version of this comparison would need independent validation samples drawn
separately from the training labels, a stratified train/test separation, and confusion
matrices for both branches, from which overall accuracy together with producer's and user's
accuracy per class could be derived. Class-wise F1 would summarise the per-class balance,
repeated train/test runs would show how far the results move with the sample draw, and
spatial cross-validation would guard against the optimism that follows from training and
testing on spatially adjacent pixels. None of these is implemented in the current script.

## References

Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32.
[doi.org/10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324)

Brown, C. F., et al. (2025). *AlphaEarth Foundations: An embedding field model for accurate
and efficient global mapping from sparse label data.* arXiv:2507.22291.
[arxiv.org/abs/2507.22291](https://arxiv.org/abs/2507.22291)

Google Earth Engine. (n.d.-a). [*Harmonized Sentinel-2 MSI: MultiSpectral Instrument,
Level-2A (SR)*](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED).
Earth Engine Data Catalog.

Google Earth Engine. (n.d.-b). [*Satellite Embedding V1
Annual*](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL).
Earth Engine Data Catalog.

Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017).
Google Earth Engine: Planetary-scale geospatial analysis for everyone. *Remote Sensing of
Environment, 202*, 18–27. [doi.org/10.1016/j.rse.2017.06.031](https://doi.org/10.1016/j.rse.2017.06.031)

McFeeters, S. K. (1996). The use of the Normalized Difference Water Index (NDWI) in the
delineation of open water features. *International Journal of Remote Sensing, 17*(7),
1425–1432. [doi.org/10.1080/01431169608948714](https://doi.org/10.1080/01431169608948714)

Rouse, J. W., Haas, R. H., Schell, J. A., & Deering, D. W. (1974). Monitoring vegetation
systems in the Great Plains with ERTS. *NASA Special Publication, 351*, 309–317.

## Source

The complete analysis is the Earth Engine script linked at the top of this page. It runs in
the Code Editor rather than being distributed as a repository, so there is no separate code
download, and no public Earth Engine App accompanies it.
