---
title: "Object-Based Crop Classification from Multi-Period Sentinel-1 Time Series"
excerpt: "Exploring whether multi-period Sentinel-1 backscatter and object-based segmentation can support crop/non-crop classification in Google Earth Engine."
collection: portfolio
thumbnail: "/images/diagrams/s1-crop-classification-workflow.svg"
thumbnail_alt: "Workflow diagram: Sentinel-1 GRD scenes are split into three periods of 2023, averaged per orbit, segmented with SNIC on the VV stack and classified with Random Forest into crop and non-crop."
methods: "SNIC segmentation · Random Forest (50 trees)"
category: technical
featured: false
date: 2024-04-14
gee_url: "https://code.earthengine.google.com/5f29a0390ddc8fbad9b742d577a6572f"
---

**Technical exploration · Google Earth Engine**

*Developed on 14 April 2024 as a technical exploration derived from my MSc thesis-related
work with Sentinel-1 radar time series.*

## Objective

To explore whether multi-period Sentinel-1 backscatter and object-based segmentation can
support crop/non-crop classification in Google Earth Engine.

## Why I explored it

This exploration grew out of the radar component of my MSc research, where I was working
with Sentinel-1 time-series data and exploring different ways to extract useful temporal
information from SAR imagery. Here, I tested an end-to-end workflow that combines
multi-period Sentinel-1 composites, object-based segmentation and Random Forest
classification in Google Earth Engine to explore crop/non-crop mapping.

## Dataset

- `COPERNICUS/S1_GRD` — Sentinel-1 Ground Range Detected
- Interferometric Wide (IW) acquisition mode
- Scenes carrying both VV and VH polarisation
- Filtered to a region of interest defined in the script
- Ascending and descending acquisitions handled separately
- Year: 2023

## Temporal design

The year is divided into three periods:

| Period | Date range |
| --- | --- |
| Period 1 | 1 January – 30 April 2023 |
| Period 2 | 1 May – 31 August 2023 |
| Period 3 | 1 September – 31 December 2023 |

Within each period, the ascending images are reduced to a temporal mean and the descending
images are reduced to a temporal mean separately. Those two mean images are then averaged
together to give a single composite for that period.

## Technical workflow

<figure>
  <img src="/images/diagrams/s1-crop-classification-workflow.svg" alt="Workflow: Sentinel-1 GRD filtered to IW mode with VV and VH over a region of interest, split into three 2023 periods; per period an ascending mean and a descending mean are computed and then averaged. The VV temporal stack feeds SNIC segmentation and object-level mean VV via reduceConnectedComponents; the VH temporal stack is used for RGB visualisation only. Merged crop and non_crop training points with a class property train smileRandomForest with 50 trees, producing a binary crop / non-crop classification.">
  <figcaption>Processing chain redrawn from the Earth Engine script used for this exploration.</figcaption>
</figure>

## Seasonal RGB visualisations

Two three-band composites are built, each mapping the three periods to the colour channels:

- **VV composite** — R / G / B = Period 1 VV, Period 2 VV, Period 3 VV
- **VH composite** — R / G / B = Period 1 VH, Period 2 VH, Period 3 VH

These are intended to visually highlight temporal differences in backscatter across the
year. They are a display aid: colour variation indicates that backscatter differs between
periods, and is not by itself evidence of change on the ground.

## SNIC object segmentation

SNIC (Simple Non-Iterative Clustering) segmentation is run on the complete three-period VV
stack — Period 1 VV, Period 2 VV and Period 3 VV. **VH is not used in the segmentation.**

SNIC groups neighbouring pixels into compact segments by combining their similarity in
feature space with their proximity in image space, growing regions from a regular grid of
seeds in a single pass rather than iterating to convergence (Achanta & Süsstrunk, 2017).
Applied to a temporal stack, the similarity is evaluated across all three periods at once,
so a segment is a patch that behaves consistently through the year rather than in any single
image. The practical effect for this workflow is that the classifier operates on field-like
units instead of individual pixels, which suppresses the speckle that dominates per-pixel
radar classification.

