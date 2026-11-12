const KATALOG = [
  { id: "01-00", baslik: "Klasör haritası", grup: "01  Kurum, ilan, süreç" },
  { id: "01-01", baslik: "İlan, puan ve mülakat", grup: "01  Kurum, ilan, süreç" },
  { id: "01-02", baslik: "MAM, YTBS, SIPS ve Türkiye şebekesi", grup: "01  Kurum, ilan, süreç" },
  { id: "01-03", baslik: "Güncel projeler, yayınlar, ürünler", grup: "01  Kurum, ilan, süreç" },
  { id: "01-04", baslik: "Tercih sebebi ve kanıt", grup: "01  Kurum, ilan, süreç" },
  { id: "01-05", baslik: "Envanter ve online değerlendirme", grup: "01  Kurum, ilan, süreç" }
];

const ANAHTAR = "mam-secmeli:";
const ekran = document.getElementById("ekran");
const baslik = document.getElementById("baslik");
const grupEl = document.getElementById("grup");
const alt = document.getElementById("alt");
const geri = document.getElementById("geri");
const bar = document.getElementById("bar");
const dolu = document.getElementById("dolu");
const sayfa = new URLSearchParams(location.search).get("sayfa");

function kacis(s) {
  return String(s).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
}

function oku(id) {
  try { return JSON.parse(localStorage.getItem(ANAHTAR + id) || "null"); }
  catch { return null; }
}

function yaz(id, veri) {
  localStorage.setItem(ANAHTAR + id, JSON.stringify(veri));
}

function taze(n) {
  return { toplam: n, ogrenilen: [], kuyruk: Array.from({ length: n }, (_, i) => i), yanlis: {} };
}

function duzelt(paket, kayit) {
  const n = paket.sorular.length;
  if (!kayit || !Array.isArray(kayit.kuyruk) || !Array.isArray(kayit.ogrenilen)) {
    return taze(n);
  }
  kayit.toplam = n;
  const gecer = (i) => Number.isInteger(i) && i >= 0 && i < n;
  kayit.ogrenilen = [...new Set(kayit.ogrenilen.filter(gecer))];
  const bildi = new Set(kayit.ogrenilen);
  kayit.kuyruk = kayit.kuyruk.filter((i) => gecer(i) && !bildi.has(i));
  for (let i = 0; i < n; i++) {
    if (!bildi.has(i) && !kayit.kuyruk.includes(i)) kayit.kuyruk.push(i);
  }
  kayit.yanlis = kayit.yanlis || {};
  return kayit;
}

function menu() {
  grupEl.textContent = "01  Kurum, ilan, süreç";
  baslik.textContent = "Hangi sayfayı deneyeceksin?";
  alt.textContent = "Çoktan seçmeli. Bilemediğin soru bu tarayıcıda kalır.";
  bar.hidden = true;
  ekran.innerHTML = `<div class="liste">${KATALOG.map((k) => {
    const kayit = oku(k.id);
    let durum = "Henüz başlamadın";
    if (kayit && kayit.toplam) {
      const kalan = kayit.toplam - (kayit.ogrenilen || []).length;
      durum = kalan === 0 ? "Hepsi öğrenildi" : `${kalan} soru kaldı`;
    }
    return `<a href="test.html?sayfa=${k.id}">${kacis(k.baslik)}<small>${durum}</small></a>`;
  }).join("")}</div>`;
}

function karistir(dizi) {
  const kopya = dizi.slice();
  for (let i = kopya.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [kopya[i], kopya[j]] = [kopya[j], kopya[i]];
  }
  return kopya;
}

function ilerleme(paket, kayit) {
  const oran = paket.sorular.length ? (kayit.ogrenilen.length / paket.sorular.length) * 100 : 0;
  bar.hidden = false;
  dolu.style.width = oran + "%";
}

