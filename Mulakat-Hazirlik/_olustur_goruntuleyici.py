# -*- coding: utf-8 -*-
"""Mülakat notlarını tek HTML görüntüleyiciye gömer. Çalıştırınca goruntule.html üretir."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MARKED = ROOT / "vendor" / "marked.min.js"
OUT = ROOT / "goruntule.html"

GROUPS = {
    "01-Kurum-Ilan-ve-Surec": "01  Kurum, ilan, süreç",
    "02-Guc-Sistemleri-Temelleri": "02  Temeller",
    "03-Iletim-Sebekeleri": "03  İletim",
    "04-Dagitim-Sistemleri": "04  Dağıtım",
    "05-Yuk-Akisi": "05  Yük akışı",
    "06-Kisa-Devre": "06  Kısa devre",
    "07-Guvenlik-Analizi": "07  Güvenlik",
    "08-Kararlilik": "08  Kararlılık",
    "09-Durum-Kestirimi": "09  Durum kestirimi",
    "10-Koruma-ve-Topraklama": "10  Koruma ve topraklama",
    "11-Ekonomik-Isletme": "11  Ekonomik işletme",
    "12-Planlama": "12  Planlama",
    "13-Optimizasyon": "13  Optimizasyon",
    "14-Programlama": "14  Programlama",
    "15-Analiz-Yazilimlari": "15  Analiz yazılımları",
    "16-Yazilim-Mimarisi": "16  Yazılım mimarisi",
    "17-Yenilenebilir-ve-Akilli-Sebeke": "17  Yenilenebilir ve akıllı şebeke",
    "18-Veri-ve-Yapay-Zeka": "18  Veri ve yapay zekâ",
    "19-Davranissal": "19  Davranışsal",
    "20-Soru-Bankasi": "20  Soru bankası",
    "21-Calisma-Plani": "21  Çalışma planı",
}


def title_of(text: str, fallback: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].replace("**", "").strip()
    return fallback


def group_of(rel: Path) -> str:
    if rel.parent == Path("."):
        return "Başlangıç"
    top = rel.parts[0]
    return GROUPS.get(top, top.replace("-", " "))


pages = []
for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT)
    if any(part.startswith("_") for part in rel.parts):
        continue
    body = path.read_text(encoding="utf-8")
    pages.append(
        {
            "id": rel.as_posix(),
            "group": group_of(rel),
            "title": title_of(body, path.stem),
            "body": body,
        }
    )

data = json.dumps(pages, ensure_ascii=False).replace("<", "\\u003c")
marked = MARKED.read_text(encoding="utf-8")

html = r"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TÜBİTAK MAM · Mülakat hazırlığı</title>
<style>
  :root {
    --bg: #f4f1ea;
    --ink: #1c1915;
    --muted: #6d655c;
    --line: #e3dcd0;
    --side: #fbf9f5;
    --accent: #0f6e56;
    --accent-soft: #e5f3ee;
    --speak: #fff7e8;
    --speak-line: #e0a106;
    --code: #f3eee6;
    --shadow: 0 1px 0 rgba(28, 25, 21, 0.04);
    color-scheme: light;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #121410;
      --ink: #ece7df;
      --muted: #a39b90;
      --line: #2a2d27;
      --side: #181b16;
      --accent: #7dcea0;
      --accent-soft: #1c2b24;
      --speak: #2a2416;
      --speak-line: #e0a106;
      --code: #1e211c;
      --shadow: none;
    }
  }
  * { box-sizing: border-box; }
  html, body { height: 100%; margin: 0; }
  body {
    font-family: "Segoe UI", system-ui, sans-serif;
    background: var(--bg);
    color: var(--ink);
  }
  .app { display: grid; grid-template-columns: 300px 1fr; height: 100%; }
  aside {
    background: var(--side);
    border-right: 1px solid var(--line);
    display: flex;
    flex-direction: column;
    min-height: 0;
  }
  .brand { padding: 22px 18px 12px; }
  .eyebrow {
    margin: 0 0 4px;
    font-size: 11px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    font-weight: 650;
  }
  .brand h1 { margin: 0; font-size: 18px; font-weight: 650; letter-spacing: -0.02em; }
  .brand p.sub { margin: 6px 0 0; color: var(--muted); font-size: 12.5px; line-height: 1.4; }
  .search { padding: 0 14px 12px; }
  .search input {
    width: 100%;
    border: 1px solid var(--line);
    background: var(--bg);
    color: var(--ink);
    border-radius: 10px;
    padding: 9px 12px;
    font: inherit;
    font-size: 14px;
    outline: none;
  }
  .search input:focus { border-color: var(--accent); }
  #nav { overflow: auto; padding: 4px 8px 24px; }
  .group {
    margin: 14px 10px 6px;
    font-size: 11px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 650;
  }
  #nav button {
    display: block;
    width: 100%;
    text-align: left;
    border: 0;
    background: transparent;
    color: var(--ink);
    font: inherit;
    font-size: 13.5px;
    line-height: 1.35;
    padding: 7px 10px;
    border-radius: 8px;
    cursor: pointer;
  }
  #nav button:hover { background: var(--accent-soft); }
  #nav button.on { background: var(--accent); color: #fff; }
  @media (prefers-color-scheme: dark) {
    #nav button.on { color: #102018; }
  }
  main { min-width: 0; overflow: auto; scroll-behavior: smooth; }
  .bar {
    position: sticky;
    top: 0;
    z-index: 2;
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 18px;
    background: color-mix(in srgb, var(--bg) 88%, transparent);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--line);
    box-shadow: var(--shadow);
  }
  .bar button, .menu {
    border: 1px solid var(--line);
    background: var(--side);
    color: var(--ink);
    border-radius: 8px;
    padding: 6px 10px;
    font: inherit;
    font-size: 13px;
    cursor: pointer;
  }
  .bar button:hover, .menu:hover { border-color: var(--accent); }
  .bar button:disabled { opacity: 0.4; cursor: default; }
  #pos { color: var(--muted); font-size: 12.5px; margin-right: auto; }
  .hint { color: var(--muted); font-size: 12px; }
  .menu { display: none; }
  article {
    max-width: 820px;
    margin: 0 auto;
    padding: 28px 28px 80px;
    font-size: 17px;
    line-height: 1.72;
  }
  article h1 { font-size: 1.85rem; letter-spacing: -0.03em; line-height: 1.2; margin: 0 0 0.6em; }
  article h2 { font-size: 1.28rem; margin: 1.6em 0 0.45em; letter-spacing: -0.02em; }
  article h3 { font-size: 1.05rem; margin: 1.3em 0 0.35em; }
  article p { margin: 0.7em 0; }
  article a { color: var(--accent); }
  article ul, article ol { padding-left: 1.25em; }
  article li { margin: 0.25em 0; }
  article code {
    font-family: Consolas, "Cascadia Code", ui-monospace, monospace;
    font-size: 0.88em;
    background: var(--code);
    padding: 0.1em 0.35em;
    border-radius: 5px;
  }
  article pre {
    background: var(--code);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 14px 16px;
    overflow: auto;
    line-height: 1.5;
  }
  article pre code { background: none; padding: 0; }
  article table { width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 0.95em; }
  article th, article td { border-bottom: 1px solid var(--line); text-align: left; padding: 8px 10px; vertical-align: top; }
  article th { font-size: 0.86em; color: var(--muted); font-weight: 650; }
  article blockquote {
    margin: 1.1em 0;
    padding: 0.7em 1em;
    border-left: 3px solid var(--accent);
    background: var(--accent-soft);
    border-radius: 0 12px 12px 0;
    color: var(--ink);
  }
  article hr { border: 0; border-top: 1px solid var(--line); margin: 1.6em 0; }
  .speak {
    margin: 1.4em 0;
    padding: 4px 16px 12px;
    background: var(--speak);
    border-radius: 14px;
    border: 1px solid color-mix(in srgb, var(--speak-line) 45%, var(--line));
  }
  .speak h2 { margin-top: 12px; }
  .speak h2::before {
    content: "Sesli söyle";
    display: block;
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--speak-line);
    font-weight: 700;
    margin-bottom: 4px;
  }
  .empty { color: var(--muted); padding: 28px 10px; font-size: 13.5px; }
  @media (max-width: 860px) {
    .app { grid-template-columns: 1fr; }
    aside {
      position: fixed;
      inset: 0 auto 0 0;
      width: min(320px, 88vw);
      z-index: 5;
      transform: translateX(-105%);
      transition: transform 0.18s ease;
      box-shadow: 8px 0 30px rgba(0,0,0,0.12);
    }
    aside.open { transform: none; }
    .menu { display: inline-flex; }
    .hint { display: none; }
    article { padding: 20px 16px 72px; }
  }
</style>
</head>
<body>
<div class="app">
  <aside id="side">
    <div class="brand">
      <p class="eyebrow">TÜBİTAK MAM</p>
      <h1>Mülakat hazırlığı</h1>
      <p class="sub">Bütün notlar bu sayfada. Soldan konu seç, okları ile ilerle.</p>
    </div>
    <div class="search">
      <input id="q" type="search" placeholder="Konu veya kelime ara" autocomplete="off">
    </div>
    <nav id="nav"></nav>
  </aside>
  <main id="main">
    <div class="bar">
      <button class="menu" id="menu" type="button">Konular</button>
      <button id="prev" type="button">Önceki</button>
      <button id="next" type="button">Sonraki</button>
      <span id="pos"></span>
      <span class="hint">← → sayfa · / ara</span>
    </div>
    <article id="doc"></article>
  </main>
</div>
<script>
__MARKED__
</script>
<script id="data" type="application/json">__DATA__</script>
<script>
const pages = JSON.parse(document.getElementById("data").textContent);
const nav = document.getElementById("nav");
const doc = document.getElementById("doc");
const q = document.getElementById("q");
const side = document.getElementById("side");
let index = 0;

function visible() {
  const needle = q.value.trim().toLocaleLowerCase("tr");
  if (!needle) return pages.map((_, i) => i);
  return pages.flatMap((p, i) => {
    const hay = (p.title + "\n" + p.group + "\n" + p.body).toLocaleLowerCase("tr");
    return hay.includes(needle) ? [i] : [];
  });
}

function renderNav() {
  const ids = visible();
  nav.innerHTML = "";
  if (!ids.length) {
    const p = document.createElement("p");
    p.className = "empty";
    p.textContent = "Eşleşen sayfa yok.";
    nav.appendChild(p);
    return;
  }
  let group = "";
  for (const i of ids) {
    const page = pages[i];
    if (page.group !== group) {
      group = page.group;
      const label = document.createElement("div");
      label.className = "group";
      label.textContent = group;
      nav.appendChild(label);
    }
    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = page.title;
    if (i === index) btn.className = "on";
    btn.addEventListener("click", () => openPage(i));
    nav.appendChild(btn);
  }
  const on = nav.querySelector(".on");
  if (on) on.scrollIntoView({ block: "nearest" });
}

function dress() {
  doc.querySelectorAll("h2").forEach((h) => {
    if (!/90 saniye/i.test(h.textContent)) return;
    const box = document.createElement("section");
    box.className = "speak";
    h.parentNode.insertBefore(box, h);
    box.appendChild(h);
    while (box.nextSibling) {
      const n = box.nextSibling;
      if (n.tagName && /^H[12]$/.test(n.tagName)) break;
      box.appendChild(n);
    }
  });
}

function openPage(i, push) {
  index = i;
  const page = pages[i];
  doc.innerHTML = marked.parse(page.body);
  dress();
  document.title = page.title + " · Mülakat hazırlığı";
  const ids = visible();
  const at = ids.indexOf(i);
  document.getElementById("pos").textContent = (i + 1) + " / " + pages.length;
  document.getElementById("prev").disabled = i <= 0;
  document.getElementById("next").disabled = i >= pages.length - 1;
  if (push !== false) history.replaceState(null, "", "#" + encodeURIComponent(page.id));
  document.getElementById("main").scrollTop = 0;
  side.classList.remove("open");
  renderNav();
  if (at < 0 && q.value) {
    /* arama bu sayfayı elemişse liste yine de güncel kalsın */
  }
}

function step(dir) {
  const next = index + dir;
  if (next < 0 || next >= pages.length) return;
  openPage(next);
}

document.getElementById("prev").addEventListener("click", () => step(-1));
document.getElementById("next").addEventListener("click", () => step(1));
document.getElementById("menu").addEventListener("click", () => side.classList.toggle("open"));
q.addEventListener("input", renderNav);
document.addEventListener("keydown", (e) => {
  const typing = e.target === q;
  if (e.key === "/" && !typing) {
    e.preventDefault();
    q.focus();
    return;
  }
  if (typing) return;
  if (e.key === "ArrowLeft") step(-1);
  if (e.key === "ArrowRight") step(1);
});

const start = decodeURIComponent(location.hash.slice(1));
const found = pages.findIndex((p) => p.id === start);
openPage(found >= 0 ? found : 0, false);
</script>
</body>
</html>
"""

html = html.replace("__MARKED__", marked).replace("__DATA__", data)
OUT.write_text(html, encoding="utf-8")
print(f"{len(pages)} sayfa -> {OUT} ({OUT.stat().st_size} bayt)")
