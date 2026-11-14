/** 3 bara NR + gömülü IEEE 14 sonuçları */
window.NrLab = (() => {
  const { c, cadd, csub, cmul, cdiv, cconj, fromPolar, solve } = window.LabMath;

  const ORNEK = {
    hatlar: [
      { i: 0, j: 1, r: 0.02, x: 0.1, b: 0 },
      { i: 0, j: 2, r: 0.04, x: 0.2, b: 0 },
      { i: 1, j: 2, r: 0.05, x: 0.25, b: 0 },
    ],
    tip: ["slack", "pv", "pq"],
    p: [0, 0.5, -0.8],
    q: [0, 0, -0.3],
    v0: [1.0, 1.02, 1.0],
  };

  const IEEE14 = {
    iterasyon: 5,
    artiklar: [0.9219, 0.1005, 7.06e-4, 4.99e-8, 2.19e-14],
    v: [1.06, 1.045, 1.01, 1.0173, 1.0193, 1.07, 1.0604, 1.09, 1.0537, 1.0491, 1.056, 1.055, 1.0501, 1.0341],
    teta_deg: [0, -4.983, -12.727, -10.307, -8.773, -14.24, -13.348, -13.348, -14.927, -15.091, -14.796, -15.094, -15.171, -16.036],
    pp: {
      v: [1.06, 1.045, 1.01, 1.0177, 1.0195, 1.07, 1.0615, 1.09, 1.0559, 1.051, 1.0569, 1.0552, 1.0504, 1.0355],
      teta_deg: [0, -4.983, -12.725, -10.313, -8.774, -14.221, -13.36, -13.36, -14.939, -15.097, -14.791, -15.076, -15.156, -16.034],
      max_dv: 0.00225,
      max_dtheta_deg: 0.0192,
    },
    hatlar: [
      [1, 2], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [4, 5], [4, 7], [4, 9], [5, 6],
      [6, 11], [6, 12], [6, 13], [7, 8], [7, 9], [9, 10], [9, 14], [10, 11], [12, 13], [13, 14],
    ],
  };

  function ybusKur(n, hatlar) {
    const Y = Array.from({ length: n }, () => Array.from({ length: n }, () => c(0, 0)));
    for (const h of hatlar) {
      const y = cdiv(c(1, 0), c(h.r, h.x));
      const ys = c(0, h.b / 2);
      Y[h.i][h.i] = cadd(Y[h.i][h.i], cadd(y, ys));
      Y[h.j][h.j] = cadd(Y[h.j][h.j], cadd(y, ys));
      Y[h.i][h.j] = csub(Y[h.i][h.j], y);
      Y[h.j][h.i] = csub(Y[h.j][h.i], y);
    }
    return Y;
  }

  function gucEnjeksiyonu(Y, v, teta) {
    const n = v.length;
    const vc = v.map((mag, i) => fromPolar(mag, teta[i]));
    const I = Array.from({ length: n }, () => c(0, 0));
    for (let i = 0; i < n; i++) {
      for (let k = 0; k < n; k++) I[i] = cadd(I[i], cmul(Y[i][k], vc[k]));
    }
    return vc.map((vi, i) => cmul(vi, cconj(I[i])));
  }

  function jacobian(Y, v, teta, pvpq, pq) {
    const n = v.length;
    const G = Y.map((row) => row.map((z) => z.re));
    const B = Y.map((row) => row.map((z) => z.im));
    const S = gucEnjeksiyonu(Y, v, teta);
    const P = S.map((s) => s.re);
    const Q = S.map((s) => s.im);
    const H = Array.from({ length: n }, () => Array(n).fill(0));
    const N = Array.from({ length: n }, () => Array(n).fill(0));
    const M = Array.from({ length: n }, () => Array(n).fill(0));
    const L = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++) {
      for (let k = 0; k < n; k++) {
        if (i === k) {
          H[i][i] = -Q[i] - B[i][i] * v[i] ** 2;
          N[i][i] = P[i] / v[i] + G[i][i] * v[i];
          M[i][i] = P[i] - G[i][i] * v[i] ** 2;
          L[i][i] = Q[i] / v[i] - B[i][i] * v[i];
        } else {
          const t = teta[i] - teta[k];
          H[i][k] = v[i] * v[k] * (G[i][k] * Math.sin(t) - B[i][k] * Math.cos(t));
          N[i][k] = v[i] * (G[i][k] * Math.cos(t) + B[i][k] * Math.sin(t));
          M[i][k] = -v[i] * v[k] * (G[i][k] * Math.cos(t) + B[i][k] * Math.sin(t));
          L[i][k] = v[i] * (G[i][k] * Math.sin(t) - B[i][k] * Math.cos(t));
        }
      }
    }
    return [
      ...pvpq.map((i) => [...pvpq.map((j) => H[i][j]), ...pq.map((j) => N[i][j])]),
      ...pq.map((i) => [...pvpq.map((j) => M[i][j]), ...pq.map((j) => L[i][j])]),
    ];
  }

  function nrAdim(state) {
    const { Y, tip, p, q, v, teta, tol } = state;
    const n = v.length;
    const pvpq = [...Array(n).keys()].filter((i) => tip[i] !== "slack");
    const pq = [...Array(n).keys()].filter((i) => tip[i] === "pq");
    const S = gucEnjeksiyonu(Y, v, teta);
    const artik = [...pvpq.map((i) => p[i] - S[i].re), ...pq.map((i) => q[i] - S[i].im)];
    const enBuyuk = artik.length ? Math.max(...artik.map(Math.abs)) : 0;
    if (enBuyuk < tol) {
      return { ...state, S, artik, enBuyuk, yakinsadi: true, dx: null };
    }
    const J = jacobian(Y, v, teta, pvpq, pq);
    const dx = solve(J, artik);
    const v2 = [...v];
    const teta2 = [...teta];
    pvpq.forEach((bus, k) => { teta2[bus] += dx[k]; });
    pq.forEach((bus, k) => { v2[bus] += dx[pvpq.length + k]; });
    return { ...state, v: v2, teta: teta2, S, artik, enBuyuk, yakinsadi: false, dx, pvpq, pq };
  }

  function nrBaslat(opts = {}) {
    const base = { ...ORNEK, ...opts };
    return {
      Y: ybusKur(3, base.hatlar),
      tip: [...base.tip],
      p: [...base.p],
      q: [...base.q],
      v: [...base.v0],
      teta: [0, 0, 0],
      tol: 1e-8,
      iterasyon: 0,
      artiklar: [],
      yakinsadi: false,
    };
  }

  return { ORNEK, IEEE14, nrBaslat, nrAdim };
})();
