---
title: "Long-Term Forest Loss Monitoring for REDD+ Using Google Earth Engine"
excerpt: "Annual tree-cover loss analysis with Hansen Global Forest Change, 2001–2023, mapping loss year and quantifying affected area across an analysis extent within West Kalimantan, Indonesia."
collection: portfolio
thumbnail: "/images/figures/hansen-annual-loss-chart.svg"
thumbnail_alt: "Bar chart of annual tree-cover loss in hectares from 2001 to 2023, computed from the Hansen loss-year band over the analysis extent within West Kalimantan."
methods: "Hansen loss-year · annual and cumulative area"
category: technical
featured: false
date: 2025-09-01   # September 2025; day set only so Jekyll can sort - not a factual day
date_precision: month   # only the month is confirmed; suppresses day-level date metadata
results_published: true
page_scripts:
  - /assets/lib/leaflet/leaflet.js
  - /assets/js/portfolio-viz.js
page_styles:
  - /assets/lib/leaflet/leaflet.css
gee_url: "https://code.earthengine.google.com/46d383bb33a5de1bf3abb4a49ce8cb88"
---

**Technical exploration · September 2025 · West Kalimantan, Indonesia · Hansen Global Forest Change, 2001–2023**

## REDD+ context

REDD+ projects require an understanding of where, when and how rapidly forest loss has
occurred within and around a project area. Historical forest-loss patterns can support
early baseline assessment, risk screening and the identification of periods or locations
experiencing elevated pressure.

This technical exploration uses Hansen Global Forest Change in Google Earth Engine to map
annual tree-cover loss from 2001–2023, quantify affected area by year and examine
cumulative change through time.

## Objective

To examine long-term tree-cover-loss dynamics within a defined analysis area by
mapping annual loss, quantifying affected area and evaluating annual and cumulative
temporal patterns from 2001–2023.

{% if page.results_published %}
## Explore forest loss

{% include geo-map.html
   id="forest-loss-map"
   overlay="/assets/data/forest-loss/loss-year-100m.png"
   bounds="-0.923468,111.033566,-0.026949,112.303784"
   outline="/assets/data/forest-loss/west-kalimantan-roi.geojson"
   legend_title="Tree-cover loss year"
   legend_from="2001"
   legend_to="2023"
   caption="Year of detected tree-cover loss across the analysis extent. Colour encodes when loss was detected, not how much was lost. This is a 100 m web version of the analysis output, generalised for browser delivery; the analysis itself uses the native 30 m Hansen data. The dashed outline is the West Kalimantan provincial boundary, shown for geographic context — it is not the analysis boundary." %}

Hansen Global Forest Change identifies tree-cover loss. Loss may result from several
disturbance processes and should not automatically be read as permanent
forest-to-non-forest conversion.

## Key results

<dl class="stat-row">
  <div><dt>Total loss 2001–2023</dt><dd>336,037 ha</dd></div>
  <div><dt>Peak year</dt><dd>2016<small>30,825 ha</small></dd></div>
  <div><dt>Lowest year</dt><dd>2007<small>5,146 ha</small></dd></div>
  <div><dt>Mean annual</dt><dd>14,610 ha</dd></div>
</dl>

All four figures come directly from the exported statistics and describe the analysis
extent within West Kalimantan, not the whole province. The total is the final cumulative
value, and the mean is that total divided by the 23 years.

## Annual tree-cover loss

{% include csv-chart.html
   id="annual-loss-chart"
   src="/assets/data/forest-loss/annual-loss.csv"
   x="year" y="loss_area_ha" type="bar"
   ylabel="Affected area (ha)"
   caption="Area of detected tree-cover loss per year, 2001–2023." %}

## Cumulative tree-cover loss

{% include csv-chart.html
   id="cumulative-loss-chart"
   src="/assets/data/forest-loss/cumulative-loss.csv"
   x="year" y="cumulative_loss_ha" type="line"
   ylabel="Cumulative area (ha)"
   caption="Running total of detected tree-cover loss, 2001–2023." %}
{% endif %}

## Dataset and workflow

- `UMD/hansen/global_forest_change_2023_v1_11` — Hansen Global Forest Change v1.11
- Bands used: `treecover2000`, `loss`, `lossyear`
- Loss-year codes run 1–23, where 1 corresponds to 2001 and 23 to 2023
- Study area: **an approximately 14,000 km² analysis extent within West Kalimantan
  (Kalimantan Barat), Indonesia** — roughly 141 × 99 km. All results on this page describe
  that extent, not the whole province

