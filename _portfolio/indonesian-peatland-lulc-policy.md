---
title: "Three Decades of Land-Use Change Across Indonesian Peatlands"
excerpt: "Landsat time series from 1990 to 2020 across four peatland landscapes in Sumatra and Kalimantan, read against the chronology of Indonesian peatland regulation."
collection: portfolio
thumbnail: "/images/diagrams/peatland-lulc-policy-workflow.svg"
thumbnail_alt: "Workflow diagram: Landsat 1990-2020 is preprocessed and classified with Random Forest into multi-temporal land cover, which is compared alongside peat-depth information and the peatland policy chronology."
methods: "Landsat time series · Random Forest · land-use change"
category: research
featured: false
date: 2022-12-02
publication_url: "https://doi.org/10.1016/j.soisec.2022.100080"
---

**Sumatra and Kalimantan, Indonesia · Research Assistant, Faculty of Geography, Universitas Gadjah Mada · University of Sydney collaboration · Co-author · 2021–2022**

## Research question

Indonesia has issued a long sequence of peatland regulations. A regulation on paper does
not, by itself, show what happened to land cover on the ground, and the two are rarely
examined against each other over a period long enough to matter.

The main study asks how land use and forest cover changed across major peatland landscapes
between **1990 and 2020**, and how those trajectories align with the chronology of peatland
regulation. A second question concerns peat depth: whether forest conversion followed
different patterns on shallow and deep peat, since depth has long been one of the criteria
used to decide where cultivation is permitted.

The numerical results reported below are findings of the collaborative studies as a whole,
not of any single contribution.

## Study areas

Four peatland landscapes, spanning both major island groups:

- **Bengkalis Island**, Riau
- **Sungai Sugihan–Sungai Lumpur**, South Sumatra
- **Kubu Raya**, West Kalimantan
- **Central Kalimantan**

## Data

Observations were compiled at roughly five-year steps: **1990, 1995, 2000, 2005, 2010/2011
where applicable, 2015 and 2020**, using **Landsat 5 TM** and **Landsat 8 OLI** surface
reflectance. Cloud and cloud shadow were removed using the QA_PIXEL / CFMask masks, and the
remaining observations were reduced to a **median composite** for each step, which is what
makes a consistent 30-year series achievable in a persistently cloudy region.

## Land-use classification

Classification was implemented in **Google Earth Engine** using a **Random Forest**
classifier, into **seven LULC classes**: forest, plantation, agriculture, built-up, bare
soil, swampy bush and water body. Because each study area and each time step needs its own
training and its own model, the study produced **26 LULC classification models** in total.

## Linking land cover with peat depth and policy

The classified series was combined with two further layers of information. Forest-area
change was overlaid with **peat-depth information**, separated into **shallow peat (<3 m)**
and **deep peat (>3 m)**, because Indonesian peatland protection rules have historically
used depth as one criterion for whether an area may be cultivated. The resulting change
trajectories were then compared against a chronology assembled from an inventory of **130
peatland-related regulations**, of which the study reports **55% concerning environmental
issues, 33% socio-economic issues and 7% disaster prevention or mitigation**.

<figure>
  <img src="/images/diagrams/peatland-lulc-policy-workflow.svg" alt="Workflow: Landsat 5 TM and 8 OLI surface reflectance from 1990 to 2020 is cloud-masked and reduced to median composites, classified by Random Forest in Google Earth Engine into seven classes across 26 models, giving multi-temporal LULC and forest-change maps. These are overlaid with shallow and deep peat-depth information and compared against a chronology of 130 peatland regulations.">
  <figcaption>Primary workflow, redrawn from the methodology described in Widyatmanti et al. (2022). Not a reproduction of a published figure; the related Bengkalis peat-thickness study is deliberately excluded.</figcaption>
</figure>

## Change formulation

Land-use change is quantified from the classified series as a difference in mapped class
area between two dates:

$$ \Delta A_c = A_{c,t_2} - A_{c,t_1} $$

where $$A_{c,t}$$ is the mapped area of land-cover class $$c$$ at time $$t$$. A positive
$$\Delta A_c$$ means the class occupies more area at $$t_2$$ than at $$t_1$$ — expansion;
a negative value means contraction. Because the classes partition the same study area at
both dates, the expansions and contractions across all classes sum to approximately zero,
and a gain in one class is necessarily a loss somewhere else.

