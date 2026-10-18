# -*- coding: utf-8 -*-
p = '../Knowledge_Guide.md'
s = open(p, encoding='utf-8').read()


def rep(old, new):
    global s
    assert old in s, old[:70]
    s = s.replace(old, new)


rep("Items marked ⚠ are not yet checked against a second source: verify before presenting them as fact.*",
    "Items marked ⚠ are still not checked against a second source. Items marked ✔ were verified on 2026-10-18 (sources in section 17).*")
rep("(e.g. **barium fluorohalide**, BaFBr:Eu²⁺ ⚠ the Eu²⁺ detail is from Bushberg, not Seeram)",
    "(e.g. **barium fluorohalide**, BaFBr:Eu²⁺ ✔ europium-doped; Seeram only says \"barium fluorohalide\")")
rep("② Reader scans IP with a **laser**: trapped electrons are released and **light is emitted**.",
    "② Reader scans IP with a **laser** (red, e.g. HeNe 633 nm or diode 650–680 nm ✔): trapped electrons are released and **light is emitted** (blue-violet, peak ≈ 390 nm for BaFBr:Eu²⁺ ✔; the red laser light is filtered out before the PMT).")
rep("- **DQE** (detective quantum efficiency) [hiệu suất lượng tử phát hiện] = how efficiently a detector converts incident X-ray information into useful image; higher DQE → same quality at lower dose ⚠ formal definition DQE = SNR²out/SNR²in (Bushberg). CR DQE is much better than film's.",
    "- **DQE** (detective quantum efficiency) [hiệu suất lượng tử phát hiện] = how efficiently a detector converts incident X-ray information into useful image; formally DQE = SNR²out / SNR²in, between 0 and 1 and dependent on exposure and spatial frequency ✔. Higher DQE → same quality at lower dose. Seeram says CR DQE is much better than film's.\n- **CR mechanism detail** ✔: X-rays create electron–hole pairs; electrons are captured in **F-centres** (bromine-vacancy traps, F(Br⁻)) and holes in V_K centres; the laser frees the electrons, which recombine and excite Eu²⁺, giving the ≈ 390 nm light. The hole-trap picture is still debated, so say \"trapped in crystal defects\" on stage.")
rep("- Seeram says light \"falls upon a matrix array of electronic elements\": in practice **amorphous-silicon photodiodes with TFT switches** ⚠ (Bushberg).",
    "- Seeram says light \"falls upon a matrix array of electronic elements\": in practice **amorphous-silicon photodiodes with TFT switches** ✔.")
rep("- Light in a scintillator can spread sideways (blur); needle-like CsI structure reduces this; direct conversion avoids the light step ⚠ (Bushberg; do not overclaim sharpness).",
    "- Light in a scintillator can spread sideways to neighbouring pixels (crosstalk, blur); structured (needle) CsI is the usual indirect choice and reduces this; direct a-Se has no light step, so its resolution is limited mainly by pixel size ✔. But indirect CsI/a-Si panels often have better DQE at moderate-to-high exposure (CsI absorbs X-rays well) ✔, so neither is simply \"better\".")

a = s.index("- **Exposure Index (EI)**")
b = s.index("- **Dose creep** [tăng liều dần]")
s = s[:a] + """- **Exposure Index (EI)** [chỉ số phơi sáng]: standardized number (IEC 62494-1; AAPM TG-116) proportional to the **detector** air-kerma (EI = K × 100 µGy⁻¹, calibrated at RQA-5, 66–74 kVp) ✔. Each body part/view/site has a **target EI (EIT)**.
- **Deviation Index** DI = 10·log₁₀(EI/EIT) ✔. DI = 0 on target; **+3.0 = ×2 exposure**; −3.0 = ×½; ±1 ≈ one step on a standard mAs/AEC scale (ISO R5). +6 ≈ ×4.
- **TG-116 action guidance, as summarised by J. A. Seibert (IUPESM slides)** ✔: *target* DI −2 to +2; DI ≤ −2 (EI ≤ 63% of target): check noise, consult the radiologist on a repeat; +2 ≤ DI ≤ +3 (160–200%): investigate the cause, **do not repeat**; DI ≥ +3 (≥ 200%): consult the radiologist (check for saturation) and counsel the technologist. These are *suggestions*; sites set their own limits.
- **Caveat** ✔: EI is derived from the **detector signal; it is not patient dose**. The same EI on different systems may not mean the same image quality (DQE, scatter and beam quality differ).
""" + s[b:]

