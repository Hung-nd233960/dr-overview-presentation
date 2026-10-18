const pptxgen = require('pptxgenjs');
const path = require('path');
const FIG = path.join(__dirname, 'fig') + path.sep;
const OLD = path.join(__dirname, '..', '..', 'presentation', 'images') + path.sep; // read-only reuse of Ch.2 CXR variants
const NAVY = '14325C', TEAL = '1FB5A8', AMB = 'F2B134', RED = 'E2574C', GRN = '3FBF6B', INK = '1B2B3A', MUTE = '5A6B7D', PALE = 'EAF1F8', WHITE = 'FFFFFF', TEALD = '0E7C74';

const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.33 x 7.5
pres.title = 'Digital Radiography: An Overview';
pres.author = 'Group (A-D)';
pres.theme = { headFontFace: 'Cambria', bodyFontFace: 'Calibri' };
const HF = 'Cambria', BF = 'Calibri';

let SN = 0;
function base(titleText, srcText, notes) {
  SN++;
  const s = pres.addSlide();
  s.background = { color: WHITE };
  s.addText(titleText, { x: 0.5, y: 0.3, w: 12.3, h: 0.8, fontFace: HF, fontSize: 30, bold: true, color: NAVY, valign: 'middle', margin: 0, isTextBox: true });
  s.addText(srcText, { x: 0.5, y: 7.02, w: 11.6, h: 0.3, fontFace: BF, fontSize: 10, color: MUTE, margin: 0, valign: 'middle', isTextBox: true });
  s.addText(String(SN), { x: 12.3, y: 7.02, w: 0.5, h: 0.3, fontFace: BF, fontSize: 10, color: MUTE, align: 'right', margin: 0, isTextBox: true });
  if (notes) s.addNotes(notes);
  return s;
}
function box(s, x, y, w, h, text, o = {}) {
  s.addText(text, {
    x, y, w, h, shape: pres.ShapeType.roundRect, rectRadius: 0.08,
    fill: { color: o.fill || PALE }, line: o.line ? { color: o.line, width: 1.5 } : { color: o.fill || PALE, width: 0.5 },
    fontFace: o.font || BF, fontSize: o.size || 16, bold: !!o.bold, color: o.color || INK, align: o.align || 'center', valign: o.valign || 'middle',
    margin: o.margin === undefined ? 6 : o.margin, isTextBox: true, strike: o.strike, italic: o.italic
  });
}
function txt(s, text, x, y, w, h, o = {}) {
  s.addText(text, { x, y, w, h, fontFace: o.font || BF, fontSize: o.size || 16, bold: !!o.bold, color: o.color || INK, align: o.align || 'left', valign: o.valign || 'top', margin: o.margin === undefined ? 0 : o.margin, isTextBox: true, paraSpaceAfter: o.psa || 0, italic: o.italic });
}
// arrows (horizontal / vertical). dir: 'r','l','d','u'
function arrow(s, x1, y1, len, dir, color = NAVY, head = true) {
  const o = { line: { color, width: 3, endArrowType: head ? 'triangle' : undefined } };
  if (dir === 'r') s.addShape(pres.ShapeType.line, { x: x1, y: y1, w: len, h: 0, ...o });
  if (dir === 'l') s.addShape(pres.ShapeType.line, { x: x1 - len, y: y1, w: len, h: 0, flipH: true, ...o });
  if (dir === 'd') s.addShape(pres.ShapeType.line, { x: x1, y: y1, w: 0, h: len, ...o });
  if (dir === 'u') s.addShape(pres.ShapeType.line, { x: x1, y: y1 - len, w: 0, h: len, flipV: true, ...o });
}
function circle(s, x, y, d, label, fill = NAVY, size = 18) {
  s.addText(String(label), { x, y, w: d, h: d, shape: pres.ShapeType.ellipse, fill: { color: fill }, line: { color: fill, width: 0.5 }, fontFace: BF, fontSize: size, bold: true, color: WHITE, align: 'center', valign: 'middle', margin: 0, isTextBox: true });
}
function band(s, y, h, text, fill = NAVY, color = WHITE, size = 20) {
  box(s, 0.5, y, 12.33, h, text, { fill, color, size, bold: true, margin: 10 });
}

// ---------- TITLE ----------
{
  const s = pres.addSlide();
  s.background = { color: NAVY };
  s.addText('Digital Radiography: An Overview', { x: 0.8, y: 1.7, w: 11.7, h: 1.2, fontFace: HF, fontSize: 48, bold: true, color: WHITE, margin: 0, isTextBox: true });
  s.addText('From film to pixels to PACS', { x: 0.8, y: 3.0, w: 11.7, h: 0.7, fontFace: BF, fontSize: 28, color: 'BFD7F0', margin: 0, isTextBox: true });
  s.addText('Diagnostic Imaging  ·  Homework 1, Topic 1', { x: 0.8, y: 4.3, w: 11.7, h: 0.5, fontFace: BF, fontSize: 20, color: WHITE, margin: 0, isTextBox: true });
  s.addText('Group: A  ·  B  ·  C  ·  D   (replace with names)', { x: 0.8, y: 4.9, w: 11.7, h: 0.5, fontFace: BF, fontSize: 20, color: AMB, margin: 0, isTextBox: true });
  s.addText('Primary source: Seeram E. (2019), Digital Radiography, 2nd ed., Springer, Ch. 1', { x: 0.8, y: 6.7, w: 11.7, h: 0.4, fontFace: BF, fontSize: 14, color: 'BFD7F0', margin: 0, isTextBox: true });
  s.addNotes('A opens. Welcome, introduce the four members and who speaks when: A (hook, definition, film, fluoroscopy), B (exposure factors, film limits, DR system, PACS), C (CR, flat panels, latitude, Activity 1), D (Activity 2, EI/DI, QA, close). Total about 17 minutes with two activities.');
}