Absolute differences are hard to compare between landscapes of unequal size, so change is
also expressed relative to the starting area:

$$ R_c = \frac{A_{c,t_2} - A_{c,t_1}}{A_{c,t_1}} \times 100\% $$

A small class can post a large $$R_c$$ from a modest absolute change, so the two measures
are read together rather than separately.

Two cautions apply to both quantities. They are differences between two classifications, so
they carry the error of both maps, and a change in mapped area is not by itself evidence of
a change on the ground. And they are descriptive: neither expresses why a class changed, so
neither supports a causal reading of the policy chronology discussed below.

## Results

### The long-term trajectory

Forest cover declined strongly through the earlier part of the record, with the most
substantial conversion during the 1990s and 2000s. From around 2010 onwards the rate of
deforestation generally slowed and stayed low — but that summary holds for the record as a
whole, not for every landscape within it.

### Differences between landscapes

The four study areas did not follow one trajectory:

- **Bengkalis Island (2010–2020)** continued to lose forest on both depth classes:
  **44.92 km²** on shallow peat and **58.19 km²** on deep peat.
- **Kubu Raya (2011–2020)** lost only about **1.03 km²** of shallow-peat forest, following
  much larger conversion in earlier periods.
- **Central Kalimantan (2010–2020)** showed roughly **246.90 km²** of reforested area.

Together these show that a national-scale statement about slowing deforestation can conceal
continuing loss in one landscape and recovery in another. They are examples of that spatial
heterogeneity rather than a representative sample of Indonesian peatlands.

### Alignment with the policy chronology

Regulation became more specific over time, particularly following major climate and fire
events. The **2015–2020** period coincided with comparatively smaller LULC changes and a
slower overall deforestation rate. The study reports this as an association in time between
the regulatory record and the observed land-cover record; the design compares two
chronologies and does not isolate regulation from the other factors acting over the same
decades.

## Interpretation

Policy information and spatial evidence have to be read together. A large body of
regulation does not by itself demonstrate implementation, and a slowing national trend does
not demonstrate that any particular landscape is protected. What a 30-year classified series
adds is the ability to see where trajectories diverge, and when.

The study's practical conclusion is that peatland management is limited less by the number
of regulations than by the information available to apply them. Better mapping of peat
depth, hydrology, land capability and condition is the prerequisite, and the paper
recommends digital soil mapping as the route to it.

## Related peat-thickness study

A separate strand, on Bengkalis Island, tested whether spectral information could predict
peat thickness directly — using vegetation and wetness indices derived from spectral
transformations, with correlation and regression modelling evaluated by the standard error
of estimate.

Predictive performance was limited. The best NDWI-based approach reached approximately
**41.96%**, and vegetation indices and NDSI proved unreliable where vegetation and land
cover had themselves changed over the study period. The result is informative in a negative
direction: surface spectral response has limited ability to predict a subsurface property
such as peat thickness, which is consistent with the main study's conclusion that improved
peat mapping requires more than optical imagery. This analysis is not part of the
multi-temporal LULC workflow described above.

## Limitations

- A five-year observation interval does not capture short-term change between steps.
- Cloud cover forced some temporal substitutions, so not every study area has an
  observation in exactly the same year.
- The policy comparison is temporal and spatial evidence, not controlled causal inference.
- Peat-depth information carries its own uncertainty.
- The related spectral peat-thickness modelling had limited predictive performance and is
  reported as a preliminary result.

## Publications

Widyatmanti, W., Minasny, B., Awanda, D., Umarhadi, D. A., Fatma, Z. S. N., Mahendra, W. K.,
& Field, D. J. (2022). *Codification to secure Indonesian peatlands: From policy to
practices as revealed by remote sensing analysis.* Soil Security, 9, 100080.
[https://doi.org/10.1016/j.soisec.2022.100080](https://doi.org/10.1016/j.soisec.2022.100080)

Ambhika, N., Widyatmanti, W., Mahendra, W. K., Awanda, D., & Umarhadi, D. A. (2022).
*Remote sensing image analysis for identification of peat thickness using spectral
transformation approach: Case study of Bengkalis Island, Riau, Indonesia.* International
Journal of Geoinformatics, 18(2), 118–128.
[https://doi.org/10.52939/ijg.v18i2.2161](https://doi.org/10.52939/ijg.v18i2.2161)

No public code repository accompanies this work.