rep("| E1 | §1.6.1 | \"Exposure latitude of CR is about 10⁴ times wider than film\" is loose | CR/DR respond linearly over a dynamic range of about **10⁴ : 1**; film's useful latitude is far narrower ⚠ check Bushberg |",
    "| E1 | §1.6.1 | \"Exposure latitude of CR is about 10⁴ times wider than film\" is loose | Image plates/digital detectors respond linearly over about **10⁴ : 1**; film-screen only about 30 : 1 to 100 : 1 depending on film (sources vary ✔). Say \"roughly 10,000 : 1 vs about 100 : 1 or less\", not \"10⁴ times wider\" |")
rep("| E5 | §1.6.2 | \"matrix array of electronic elements\" | **a-Si photodiodes + TFT switches** ⚠ |",
    "| E5 | §1.6.2 | \"matrix array of electronic elements\" | **a-Si photodiodes + TFT switches** ✔ |")
rep("| E7 | §1.6.1 | \"electrons return to original orbit\" is simplified | Laser releases trapped electrons; recombination at activator sites emits light ⚠ (Bushberg) |",
    "| E7 | §1.6.1 | \"electrons return to original orbit\" is simplified | Laser releases electrons from F-centre traps; they recombine and excite Eu²⁺, which emits ≈ 390 nm light ✔ |")
rep("4. **Why does the light step matter (indirect vs direct)?** Light can spread in the scintillator (blur); CsI needle structure reduces it. Direct a-Se keeps charge localized ⚠.",
    "4. **Why does the light step matter (indirect vs direct)?** Light can spread sideways in the scintillator (crosstalk), which blurs; needle-structured CsI limits this. Direct a-Se has no light step, so resolution is limited mainly by pixel size. Indirect CsI panels often have better DQE at moderate-to-high exposure ✔.")
rep("5. **Why is CR's spatial resolution lower than film?** Laser light scatters in the phosphor during readout and sampling limits resolution ⚠ (Bushberg).",
    "5. **Why is CR's spatial resolution lower than film?** Seeram gives 3–5 lp/mm for CR. Commonly cited reasons are light spread in the phosphor layer during laser readout and the sampling pitch ⚠ (not checked in a primary source; say \"commonly attributed to\").")
rep("6. **What does DI = +6 mean?** About four times the target exposure.",
    "6. **What does DI = +6 mean?** About four times the target exposure at the detector. Per TG-116 guidance, ≥ +3 means consult the radiologist and counsel the technologist. **Is EI patient dose?** No: it is derived from the detector signal ✔.")

s += """
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
| Higher kVp + lower mAs reduces dose but lowers contrast | ⚠ standard physics, not re-checked | Seeram §1.3.6; Bushong |
| Seeram's own wording and figures | read directly from `Material_CH1.pdf` | none |
"""
open(p, 'w', encoding='utf-8').write(s)

q = '../sources.md'
t = open(q, encoding='utf-8').read()
t = t.replace("| 12 | 1× and 3× images; DI scale bar | Simulated; DI scale drawn by the group (bands are a teaching summary of AAPM TG-116) | CC0-derived / own work |",
              "| 12 | 1× and 3× images; DI scale bar | Simulated; DI scale drawn by the group. Bands: AAPM TG-116 action guidance as summarised in Seibert, IUPESM slides (https://iupesm.org/wp-content/uploads/2015/08/Dose-metrics-New-_Exposure-Index_-_-J.-Anthony-Seibert.pdf) | CC0-derived / own work |")
t = t.replace("⚠ The DI bands on slide 12 are a teaching summary; confirm exact thresholds before quoting them as official.",
              "DI bands on slide 12 verified 2026-10-18 against Seibert's TG-116 summary (a secondary source); a site may set its own limits. Verification log: Knowledge_Guide.md §17.")
t = t.replace("(supplementary; ⚠ items in Knowledge Guide still to be checked in the book itself)",
              "(supplementary; not read directly. Equivalent facts were verified in open sources, see Knowledge Guide §17)")
open(q, 'w', encoding='utf-8').write(t)
print('patched')
