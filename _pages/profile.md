---
layout: single
title: "Profile"
permalink: /profile/
author_profile: true
classes: wide
---

I use GIS, remote sensing, and carbon modelling to understand forests and ecosystems and how they change over time. My professional experience includes carbon and restoration projects across Africa, Asia, and Latin America, with a particular focus on land-use change, deforestation, forest structure, and biomass estimation. I am interested in applying machine learning, deep learning, and satellite time-series analysis to multisource Earth observation data, while combining technical analysis with field observations and transparent, reproducible workflows. I am also experienced in communicating geospatial results to clients, project partners, researchers, and non-technical audiences.

## Experience

<div class="timeline">

  <div class="timeline__row">
    <div class="timeline__date">
      08/2024 – 04/2026<br>
      Zwolle, The Netherlands
    </div>

    <div class="timeline__body">
      <span class="timeline__role">GIS and Forestry Consultant</span>
      <span class="timeline__org">Form International</span>
    </div>
  </div>


  <div class="timeline__row">
    <div class="timeline__date">
      01/2024 – 06/2024<br>
      Utrecht, The Netherlands
    </div>

    <div class="timeline__body">
      <span class="timeline__role">Remote Sensing Intern</span>
      <span class="timeline__org">Acorn / Rabobank</span>
    </div>
  </div>


  <div class="timeline__row">
    <div class="timeline__date">
      04/2021 – 05/2022<br>
      Yogyakarta, Indonesia
    </div>

    <div class="timeline__body">
      <span class="timeline__role">Research Assistant</span>
      <span class="timeline__org">
        Faculty of Geography, Universitas Gadjah Mada
      </span>
    </div>
  </div>

</div>


## Education

{% assign logo_twente = site.static_files | where: "path", "/images/logos/university-of-twente.png" | first %}
{% unless logo_twente %}
  {% assign logo_twente = site.static_files | where: "path", "/images/logos/university-of-twente.svg" | first %}
{% endunless %}

{% assign logo_lund = site.static_files | where: "path", "/images/logos/lund-university.png" | first %}
{% unless logo_lund %}
  {% assign logo_lund = site.static_files | where: "path", "/images/logos/lund-university.svg" | first %}
{% endunless %}

{% assign logo_ugm = site.static_files | where: "path", "/images/logos/universitas-gadjah-mada.png" | first %}
{% unless logo_ugm %}
  {% assign logo_ugm = site.static_files | where: "path", "/images/logos/universitas-gadjah-mada.svg" | first %}
{% endunless %}


<div class="timeline timeline--edu{% unless logo_twente or logo_lund or logo_ugm %} timeline--nologo{% endunless %}">

  <div class="timeline__row">

    <div class="timeline__logo">
      {% if logo_twente %}
        <img src="{{ logo_twente.path }}"
             alt="University of Twente logo"
             loading="lazy">
      {% endif %}
    </div>

    <div class="timeline__date">
      08/2023 – 07/2024<br>
      Enschede, The Netherlands
    </div>

    <div class="timeline__body">

      <span class="timeline__role">
        MSc Geo-information Science and Earth Observation
      </span>

      <span class="timeline__org">
        University of Twente — Faculty of Geo-Information Science and Earth Observation (ITC)
      </span>

      <div class="timeline__education">

        <p>
          <strong>Thesis:</strong>
          <em>Assessment of Canopy Height Loss Using Sentinel-1 Time Series Data:
          A Case Study of Jambi Province, Indonesia</em>
        </p>

        <p class="timeline__small">
          Supervisors: Dr. Michael Schlund and Dr. Claudia Paris
        </p>

        <ul>
          <li>
            Analysed vegetation loss across land-use and land-cover classes using
            Sentinel-1 SAR time series, focusing on backscatter changes associated
            with vegetation structure.
          </li>

          <li>
            Investigated relationships between Sentinel-1A polarization and canopy
            height and developed a Python-based automated spatio-temporal workflow
            for canopy-height loss detection.
          </li>
        </ul>

      </div>
    </div>
  </div>


  <div class="timeline__row">

    <div class="timeline__logo">
      {% if logo_lund %}
        <img src="{{ logo_lund.path }}"
             alt="Lund University logo"
             loading="lazy">
      {% endif %}
    </div>

    <div class="timeline__date">
      08/2022 – 06/2023<br>
      Lund, Sweden
    </div>

    <div class="timeline__body">

      <span class="timeline__role">
        MSc Physical Geography and Ecosystem Science
      </span>

      <span class="timeline__org">
        Lund University — Faculty of Science
      </span>

      <span class="timeline__note">
        VG (Pass with Distinction)
      </span>

      <div class="timeline__education">
        <p><strong>Selected coursework:</strong></p>

        <ul>
          <li>Geographic Information Systems</li>
          <li>Advanced Geographic Information Systems</li>
          <li>Ecosystem Modelling</li>
          <li>Satellite Remote Sensing</li>
        </ul>
      </div>

    </div>
  </div>


  <div class="timeline__row">

    <div class="timeline__logo">
      {% if logo_ugm %}
        <img src="{{ logo_ugm.path }}"
             alt="Universitas Gadjah Mada logo"
             loading="lazy">
      {% endif %}
    </div>

    <div class="timeline__date">
      09/2016 – 11/2020<br>
      Sleman, Indonesia
    </div>

    <div class="timeline__body">

      <span class="timeline__role">
        BSc Geographic Information Science
      </span>

      <span class="timeline__org">
        Universitas Gadjah Mada — Faculty of Geography
      </span>

      <span class="timeline__note">
        GPA: 3.6/4.0 — Cum laude
      </span>

      <div class="timeline__education">

        <p>
          <strong>Thesis:</strong>
          <em>Understanding the Influence of Different Sampling Techniques and
          Sample Sizes on Accuracy Assessment of Land-Use Mapping in Parts of
          Salatiga, Indonesia</em>
        </p>

        <p class="timeline__small">
          Supervisor: Prof. Projo Danoedoro
        </p>

      </div>
    </div>
  </div>

