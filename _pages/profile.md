---
layout: single
title: "Profile"
permalink: /profile/
author_profile: true
classes: wide
---

Geospatial specialist working in GIS, remote sensing, geodatabase management and carbon
project calculation, with delivery experience across Africa, Latin America and Asia. I
apply machine learning and deep learning to multisource satellite data for land-use change,
deforestation and carbon calculation, and use FME for data integration. I combine technical
analysis with field observation, and I am used to explaining spatial results to clients,
partners and non-technical audiences.

## Experience

<div class="timeline">
  <div class="timeline__row">
    <div class="timeline__date">08/2024 – 04/2026</div>
    <div class="timeline__body">
      <span class="timeline__role">GIS and Forestry Consultant</span>
      <span class="timeline__org">Form International</span>
    </div>
  </div>
  <div class="timeline__row">
    <div class="timeline__date">01/2024 – 06/2024</div>
    <div class="timeline__body">
      <span class="timeline__role">Remote Sensing Intern</span>
      <span class="timeline__org">Acorn / Rabobank</span>
    </div>
  </div>
  <div class="timeline__row">
    <div class="timeline__date">04/2021 – 05/2022</div>
    <div class="timeline__body">
      <span class="timeline__role">Research Assistant</span>
      <span class="timeline__org">Faculty of Geography, Universitas Gadjah Mada</span>
    </div>
  </div>
</div>

## Education

{% assign logo_twente = site.static_files | where: "path", "/images/logos/university-of-twente.png" | first %}
{% unless logo_twente %}{% assign logo_twente = site.static_files | where: "path", "/images/logos/university-of-twente.svg" | first %}{% endunless %}
{% assign logo_lund = site.static_files | where: "path", "/images/logos/lund-university.png" | first %}
{% unless logo_lund %}{% assign logo_lund = site.static_files | where: "path", "/images/logos/lund-university.svg" | first %}{% endunless %}
{% assign logo_ugm = site.static_files | where: "path", "/images/logos/universitas-gadjah-mada.png" | first %}
{% unless logo_ugm %}{% assign logo_ugm = site.static_files | where: "path", "/images/logos/universitas-gadjah-mada.svg" | first %}{% endunless %}

<div class="timeline timeline--edu{% unless logo_twente or logo_lund or logo_ugm %} timeline--nologo{% endunless %}">
  <div class="timeline__row">
    <div class="timeline__logo">{% if logo_twente %}<img src="{{ logo_twente.path }}" alt="University of Twente logo" loading="lazy">{% endif %}</div>
    <div class="timeline__date">08/2023 – 07/2024</div>
    <div class="timeline__body">
      <span class="timeline__role">MSc Geoinformation Science and Earth Observation</span>
      <span class="timeline__org">University of Twente — Faculty of Geo-Information Science and Earth Observation (ITC)</span>
    </div>
  </div>
  <div class="timeline__row">
    <div class="timeline__logo">{% if logo_lund %}<img src="{{ logo_lund.path }}" alt="Lund University logo" loading="lazy">{% endif %}</div>
    <div class="timeline__date">08/2022 – 06/2023</div>
    <div class="timeline__body">
      <span class="timeline__role">MSc Physical Geography and Ecosystem Science</span>
      <span class="timeline__org">Lund University</span>
      <span class="timeline__note">VG (Pass with Distinction)</span>
    </div>
  </div>
  <div class="timeline__row">
    <div class="timeline__logo">{% if logo_ugm %}<img src="{{ logo_ugm.path }}" alt="Universitas Gadjah Mada logo" loading="lazy">{% endif %}</div>
    <div class="timeline__date">09/2016 – 11/2020</div>
    <div class="timeline__body">
      <span class="timeline__role">BSc Geographic Information Science</span>
      <span class="timeline__org">Universitas Gadjah Mada</span>
      <span class="timeline__note">Cum laude</span>
    </div>
  </div>
</div>

## Technical expertise

### Geospatial data processing
- **Python:** Rasterio, GeoPandas, GEEMap, Matplotlib, TensorFlow, FilterPy, Seaborn
- **R:** raster, lidR, TreeLS, sf, ggplot2, rgeos, randomForest, MatchIt
- Image processing software: SNAP, PolSARPro, ENVI, IDRISI
- LiDAR processing and visualisation using Fusion and Agisoft Metashape

### Google Earth Engine
- Data collection and preprocessing
- Image classification and regression
- Time-series analysis

### Time series and ecosystem modelling
- Intermediate proficiency in TIMESAT and LPJ-GUESS
- Satellite time-series analysis, and dynamic vegetation and ecosystem modelling

### Data analysis and visualisation
- QGIS and ArcGIS products
