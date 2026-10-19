# Site source

Folders starting with `_` are not published by GitHub Pages.

- `src/content.py` – all English and Turkish copy
- `src/build.py` – builds the site: `cd _source/src && python3 build.py`, then copy `dist/` contents to the repo root
- `src/assets/` – styles, script, form endpoint (`config.js`), favicon, link-preview images
- `apps-script/Code.gs` – Google Apps Script that writes check-up requests to Google Sheets and emails them
