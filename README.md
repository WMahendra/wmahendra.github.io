# wmahendra.github.io

Source for the personal academic website of **William Kristam Mahendra** — GIS and forestry specialist working on geospatial analysis, remote sensing, and forest carbon.

Live site: <https://wmahendra.github.io/>

## About this site

The site is a static [Jekyll](https://jekyllrb.com/) website hosted on GitHub Pages, based on the
[Academic Pages](https://github.com/academicpages/academicpages.github.io) template
(itself derived from [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes)).

Current sections:

| Page | Path | Content |
| --- | --- | --- |
| Home | `/` | Research interests in tropical forest degradation, carbon, and geospatial intelligence |
| Profile | `/profile/` | Education, professional experience, and technical skills |
| Publications | `/publications/` | Peer-reviewed journal articles and conference papers |
| Projects | `/portfolio/` | Academic (`/academic/`) and professional (`/professional/`) project portfolios |
| CV | `/files/William Mahendra_CV.pdf` | Downloadable CV |

## Repository layout

```
_config.yml        Site-wide configuration (title, author, social links, collections)
_data/             Navigation and UI text
_pages/            Standalone pages (home, profile, publications, portfolio, sitemap, 404)
_publications/     One Markdown file per publication
_portfolio/        One Markdown file per project
_includes/         Reusable template partials
_layouts/          Page layouts
_sass/, assets/    Styles and compiled front-end assets
files/             Downloadable files (CV)
images/            Figures and photographs used across the site
```

## Adding content

- **Publication:** add a Markdown file to `_publications/` with front matter
  `title`, `collection: publications`, `category` (`manuscripts`, `conferences`, or `books`),
  `date`, `venue`, and `paperurl`.
- **Project:** add a Markdown file to `_portfolio/` with `title`, `collection: portfolio`,
  `category` (`academic` or `professional`), and `date`. Set `published: false` to keep a
  project as a draft — drafts are excluded from the built site.
- **Navigation:** edit `_data/navigation.yml`.

## Running locally

Requires Ruby with Bundler.

```bash
bundle install
bundle exec jekyll serve --livereload
```

The site is then available at <http://localhost:4000>.

Alternatively, with Docker:

```bash
docker compose up
```

## Deployment

Pushing to the default branch triggers the GitHub Pages build; no separate deployment step is
needed.

## License

Site content (text, figures, and photographs) © William Kristam Mahendra, all rights reserved.
The underlying template is distributed under the MIT License — see [LICENSE](LICENSE).
