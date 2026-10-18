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
chk([8], 0.96, 98.0, 13.8, 182.2);
chk([10], 1.2, 100, 16.2, 183.8);
chk([15], 1.8, 100, 22.2, 177.8);
chk([40], 4.8, 94.7, 52.2, 137.2);
chk([2, 10], 1.2, 100, 21.6, 178.4);
chk([4, 10], 1.2, 100, 24.0, 176.0);
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
near(res[0].score, 183.8);
// sigma reference values
[[0.12, 0.226], [0.25, 0.12], [0.5, 0.050], [0.72, 0.021], [0.96, 0.0025]].forEach(([r, s]) => near(E.sigma(r), s, 0.002));
console.log('ALL ENGINE TESTS PASS');
