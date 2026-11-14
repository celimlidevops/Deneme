window.WlsLab = (() => {
  const { solve } = window.LabMath;
  const OLCUM_ADLARI = ["P12", "P13", "P23", "P2"];

  function model() {
    const H = [
      [-10, 0],
      [0, -5],
      [4, -4],
      [14, -4],
    ];
    const tetaGercek = [1.3 / 110, -9.2 / 110];
    return { H, tetaGercek };
  }

  function invert2(G) {
    const det = G[0][0] * G[1][1] - G[0][1] * G[1][0];
    return [
      [G[1][1] / det, -G[0][1] / det],
      [-G[1][0] / det, G[0][0] / det],
    ];
  }

  function kestir(H, z, sigma) {
    const m = z.length;
    const n = H[0].length;
    const Wdiag = sigma.map((s) => 1 / (s * s));
    const G = Array.from({ length: n }, () => Array(n).fill(0));
    const HTw = Array.from({ length: n }, () => Array(m).fill(0));
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) HTw[i][j] = H[j][i] * Wdiag[j];
    }
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        let s = 0;
        for (let k = 0; k < m; k++) s += HTw[i][k] * H[k][j];
        G[i][j] = s;
      }
    }
    const rhs = Array(n).fill(0);
    for (let i = 0; i < n; i++) {
      for (let k = 0; k < m; k++) rhs[i] += HTw[i][k] * z[k];
    }
    const x = solve(G, rhs);
    const Hx = H.map((row) => row[0] * x[0] + row[1] * x[1]);
    const r = z.map((zi, i) => zi - Hx[i]);
    const Ginv = invert2(G);
    const omega = Array(m).fill(0);
    for (let i = 0; i < m; i++) {
      let hGh = 0;
      for (let a = 0; a < n; a++) {
        for (let b = 0; b < n; b++) hGh += H[i][a] * Ginv[a][b] * H[i][b];
      }
      omega[i] = Math.max(sigma[i] ** 2 - hGh, 1e-14);
    }
    const rN = r.map((ri, i) => Math.abs(ri) / Math.sqrt(omega[i]));
    let J = 0;
    for (let i = 0; i < m; i++) J += r[i] * Wdiag[i] * r[i];
    return { x, r, rN, J, Hx };
  }

  function olcumUret(bozukP23 = 0) {
    const { H, tetaGercek } = model();
    const zTemiz = H.map((row) => row[0] * tetaGercek[0] + row[1] * tetaGercek[1]);
    const z = [...zTemiz];
    z[2] += bozukP23;
    return { H, tetaGercek, z, zTemiz, sigma: [0.01, 0.01, 0.01, 0.02] };
  }

  return { OLCUM_ADLARI, kestir, olcumUret };
})();
