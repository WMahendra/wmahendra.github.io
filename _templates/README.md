# Page templates

Files here are **not** part of the built site (`_templates` is excluded in
`_config.yml`). They are starting points to copy from.

## Adding a Technical Exploration

1. Copy `technical-exploration.md` to `_portfolio/<short-slug>.md`.
2. Fill in the front matter. `category: technical` is what places it in the
   "Technical explorations" section of `/portfolio/`.
3. Delete any optional link line you do not have a real URL for. Buttons are
   rendered only for URLs that exist, so an absent field simply shows no button.
4. Delete any body section that does not apply - the structure is a guide, not a
   requirement.
5. Put figures in `images/projects/` and reference them as `/images/projects/<file>.png`.

The page appears on `/portfolio/` as soon as the file exists. To keep it out of
the site while drafting, add `published: false` to the front matter.

## Front matter reference (portfolio collection)

| Field | Required | Notes |
| --- | --- | --- |
| `title` | yes | |
| `collection: portfolio` | yes | |
| `category` | yes | `research`, `professional`, or `technical` |
| `date` | yes | Controls ordering (newest first) |
| `excerpt` | recommended | Shown under the title in listings |
| `featured` | no | `true` adds it to the "Featured work" section |
| `publication_url` | no | Renders a "View publication" button |
| `github_url` | no | Renders a "View code" button |
| `gee_url` | no | Renders an "Open in Google Earth Engine" button |
| `demo_url` | no | Renders an "Open demo" button |

Sections on `/portfolio/` render only when they contain at least one project, so
an unused category never shows an empty heading.