*West Kalimantan provincial boundary derived from 2017 Kemendes village-boundary data and
dissolved to the province level. It is drawn on the map for geographic context only and is
not the analysis boundary.*

Hansen Global Forest Change identifies tree-cover loss rather than confirmed permanent
forest-to-non-forest conversion. Tree-cover loss may reflect several disturbance processes,
so additional land-cover and persistence information would be required for a
methodology-specific deforestation assessment.

<figure>
  <img src="/images/diagrams/hansen-forest-loss-workflow.svg" alt="Workflow: Hansen Global Forest Change bands treecover2000, loss and lossyear are masked to pixels with detected tree-cover loss and clipped to a region of interest, giving an annual loss map for 2001–2023. Pixel area is converted from square metres to hectares and summed per loss-year code, producing annual statistics, a cumulative running total, and GeoTIFF and CSV exports.">
  <figcaption>Processing chain redrawn from the Earth Engine script used for this analysis.</figcaption>
</figure>

Pixels without detected tree-cover loss are masked out, and the loss-year layer is clipped
to the region of interest, giving a map of the year in which loss was detected. A list of
Hansen loss-year codes from 1 to 23 drives the per-year statistics.

### How annual area is calculated

Affected area is derived from `ee.Image.pixelArea()`, which returns pixel area in square
metres; dividing by 10,000 converts it to hectares. For a given loss year, the area is the
sum of the areas of every pixel whose loss-year band carries that year's code:

$$ A_y = \sum_{i \in R} a_i \, \mathbb{1}(L_i = y) $$

where $$a_i$$ is the area represented by pixel $$i$$, $$L_i$$ is that pixel's Hansen
loss-year code, $$R$$ is the region of interest, and $$\mathbb{1}(\cdot)$$ is the indicator
function — one when the condition holds, zero otherwise. The indicator is what the masking
step implements: pixels of other years, and pixels with no detected loss at all, contribute
zero. Because each pixel carries a single loss year, the annual series partitions the
detected loss and no area is counted twice.

### How cumulative area is calculated

The cumulative series is the running sum of the annual series from the start of the record
to year $$t$$:

$$ C_t = \sum_{y=2001}^{t} A_y $$

so $$C_t$$ is the total area on which loss had been detected at any point up to and
including $$t$$. It rises monotonically by construction: a year with little loss flattens
the curve but cannot lower it, because the quantity is accumulated detection, not standing
forest. Regrowth after a loss event is not subtracted, and a pixel that loses tree cover
once is counted once and never removed.

## Relevance to REDD+

Knowing when and where tree-cover loss occurred, and how the annual pattern changes,
supports early screening: identifying periods of elevated pressure, comparing activity
inside and around an area of interest, and deciding where more detailed assessment is
warranted.

This workflow does not provide a REDD+ reference level, baseline emissions, an
additionality assessment, a leakage assessment or a methodology-compliant deforestation
analysis. It is a screening step that precedes that work.

## Limitations

These describe the scope of the current workflow rather than faults in it.

- Hansen tree-cover loss does not automatically equal permanent deforestation.
- The workflow does not classify post-loss land cover.
- The workflow does not test whether forest conversion persists.
- Loss drivers are not attributed.
- The optional `treecover2000 >= 30%` baseline tree-cover mask is present in the script but
  is commented out, so **no baseline canopy threshold is applied** in the current version.
- No methodology-specific REDD+ forest definition is applied.
- Results describe the analysis extent used for this exploration, not the whole of West
  Kalimantan province, and depend entirely on that extent.
- No REDD+ reference level or baseline emission estimate is calculated.

## References

Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017).
Google Earth Engine: Planetary-scale geospatial analysis for everyone. *Remote Sensing of
Environment, 202*, 18–27.
[doi.org/10.1016/j.rse.2017.06.031](https://doi.org/10.1016/j.rse.2017.06.031)

Hansen, M. C., Potapov, P. V., Moore, R., Hancher, M., Turubanova, S. A., Tyukavina, A.,
Thau, D., Stehman, S. V., Goetz, S. J., Loveland, T. R., Kommareddy, A., Egorov, A., Chini,
L., Justice, C. O., & Townshend, J. R. G. (2013). High-resolution global maps of
21st-century forest cover change. *Science, 342*(6160), 850–853.
[doi.org/10.1126/science.1244693](https://doi.org/10.1126/science.1244693)

Data accessed as `UMD/hansen/global_forest_change_2023_v1_11` through the Earth Engine Data
Catalog.

## Open in Google Earth Engine

The full workflow, including the export steps, is available in the Earth Engine Code
Editor via the link at the top of this page. It runs in the Code Editor rather than being
distributed as a repository, so there is no separate code download.
