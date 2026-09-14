# Academic Homepage

A lightweight, responsive academic portfolio hosted with GitHub Pages.

## Customize the site

Most content is in `index.html`. Search for these placeholders and replace them:

- `Your Name` and `YN`
- `Your Institution`
- `your research area`
- sample research projects
- sample publications and news
- placeholder links using `href="#"`

To add a portrait, upload an image to `assets/` and replace the `portrait-placeholder` element in `index.html` with an image.

## Files

- `index.html` — page content and structure
- `styles.css` — colors, typography, layout, and responsive design
- `script.js` — theme toggle and mobile navigation
- `assets/favicon.svg` — browser icon

## Local preview

Open `index.html` in a browser, or run a small static server:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Publishing

The repository is named for a GitHub Pages user site. In repository **Settings → Pages**, set the source to **Deploy from a branch**, choose **main** and **/(root)** if it is not already enabled.