// ---------- 1 HOOK ----------
{
  const s = base('Same mistake, two outcomes', 'Images: simulated by the group from a CC0 chest PA radiograph (Wikimedia Commons, Stillwaterising); film via an H&D-curve model, cf. Seeram (2019) Figs 1.3-1.4. Noise/exposure exaggerated.',
    'A. Show the same chest taken with 4x the correct mAs. On film it comes out almost black and must be repeated, so the patient gets more radiation. On digital it looks normal. Ask: which patient received too much radiation? Answer: both did, but only one image shows it. Keep this question open, we come back to it. Agenda: film, detectors, dose, PACS. HANDOVER: "First, how did film work and why did we leave it?"');
  s.addImage({ path: FIG + 'film_4x.png', x: 0.9, y: 1.3, w: 4.0, h: 4.0 });
  s.addImage({ path: FIG + 'dr_4x.png', x: 8.43, y: 1.3, w: 4.0, h: 4.0 });
  txt(s, 'Film', 0.9, 5.4, 4.0, 0.5, { size: 24, bold: true, align: 'center', color: NAVY });
  txt(s, 'almost black: repeat needed', 0.9, 5.85, 4.0, 0.4, { size: 16, align: 'center', color: MUTE });
  txt(s, 'Digital (DR)', 8.43, 5.4, 4.0, 0.5, { size: 24, bold: true, align: 'center', color: TEALD });
  txt(s, 'looks normal', 8.43, 5.85, 4.0, 0.4, { size: 16, align: 'center', color: MUTE });
  box(s, 5.3, 1.5, 2.73, 1.0, 'Same chest.\nSame 4× mAs.', { fill: AMB, color: INK, size: 20, bold: true });
  ['Film', 'Detectors', 'Dose', 'PACS'].forEach((t, i) => box(s, 5.5, 2.9 + i * 0.6, 2.33, 0.48, t, { fill: PALE, size: 16, bold: true }));
  band(s, 6.35, 0.6, 'Which patient received too much radiation?', NAVY, WHITE, 22);
}

// ---------- 2 DEFINITION + CHAIN ----------
{
  const s = base('What is digital radiography?', 'Redrawn from Seeram (2019) Fig 1.1 and Fig 1.5; definition after AAPM Report 116, quoted in Seeram §1.2.',
    'A. In our words: digital radiography uses electronic or phosphor detectors to produce a digital projection image, and it works over a wider range of exposures than film. Walk the chain: tube, patient, detector. The detector produces an analog signal; the ADC converts it to numbers; the computer processes it; the DAC turns the numbers back into a signal for the monitor. Key point: the radiologist never sees the numbers, only the displayed image. HANDOVER: "Before we see how digital works, how did film work?" (still A).');
  txt(s, 'Digital detectors turn X-ray exposure into numbers, and give usable images over a wider range of exposures than film.', 0.5, 1.2, 12.3, 0.8, { size: 20 });
  const y1 = 2.35, y2 = 4.45, w = 2.4, h = 1.3, xs = [0.7, 3.9, 7.1, 10.3];
  box(s, xs[0], y1, w, h, 'X-ray tube', { fill: NAVY, color: WHITE, size: 18, bold: true });
  box(s, xs[1], y1, w, h, 'Patient', { fill: NAVY, color: WHITE, size: 18, bold: true });
  box(s, xs[2], y1, w, h, 'Digital detector', { fill: TEAL, color: INK, size: 18, bold: true });
  box(s, xs[3], y1, w, h, 'ADC\nanalog → digital', { fill: AMB, color: INK, size: 18, bold: true });
  arrow(s, xs[0] + w, y1 + h / 2, 0.8, 'r'); arrow(s, xs[1] + w, y1 + h / 2, 0.8, 'r'); arrow(s, xs[2] + w, y1 + h / 2, 0.8, 'r');
  txt(s, 'analog signal', xs[2] + w - 0.1, y1 - 0.35, 1.3, 0.3, { size: 14, color: MUTE, italic: true });
  arrow(s, xs[3] + w / 2, y1 + h, 0.9, 'd');
  txt(s, 'digital data', xs[3] + w / 2 + 0.15, y1 + h + 0.3, 1.5, 0.3, { size: 14, color: MUTE, italic: true });
  box(s, xs[3], y2, w, h, 'Computer\nprocessing', { fill: NAVY, color: WHITE, size: 18, bold: true });
  box(s, xs[2], y2, w, h, '27 22 24\n25 28 21\ndigital image = numbers', { fill: PALE, size: 14, font: 'Courier New' });
  box(s, xs[1], y2, w, h, 'DAC\ndigital → analog', { fill: AMB, color: INK, size: 18, bold: true });
  box(s, xs[0], y2, w, h, 'Displayed image', { fill: TEAL, color: INK, size: 18, bold: true });
  arrow(s, xs[3], y2 + h / 2, 0.8, 'l'); arrow(s, xs[2], y2 + h / 2, 0.8, 'l'); arrow(s, xs[1], y2 + h / 2, 0.8, 'l');
  band(s, 6.2, 0.65, 'Radiologists never see the numbers, only the displayed image.', TEALD, WHITE, 20);
}

