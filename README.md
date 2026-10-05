# Academic Homepage

A lightweight, responsive, single-page academic homepage built with Jekyll and hosted on GitHub Pages.
The earlier multi-page version is kept on the `multipage-backup` branch.

## Structure

- `index.html` — the homepage: introduction and all sections
- `_config.yml` — name (`author`), email, and site description
- `_layouts/default.html` — `<head>`, header, and footer
- `_includes/section.html` — renders one dated section from `_data/cv.yml`
- `_data/publications.yml` — publication list (newest first)
- `_data/cv.yml` — Research and Education sections
- `assets/fonts/` — self-hosted Newsreader and Hanken Grotesk (SIL OFL)
- `assets/katex/` — self-hosted KaTeX 0.19.0 (MIT) for inline `$...$` math

Shared presentation and interactions live in `styles.css` and `script.js`.

## Update the content

- Add papers to `_data/publications.yml`; your name is bolded automatically.
- Add entries to the sections in `_data/cv.yml`, or add a new section with its own `id`.
- The introduction and contact details are written directly in `index.html`.
- The CV linked from the homepage is `assets/Yifan_Li_CV.pdf`; replace that file to update it.
- An at-a-glance band (interests, reading groups, latest news) is kept in `index.html` inside a `{% comment %}` block; remove the wrapper to show it.

To add a portrait, upload an image to `assets/` and add an `img` element to the `home` section in `index.html`.

## Local preview

Requires Ruby. Install dependencies once, then serve:

```bash
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000`.

## Publishing

In repository **Settings → Pages**, use **Deploy from a branch**, with **main** and **/(root)** selected. GitHub Pages builds the Jekyll site automatically on every push.
