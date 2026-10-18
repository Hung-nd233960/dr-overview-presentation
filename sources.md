# Image and figure sources

Accessed 2026-10-18. Nothing was downloaded from the web except the license lookup below; the base radiograph was already in `Homework_1/presentation/images/` (taken earlier for the Chapter 2 project).

## Base image

| Item | Source | License |
|---|---|---|
| Chest PA radiograph (base for every simulated image) | "Chest Xray PA 3-8-2010.png", author Stillwaterising ("Own work"), Wikimedia Commons, https://commons.wikimedia.org/wiki/File:Chest_Xray_PA_3-8-2010.png | **CC0 1.0** (verified on the file page, 2026-10-18; no attribution required, credited anyway) |

## Slides

| Slide | Image / figure | Source | License / note |
|---|---|---|---|
| 1 | Film 4× and DR 4× chest images | Simulated by the group from the base image (`_build/gen_images.js`; film = sigmoid H&D model, DR = linear + saturation) | CC0-derived; labelled "simulated" |
| 2 | Imaging-chain diagram | Redrawn by the group from Seeram (2019) Fig 1.1 and 1.5 | Redrawn, no textbook pixels |
| 3 | H&D curve; film thumbnails (¼×, 1×, 4×) | Curve redrawn from Seeram (2019) Fig 1.4 (OD values from §1.3.2); thumbnails simulated from the base image | Redrawn / CC0-derived |
| 4 | kVp vs mAs table | Table by the group; content after Seeram §1.3.3–1.3.6 | — |
| 5 | Three cards | Group-made shapes; content after Seeram §1.3.7 | — |
| 6 | Six-block system diagram; EUCLID binary; low- vs high-contrast chest | Diagram redrawn from Seeram (2019) Fig 1.5; contrast pair = base image processed by the group (`presentation/images/cxr_lowc.png`, `cxr_highc.png`, made for Homework 1 Ch.2) | Redrawn / CC0-derived |
| 7 | CR 7-step cycle | Redrawn from Seeram (2019) Fig 1.8 | Redrawn |
| 8 | Indirect vs direct layer stacks | Redrawn from Seeram (2019) Figs 1.9, 1.10 | Redrawn |
| 9 | Film S-curve vs digital linear response | Matplotlib figure by the group, after Seeram (2019) Figs 1.4, 1.11 (`_build/make_figs.py`) | Own work |
| 10 | Four warm-up panels | Simulated from the base image (exposures 1×, ¼×, 3×, ½×) | CC0-derived |
| 11 | Start (≈0.12×) and ideal images; card chips; dose bar | Simulated from the base image; chips/bar group-made | CC0-derived |
| 12 | 1× and 3× images; DI scale bar | Simulated; DI scale drawn by the group. Bands: AAPM TG-116 action guidance as summarised in Seibert, IUPESM slides (https://iupesm.org/wp-content/uploads/2015/08/Dose-metrics-New-_Exposure-Index_-_-J.-Anthony-Seibert.pdf) | CC0-derived / own work |
| 13 | DSA subtraction diagram; mammography detector chips | Group-made shapes; content after Seeram §1.6.3–1.6.4 | — |
| 14 | PACS hub diagram | Redrawn from Seeram (2019) Fig 1.14 | Redrawn |
| 15 | Take-home cards | Group-made | — |

## Text sources

- Seeram E. *Digital Radiography: Physical Principles and Quality Control*, 2nd ed., Springer 2019, Ch. 1 (primary).
- Seibert JA. Dose metrics: exposure index. IUPESM teaching slides, 2015: https://iupesm.org/wp-content/uploads/2015/08/Dose-metrics-New-_Exposure-Index_-_-J.-Anthony-Seibert.pdf (EI/DI, TG-116 action guidance).
- Storage Phosphors for Medical Imaging, Materials 2011 (PMC5448636): https://pmc.ncbi.nlm.nih.gov/articles/PMC5448636/ (CR mechanism).
- Axis Imaging News, "Flat panel DR: what you need to know" and howradiologyworks.com (direct vs indirect). Textbooks by Bushberg and Bushong were **not** consulted; the group may add them if available.
- AAPM Report No. 116 (2009) and IEC 62494-1:2008 for EI / DI. DI bands on slide 12 verified 2026-10-18 against Seibert's TG-116 summary (a secondary source); a site may set its own limits. Verification log: Knowledge_Guide.md §17.

## AI declaration

Claude (Anthropic) assisted with planning, the game design, the scripting, the HTML lab and the slide drafting. The Blackjack scoring table was re-derived by exhaustive simulation (`_build/test_engine.js`). All content must still be checked by the group against the sources above.
