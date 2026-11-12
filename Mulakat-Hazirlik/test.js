const KATALOG = [
  { id: "01-00", baslik: "Klasör haritası", grup: "01  Kurum, ilan, süreç" },
  { id: "01-01", baslik: "İlan, puan ve mülakat", grup: "01  Kurum, ilan, süreç" },
  { id: "01-02", baslik: "MAM, YTBS, SIPS ve Türkiye şebekesi", grup: "01  Kurum, ilan, süreç" },
  { id: "01-03", baslik: "Güncel projeler, yayınlar, ürünler", grup: "01  Kurum, ilan, süreç" },
  { id: "01-04", baslik: "Tercih sebebi ve kanıt", grup: "01  Kurum, ilan, süreç" },
  { id: "01-05", baslik: "Envanter ve online değerlendirme", grup: "01  Kurum, ilan, süreç" }
];

const ekran = document.getElementById("ekran");
const baslik = document.getElementById("baslik");
const grupEl = document.getElementById("grup");
const alt = document.getElementById("alt");
const geri = document.getElementById("geri");
const bar = document.getElementById("bar");
const dolu = document.getElementById("dolu");

const sayfa = new URLSearchParams(location.search).get("sayfa");

function kacis(s) {
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function menu() {
  grupEl.textContent = "01  Kurum, ilan, süreç";
  baslik.textContent = "Hangi sayfayı deneyeceksin?";
  alt.textContent = "Her sayfanın soruları kendi dosyasında. Cevabı önce sen yaz.";
  ekran.innerHTML = `<div class="liste">${KATALOG.map((k) => {
    const kayit = oku(k.id);
    const n = kayit && kayit.bitti ? "Son tur bitti" : "Henüz bitmedi";
    return `<a href="test.html?sayfa=${k.id}">${kacis(k.baslik)}<small>${n}</small></a>`;
  }).join("")}</div>`;
}

function oku(id) {
  try {
    return JSON.parse(localStorage.getItem("mam-quiz:" + id) || "null");
  } catch {
    return null;
  }
}

function yaz(id, veri) {
  localStorage.setItem("mam-quiz:" + id, JSON.stringify(veri));
}

async function yukle() {
  if (!sayfa) {
    menu();
    return;
  }
  let paket;
  try {
    const yanit = await fetch("sorular/" + sayfa + ".json");
    if (!yanit.ok) throw new Error(String(yanit.status));
    paket = await yanit.json();
  } catch {
    baslik.textContent = "Sorular açılmadı";
    alt.textContent = "Bu adres sunucudan açılmalı. Dosyayı çift tıklayarak açarsan JSON okunamaz.";
    ekran.innerHTML = `<p><a class="linkbuton asil" href="test.html">Sayfa listesine dön</a></p>`;
    return;
  }
  geri.href = paket.geri || "goruntule.html";
  grupEl.textContent = paket.grup || "";
  baslik.textContent = paket.baslik;
  const kayit = oku(paket.id) || { sira: 0, notlar: {}, tur: "hepsi" };
  if (!Array.isArray(kayit.kuyruk) || kayit.kuyruk.length !== paket.sorular.length && kayit.tur === "hepsi") {
    kayit.kuyruk = paket.sorular.map((_, i) => i);
    kayit.sira = 0;
    kayit.notlar = {};
    kayit.tur = "hepsi";
    kayit.bitti = false;
  }
  ciz(paket, kayit);
}

function ilerleme(kayit) {
  const oran = kayit.kuyruk.length ? (kayit.sira / kayit.kuyruk.length) * 100 : 0;
  bar.hidden = false;
  dolu.style.width = oran + "%";
}

function ciz(paket, kayit) {
  yaz(paket.id, kayit);
  if (kayit.sira >= kayit.kuyruk.length) {
    sonuc(paket, kayit);
    return;
  }
  const indeks = kayit.kuyruk[kayit.sira];
  const soru = paket.sorular[indeks];
  ilerleme(kayit);
  alt.textContent = `Soru ${kayit.sira + 1} / ${kayit.kuyruk.length}. Önce yaz, sonra aç.`;
  ekran.innerHTML = `
    <section class="soru"><p>${kacis(soru.soru)}</p></section>
    <textarea id="yazi" placeholder="Aklına geleni yaz. Tam cümle olmak zorunda değil."></textarea>
    <p class="uyari" id="uyari" hidden>Önce bir cümle dene. Hiç bilmiyorsan düğmeye bir kez daha bas.</p>
    <div class="satir">
      <button type="button" class="asil" id="ac">Cevabı aç</button>
      <button type="button" id="ipucu">İpucu</button>
    </div>
    <div class="ipucu" id="ipucuKutu" hidden>
      <p class="etiket">İpucu</p>
      <p>${kacis(soru.ipucu || "")}</p>
    </div>`;
  const yazi = document.getElementById("yazi");
  const uyari = document.getElementById("uyari");
  let zorladi = false;
  document.getElementById("ipucu").addEventListener("click", () => {
    document.getElementById("ipucuKutu").hidden = false;
  });
  document.getElementById("ac").addEventListener("click", () => {
    if (!zorladi && yazi.value.trim().length < 2) {
      zorladi = true;
      uyari.hidden = false;
      return;
    }
    goster(paket, kayit, indeks, yazi.value.trim());
  });
  yazi.focus();
}

function goster(paket, kayit, indeks, benim) {
  const soru = paket.sorular[indeks];
  alt.textContent = "Cevabı kendi cümlenle karşılaştır. Ezber aynısı olmak zorunda değil.";
  const benimHtml = benim
    ? `<div class="benim"><p class="etiket">Senin yazdığın</p><p>${kacis(benim)}</p></div>`
    : "";
  ekran.innerHTML = `
    <section class="soru"><p>${kacis(soru.soru)}</p></section>
    ${benimHtml}
    <div class="cevap"><p class="etiket">Sayfadaki cevap</p><p>${kacis(soru.cevap)}</p></div>
    <div class="satir">
      <button type="button" class="asil" data-not="biliyordum">Biliyordum</button>
      <button type="button" data-not="eksik">Eksik kaldı</button>
      <button type="button" data-not="bilmiyordum">Bilmiyordum</button>
    </div>`;
  ekran.querySelectorAll("[data-not]").forEach((dugme) => {
    dugme.addEventListener("click", () => {
      kayit.notlar[indeks] = dugme.dataset.not;
      kayit.sira += 1;
      ciz(paket, kayit);
    });
  });
}

function sonuc(paket, kayit) {
  kayit.bitti = true;
  yaz(paket.id, kayit);
  bar.hidden = false;
  dolu.style.width = "100%";
  const say = { biliyordum: 0, eksik: 0, bilmiyordum: 0 };
  kayit.kuyruk.forEach((i) => {
    say[kayit.notlar[i]] = (say[kayit.notlar[i]] || 0) + 1;
  });
  const kacir = kayit.kuyruk.filter((i) => kayit.notlar[i] !== "biliyordum");
  alt.textContent = kacir.length
    ? "Eksik kalanlar bir sonraki turda yeniden gelir."
    : "Bu turda hepsini biliyordun.";
  const liste = kacir.map((i) => {
    const s = paket.sorular[i];
    return `<li><strong>${kacis(s.soru)}</strong><p>${kacis(s.cevap)}</p></li>`;
  }).join("");
  ekran.innerHTML = `
    <div class="ozet">
      <div><strong>${say.biliyordum}</strong><span>Biliyordum</span></div>
      <div><strong>${say.eksik}</strong><span>Eksik</span></div>
      <div><strong>${say.bilmiyordum}</strong><span>Bilmiyordum</span></div>
    </div>
    ${liste ? `<ol class="kacirilan">${liste}</ol>` : ""}
    <div class="satir">
      ${kacir.length ? `<button type="button" class="asil" id="tekrar">Eksikleri tekrarla</button>` : ""}
      <button type="button" id="bastan">Baştan başla</button>
      <a class="linkbuton" href="test.html">Diğer sayfalar</a>
    </div>`;
  const tekrar = document.getElementById("tekrar");
  if (tekrar) {
    tekrar.addEventListener("click", () => {
      kacir.forEach((i) => delete kayit.notlar[i]);
      kayit.kuyruk = kacir;
      kayit.sira = 0;
      kayit.tur = "eksik";
      kayit.bitti = false;
      ciz(paket, kayit);
    });
  }
  document.getElementById("bastan").addEventListener("click", () => {
    kayit.kuyruk = paket.sorular.map((_, i) => i);
    kayit.sira = 0;
    kayit.notlar = {};
    kayit.tur = "hepsi";
    kayit.bitti = false;
    ciz(paket, kayit);
  });
}

yukle();
