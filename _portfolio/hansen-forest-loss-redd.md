---
title: "Long-Term Forest Loss Monitoring for REDD+ Using Google Earth Engine"
excerpt: "Annual tree-cover loss analysis with Hansen Global Forest Change, 2001–2023, mapping loss year and quantifying affected area across West Kalimantan, Indonesia."
collection: portfolio
category: technical
featured: false
date: 2025-09-01   # September 2025; day set only so Jekyll can sort - not a factual day
date_precision: month   # only the month is confirmed; suppresses day-level date metadata
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

To examine long-term tree-cover-loss dynamics within a defined region of interest by
mapping annual loss, quantifying affected area and evaluating annual and cumulative
temporal patterns from 2001–2023.

## Explore forest loss

{% include geo-map.html
   id="forest-loss-map"
   overlay="/assets/data/forest-loss/loss-year-100m.png"
   bounds="-0.923468,111.033566,-0.026949,112.303784"
   outline="/assets/data/forest-loss/west-kalimantan-roi.geojson"
   legend_title="Tree-cover loss year"
   legend_from="2001"
   legend_to="2023"
   caption="Year of detected tree-cover loss across the analysis extent. Colour encodes when loss was detected, not how much was lost. This is a 100 m web version of the analysis output, generalised for browser delivery; the analysis itself uses the native 30 m Hansen data. The dashed outline is the West Kalimantan provincial boundary, shown for geographic context." %}

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

All four figures come directly from the exported statistics: the total is the final
cumulative value, and the mean is that total divided by the 23 years.

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

## Dataset and workflow

- `UMD/hansen/global_forest_change_2023_v1_11` — Hansen Global Forest Change v1.11
- Bands used: `treecover2000`, `loss`, `lossyear`
- Loss-year codes run 1–23, where 1 corresponds to 2001 and 23 to 2023
- Analysis extent: the area covered by the exported layers, roughly 141 × 99 km (about
  14,000 km²) in **West Kalimantan (Kalimantan Barat), Indonesia**. The exported raster and
  the annual and cumulative statistics all describe this extent, not the whole province

*Study-area boundary: West Kalimantan provincial boundary derived from 2017 Kemendes
village-boundary data and dissolved to the province level. It is drawn on the map for
geographic context; the analysis covers the smaller extent described above.*

Hansen Global Forest Change identifies tree-cover loss rather than confirmed permanent
forest-to-non-forest conversion. Tree-cover loss may reflect several disturbance processes,
so additional land-cover and persistence information would be required for a
methodology-specific deforestation assessment.

<figure>
  <img src="/images/diagrams/hansen-forest-loss-workflow.svg" alt="Workflow: Hansen Global Forest Change bands treecover2000, loss and lossyear are masked to pixels with detected tree-cover loss and clipped to a region of interest, giving an annual loss map for 2001–2023. Pixel area is converted from square metres to hectares and summed per loss-year code, producing annual statistics, a cumulative running total, and GeoTIFF and CSV exports.">
  <figcaption>Processing chain implemented in the Earth Engine script.</figcaption>
</figure>

Pixels without detected tree-cover loss are masked out, and the loss-year layer is clipped
to the region of interest, giving a map of the year in which loss was detected. A list of
Hansen loss-year codes from 1 to 23 drives the per-year statistics.

### How annual area is calculated

Affected area is derived from `ee.Image.pixelArea()`, which returns pixel area in square
metres. Dividing by 10,000 converts it to hectares. For each Hansen loss-year code, the
hectare values are summed inside the region of interest, and the code is converted to its
calendar year — 1 to 2001, through to 23 to 2023. The script produces annual statistics
along with bar and line charts of the annual series.


### How cumulative area is calculated

Total affected area across 2001–2023 is calculated, along with a running cumulative area
that accumulates each year's loss in sequence, and a cumulative chart of that series.

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
- Results depend entirely on the region of interest supplied to the script.
- No REDD+ reference level or baseline emission estimate is calculated.

## Open in Google Earth Engine

The full workflow, including the export steps, is available in the Earth Engine Code
Editor via the link at the top of this page. It runs in the Code Editor rather than being
distributed as a repository, so there is no separate code download.
