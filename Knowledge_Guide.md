# Knowledge Guide — Digital Radiography: An Overview (Seeram 2019, Ch. 1)

*For presenters A–D. Read your own slides' sections twice, everyone else's once. Vietnamese key terms in brackets. Items marked ⚠ are still not checked against a second source. Items marked ✔ were verified on 2026-10-18 (sources in section 17).*

## 0. The one-page story

1. **Film** was detector, display and archive in one object, with a narrow useful exposure range. A wrong exposure meant a repeat and extra dose.
2. **Digital radiography (DR)** separates the jobs: **detector** (CR plate, indirect or direct flat panel) → **ADC** → **computer** → **display** → **PACS** storage and communication.
3. The digital detector responds **linearly over a very wide range**, so the computer can rescale brightness. Under-exposure shows as **noise**; over-exposure is **invisible**. That is the root of **dose creep**.
4. Defence: read the **Exposure Index (EI) / Deviation Index (DI)**, follow **ALARA**, run QA/QC.

## 1. Definition of DR (slide 2)

AAPM defines digital radiography as radiographic imaging technology producing digital projection images, using photostimulable storage phosphor (computed radiography, CR), amorphous selenium, amorphous silicon, CCD or MOSFET (CMOS) technology; it can give acceptable image quality over a wider range of exposures than film-screen radiography (Seeram §1.2, citing AAPM Report 116).
**Chain:** X-ray tube → patient → detector → **analog signal** → **ADC** → digital data → computer → digital image (numbers) → **DAC** → displayed image (Fig 1.1, 1.5).
*Medical imaging informatics* [tin học y tế hình ảnh] = IT applied to image acquisition, processing, display, storage and communication.
*Say it simply:* "The detector makes a signal, the ADC makes it numbers, the computer improves it, the DAC lets us see it."

## 2. Film-screen radiography (slide 3)

- Steps: X-rays pass through the patient and strike the film-screen cassette → **latent image** [ảnh ẩn] → **chemical processing** → viewed on a **viewbox** (Fig 1.2).
- **Film density** = blackening. **Film contrast** = difference in densities, which converts tissue contrast into film contrast.
- **Optical density (OD)** = log₁₀ (intensity of viewbox light / intensity of transmitted light). Measured by a densitometer.
- **Characteristic (H&D, Hurter–Driffield) curve** [đường cong đặc trưng] = OD plotted against log relative exposure (Fig 1.4):
  - **Toe**: underexposure, light image, OD ≈ 0.12–0.20 (base + fog).
  - **Straight-line portion (slope)**: useful, correct exposure, OD ≈ 0.3–2.2.
  - **Shoulder**: overexposure, dark image, OD ≈ 3.2.
- **Film speed = 1/E** (E = exposure needed): fast film needs less exposure. **Latitude** = range of exposures giving useful densities; wide-latitude film tolerates more error.
- Film is **detector + display + archive** in one object.

## 3. Exposure factors and image quality (slide 4)

| | kVp | mAs |
|---|---|---|
| Meaning | tube voltage: beam **quality**, penetrating power | tube current × time: beam **quantity**, number of photons |
| Main control of | **contrast** (low kVp → high contrast); grids also improve contrast by removing scatter | **noise** (low mAs → quantum mottle) |
| Dose | roughly ∝ kVp² at fixed mAs (approximation) | **directly proportional** to mAs |

