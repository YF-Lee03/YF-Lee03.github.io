# Academic Homepage

A lightweight, responsive, multi-page academic portfolio hosted with GitHub Pages.

## Pages

- `index.html` — concise academic introduction
- `research/index.html` — interests and selected projects
- `publications/index.html` — papers and preprints
- `cv/index.html` — education, experience, awards, and service
- `contact/index.html` — contact details and academic profiles

Shared presentation and interactions live in `styles.css` and `script.js`.

## Customize the site

Search the HTML files for these placeholders:

- `Your Name` and `YN`
- `Your Institution`
- research-project and publication examples
- placeholder links using `href="#"`

To add a portrait, upload an image to `assets/` and replace the `portrait-placeholder` element on the homepage with an `img` element.

## Local preview

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Publishing

In repository **Settings → Pages**, use **Deploy from a branch**, with **main** and **/(root)** selected.
