const E = require('./engine.js');
const assert = require('assert');
const near = (a, b, t = 0.1) => assert(Math.abs(a - b) <= t, `${a} vs ${b}`);
const idx = c => E.CARDS.findIndex(x => Math.abs(x - c) < 1e-9);
function chk(cards, r, Q, D, S) {
  const o = E.play(cards.map(idx));
  near(o.r, r, 0.01); near(o.Q, Q); near(o.D, D); near(o.score, S);
}
chk([], 0.12, 34.6, 1.2, 68.1);
chk([6], 0.72, 84.9, 11.4, 158.3);
chk([3, 3], 1.08, 100, 21.6, 178.4);
chk([2, 4], 0.96, 98.0, 19.2, 176.8);
chk([4, 2], 0.96, 98.0, 21.6, 174.4);
chk([3, 4], 1.44, 100, 25.2, 174.8);
chk([4, 4], 1.92, 100, 31.2, 168.8);
chk([2, 2, 2], 0.96, 98.0, 27.0, 169.0);
chk([6, 6], 4.32, 97.8, 57.6, 137.9);
// exhaustive top-3
const res = [];
function rec(seq) {
  const o = E.play(seq);
  if (o.steps === seq.length) res.push({ seq: seq.slice(), ...o });
  if (seq.length < 4) for (let i = 0; i < 8; i++) { seq.push(i); rec(seq); seq.pop(); }
}
rec([]);
res.sort((a, b) => b.score - a.score);
console.log('TOP3', res.slice(0, 3).map(x => x.seq.map(i => E.CARD_LABELS[i]).join('>') + ' ' + x.score.toFixed(1)));
near(res[0].score, 178.4);
// sigma reference values
[[0.12, 0.226], [0.25, 0.12], [0.5, 0.050], [0.72, 0.021], [0.96, 0.0025]].forEach(([r, s]) => near(E.sigma(r), s, 0.002));
console.log('ALL ENGINE TESTS PASS');