// ---------- 3 FILM + H&D ----------
{
  const s = base('How film works, and its S-curve', 'Redrawn from Seeram (2019) Figs 1.2 and 1.4 (OD values from §1.3.2). Thumbnails: simulated by the group from a CC0 chest radiograph.',
    'A. Film chain: X-rays make a latent image, chemical processing makes it visible, the radiologist reads it on a viewbox. Optical density OD = log of incident over transmitted light. The characteristic or H&D curve plots OD against log exposure. Toe: underexposed, light, OD about 0.12 to 0.20. Straight-line portion: useful, OD about 0.3 to 2.2. Shoulder: overexposed, dark, OD about 3.2. Film is detector, display and archive in one. HANDOVER: "B will show what technologists can control, and why film had to go."');
  const steps = ['X-ray exposure', 'Latent image', 'Chemical processing', 'Viewbox'];
  steps.forEach((t, i) => {
    box(s, 0.5, 1.35 + i * 1.1, 2.8, 0.8, t, { fill: i === 3 ? TEAL : PALE, size: 17, bold: true });
    if (i < 3) arrow(s, 1.9, 2.15 + i * 1.1, 0.3, 'd');
  });
  s.addImage({ path: FIG + 'hd_curve.png', x: 3.6, y: 1.3, w: 5.8, h: 5.8 * 1000 / 1440 });
  const th = [['film_4x.png', 'Shoulder', 'overexposed'], ['film_1x.png', 'Straight line', 'useful'], ['film_q.png', 'Toe', 'underexposed']];
  th.forEach((t, i) => {
    s.addImage({ path: FIG + t[0], x: 9.75, y: 1.3 + i * 1.45, w: 1.35, h: 1.35 });
    txt(s, t[1], 11.2, 1.55 + i * 1.45, 1.7, 0.4, { size: 16, bold: true, color: NAVY });
    txt(s, t[2], 11.2, 1.95 + i * 1.45, 1.7, 0.4, { size: 14, color: MUTE });
  });
  band(s, 5.95, 0.8, 'OD = log₁₀ (I₀ / Iₜ)     ·     Film = detector + display + archive in one', NAVY, WHITE, 20);
}

// ---------- 4 EXPOSURE FACTORS ----------
{
  const s = base('Exposure factors: what the technologist controls', 'Seeram (2019) §1.3.3-1.3.6. Dose-vs-kVp relation is an approximation at fixed mAs.',
    'B. kVp sets beam quality or penetration and is the main control of contrast: lower kVp, higher contrast. mAs is mA times seconds, it sets the number of photons and is the main control of noise: low mAs gives quantum mottle. Dose is directly proportional to mAs; at fixed mAs it rises roughly with kVp squared (approximation). Higher kVp with lower mAs can cut dose but also lowers contrast. AEC ends the exposure when a preset detector level is reached: optical density for film, signal-to-noise for digital. HANDOVER from A: "B now explains..." HANDOVER to next slide: "What went wrong with film?"');
  const hdr = { bold: true, color: WHITE, fill: { color: NAVY }, fontSize: 18, align: 'center', valign: 'middle', fontFace: BF };
  const c = (t, o = {}) => ({ text: t, options: { fontSize: 17, fontFace: BF, color: INK, valign: 'middle', ...o } });
  const rows = [
    [{ text: '', options: { ...hdr } }, { text: 'kVp (tube voltage)', options: hdr }, { text: 'mAs (tube current × time)', options: hdr }],
    [c('Controls', { bold: true, fill: { color: PALE } }), c('Beam quality: penetrating power'), c('Beam quantity: number of photons')],
    [c('Main image effect', { bold: true, fill: { color: PALE } }), c('Contrast: lower kVp = higher contrast'), c('Noise: low mAs = grainy (quantum mottle)')],
    [c('Patient dose', { bold: true, fill: { color: PALE } }), c('≈ kVp² at fixed mAs'), c('Proportional: 2× mAs = 2× dose')]
  ];
  s.addTable(rows, { x: 0.5, y: 1.4, w: 12.33, colW: [2.6, 4.87, 4.86], rowH: [0.65, 0.85, 0.85, 0.85], border: { type: 'solid', pt: 1, color: 'C9D6E4' } });
  band(s, 5.45, 0.9, 'AEC stops the exposure at a preset detector level (film: optical density · digital: signal-to-noise)', TEALD, WHITE, 20);
}

// ---------- 5 WHY FILM HAD TO GO ----------
{
  const s = base('Why film had to go', 'Seeram (2019) §1.3.7.',
    'B. Three limitations. One: if exposure is wrong the film is too light or too dark; it must be repeated, so extra dose; film also cannot show tissue contrast differences below about 10 percent. Two: the display is fixed once processed; to change contrast you would need a new exposure. Three: the archive is physical, envelopes in a big room, retrieved by hand, one copy in one place. Film does have excellent spatial resolution, about 5 to 15 line pairs per mm. HANDOVER: "So what replaced the cassette and the darkroom? Let us look inside a digital system."');
  const cards = [['Wrong exposure = repeat', 'Too light or too dark film is unusable. A repeat means extra dose.'], ['The display is fixed', 'Brightness and contrast are set at exposure. A change needs a new exposure.'], ['The archive is physical', 'Envelopes, large rooms, manual retrieval. One copy in one place.']];
  cards.forEach((cd, i) => {
    const x = 0.5 + i * 4.215;
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.4, w: 3.9, h: 3.7, rectRadius: 0.1, fill: { color: PALE }, line: { color: PALE, width: 0.5 } });
    circle(s, x + 0.3, 1.65, 0.7, i + 1, i === 0 ? RED : i === 1 ? AMB : NAVY, 24);
    txt(s, cd[0], x + 0.3, 2.55, 3.3, 0.9, { size: 22, bold: true, color: NAVY });
    txt(s, cd[1], x + 0.3, 3.5, 3.3, 1.4, { size: 17 });
  });
  band(s, 5.5, 0.8, 'Film’s one strength: spatial resolution ≈ 5–15 lp/mm', AMB, INK, 22);
}

