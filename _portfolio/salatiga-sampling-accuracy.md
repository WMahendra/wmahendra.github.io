---
title: "Sampling Design and Accuracy Assessment for Land-Cover Mapping"
excerpt: "How sample size and sampling technique change the measured accuracy of a land-cover map — Salatiga, Indonesia. First-author study, published by SPIE."
collection: portfolio
category: academic
date: 2024-01-29
---

**Salatiga, Indonesia · BSc research, Universitas Gadjah Mada · published by SPIE (2024)**

## Problem

A land-cover map is only accepted once its accuracy has been demonstrated, but the
accuracy figure itself depends on how it was measured. Two choices are rarely justified
in practice: how many reference samples to collect, and how to distribute them. This
study set out to measure how much those two choices move the reported accuracy of a
large-scale land-cover map.

## Data

- A multispectral classification, produced independently, as the map under test
- A visual interpretation of the same area, used as the reference
- Two class schemes of different complexity: **25 classes** and **9 classes**

## Method

Accuracy was assessed using an area-based approach, with a confusion matrix used to
derive overall accuracy. Three sampling techniques were compared — random sampling,
stratified random sampling, and systematic grid sampling — and each was repeated across
a range of sample sizes so that the accuracy value could be tracked as sample size grew.

<figure>
  <img src="/images/diagrams/salatiga-accuracy-workflow.svg" alt="Workflow: a multispectral classification and a visual-interpretation reference are compared under three sampling designs at varying sample sizes, producing a confusion matrix and overall accuracy, which is examined for the point at which accuracy stabilises.">
  <figcaption>Assessment workflow, drawn from the method described in the publication.</figcaption>
</figure>

## My contribution

First author of the resulting paper, with the work carried out as my BSc thesis at the
Faculty of Geography, Universitas Gadjah Mada, supervised by Prof. Projo Danoedoro.
I presented the study as an oral presentation at the 8th Geoinformation Science
Symposium in 2023. The paper is co-authored with my supervisor.

## Results

- Accuracy estimates became more stable at around **200 samples for the 25-class scheme**
  and **36 samples for the 9-class scheme**. Below those sample numbers, the study observed
  irregular fluctuation in the accuracy value.
- **Stratified random sampling** performed better than random and systematic grid sampling
  for estimating map accuracy.
- The more complex class scheme required the larger number of reference samples before the
  accuracy estimate settled.

These sample numbers are the points at which the study observed the accuracy estimate
becoming regular; the paper does not define them as statistically derived thresholds.

## Limitations

The study covers a single urban study area and two class schemes, so the sample sizes
reported are specific to that setting rather than universal thresholds. The reference
data is a visual interpretation, which carries its own interpretation error, and the
comparison is based on overall accuracy from a confusion matrix rather than a wider set
of agreement measures.

## Publication

Mahendra, W. K., & Danoedoro, P. (2024). *Understanding the influence of different sample
sizes and sample techniques on accuracy assessment of land cover mapping: Case study of
Salatiga City, Indonesia.* Proceedings of SPIE, Eighth Geoinformation Science Symposium,
12977, 129770E.
[https://doi.org/10.1117/12.3009445](https://doi.org/10.1117/12.3009445)

No public code repository accompanies this study.
