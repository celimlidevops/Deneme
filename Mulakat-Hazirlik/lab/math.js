/** Küçük kompleks / lineer cebir yardımcıları (eğitici lab için). */
window.LabMath = (() => {
  function c(re = 0, im = 0) {
    return { re, im };
  }
  function cadd(a, b) {
    return c(a.re + b.re, a.im + b.im);
  }
  function csub(a, b) {
    return c(a.re - b.re, a.im - b.im);
  }
  function cmul(a, b) {
    return c(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re);
  }
  function cdiv(a, b) {
    const d = b.re * b.re + b.im * b.im;
    return c((a.re * b.re + a.im * b.im) / d, (a.im * b.re - a.re * b.im) / d);
  }
  function cconj(a) {
    return c(a.re, -a.im);
  }
  function fromPolar(mag, ang) {
    return c(mag * Math.cos(ang), mag * Math.sin(ang));
  }
  function solve(A, b) {
    const n = b.length;
    const M = A.map((row, i) => [...row, b[i]]);
    for (let col = 0; col < n; col++) {
      let piv = col;
      for (let r = col + 1; r < n; r++) {
        if (Math.abs(M[r][col]) > Math.abs(M[piv][col])) piv = r;
      }
      [M[col], M[piv]] = [M[piv], M[col]];
      const diag = M[col][col];
      if (Math.abs(diag) < 1e-14) throw new Error("tekil matris");
      for (let j = col; j <= n; j++) M[col][j] /= diag;
      for (let r = 0; r < n; r++) {
        if (r === col) continue;
        const f = M[r][col];
        for (let j = col; j <= n; j++) M[r][j] -= f * M[col][j];
      }
    }
    return M.map((row) => row[n]);
  }
  return { c, cadd, csub, cmul, cdiv, cconj, fromPolar, solve };
})();