// ---------- 6 DR SYSTEM ----------
{
  const s = base('Inside a digital radiography system', 'Redrawn from Seeram (2019) Fig 1.5 and §1.4; grayscale mapping after Fig 1.6 (same CC0 chest radiograph, processed by the group).',
    'B. Six building blocks. One, data acquisition: the detector. Two, ADC and computer processing; computers store bits, for example the word EUCLID in 8-bit ASCII. Three, display and post-processing: DAC, then tools such as grayscale mapping that turn a low-contrast image into a high-contrast one. Four, storage: RAID, tape, optical disk. Five, communications: LAN inside the hospital, WAN outside. Six, image and information management: PACS, RIS, HIS. HANDOVER: "C will open the detector and show what turns X-rays into a signal."');
  const st = [['Acquisition', 'digital detector'], ['ADC + computer', 'binary processing'], ['Display + post-processing', 'DAC, monitor, grayscale mapping'], ['Storage', 'RAID, tape, optical disk'], ['Communications', 'LAN inside, WAN outside'], ['Management', 'PACS, RIS, HIS']];
  st.forEach((t, i) => {
    const x = 0.5 + i * 2.086;
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.35, w: 1.95, h: 2.5, rectRadius: 0.08, fill: { color: PALE }, line: { color: PALE, width: 0.5 } });
    circle(s, x + 0.65, 1.5, 0.65, i + 1, NAVY, 20);
    txt(s, t[0], x + 0.1, 2.25, 1.75, 0.7, { size: 16, bold: true, align: 'center', color: NAVY });
    txt(s, t[1], x + 0.1, 2.95, 1.75, 0.8, { size: 14, align: 'center', color: MUTE });
  });
  s.addShape(pres.ShapeType.roundRect, { x: 0.5, y: 4.15, w: 7.3, h: 2.1, rectRadius: 0.08, fill: { color: WHITE }, line: { color: TEAL, width: 2 } });
  txt(s, 'Computers store everything as bits', 0.7, 4.25, 6.9, 0.45, { size: 18, bold: true, color: TEALD });
  txt(s, 'EUCLID in binary:', 0.7, 4.75, 6.9, 0.35, { size: 16 });
  txt(s, '01000101 01010101 01000011\n01001100 01001001 01000100', 0.7, 5.15, 6.9, 0.9, { size: 20, font: 'Courier New', bold: true, color: NAVY });
  s.addImage({ path: OLD + 'cxr_lowc.png', x: 8.2, y: 4.2, w: 1.9, h: 1.9 });
  arrow(s, 10.2, 5.15, 0.55, 'r');
  s.addImage({ path: OLD + 'cxr_highc.png', x: 10.85, y: 4.2, w: 1.9, h: 1.9 });
  txt(s, 'Grayscale mapping: low → high contrast', 8.2, 6.2, 4.6, 0.4, { size: 15, align: 'center', color: MUTE });
}

// ---------- 7 CR ----------
{
  const s = base('Computed radiography (CR): the reusable plate', 'Redrawn from Seeram (2019) Fig 1.8 and §1.6.1. Laser/emission details: Storage Phosphors for Medical Imaging, Materials 2011 (PMC5448636).',
    'C. CR uses a photostimulable phosphor, barium fluorohalide, on an imaging plate in a cassette, so existing X-ray rooms can be used. Fuji introduced it clinically in 1983. Cycle: one, expose the plate, electrons are trapped as a latent image. Two, a laser scans the plate, trapped electrons are released and light is emitted. Three, a light guide and photomultiplier tube turn the light into an electrical signal. Four, the computer processes it. Five, display. Six, erase the plate with bright light. Seven, reuse. Spatial resolution about 3 to 5 lp/mm, but a far wider dynamic range than film. HANDOVER: "Now the detector that needs no cassette at all."');
  const bw = 2.0, bh = 1.25, xs = [0.5, 2.85, 5.2, 7.55], y1 = 1.4, y2 = 3.6;
  const top = ['Expose the plate\n(latent image)', 'Laser scan\n(light emitted)', 'Light guide + PMT\n(electrical signal)', 'Digital processing'];
  top.forEach((t, i) => { box(s, xs[i], y1, bw, bh, t, { fill: i === 0 ? NAVY : PALE, color: i === 0 ? WHITE : INK, size: 16, bold: true }); circle(s, xs[i] - 0.12, y1 - 0.15, 0.45, i + 1, TEALD, 15); if (i < 3) arrow(s, xs[i] + bw, y1 + bh / 2, 0.35, 'r'); });
  arrow(s, xs[3] + bw / 2, y1 + bh, 0.85, 'd');
  const bot = [['Display', xs[3], 5], ['Erase with\nbright light', xs[2], 6], ['Plate ready\nfor reuse', xs[1], 7]];
  bot.forEach((b, i) => { box(s, b[1], y2, bw, bh, b[0], { fill: i === 2 ? GRN : PALE, size: 16, bold: true }); circle(s, b[1] - 0.12, y2 - 0.15, 0.45, b[2], TEALD, 15); });
  arrow(s, xs[3], y2 + bh / 2, 0.35, 'l'); arrow(s, xs[2], y2 + bh / 2, 0.35, 'l');
  arrow(s, xs[1], y2 + bh / 2, 1.35, 'l', NAVY, false);
  arrow(s, 1.5, y2 + bh / 2, y2 + bh / 2 - (y1 + bh), 'u');
  txt(s, 'back to step 1', 0.5, y2 + bh / 2 + 0.1, 1.9, 0.3, { size: 14, color: MUTE, italic: true });
  s.addShape(pres.ShapeType.roundRect, { x: 9.95, y: 1.4, w: 2.88, h: 4.6, rectRadius: 0.1, fill: { color: PALE }, line: { color: PALE, width: 0.5 } });
  txt(s, [{ text: 'Phosphor', options: { bold: true, color: NAVY, breakLine: true } }, { text: 'BaFBr:Eu²⁺ on an imaging plate (IP)', options: { breakLine: true } }, { text: ' ', options: { breakLine: true } }, { text: 'Introduced', options: { bold: true, color: NAVY, breakLine: true } }, { text: 'Fuji, 1983', options: { breakLine: true } }, { text: ' ', options: { breakLine: true } }, { text: 'Spatial resolution', options: { bold: true, color: NAVY, breakLine: true } }, { text: '≈ 3–5 lp/mm', options: { breakLine: true } }, { text: ' ', options: { breakLine: true } }, { text: 'Dynamic range', options: { bold: true, color: NAVY, breakLine: true } }, { text: '≈ 10,000 : 1 (far wider than film)' }], 10.15, 1.55, 2.5, 4.3, { size: 16 });
  band(s, 6.25, 0.6, 'Latent image = trapped electrons; the laser frees them as light', TEALD, WHITE, 19);
}

