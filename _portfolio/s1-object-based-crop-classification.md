---
title: "Object-Based Crop Classification from Seasonal Sentinel-1 Time Series"
excerpt: "Exploring whether multi-period Sentinel-1 backscatter and object-based segmentation can support crop/non-crop classification in Google Earth Engine."
collection: portfolio
category: technical
featured: false
# date: NEEDS USER CONFIRMATION - the date the work was carried out is not
# established, so no date is published. Adding one here sets the ordering on
# /portfolio/ and displays the year on the project card.
gee_url: "https://code.earthengine.google.com/5f29a0390ddc8fbad9b742d577a6572f"
---

**Technical exploration · Google Earth Engine**

## Objective

To explore whether multi-period Sentinel-1 backscatter and object-based segmentation can
support crop/non-crop classification in Google Earth Engine.

## Why I explored it

The workflow brings together three things that are usually treated separately: summarising
a year of radar acquisitions into a small number of temporal composites, segmenting that
temporal stack into objects rather than classifying pixels, and training a classifier on
the resulting object-level values. This exploration was about establishing whether that
chain runs end to end in Earth Engine and what it produces.

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
  <figcaption>Processing chain implemented in the Earth Engine script.</figcaption>
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
- The three periods are fixed four-month windows, not derived from a crop calendar or
  observed phenology.
- Only VV information reaches the classifier; the VH signal is visualised but unused.
- The output is binary crop / non-crop — no crop type is distinguished.

## Tools

Google Earth Engine (JavaScript API), using `ee.Algorithms.Image.Segmentation.SNIC` for
segmentation, `reduceConnectedComponents()` for object-level statistics, and
`ee.Classifier.smileRandomForest` for classification.

## Source and executable analysis

The complete analysis is the Earth Engine script linked at the top of this page. It runs in
the Code Editor rather than being distributed as a repository, so there is no separate code
download.