</div>


## Technical Expertise

<div class="focus-grid">

  <article class="focus-card">

    <h3>Geospatial Data Processing</h3>

    <p>
      I work with raster, vector, LiDAR, SAR, optical, and field datasets for
      environmental and forest applications, including preprocessing, spatial
      analysis, classification, modelling, validation, and workflow automation.
    </p>

    <p>
      <strong>Python:</strong> Rasterio, GeoPandas, GEEMap, Matplotlib,
      TensorFlow, FilterPy
    </p>

    <p>
      <strong>R:</strong> sf, raster, lidR, TreeLS, ggplot2, rgeos,
      randomForest, MatchIt
    </p>

    <p>
      <strong>Image & point-cloud processing:</strong> SNAP, PolSARPro, ENVI,
      IDRISI, Fusion, and Agisoft Metashape
    </p>

  </article>


  <article class="focus-card">

    <h3>Google Earth Engine</h3>

    <p>
      I use Google Earth Engine for accessing and processing large Earth
      observation datasets and for developing scalable workflows for forest and
      land monitoring.
    </p>

    <p>
      My work includes satellite-data preprocessing, multisource data
      integration, image classification and regression, land-use and land-cover
      mapping, deforestation monitoring, and satellite time-series analysis.
    </p>

    <p>
      I have worked particularly with Sentinel-1, Sentinel-2, Landsat, and other
      Earth observation datasets for forest and carbon applications.
    </p>

  </article>


  <article class="focus-card">

    <h3>Time Series & Ecosystem Modelling</h3>

    <p>
      I use satellite time-series analysis to investigate vegetation dynamics,
      forest change, and temporal patterns that cannot be reliably captured from
      individual satellite observations.
    </p>

    <p>
      My experience includes Kalman filtering, temporal compositing,
      change-detection workflows, and analysis of optical and SAR satellite time
      series.
    </p>

    <p>
      I also have experience with ecosystem and vegetation modelling using
      <strong>TIMESAT</strong> and <strong>LPJ-GUESS</strong>.
    </p>

  </article>


  <article class="focus-card">

    <h3>Data Analysis & Visualization</h3>

    <p>
      I analyse and communicate spatial information through maps, statistical
      analysis, visualisation, and geospatial products designed for both technical
      and non-technical audiences.
    </p>

    <p>
      I work with <strong>QGIS</strong> and <strong>ArcGIS Pro</strong> for
      spatial analysis, cartography, geodatabase management, QA/QC, and map
      production.
    </p>

    <p>
      I also use Python and R for statistical analysis, model validation,
      accuracy assessment, uncertainty analysis, and reproducible data
      visualisation.
    </p>

  </article>

</div>
