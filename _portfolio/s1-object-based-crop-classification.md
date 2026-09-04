---
title: "Object-Based Crop Classification from Seasonal Sentinel-1 Time Series"
excerpt: "Testing whether multi-period Sentinel-1 VV/VH backscatter combined with SNIC object segmentation can separate crop from non-crop in Google Earth Engine."
collection: portfolio
category: technical
featured: false
date: 2026-09-04
gee_url: "https://code.earthengine.google.com/5f29a0390ddc8fbad9b742d577a6572f"
---

**Technical exploration · Google Earth Engine**

## Objective

Test whether multi-period Sentinel-1 VV and VH backscatter, summarised into seasonal
composites and segmented into image objects, can support a binary crop / non-crop
classification. The workflow is written end-to-end in Google Earth Engine and is runnable
from the link at the top of this page.

## Why I explored it

Crop mapping in the tropics is constrained by cloud cover, which limits how often optical
sensors return a usable observation. Sentinel-1 is unaffected by cloud, so the question is
how much can be recovered from radar backscatter alone. Two things seemed worth testing
together: whether a small number of wide seasonal windows carries enough of the growth
signal to separate cropland, and whether classifying image objects rather than individual
pixels produces a more coherent result from inherently speckled radar data.

## Dataset

- `COPERNICUS/S1_GRD` — Sentinel-1 Ground Range Detected
- Interferometric Wide (IW) acquisition mode
- Scenes carrying both VV and VH polarisation
- Restricted to a region of interest defined in the script
- Year: 2023

## Temporal design

The year is divided into three four-month windows rather than conventional three-month
calendar quarters:

| Period | Months |
| --- | --- |
| Q1 | January – April |
| Q2 | May – August |
| Q3 | September – December |

Within each period, ascending and descending acquisitions are handled separately, and a
temporal mean backscatter image is calculated for each orbit direction. The two are then
combined into a single composite per period.

## Technical workflow

<figure>
  <img src="/images/diagrams/s1-crop-classification-workflow.svg" alt="Workflow: Sentinel-1 GRD scenes are filtered to IW mode with VV and VH over a region of interest, split into three 2023 periods, averaged per orbit direction, and combined into composites; VV and VH temporal stacks feed a seasonal RGB visualisation and a SNIC segmentation of the VV stack; object-level mean VV values and crop/non-crop training points train a Random Forest of 50 trees, producing a crop/non-crop classification.">
  <figcaption>Processing chain implemented in the Earth Engine script.</figcaption>
</figure>

The composites are assembled into VV and VH temporal stacks, which are also rendered as
seasonal RGB visualisations — mapping the three periods to the three colour channels, so
that areas changing between seasons stand out from areas that do not.

## SNIC object segmentation

The VV temporal stack is segmented using SNIC (Simple Non-Iterative Clustering), which
groups neighbouring pixels with similar multi-temporal backscatter into objects. Mean VV
backscatter is then calculated per object using the connected-components output of the
segmentation, so the classifier sees one value per segment rather than per pixel.

## Random Forest classification

Crop and non-crop training points are sampled and used to train a Random Forest classifier
with 50 trees, which is applied to produce a binary crop / non-crop map.

## Outputs

- Seasonal RGB visualisations of VV and VH backscatter across the three periods
- A SNIC segmentation of the VV temporal stack
- Object-level mean VV backscatter
- A binary crop / non-crop classification

No accuracy figures are reported, because the script does not compute any — see
Limitations.

## Technical observations

The exploration is structural rather than quantitative: it establishes that the chain from
Sentinel-1 GRD through seasonal compositing, SNIC segmentation and object-level Random
Forest classification runs end-to-end within Earth Engine, and produces a crop / non-crop
surface from radar input alone. Whether that surface is *correct* is not established by
this script, and nothing here should be read as a validated result.

## Limitations

These are characteristics of an exploratory workflow, not defects, but they bound what the
output can be used for:

- **No independent validation is implemented.** The script contains no accuracy assessment,
  so no classification accuracy is reported and none should be inferred.
- **No explicit speckle filtering.** Radar speckle is not filtered before analysis; the
  temporal averaging and the object-level aggregation reduce it incidentally, but neither
  is a substitute for a speckle filter.
- **No explicit radiometric terrain correction or terrain flattening.** Backscatter is not
  corrected for terrain effects, so results in areas of relief should be treated with
  caution.
- **Ascending and descending observations are combined by averaging.** The two orbit
  directions view the surface from different geometries; averaging them mixes those
  geometries rather than modelling them separately.
- **The three periods are four-month windows**, not three-month calendar quarters, so they
  do not align with conventional seasonal or phenological definitions.
- The classification is binary crop / non-crop; no crop type is distinguished.

## Tools

Google Earth Engine (JavaScript API) — `ee.Algorithms.Image.Segmentation.SNIC` for
segmentation and a Random Forest classifier for the classification step.

## Source and executable analysis

The complete analysis is the Earth Engine script itself, linked at the top of this page.
It is executable in the Code Editor rather than distributed as a repository, so there is no
separate code download.