async function yukle() {
  if (!sayfa) { menu(); return; }
  let paket;
  try {
    const yanit = await fetch("sorular/" + sayfa + ".json");
    if (!yanit.ok) throw new Error(String(yanit.status));
    paket = await yanit.json();
  } catch {
    baslik.textContent = "Sorular açılmadı";
    alt.textContent = "Sayfayı sunucudan aç. Dosyaya çift tıklarsan soru dosyası okunamaz.";
    ekran.innerHTML = `<p><a class="linkbuton asil" href="test.html">Sayfa listesine dön</a></p>`;
    return;
  }
  geri.href = paket.geri || "goruntule.html";
  grupEl.textContent = paket.grup || "";
  baslik.textContent = paket.baslik;
  ciz(paket, duzelt(paket, oku(paket.id)));
}

function ciz(paket, kayit) {
  yaz(paket.id, kayit);
  ilerleme(paket, kayit);
  if (kayit.kuyruk.length === 0) { sonuc(paket, kayit); return; }
  const indeks = kayit.kuyruk[0];
  const soru = paket.sorular[indeks];
  const secenekler = karistir(soru.secenekler.map((metin, i) => ({ metin, i })));
  const tekrar = (kayit.yanlis[indeks] || 0) > 0;
  alt.textContent = tekrar
    ? `Yeniden: ${kayit.ogrenilen.length} / ${paket.sorular.length} öğrenildi. Kuyrukta ${kayit.kuyruk.length} soru var.`
    : `${kayit.ogrenilen.length} / ${paket.sorular.length} öğrenildi. Kuyrukta ${kayit.kuyruk.length} soru var.`;
  ekran.innerHTML = `
    <section class="soru"><p>${kacis(soru.soru)}</p></section>
    <div class="secenekler" id="secenekler">
      ${secenekler.map((s, gorunen) => `<button type="button" class="secenek" data-i="${s.i}">${kacis(s.metin)}</button>`).join("")}
    </div>
    <div class="cevap" id="sonuc" hidden></div>
    <div class="satir"><button type="button" class="asil" id="devam" hidden>Devam</button></div>`;
  const dugmeler = [...ekran.querySelectorAll(".secenek")];
  dugmeler.forEach((dugme) => {
    dugme.addEventListener("click", () => {
      if (dugme.disabled) return;
      const secilen = Number(dugme.dataset.i);
      const bildi = secilen === soru.dogru;
      dugmeler.forEach((d) => {
        d.disabled = true;
        if (Number(d.dataset.i) === soru.dogru) d.classList.add("dogru");
        else if (d === dugme) d.classList.add("yanlis");
      });
      const kutu = document.getElementById("sonuc");
      kutu.hidden = false;
      kutu.innerHTML = bildi
        ? `<p class="etiket">Doğru</p><p>${kacis(soru.neden || soru.secenekler[soru.dogru])}</p>`
        : `<p class="etiket">Bu soru yeniden gelecek</p><p>${kacis(soru.neden || ("Doğru cevap: " + soru.secenekler[soru.dogru]))}</p>`;
      document.getElementById("devam").hidden = false;
      document.getElementById("devam").onclick = () => {
        if (bildi) {
          kayit.ogrenilen.push(indeks);
          kayit.kuyruk.shift();
        } else {
          kayit.yanlis[indeks] = (kayit.yanlis[indeks] || 0) + 1;
          kayit.kuyruk.shift();
          kayit.kuyruk.push(indeks);
        }
        ciz(paket, kayit);
      };
    });
  });
}

function sonuc(paket, kayit) {
  const yanlisAdet = Object.values(kayit.yanlis).reduce((a, b) => a + b, 0);
  alt.textContent = "Bu sayfadaki soruların hepsini en az bir kez doğru bildin.";
  dolu.style.width = "100%";
  ekran.innerHTML = `
    <div class="ozet">
      <div><strong>${paket.sorular.length}</strong><span>Soru</span></div>
      <div><strong>${yanlisAdet}</strong><span>Yanlış deneme</span></div>
      <div><strong>${kayit.ogrenilen.length}</strong><span>Öğrenilen</span></div>
    </div>
    <div class="satir">
      <button type="button" class="asil" id="bastan">Baştan başla</button>
      <a class="linkbuton" href="test.html">Diğer sayfalar</a>
    </div>`;
  document.getElementById("bastan").onclick = () => ciz(paket, taze(paket.sorular.length));
}

yukle();