// ---------- 8 FLAT PANELS ----------
{
  const s = base('Flat-panel detectors: indirect vs direct', 'Redrawn from Seeram (2019) Figs 1.9 and 1.10, §1.6.2. Terms (a-Si photodiode + TFT): see sources.md.',
    'C. Two families of flat-panel detector. Indirect: a scintillator, usually caesium iodide, turns X-rays into light; an amorphous-silicon photodiode and TFT array turn the light into charge and signal. X-ray to light to electrical signal. Direct: a photoconductor, amorphous selenium, turns X-rays straight into charge, which the TFT array reads out. X-ray to electrical signal, no light step. A third variant uses scintillator, optics and a CCD array. All flat panels read out immediately, have high DQE and resolution comparable to CR. HANDOVER: "These detectors are linear. Why that matters for exposure..."');
  const cols = [{ x: 0.5, head: 'Indirect: X-ray → light → signal', l1: 'Scintillator (CsI)', mid: 'light', l2: 'a-Si photodiode + TFT array', hd: TEAL }, { x: 6.93, head: 'Direct: X-ray → signal', l1: 'Photoconductor (a-Se)', mid: 'light', l2: 'TFT array', hd: NAVY }];
  cols.forEach((c, i) => {
    const w = 5.9, x = c.x;
    box(s, x, 1.3, w, 0.55, c.head, { fill: c.hd, color: i === 0 ? INK : WHITE, size: 19, bold: true });
    txt(s, 'X-ray photons ↓', x, 1.95, w, 0.4, { size: 16, align: 'center', color: MUTE });
    box(s, x, 2.4, w, 0.85, c.l1, { fill: PALE, line: c.hd, size: 19, bold: true });
    if (i === 0) box(s, x + 1.7, 3.35, w - 3.4, 0.5, 'light', { fill: AMB, size: 17, bold: true });
    else box(s, x + 1.7, 3.35, w - 3.4, 0.5, 'light', { fill: 'F1F1F1', color: '9AA5B1', size: 17, strike: 'sngStrike', italic: true });
    box(s, x, 3.95, w, 0.95, c.l2, { fill: PALE, line: c.hd, size: 19, bold: true });
    box(s, x, 5.0, w, 0.6, 'Electrical signal → digital image', { fill: GRN, color: INK, size: 17, bold: true });
  });
  txt(s, 'no light step', 7.0 + 3.7, 3.35, 1.8, 0.5, { size: 14, color: RED, bold: true, valign: 'middle' });
  band(s, 5.9, 0.9, 'Both: immediate readout · high DQE · resolution comparable to CR · (variant: scintillator + optics + CCD)', TEALD, WHITE, 18);
}

// ---------- 9 LINEAR RESPONSE ----------
{
  const s = base('Straight line vs S-curve: exposure latitude', 'Redrawn from Seeram (2019) Figs 1.4 and 1.11, §1.6.2. Dynamic range: Seeram §1.6.1 (see Knowledge Guide for caveat).',
    'C. Film has an S-shaped curve and a narrow useful range. A digital detector responds linearly over a very wide range, so the computer can rescale the brightness and give an acceptable image even if exposure was too low or too high. The catch: under-exposure shows up as noise, grain. Over-exposure does not show at all until the detector saturates, so nobody notices the extra dose. That is why we test your eyes now. HANDOVER: "Activity 1: the Radiologist Eye Test."');
  s.addImage({ path: FIG + 'response.png', x: 0.5, y: 1.35, w: 8.3, h: 8.3 * 860 / 1920 });
  txt(s, 'Digital dynamic range ≈ 10,000 : 1; film’s useful latitude is far narrower.', 0.5, 5.3, 8.3, 0.7, { size: 17, color: MUTE });
  box(s, 9.2, 1.4, 3.63, 1.7, 'Too little exposure\n→ grain (noise) shows', { fill: AMB, size: 20, bold: true });
  box(s, 9.2, 3.35, 3.63, 1.7, 'Too much exposure\n→ looks fine, dose is hidden', { fill: RED, color: WHITE, size: 20, bold: true });
  band(s, 6.2, 0.65, 'So how good are your eyes at judging exposure?', NAVY, WHITE, 22);
}

// ---------- 10 WARM-UP ----------
{
  const s = base('Activity 1: the Radiologist Eye Test', 'Images: simulated by the group from a CC0 chest radiograph (Wikimedia Commons); noise exaggerated for projection. Run from DR_Lab.html, tab 2.',
    'C hosts, D reveals. Open DR_Lab.html tab 2. Say: four chest X-rays, same patient, different doses. Hold up fingers: which panel got the LOWEST dose? (10 s; most hold up 2, the grainiest.) D clicks Reveal lowest. Now: which got the HIGHEST dose? (10 s; class splits between 1 and 3.) D clicks Reveal all: panels are 1x, 1/4x, 3x, 1/2x. Punchline: grain tells you when you gave too little; nothing tells you when you gave too much. Remember that for the next game. HANDOVER to D: "D runs X-ray Blackjack."');
  box(s, 0.5, 1.4, 2.3, 0.55, 'ACTIVITY 1  ·  1 min', { fill: AMB, size: 16, bold: true });
  txt(s, [{ text: 'Four chest X-rays: same patient, different dose.', options: { breakLine: true, bullet: true } }, { text: 'Hold up 1–4 fingers: which got the LOWEST dose?', options: { breakLine: true, bullet: true } }, { text: 'Now: which got the HIGHEST?', options: { bullet: true } }], 0.5, 2.25, 5.9, 2.6, { size: 20, psa: 10 });
  box(s, 0.5, 5.1, 5.9, 0.9, 'Open DR_Lab.html → tab 2 “Warm-up”', { fill: PALE, size: 18, bold: true, color: NAVY });
  [[1, 0], [2, 0], [3, 1], [4, 1]].forEach(([n, r], i) => s.addImage({ path: FIG + 'warm_' + n + '.png', x: 7.0 + (i % 2) * 2.85, y: 1.3 + r * 2.8, w: 2.7, h: 2.7 }));
}

