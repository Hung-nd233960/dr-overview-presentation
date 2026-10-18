// Shared engine: scoring + image rendering helpers (pure functions, node-testable)
(function (root) {
  'use strict';
  const R0 = 1 / 8.33;          // hidden start exposure (fraction of ideal)
  const RETAKE = 3;             // fixed per-retake dose cost
  const LIMIT = 50;             // dose limit
  const CARDS = [1 / 6, 1 / 4, 1 / 3, 1 / 2, 1.5, 2, 3, 4, 6];
  const CARD_LABELS = ['×⅙', '×¼', '×⅓', '×½', '×1.5', '×2', '×3', '×4', '×6'];
  const SIGMA0 = 0.12;          // noise constant (full-scale units)

  function quality(r) {
    if (r < 1) return 100 * Math.sqrt(r);
    if (r <= 4) return 100;
    return Math.max(0, 100 - 20 * Math.log2(r / 4));
  }
  function doseOf(r) { return 10 * r; }
  function di(r) { return 10 * Math.log10(r); }
  function sigma(r) { return r >= 1 ? 0 : SIGMA0 * (1 / Math.sqrt(r) - 1); }
  function satThreshold(r) { return r > 4 ? Math.min(0.5, 0.3 * Math.log2(r / 4)) : 0; }

  // play a sequence of card indexes; stops early if dose limit is reached (checked before each card)
  function play(seq, r0) {
    r0 = r0 === undefined ? R0 : r0;
    let r = r0, D = doseOf(r0), n = 0;
    for (const ci of seq) {
      if (D >= LIMIT) break;
      r *= CARDS[ci]; D += doseOf(r) + RETAKE; n++;
    }
    const Q = quality(r);
    return { r, D, Q, score: 2 * Q - D, steps: n };
  }

  // mulberry32 seeded PRNG
  function rng(seed) {
    let a = seed >>> 0;
    return function () {
      a = (a + 0x6D2B79F5) >>> 0;
      let t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function gauss(rand) {
    let u = 0, v = 0;
    while (u === 0) u = rand();
    v = rand();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }

  // base: Float32Array/Array of v in [0,1], size n*n. returns Uint8ClampedArray gray n*n.
  function renderDR(base, n, r, seed) {
    const out = new Uint8ClampedArray(n * n);
    const s = sigma(r), t = satThreshold(r);
    const m = n >> 1;
    let noise = null;
    if (s > 0) {
      const rand = rng(seed);
      noise = new Float32Array(m * m);
      for (let i = 0; i < noise.length; i++) noise[i] = gauss(rand) * s;
    }
    for (let y = 0; y < n; y++) {
      for (let x = 0; x < n; x++) {
        let v = base[y * n + x];
        if (noise) {
          const fx = Math.min(m - 1.001, (x + 0.5) / 2 - 0.5), fy = Math.min(m - 1.001, (y + 0.5) / 2 - 0.5);
          const x0 = Math.max(0, Math.floor(fx)), y0 = Math.max(0, Math.floor(fy));
          const ax = Math.max(0, fx - x0), ay = Math.max(0, fy - y0);
          const a = noise[y0 * m + x0], b = noise[y0 * m + x0 + 1], c = noise[(y0 + 1) * m + x0], d = noise[(y0 + 1) * m + x0 + 1];
          v += (a * (1 - ax) + b * ax) * (1 - ay) + (c * (1 - ax) + d * ax) * ay;
        }
        if (t > 0 && v < t) v = 0;
        out[y * n + x] = Math.max(0, Math.min(1, v)) * 255;
      }
    }
    return out;
  }

  // Film: sigmoid (H&D-like) mapping in logit space; r = 1 reproduces the base image.
  function renderFilm(base, n, r) {
    const out = new Uint8ClampedArray(n * n);
    const sh = 2.0 * Math.log(r);
    for (let i = 0; i < n * n; i++) {
      let e = 1 - base[i];
      e = Math.max(0.02, Math.min(0.98, e));
      const y = Math.log(e / (1 - e)) + sh;
      const d = 1 / (1 + Math.exp(-y));
      out[i] = (1 - d) * 255;
    }
    return out;
  }

  const api = { R0, RETAKE, LIMIT, CARDS, CARD_LABELS, SIGMA0, quality, doseOf, di, sigma, satThreshold, play, rng, gauss, renderDR, renderFilm };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.Engine = api;
})(typeof window !== 'undefined' ? window : globalThis);
