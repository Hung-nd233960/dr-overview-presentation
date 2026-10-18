# Digital Radiography: An Overview

Group presentation for Diagnostic Imaging, based on Seeram (2019) *Digital Radiography*, Ch. 1.

- `DR_Overview.pptx` / `.pdf`: the deck (15 content slides + title + references)
- `DR_Lab.html`: offline single-file lab with the Hook, the Warm-up (Radiologist Eye Test) and **X-ray Blackjack**
- `Script_EN_VI.*`, `Knowledge_Guide.*`, `Rehearsal_Checklist.md`, `sources.md`: presenter material
- `_build/`: scripts that generate the lab, figures, deck and documents (`engine.js` is the shared scoring/rendering engine)

## Deployment

Every push to `main` runs `.github/workflows/pages.yml`, which tests the scoring engine (`node _build/test_engine.js`), checks that the lab has no external URLs, and publishes the site (`site/index.html` plus the deliverables) to GitHub Pages.

## Rebuild locally

```bash
cd _build
node test_engine.js          # engine tests
python build_lab.py          # DR_Lab.html from lab_template.html + engine.js + base768.jpg
python make_figs.py          # slide figures (needs matplotlib, Pillow)
python build_docs.py         # script and guide .docx (needs python-docx)
node build_deck.js           # deck (needs pptxgenjs)
```

Image licence: base chest radiograph is CC0 (Wikimedia Commons). See `sources.md`.
