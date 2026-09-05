---
title: "Sampling Design and Accuracy Assessment for Land-Cover Mapping"
excerpt: "How many reference samples a land-cover map needs, and how they should be distributed, tested against a full-area benchmark for 25- and 9-class schemes in Salatiga, Indonesia."
collection: portfolio
category: research
featured: false
date: 2024-01-29
publication_url: "https://doi.org/10.1117/12.3009445"
---

**Salatiga, Indonesia · BSc research, Universitas Gadjah Mada · First author · SPIE 2024**

## Research question

Thematic accuracy is reported as a property of a map, but it is really a property of the
map *and* the procedure used to measure it. Two decisions in that procedure are rarely
justified: how many reference samples to collect, and how to distribute them across the
scene. Both are usually settled by convention or by budget.

The study tested how far those two decisions move the estimated accuracy of a detailed
land-cover classification, and whether the answer changes when the classification becomes
more detailed.

## Study setup

| | |
| --- | --- |
| Study area | approximately **12 km²**, Salatiga, Indonesia |
| Imagery | WorldView-2, acquired **14 May 2018** |
| Resolution | 2 m original, resampled to **5 m** for analysis |
| Reference map | **2,621 polygons** across **25 land-cover classes** |
| Field observations | **367 samples** — 257 for reinterpretation, 110 for reference-map accuracy assessment |
| Class schemes compared | **25 classes** and **9 classes** |

The reference map was produced by visual interpretation and checked in the field; the
multispectral classification under test was produced independently of it. Aggregating the
25 classes into 9 gave a second, coarser scheme over the same area, so the effect of class
complexity could be isolated from every other variable.

## Method

Three sampling techniques were compared. They differ in what they control:

- **Random sampling** places points without constraint, so classes are represented roughly
  in proportion to their area only on average, and rare classes may be missed entirely in
  any single draw.
- **Stratified random sampling** allocates points per class before drawing them, so each
  mapped class contributes in proportion to its extent rather than by chance.
- **Systematic grid sampling** places points at fixed intervals, which guarantees spatial
  coverage but ties the sample to the geometry of the grid rather than to the distribution
  of the classes.

Each technique was repeated across progressively larger sample sizes — from **9 up to
4,608 samples** for the 9-class scheme, and from **25 up to 12,800 samples** for the
25-class scheme. Accuracy was assessed with an area-based approach in which each validation
location was represented by a **50 m buffer**, and overall accuracy was derived from a
confusion matrix.

The benchmark was not another sample. A full-area overlay between the classified map and
the reference map gave the actual accuracy: **52.76% for 9 classes** and **31.2% for 25
classes**. Every sampled estimate was then judged by whether it fell within **±2%** of that
value.

<figure>
  <img src="/images/diagrams/salatiga-accuracy-workflow.svg" alt="Workflow: a multispectral classification and a visual-interpretation reference are compared under three sampling designs at varying sample sizes, producing a confusion matrix and overall accuracy, which is examined against a full-area benchmark.">
  <figcaption>Assessment workflow, drawn from the method described in the publication.</figcaption>
</figure>

## Results

### How estimates behaved as sample size grew

For the 9-class scheme, estimates became comparatively stable at around **36 samples**. For
the 25-class scheme, roughly **200 samples** were needed before estimates began to settle
against the full-area benchmark. Below those sizes the estimated accuracy fluctuated
irregularly from draw to draw — the number returned depended as much on which points were
drawn as on the map being assessed.

These are the points at which the experiment began showing greater regularity under the
conditions tested. They are not statistically derived thresholds, and the paper does not
present them as universal sample sizes.

### How the sampling technique performed

For the 9-class scheme, **7 of 10** stratified-random scenarios fell within ±2% of the
actual accuracy, against **3 of 10** for random sampling and **2 of 10** for systematic
grid sampling. Stratification fluctuated least because sample allocation followed the
relative area of the mapped classes, so classes covering little ground still entered the
estimate instead of appearing or disappearing between draws.

For the 25-class scheme the same technique reached only **3 of 10**. Splitting the same
12 km² into 25 classes leaves many classes with small and fragmented extents, and the
estimation problem becomes harder for every technique, stratification included.

## Interpretation

The practical conclusion is not simply "collect more samples". The number required depends
on how many classes the legend carries, how evenly those classes are represented on the
ground, and how the samples are distributed among them. A sample size that is adequate for
a 9-class map can be well short for a 25-class map of the same area, and adding points at
random buys less stability than allocating them by class extent.

For anyone specifying an accuracy assessment, the useful step is to decide the sampling
design against the legend actually being validated, rather than adopting a fixed sample
size and reporting whatever figure it returns.

## Limitations

- A single, heterogeneous urban study area, and only two class schemes.
- The reference map is a visual interpretation, so it carries its own interpretation
  uncertainty; the benchmark is agreement with that map, not with ground truth.
- Overall accuracy from a confusion matrix was the primary agreement measure, rather than a
  wider set of agreement statistics.
- **36 and 200 samples are observations from this experiment, not universal thresholds.**

## Publication

Mahendra, W. K., & Danoedoro, P. (2024). *Understanding the influence of different sample
sizes and sample techniques on accuracy assessment of land cover mapping: Case study of
Salatiga City, Indonesia.* Proceedings of SPIE, Eighth Geoinformation Science Symposium,
12977, 129770E.
[https://doi.org/10.1117/12.3009445](https://doi.org/10.1117/12.3009445)

Presented as an oral presentation at the 8th Geoinformation Science Symposium, 2023.
Supervised by Prof. Projo Danoedoro. No public code repository accompanies this study.