- Higher kVp with lower mAs can reduce dose, but also lowers contrast ⚠ (state as a trade-off, not a rule).
- **AEC** (automatic exposure control) ends the exposure when a preset quantity reaches the detector: preset OD for film, preset **SNR** for digital.
- **Image quality** [chất lượng ảnh]: *spatial resolution* (detail, lp/mm; affected by focal-spot size, motion, receptor design), *contrast resolution* (differences in tissue contrast), *noise* (quantum mottle).
- **Quantum mottle**: grainy look from too few photons. Relative noise ∝ 1/√(number of photons) (this is the basis of our game's noise model).

## 4. Limits of film (slide 5)

1. **Wrong exposure → repeat → extra dose.** Narrow latitude. Film cannot show tissue-contrast differences below about 10% (limited contrast resolution).
2. **Fixed display**: optical range and contrast are set at exposure; changing them needs another exposure.
3. **Physical archive**: envelopes, large rooms, manual retrieval.
- Film's strength: **spatial resolution**, the highest of all modalities, about 5–15 lp/mm per Seeram.

## 5. Components of a DR system (slide 6)

1. **Data acquisition**: digital detector replaces the cassette. Some detectors convert X-rays to light then to electrical signal; others go straight to electrical signal.
2. **Computer data processing**: the computer uses **binary** (base 2: 0 and 1; **bits** = binary digits). *Example from the book:* EUCLID = `01000101 01010101 01000011 01001100 01001001 01000100` (verified: 8-bit ASCII).
3. **Display and post-processing**: output is converted by the **DAC** to an analog signal for the monitor. Post-processing (reduce noise, sharpen, change contrast, stitch images) turns the input into an output image that suits the viewer. **Grayscale mapping** is one common tool (Fig 1.6).
4. **Storage**: magnetic tape, disks, laser optical disks, **RAID** (redundant array of independent disks). Short-term archives are deleted after an institution-defined period.
5. **Communications**: **LAN** inside the hospital (intranet), **WAN** outside (internet). **PACS** + **RIS/HIS** integrated via **DICOM** and **HL7**. **Image compression**: *lossless (reversible)* loses no information; *lossy (irreversible)* does.
6. **Image and information management**: RIS and HIS hold text; PACS holds images.
- **IHE** (Integrating the Healthcare Enterprise): framework so DICOM and HL7 work together; origin 1998, RSNA + HIMSS; three elements: data model, actor, integration profile.

## 6. Computed radiography (slide 7)

- Photostimulable phosphor (e.g. **barium fluorohalide**, BaFBr:Eu²⁺ ✔ europium-doped; Seeram only says "barium fluorohalide") coated on an **imaging plate (IP)** in a cassette. Works with existing X-ray equipment. **Fuji, 1983.**
- **7 steps** (Fig 1.8): ① IP exposed: electrons move to higher energy states and stay **trapped** (latent image). ② Reader scans IP with a **laser** (red, e.g. HeNe 633 nm or diode 650–680 nm ✔): trapped electrons are released and **light is emitted** (blue-violet, peak ≈ 390 nm for BaFBr:Eu²⁺ ✔; the red laser light is filtered out before the PMT). ③ Light collected by a light guide → **photomultiplier tube (PMT)** → electrical signal → ADC. ④ Digital processor. ⑤ Display. ⑥ IP **erased** with bright light. ⑦ Reuse.
- CR exposure **dynamic range ≈ 10⁴ : 1** (Seeram writes "10⁴ times wider than the widest film-screen systems": see errata E1).
- **Spatial resolution** CR ≈ 3–5 lp/mm; film-screen ≈ 10–15 lp/mm (Seeram §1.6.1). **Contrast resolution** of CR is better and can be manipulated; film's is fixed.
- **DQE** (detective quantum efficiency) [hiệu suất lượng tử phát hiện] = how efficiently a detector converts incident X-ray information into useful image; formally DQE = SNR²out / SNR²in, between 0 and 1 and dependent on exposure and spatial frequency ✔. Higher DQE → same quality at lower dose. Seeram says CR DQE is much better than film's.
- **CR mechanism detail** ✔: X-rays create electron–hole pairs; electrons are captured in **F-centres** (bromine-vacancy traps, F(Br⁻)) and holes in V_K centres; the laser frees the electrons, which recombine and excite Eu²⁺, giving the ≈ 390 nm light. The hole-trap picture is still debated, so say "trapped in crystal defects" on stage.

## 7. Flat-panel detectors (slide 8)

| | Indirect | Direct |
|---|---|---|
| Layers | **Scintillator** (caesium iodide) → **photodiode array + TFT** (active-matrix) → glass support | **Photoconductor** (amorphous selenium) → **TFT array** |
| Steps | X-ray → **light** → electrical signal | X-ray → electrical signal (no light) |
| Variant | Scintillator + optics + **CCD** array (Fig 1.10) | none |

- Seeram says light "falls upon a matrix array of electronic elements": in practice **amorphous-silicon photodiodes with TFT switches** ✔.
- All flat panels: after readout the charges are cleared and the detector is ready again; **DQE** high; **spatial resolution** comparable to CR; no cassette handling.
- Light in a scintillator can spread sideways to neighbouring pixels (crosstalk, blur); structured (needle) CsI is the usual indirect choice and reduces this; direct a-Se has no light step, so its resolution is limited mainly by pixel size ✔. But indirect CsI/a-Si panels often have better DQE at moderate-to-high exposure (CsI absorbs X-rays well) ✔, so neither is simply "better".

## 8. Linear response and latitude (slide 9)

- Digital detectors (CR and FPD) output a signal **linear** with input exposure (Fig 1.11); film's response is the **S-shaped** H&D curve.
- Linear response → **wider exposure latitude** → acceptable image whether the input exposure is low or high, because brightness is **rescaled by software**.
- Under-exposed digital image → **noisy** (not dark). Over-exposed → **not visible** until the detector saturates. This is exactly the lesson of Activity 1 and 2.

## 9. EI, DI and dose creep (slide 12)

- **Exposure Index (EI)** [chỉ số phơi sáng]: standardized number (IEC 62494-1; AAPM TG-116) proportional to the **detector** air-kerma (EI = K × 100 µGy⁻¹, calibrated at RQA-5, 66–74 kVp) ✔. Each body part/view/site has a **target EI (EIT)**.
- **Deviation Index** DI = 10·log₁₀(EI/EIT) ✔. DI = 0 on target; **+3.0 = ×2 exposure**; −3.0 = ×½; ±1 ≈ one step on a standard mAs/AEC scale (ISO R5). +6 ≈ ×4.
- **TG-116 action guidance, as summarised by J. A. Seibert (IUPESM slides)** ✔: *target* DI −2 to +2; DI ≤ −2 (EI ≤ 63% of target): check noise, consult the radiologist on a repeat; +2 ≤ DI ≤ +3 (160–200%): investigate the cause, **do not repeat**; DI ≥ +3 (≥ 200%): consult the radiologist (check for saturation) and counsel the technologist. These are *suggestions*; sites set their own limits.
- **Caveat** ✔: EI is derived from the **detector signal; it is not patient dose**. The same EI on different systems may not mean the same image quality (DQE, scatter and beam quality differ).
- **Dose creep** [tăng liều dần]: gradual drift to higher exposures because overexposed digital images look fine. Counter: ALARA, EI/DI feedback, technologist training, QC.

## 10. Digital fluoroscopy and mammography (slide 13)

- **Conventional fluoroscopy**: X-ray tube → patient → **image intensifier** → optics → **TV camera or CCD** → TV monitor (Fig 1.12). **Digital fluoroscopy**: the camera output signal is digitized by the **ADC**; flat-panel detectors are being used too (Fig 1.13). Dynamic images (real time) vs static radiography.
- **DSA** (digital subtraction angiography): pre-contrast image subtracted from post-contrast images → only vessels remain. **Temporal subtraction** (in time) and **energy subtraction** (different kV).
- **Digital mammography**: CR, direct/indirect flat panels, CCD; digital post-processing; **CAD** (computer-aided detection) as a "second reader" for microcalcifications and malignant lesions; leads to **digital tomosynthesis** (Seeram Ch. 8–9).

## 11. PACS and informatics (slide 14)

- **PACS** = computer system for electronic storage and distribution of medical images, integrated with acquisition and display devices, linked to **RIS/HIS** (Seeram §1.7.1).
- Components (Fig 1.14): acquisition modalities (CT, MRI, CR, DR, US, nuclear medicine, film digitizers) → **interfaces** → **PACS computer** (database server + archive) → **display workstations** (diagnostic, high-resolution; review workstations for technologists) + **web access**.
- **DICOM** = images and their data; **HL7** = text from HIS/RIS. Data security is central.
- **Imaging informatics** (SIIM): study and application of processes of information and communications technology for acquisition, manipulation, analysis and distribution of image data.
- **Next era** (Seeram §1.9.2, 2017): **enterprise imaging** (HIMSS–SIIM), **cloud computing** (IaaS, PaaS, SaaS), **Big Data** (4 Vs: volume, variety, velocity, veracity), **machine learning** vs **deep learning** (DL needs no hand-made feature step), **artificial intelligence**.
- The **technologist as informaticist / PACS administrator**.

## 12. QA and QC (slide 15)

Aims: (1) patients exposed to minimum radiation, **ALARA**; (2) **optimum image quality** for diagnosis; (3) **reduce costs**. DR-specific QC examples: dark noise, exposure index calibration (AAPM, 2006).

## 13. How the games map to the physics

- **Noise model**: relative quantum noise ∝ 1/√photons, so image noise σ(r) = 0.12·(1/√r − 1) in our simulation (zero at r ≥ 1). This is a teaching simplification and is **exaggerated for projection**.
- **Quality** Q(r) = 100·√r for r < 1 (SNR ∝ √exposure); 100 for 1 ≤ r ≤ 4 (already diagnostic); falls slowly above 4× (detector saturation).
- **Cards chain:** each card multiplies the team's *last* scan, so ×6 then ×3 = ×18 of the start. This makes the game less predictable than a lookup of "initial × card" and keeps the fractional cards useful for correcting an overshoot. The **START image** appears as a reference column once any team has played, and each team's **history** shows the multiplier used under every image.
- **Dose** per exposure = 10·r, **+3** fixed cost per retake (repositioning, time, extra exposure). The +3 stops "deliberately under-expose first" from being a free strategy.
- **Why no exact 1× route exists**: the start is 1/8.33 ≈ 0.12× and the cards are ×⅙, ¼, ⅓, ½, 2, 3, 4, 6. The best route is ×3 → ×3 = 1.08× (score 178.4).
- **Verified top 3 routes** (exhaustive simulation of all sequences ≤ 4 cards, script in `_build/test_engine.js`): **×3 → ×3 = 178.4**, ×¼ → ×6 → ×6 = 176.9, ×2 → ×4 = 176.8.
- **Real limit of the model**: real SNR keeps rising with dose, but diagnostic value does not; the cap at 1× is a deliberate simplification.

## 14. Errata and cautions (do not repeat these as fact)

| # | Where | Issue | Say this instead |
|---|---|---|---|
| E1 | §1.6.1 | "Exposure latitude of CR is about 10⁴ times wider than film" is loose | Image plates/digital detectors respond linearly over about **10⁴ : 1**; film-screen only about 30 : 1 to 100 : 1 depending on film (sources vary ✔). Say "roughly 10,000 : 1 vs about 100 : 1 or less", not "10⁴ times wider" |
| E2 | §1.3.6 | "Dose ∝ square of kVp change" and "higher kVp → less dose" | Approximation at **fixed mAs**; higher kVp lowers dose only if mAs is reduced to keep detector exposure constant |
| E3 | §1.3.7 | Contrast-resolution comparison across modalities ("mm at 0.5% difference: 10, 20, 10, 4, 1") is confusing | **Not used** on our slides |
| E4 | §1.6.1 | "Cannon" | **Canon** |
| E5 | §1.6.2 | "matrix array of electronic elements" | **a-Si photodiodes + TFT switches** ✔ |
| E6 | Fig 1.1/1.5 | DAC needed for analog (CRT) monitors; modern displays take digital video | Keep the book's chain; if asked: "modern monitors accept digital signals, but 'numbers → visible image' is the same idea" |
| E7 | §1.6.1 | "electrons return to original orbit" is simplified | Laser releases electrons from F-centre traps; they recombine and excite Eu²⁺, which emits ≈ 390 nm light ✔ |
| E8 | §1.3.5 | Lists resolution, contrast, noise, distortion and artifacts as quality factors but explains only the first three | We use noise as the key link to the game; do not claim the book covers distortion/artifacts here |
| E9 | §1.3.7 | Film spatial resolution given as 5–15 lp/mm (§1.3.7) and 10–15 lp/mm (§1.6.1) | Say "about 5–15 lp/mm" |

## 15. Q&A bank (answers verified unless marked ⚠)

1. **Why doesn't an overexposed DR image look dark?** The detector is linear over a wide range and the software rescales the signal to a standard brightness; only the noise differs (less), until the detector saturates.
2. **Then why not always overexpose for a cleaner image?** Patient dose rises in proportion (ALARA); the extra SNR rarely adds diagnostic value. That is dose creep.
3. **CR vs flat panel: which is better?** Flat panel: immediate readout, higher DQE (same quality at lower dose), no cassette handling. CR: cheaper, uses existing rooms and portable cassettes. Spatial resolution comparable.
4. **Why does the light step matter (indirect vs direct)?** Light can spread sideways in the scintillator (crosstalk), which blurs; needle-structured CsI limits this. Direct a-Se has no light step, so resolution is limited mainly by pixel size. Indirect CsI panels often have better DQE at moderate-to-high exposure ✔.
5. **Why is CR's spatial resolution lower than film?** Seeram gives 3–5 lp/mm for CR. Commonly cited reasons are light spread in the phosphor layer during laser readout and the sampling pitch ⚠ (not checked in a primary source; say "commonly attributed to").
6. **What does DI = +6 mean?** About four times the target exposure at the detector. Per TG-116 guidance, ≥ +3 means consult the radiologist and counsel the technologist. **Is EI patient dose?** No: it is derived from the detector signal ✔.
7. **DICOM vs HL7?** DICOM: images and their metadata; HL7: text/administrative and clinical messages between HIS/RIS.
8. **Is lossy compression allowed for diagnosis?** Lossless keeps every value. Lossy only within professional/regulatory guidance that varies by modality and country. Do not quote a ratio.
9. **Why a DAC if the monitor is digital?** See E6.
10. **Can processing fix a badly underexposed image?** It can adjust brightness/contrast but cannot remove the quantum noise that comes from too few photons; a repeat may be needed.
11. **What does AEC measure in DR?** It ends the exposure when a preset signal (related to SNR) at the detector is reached.
12. **In the game, why the +3 per retake?** It represents the fixed cost of every repeat (time, repositioning, extra exposure) and keeps the strategy realistic.
13. **Is the game's image physically accurate?** No. It is a simplified model (additive Gaussian noise ∝ 1/√r, hard saturation above 4×) with exaggerated noise for the projector. The principle (grain when under-exposed, nothing visible when over-exposed) is real.
14. **Which patient got too much radiation in the hook?** Both did; only film showed it.

## 16. Self-check before presenting

- Can you say what ADC and DAC do, in one sentence each?
- Can you draw the H&D curve and name the three regions with OD values?
- Can you explain kVp vs mAs without notes?
- Can you list the 7 CR steps?
- Can you say why a direct detector has no "light" step?
- What does DI +3 mean? What is dose creep?
- Who clicks, who referees, who collects votes in Activity 2?

## 17. Verification log (2026-10-18)

| Claim | Result | Source |
|---|---|---|
| DI = 10·log₁₀(EI/EIT); +3 = 2×, −3 = ½× | ✔ | Seibert (IUPESM) slides summarising AAPM TG-116 and IEC 62494-1: https://iupesm.org/wp-content/uploads/2015/08/Dose-metrics-New-_Exposure-Index_-_-J.-Anthony-Seibert.pdf |
| DI action bands (target −2…+2; +2…+3 investigate; ≥ +3 consult; ≤ −2 check noise) | ✔ as summarised by Seibert (secondary to TG-116 itself; original PDF: https://law.resource.org/pub/us/cfr/ibr/inc/ansi/aapm.116.2009.pdf) | same |
| EI is detector exposure, not patient dose | ✔ | same |
| BaFBr:Eu²⁺, 633 nm laser, ≈ 390 nm emission, F-centre traps | ✔ | Storage Phosphors for Medical Imaging, PMC5448636: https://pmc.ncbi.nlm.nih.gov/articles/PMC5448636/ |
| DQE = SNR²out / SNR²in | ✔ | https://en.wikipedia.org/wiki/Detective_quantum_efficiency and lecture notes (Nishikawa 2003) |
| Indirect: light spread/crosstalk; direct: resolution limited by pixel size; CsI needles standard | ✔ | https://axisimagingnews.com/miscellaneous/flat-panel-dr-what-you-need-to-know ; https://howradiologyworks.com/direct-vs-indirect-digital-radiography/ |
| Digital detector dynamic range ≈ 1:10,000 vs screen-film ≈ 1:30 (other sources: film 10:1–100:1) | ✔ approximately; numbers vary by source | https://iupesm.org/wp-content/uploads/2014/08/02Seibert_CRDR.pdf and others |
| CR resolution lower because of laser scatter / sampling | ⚠ not verified | none |
| Higher kVp + lower mAs reduces dose but lowers contrast | ⚠ standard physics, not re-checked | Seeram §1.3.6 |
| Seeram's own wording and figures | read directly from `Material_CH1.pdf` | none |
