---
layout: single
title: "Research Focus"
permalink: /research/
author_profile: true
---

<p class="hero__lead">
  Four areas I work on and want to develop further.
</p>

<div class="focus-grid">

  <article class="focus-card">
    <h2>Forest &amp; LULC Dynamics</h2>

    <p>
      Understanding when, where, and how LULC changes occur is a substantial part of the challenge, particularly when distinguishing forest degradation from outright deforestation. Satellite observations are often incomplete and can easily be confused with seasonal variation.
    </p>

    <p>
      Rather than comparing observations from specific dates, I use a satellite time-series approach, integrating optical and SAR measurements, particularly in regions where persistent cloud cover limits the availability of reliable optical observations.
    </p>
  </article>


  <article class="focus-card">
    <h2>Forest Structure &amp; Carbon</h2>

    <p>
      I am interested in how canopy height, vertical structure, and related biomass indicators can be measured reliably, as well as in understanding the uncertainty associated with those estimates. Low-biomass and structurally heterogeneous landscapes are particularly challenging because structural estimates are often weakest in these environments.
    </p>

    <p>
      I am interested in extending my work on forest structure and biomass using LiDAR and spaceborne observations such as GEDI, alongside SAR, optical imagery, and field measurements.
    </p>
  </article>


  <article class="focus-card">
    <h2>Geospatial Evidence for Nature-based Solutions</h2>

    <p>
      Forest-carbon and restoration activities depend on spatial evidence: which land is eligible, what the baseline was, and what has actually changed over time. These questions need to be answered in a form that can be understood, evaluated, and reproduced by people who did not produce the original analysis.
    </p>

    <p>
      My interest is in how geospatial analysis can be integrated into monitoring and environmental decision-making, and in what makes the resulting evidence transparent, reproducible, and auditable.
    </p>
  </article>


  <article class="focus-card">
    <h2>Reproducible Earth Observation Workflows</h2>

    <p>
      I believe that an analysis that cannot be re-run is difficult to trust. I develop processing workflows that are explicit from end to end, from data selection and preprocessing through to the final map, so that each step and its assumptions can be scrutinized rather than taken on faith.
    </p>

    <p>
      This includes machine learning for classification and regression, as well as automating repetitive processing, validation, and quality-control tasks so that analyses can be updated and re-run efficiently.
    </p>
  </article>

</div>

<style>

.focus-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-top: 30px;
}

.focus-card {
  border: 1px solid #dddddd;
  border-radius: 6px;
  padding: 24px;
  background: #ffffff;
}

.focus-card h2 {
  margin-top: 0;
  margin-bottom: 18px;
}

.focus-card p {
  text-align: justify;
  line-height: 1.7;
  margin-bottom: 14px;
}

.focus-card p:last-child {
  margin-bottom: 0;
}

@media (max-width: 768px) {
  .focus-grid {
    grid-template-columns: 1fr;
  }
}

</style>