// ---------- 11 BLACKJACK ----------
{
  const s = base('Activity 2: X-ray Blackjack', 'Images: simulated by the group from a CC0 chest radiograph (Wikimedia Commons); simplified model: noise ∝ 1/√photons, dose ∝ mAs (Seeram §1.3.5-1.3.6). DR_Lab.html, tab 3.',
    'D hosts; A clicks cards, B referees, C collects Team Left votes. Split the room into Team Left and Team Right, each with a captain. Both teams start from the same grainy image; the ideal image is always on screen. Each round, a team plays a multiplier card on its own exposure; the new image appears for both teams, so they compare. The first team\'s card is blocked for the second team that round. First pick alternates (coin flip in round 1). Up to 4 rounds or STAND; a team that stands is out, but the other team keeps playing all its remaining rounds, so standing early gives no advantage. The last image is the submission. Score = Quality x 2 minus Dose; quality is hidden until the reveal, dose is the bar. About 25 s per round. Then press Reveal and hand to slide 12.');
  box(s, 0.5, 1.3, 2.6, 0.55, 'ACTIVITY 2  ·  2.5 min', { fill: AMB, size: 16, bold: true });
  const rules = ['Both teams start from the same grainy image.', 'Each round: play a × card on your own exposure. New image, more dose.', 'No copying: the first team’s card is blocked for the second.', 'Up to 4 rounds, or STAND. The other team keeps playing. Last image counts.'];
  rules.forEach((t, i) => { circle(s, 0.5, 2.1 + i * 0.95, 0.55, i + 1, NAVY, 18); txt(s, t, 1.25, 2.05 + i * 0.95, 5.3, 0.8, { size: 18, valign: 'middle' }); });
  box(s, 0.5, 5.95, 6.0, 0.8, 'Score = Quality × 2 − Dose', { fill: NAVY, color: WHITE, size: 26, bold: true });
  s.addImage({ path: FIG + 'start.png', x: 7.0, y: 1.3, w: 2.7, h: 2.7 });
  arrow(s, 9.75, 2.65, 0.45, 'r');
  s.addImage({ path: FIG + 'ideal.png', x: 10.25, y: 1.3, w: 2.58, h: 2.58 });
  txt(s, 'Start: both teams', 7.0, 4.05, 2.7, 0.4, { size: 15, align: 'center', color: MUTE });
  txt(s, 'Ideal', 10.25, 4.05, 2.58, 0.4, { size: 15, align: 'center', color: MUTE });
  ['×⅙', '×¼', '×⅓', '×½', '×2', '×3', '×4', '×6'].forEach((t, i) => box(s, 7.0 + i * 0.73, 4.7, 0.65, 0.6, t, { fill: WHITE, line: NAVY, size: 18, bold: true, margin: 0 }));
  txt(s, 'Dose bar (relative):', 7.0, 5.5, 3.0, 0.35, { size: 15, color: MUTE });
  s.addShape(pres.ShapeType.rect, { x: 7.0, y: 5.95, w: 1.9, h: 0.4, fill: { color: GRN }, line: { color: GRN, width: 0.5 } });
  s.addShape(pres.ShapeType.rect, { x: 8.9, y: 5.95, w: 1.9, h: 0.4, fill: { color: AMB }, line: { color: AMB, width: 0.5 } });
  s.addShape(pres.ShapeType.rect, { x: 10.8, y: 5.95, w: 1.9, h: 0.4, fill: { color: RED }, line: { color: RED, width: 0.5 } });
  txt(s, 'Open DR_Lab.html → tab 3', 7.0, 6.45, 5.7, 0.4, { size: 15, bold: true, color: NAVY });
}

// ---------- 12 EI / DI ----------
{
  const s = base('The number your eyes can’t see: EI, DI and dose creep', 'AAPM Report No. 116 (2009) and IEC 62494-1 (2008); DI action bands as summarised in Seibert, IUPESM slides (see sources.md). Images: simulated by the group.',
    'D debriefs the game. Show the two final images: they look the same, yet one team gave about three times the exposure. The Exposure Index is a standardized number tied to the detector exposure; each exam has a target EI. The Deviation Index is ten times log10 of EI over target EI. DI zero is on target; plus 3 is about double the exposure; minus 3 is about half. Guidance summarised from AAPM TG-116: target DI about minus 2 to plus 2; between plus 2 and plus 3 investigate the cause; at plus 3 or more consult the radiologist and counsel the technologist; at minus 2 or below check for noise and consider a repeat. Remember EI reflects the signal at the detector, it is not a measure of patient dose. Dose creep is the gradual drift to higher exposures because overexposed digital images look fine. That is the ALARA problem of digital. Answer to the opening question: both patients got extra dose, only film showed it. HANDOVER to A: "A will show where else digital imaging is used."');
  s.addImage({ path: FIG + 'ideal.png', x: 0.5, y: 1.4, w: 2.75, h: 2.75 });
  s.addImage({ path: FIG + 'dr_3x.png', x: 3.4, y: 1.4, w: 2.75, h: 2.75 });
  txt(s, '1×  ·  DI 0.0', 0.5, 4.2, 2.75, 0.4, { size: 18, bold: true, align: 'center', color: TEALD });
  txt(s, '3×  ·  DI +4.8', 3.4, 4.2, 2.75, 0.4, { size: 18, bold: true, align: 'center', color: RED });
  txt(s, 'Both look right. Only the DI shows who gave 3× the exposure.', 0.5, 4.75, 5.65, 0.8, { size: 18, color: MUTE });
  box(s, 6.6, 1.4, 6.23, 0.95, 'DI = 10 · log₁₀ (EI / EIₜ)', { fill: NAVY, color: WHITE, size: 28, bold: true });
  txt(s, 'EI: standardized detector-exposure number (not patient dose). EIₜ: target for the exam.   +3 ≈ 2× exposure · −3 ≈ ½×', 6.6, 2.5, 6.23, 0.8, { size: 17 });
  s.addImage({ path: FIG + 'di_scale.png', x: 6.6, y: 3.4, w: 6.23, h: 6.23 * 1.7 / 8.4 });
  txt(s, 'Dose creep: exposures drift upward because over-exposed digital images look fine.', 6.6, 4.85, 6.23, 0.8, { size: 17, bold: true, color: RED });
  band(s, 6.0, 0.8, 'ALARA: read the number, not just the image', TEALD, WHITE, 22);
}

