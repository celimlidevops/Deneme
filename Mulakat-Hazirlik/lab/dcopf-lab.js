window.DcOpfLab = (() => {
  const { solve } = window.LabMath;
  const SEBEKE = { x: { "1-2": 0.1, "1-3": 0.2, "2-3": 0.25 } };

  function maliyet(p1, p2) {
    return 0.02 * p1 * p1 + 4 * p1 + 0.03 * p2 * p2 + 3 * p2;
  }
  function artan(p1, p2) {
    return [0.04 * p1 + 4, 0.06 * p2 + 3];
  }

  function ekonomikDagitim(talep, p1Max = 100, p2Max = 100) {
    let p1 = 0.6 * talep - 10;
    let p2 = talep - p1;
    p1 = Math.min(Math.max(p1, 0), p1Max);
    p2 = talep - p1;
    if (p2 < 0) { p2 = 0; p1 = Math.min(talep, p1Max); }
    if (p2 > p2Max) { p2 = p2Max; p1 = Math.min(talep - p2, p1Max); }
    const [l1, l2] = artan(p1, p2);
    let lambda = l1;
    if (p1 <= 1e-9 || p1 >= p1Max - 1e-9) lambda = l2;
    else if (p2 <= 1e-9 || p2 >= p2Max - 1e-9) lambda = l1;
    else lambda = (l1 + l2) / 2;
    return { p1, p2, lambda, maliyet: maliyet(p1, p2) };
  }

  function dcYukAkisi(pEnj, x = SEBEKE.x) {
    const b12 = 1 / x["1-2"], b13 = 1 / x["1-3"], b23 = 1 / x["2-3"];
    const B = [[b12 + b23, -b23], [-b23, b13 + b23]];
    const th = solve(B, [pEnj[2] ?? 0, pEnj[3] ?? 0]);
    const teta = { 1: 0, 2: th[0], 3: th[1] };
    const akis = {
      "1-2": (teta[1] - teta[2]) / x["1-2"],
      "1-3": (teta[1] - teta[3]) / x["1-3"],
      "2-3": (teta[2] - teta[3]) / x["2-3"],
    };
    return { teta, akis, p1: -akis["1-2"] - akis["1-3"] };
  }

  function dcOpf({ talepMw = 100, p2Max = 100, f13MaxPu = 0.8, sbase = 100 }) {
    const ed = ekonomikDagitim(talepMw, 100, p2Max);
    let p2 = ed.p2 / sbase;
    let p3 = -talepMw / sbase;
    let p1 = -p2 - p3;
    let flow = dcYukAkisi({ 2: p2, 3: p3 });
    let congested = Math.abs(flow.akis["1-3"]) > f13MaxPu + 1e-9;
    let mu = 0;

    if (congested) {
      let best = null;
      for (let p2mw = 0; p2mw <= Math.min(p2Max, talepMw); p2mw += 0.25) {
        const f = dcYukAkisi({ 2: p2mw / sbase, 3: -talepMw / sbase });
        const ok = Math.abs(f.akis["1-3"]) <= f13MaxPu + 1e-6;
        const cost = maliyet(talepMw - p2mw, p2mw);
        if (ok && (best == null || cost < best.cost)) {
          best = { p2mw, p1mw: talepMw - p2mw, flow: f, cost };
        }
      }
      if (best) {
        p2 = best.p2mw / sbase;
        p1 = best.p1mw / sbase;
        flow = best.flow;
        congested = Math.abs(flow.akis["1-3"]) > f13MaxPu - 1e-4;
        mu = congested ? 8 : 0;
      }
    }

    const p1mw = p1 * sbase;
    const p2mw = p2 * sbase;
    const [mc1, mc2] = artan(p1mw, p2mw);
    const lambda = congested ? Math.min(mc1, mc2) : (mc1 + mc2) / 2;
    const lmp = {
      1: lambda,
      2: lambda + (congested ? mu * 0.3 : 0),
      3: lambda + (congested ? mu : 0),
    };
    return { p1mw, p2mw, maliyet: maliyet(p1mw, p2mw), ed, flow, congested, f13MaxPu, lmp, mu, mc: [mc1, mc2] };
  }

  return { dcOpf, ekonomikDagitim, dcYukAkisi, maliyet };
})();