Object-level mean backscatter is then calculated from the VV temporal stack using the SNIC
cluster labels together with `reduceConnectedComponents()`, so that each segment carries a
single mean value per period rather than a per-pixel value.

## Random Forest classification

The classifier is trained on the **object-level VV features**. This is the important
distinction in this version of the script: VH contributes to the RGB visualisations only,
and is not part of the feature stack used for either segmentation or classification.

Training uses `crop` and `non_crop` feature collections, merged into a single collection,
with `class` as the training property. The classifier is `smileRandomForest(50)` — a Random
Forest of 50 trees.

A Random Forest fits many decision trees to bootstrap samples of the training data, with a
random subset of features considered at each split, and combines them by majority vote
(Breiman, 2001):

$$ \hat{y}(x) = \operatorname{mode}\{ T_1(x), T_2(x), \ldots, T_B(x) \} $$

where $$T_b(x)$$ is the class predicted for object $$x$$ by tree $$b$$, and $$B$$ is the
number of trees — here $$B = 50$$. Each tree is a weak, unstable classifier on its own;
averaging their votes cancels much of that instability, which is why the ensemble tolerates
the correlated, noisy features typical of radar data without prior feature selection.

Individual trees choose their splits by looking for subsets that are more homogeneous in
class than the node being split. Gini impurity measures that homogeneity:

$$ G = 1 - \sum_{k=1}^{K} p_k^2 $$

where $$p_k$$ is the proportion of training samples of class $$k$$ at the node and $$K$$ is
the number of classes. $$G$$ is zero when a node holds a single class and largest when the
classes are evenly mixed, so a split is preferred when it lowers the impurity of the
resulting nodes. For the binary crop / non-crop problem here, $$K = 2$$.

## Outputs

- Seasonal RGB composites of VV and of VH across the three periods
- A SNIC segmentation of the three-period VV stack
- Object-level mean VV backscatter
- A binary crop / non-crop classification

## Technical observations

The exploration is structural rather than quantitative. It establishes that the chain from
`COPERNICUS/S1_GRD` through per-period orbit-wise averaging, SNIC segmentation of the VV
stack and object-level Random Forest classification runs end to end in Earth Engine and
produces a crop / non-crop surface from radar input alone. Whether that surface is correct
is not established by this script, and no part of it should be read as a validated result.

## Limitations

These bound what the current output can be used for. They are the scope of an exploratory
workflow rather than defects in it.

- **No independent validation** is implemented.
- **No confusion matrix** is computed.
- **No accuracy assessment**, and therefore **no classification accuracy is reported** — none
  should be inferred.
- **No explicit speckle filtering** is applied.
- **No explicit radiometric terrain correction or terrain flattening** is applied.
- Ascending and descending observations are combined by averaging the two orbit-wise mean
  images, which mixes the two viewing geometries rather than modelling them separately.
- The workflow uses three fixed four-month periods and does not explicitly model crop
  calendars or phenological stages.
- Only VV information reaches the classifier; the VH signal is visualised but unused.
- The output is binary crop / non-crop — no crop type is distinguished.

## References

Achanta, R., & Süsstrunk, S. (2017). Superpixels and polygons using simple non-iterative
clustering. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition
(CVPR)*, 4651–4660.
[doi.org/10.1109/CVPR.2017.520](https://doi.org/10.1109/CVPR.2017.520)

Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32.
[doi.org/10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324)

Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017).
Google Earth Engine: Planetary-scale geospatial analysis for everyone. *Remote Sensing of
Environment, 202*, 18–27.
[doi.org/10.1016/j.rse.2017.06.031](https://doi.org/10.1016/j.rse.2017.06.031)

## Tools

Google Earth Engine (JavaScript API), using `ee.Algorithms.Image.Segmentation.SNIC` for
segmentation, `reduceConnectedComponents()` for object-level statistics, and
`ee.Classifier.smileRandomForest` for classification.

## Source and executable analysis

The complete analysis is the Earth Engine script linked at the top of this page. It runs in
the Code Editor rather than being distributed as a repository, so there is no separate code
download.