// ---------- 13 DF + MAMMO ----------
{
  const s = base('Beyond the chest X-ray: fluoroscopy and mammography', 'Seeram (2019) §1.6.3-1.6.4, Figs 1.12-1.13. Diagram redrawn by the group.',
    'A. Digital fluoroscopy gives real-time moving images, for the GI tract and blood vessels. It uses an image intensifier with a TV or CCD camera; the output is digitized by the ADC, and flat panels are replacing the intensifier. Digital subtraction angiography subtracts the pre-contrast image from the post-contrast image, leaving only the vessels. Temporal subtraction works in time; energy subtraction uses two kVp. Digital mammography uses CR, flat-panel or CCD detectors, allows post-processing, and computer-aided detection acts as a second reader for microcalcifications and masses. HANDOVER to B: "All these images go to PACS."');
  box(s, 0.5, 1.3, 6.0, 0.6, 'Digital fluoroscopy and DSA', { fill: NAVY, color: WHITE, size: 20, bold: true });
  box(s, 0.5, 2.2, 1.65, 1.1, 'Pre-contrast image', { fill: PALE, size: 15, bold: true });
  txt(s, '−', 2.2, 2.25, 0.5, 1.0, { size: 36, bold: true, align: 'center', valign: 'middle', color: NAVY });
  box(s, 2.75, 2.2, 1.65, 1.1, 'Post-contrast image', { fill: PALE, size: 15, bold: true });
  txt(s, '=', 4.45, 2.25, 0.5, 1.0, { size: 36, bold: true, align: 'center', valign: 'middle', color: NAVY });
  box(s, 5.0, 2.2, 1.5, 1.1, 'Vessels only', { fill: TEAL, size: 15, bold: true });
  txt(s, [{ text: 'Real-time moving images (GI tract, vessels)', options: { bullet: true, breakLine: true } }, { text: 'Image intensifier + TV/CCD → ADC', options: { bullet: true, breakLine: true } }, { text: 'Subtraction: temporal (in time) or energy (two kVp)', options: { bullet: true } }], 0.5, 3.65, 6.0, 2.4, { size: 17, psa: 8 });
  box(s, 6.9, 1.3, 5.93, 0.6, 'Digital mammography', { fill: TEALD, color: WHITE, size: 20, bold: true });
  ['CR', 'Direct FPD', 'Indirect FPD', 'CCD'].forEach((t, i) => box(s, 6.9 + i * 1.5, 2.2, 1.38, 0.8, t, { fill: PALE, size: 15, bold: true }));
  txt(s, 'detectors used', 6.9, 3.05, 5.9, 0.3, { size: 14, color: MUTE, italic: true });
  txt(s, [{ text: 'Digital post-processing to enhance interpretation', options: { bullet: true, breakLine: true } }, { text: 'CAD = “second reader” for microcalcifications and masses', options: { bullet: true, breakLine: true } }, { text: 'Leads to digital tomosynthesis', options: { bullet: true } }], 6.9, 3.65, 5.93, 2.4, { size: 17, psa: 8 });
  band(s, 6.2, 0.65, 'Digital tools: process, subtract and flag, after the exposure', TEALD, WHITE, 20);
}

