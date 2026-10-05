# Academic Homepage

A lightweight, responsive, multi-page academic portfolio built with Jekyll and hosted on GitHub Pages.

## Structure

- `_config.yml` — site title, your name (`author`), and default description
- `_layouts/default.html` — shared `<head>`, header, navigation, and footer
- `_layouts/page.html` — inner-page header (breadcrumb, eyebrow, title, lede)
- `_data/navigation.yml` — navigation links
- `_data/publications.yml` — publication list (newest first)
- `_data/cv.yml` — CV sections and entries
- `assets/fonts/` — self-hosted Newsreader and Hanken Grotesk (SIL OFL)

Pages:

- `index.html` — concise academic introduction
- `research/index.html` — interests and selected projects
- `publications/index.html` — rendered from `_data/publications.yml`
- `cv/index.html` — rendered from `_data/cv.yml`
- `contact/index.html` — contact details and academic profiles

Shared presentation and interactions live in `styles.css` and `script.js`.

## Customize the site

- Set your name once as `author` in `_config.yml`; it appears on the homepage, in the footer, and is bolded in publication author lists.
- Add papers to `_data/publications.yml` and CV entries to `_data/cv.yml`.
- Each page's title, description, eyebrow, and lede are in the front matter at the top of the file.
- Remaining placeholders: `YN`, `Your Institution`, research-project examples, and links using `href="#"`.

To add a portrait, upload an image to `assets/` and replace the `portrait-placeholder` element on the homepage with an `img` element.

## Local preview

Requires Ruby. Install dependencies once, then serve:

```bash
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000`.

## Publishing

In repository **Settings → Pages**, use **Deploy from a branch**, with **main** and **/(root)** selected. GitHub Pages builds the Jekyll site automatically on every push.