// ---------- 14 PACS ----------
{
  const s = base('PACS: the department’s backbone', 'Redrawn from Seeram (2019) Fig 1.14, §1.4.4-1.7, §1.9. IHE: RSNA + HIMSS, 1998. Next-era terms: Seeram §1.9.2.',
    'B. PACS is a computer system for electronic storage and distribution of medical images, integrated with the acquisition and display devices and linked to RIS and HIS. Modalities such as CT, MRI, CR, DR, ultrasound, nuclear medicine and film digitizers send images through interfaces to the PACS server with its database and archive; diagnostic and review workstations and web access display them. DICOM is for images; HL7 is for text and patient information; IHE makes the standards work together. Compression: lossless is reversible, lossy is not. One line on the next era: enterprise imaging, cloud, Big Data with its four Vs, machine learning, deep learning, AI. HANDOVER to D: "D closes with quality assurance and the take-home."');
  const mods = ['CT', 'MRI', 'CR', 'DR', 'US', 'Nuclear med.', 'Film digitizer'];
  mods.forEach((m, i) => box(s, 0.5, 1.3 + i * 0.6, 1.9, 0.5, m, { fill: PALE, size: 15, bold: true }));
  arrow(s, 2.45, 3.3, 0.55, 'r');
  box(s, 3.05, 2.5, 1.1, 1.6, 'Inter-\nfaces', { fill: AMB, size: 15, bold: true });
  arrow(s, 4.2, 3.3, 0.5, 'r');
  box(s, 4.75, 1.3, 2.3, 0.8, 'HIS / RIS\n(text data)', { fill: PALE, line: NAVY, size: 15, bold: true });
  arrow(s, 5.9, 2.15, 0.6, 'd');
  box(s, 4.75, 2.8, 2.3, 1.7, 'PACS server\ndatabase + archive', { fill: NAVY, color: WHITE, size: 17, bold: true });
  arrow(s, 7.1, 3.1, 0.5, 'r'); arrow(s, 7.1, 3.9, 0.5, 'r');
  box(s, 7.65, 2.6, 1.95, 0.8, 'Diagnostic workstation', { fill: TEAL, size: 14, bold: true });
  box(s, 7.65, 3.55, 1.95, 0.8, 'Review workstation', { fill: PALE, size: 14, bold: true });
  box(s, 7.65, 4.5, 1.95, 0.6, 'Web access', { fill: PALE, size: 14, bold: true });
  const cards = [['DICOM', 'images + metadata'], ['HL7', 'text / patient information'], ['IHE', 'makes them work together']];
  cards.forEach((c, i) => { box(s, 9.95, 1.3 + i * 0.95, 2.88, 0.85, '', { fill: PALE }); txt(s, c[0], 10.1, 1.35 + i * 0.95, 2.6, 0.4, { size: 17, bold: true, color: NAVY }); txt(s, c[1], 10.1, 1.75 + i * 0.95, 2.6, 0.35, { size: 14, color: MUTE }); });
  box(s, 9.95, 4.2, 1.4, 0.9, 'Lossless\n(reversible)', { fill: GRN, size: 14, bold: true });
  box(s, 11.43, 4.2, 1.4, 0.9, 'Lossy\n(irreversible)', { fill: AMB, size: 14, bold: true });
  txt(s, 'Compression', 9.95, 5.15, 2.9, 0.3, { size: 13, color: MUTE, italic: true });
  band(s, 5.7, 1.0, 'Next era: enterprise imaging · cloud · Big Data (volume, variety, velocity, veracity) · machine / deep learning · AI', TEALD, WHITE, 17);
}

// ---------- 15 QA + TAKE-HOME ----------
{
  const s = base('Quality assurance and take-home', 'Seeram (2019) §1.8 and §1.9.3; EI/DI: AAPM Report 116 (2009).',
    'D closes. QA and QC have three goals: patients get minimum dose, ALARA; the image quality is optimal for diagnosis; and radiology operations cost less. Digital systems have their own QC tests, for example dark noise and exposure index calibration. The technologist of the future is also an informaticist or PACS administrator. Three messages. One: film combined detector, display and archive in one object, with narrow latitude. Two: digital splits them: detector, computer, display, PACS. Three: wide latitude hides overexposure, so read the EI and DI, not just the image. Thank the class and invite questions. Remind everyone to credit the AI declaration on the last slide.');
  const msgs = [['1', 'Film = detector + display + archive in one, with narrow latitude.'], ['2', 'DR splits them: detector (CR / indirect / direct) → computer → display → PACS.'], ['3', 'Wide latitude hides overexposure: read the EI / DI, not just the image.']];
  msgs.forEach((m, i) => {
    const x = 0.5 + i * 4.215;
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.35, w: 3.9, h: 2.9, rectRadius: 0.1, fill: { color: i === 2 ? TEALD : PALE }, line: { color: PALE, width: 0.5 } });
    circle(s, x + 0.3, 1.6, 0.7, m[0], i === 2 ? AMB : NAVY, 24);
    txt(s, m[1], x + 0.3, 2.5, 3.3, 1.6, { size: 19, bold: true, color: i === 2 ? WHITE : INK });
  });
  txt(s, 'QA / QC aims', 0.5, 4.5, 4.0, 0.4, { size: 18, bold: true, color: NAVY });
  ['Minimum dose (ALARA)', 'Optimum image quality for diagnosis', 'Lower the cost of radiology operations'].forEach((t, i) => box(s, 0.5 + i * 4.215, 4.95, 3.9, 0.8, t, { fill: WHITE, line: NAVY, size: 17, bold: true }));
  band(s, 6.1, 0.7, 'The technologist of the future is also an informaticist', NAVY, WHITE, 20);
}

// ---------- REFERENCES / AI ----------
{
  const s = pres.addSlide();
  s.background = { color: WHITE };
  s.addText('References and AI declaration', { x: 0.5, y: 0.3, w: 12.3, h: 0.8, fontFace: HF, fontSize: 30, bold: true, color: NAVY, valign: 'middle', margin: 0, isTextBox: true });
  const refs = [
    'Seeram E. Digital Radiography: Physical Principles and Quality Control. 2nd ed. Springer; 2019. Ch. 1. doi:10.1007/978-981-13-3244-9_1 (primary source)',
    'Seibert JA. Dose metrics: exposure index (summary of AAPM TG-116 / IEC 62494-1). IUPESM teaching slides, 2015.',
    'Leblans P, et al. Storage phosphors for medical imaging. Materials 2011;4:1034-86 (PMC5448636).',
    'AAPM Report No. 116. An exposure indicator for digital radiography. 2009.',
    'IEC 62494-1:2008. Exposure index of digital X-ray imaging systems.',
    'Chest radiograph: "Chest Xray PA 3-8-2010.png", Stillwaterising, Wikimedia Commons, CC0 1.0. All exposure/film simulations were generated by the group from it.'
  ];
  txt(s, refs.map((r, i) => ({ text: r, options: { bullet: true, breakLine: i < refs.length - 1 } })), 0.5, 1.3, 12.3, 3.6, { size: 15, psa: 6 });
  box(s, 0.5, 5.15, 12.33, 1.7, 'AI declaration: Claude (Anthropic) assisted with planning, game design, scripting and slide drafting. The group checked all content against Seeram (2019) and the references above, and re-derived the game scores by simulation.', { fill: PALE, size: 17, align: 'left', margin: 14 });
  s.addNotes('D. References and AI declaration. Adjust the wording to the course regulation text if it differs.');
}

pres.writeFile({ fileName: path.join(__dirname, '..', process.env.OUT || 'DR_Overview.pptx') }).then(f => console.log('wrote', f));
