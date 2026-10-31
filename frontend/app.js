// Notitas: la página solo muestra y anima. Toda regla (validar, mover, filtrar…) la decide el backend con las tareas t01–t24.
const COLORES = { matcha: "#BCC86F", semolina: "#F5CB99", fresa: "#FFABA9", rosa: "#F68578", mani: "#B9794A", chocolate: "#79371D" };
// Íconos propios en SVG (trazo de 2 px, sin emojis): se pintan con el color del texto.
const TRAZOS = {
  nota: "M4 4h16v10l-6 6H4z M14 20v-6h6", ordenar: "M7 4v16 M3 8l4-4 4 4 M17 20V4 M13 16l4 4 4-4",
  deshacer: "M9 14 4 9l5-5 M4 9h10a6 6 0 0 1 0 12h-3", mas: "M5 12h.01 M12 12h.01 M19 12h.01", agregar: "M12 5v14 M5 12h14",
  archivar: "M3 4h18v4H3z M5 8v12h14V8 M10 12h4", lista: "M8 6h13 M8 12h13 M8 18h13 M3 6h.01 M3 12h.01 M3 18h.01",
  bajar: "M12 3v12 M7 10l5 5 5-5 M5 21h14", subir: "M12 15V3 M7 8l5-5 5 5 M5 21h14", copiar: "M9 9h11v11H9z M5 15H4V4h11v1",
  candado: "M5 11h14v10H5z M8 11V7a4 4 0 0 1 8 0v4", abierto: "M5 11h14v10H5z M8 11V7a4 4 0 0 1 7.5-2",
  sincronizar: "M4 7h13l-3-3 M20 17H7l3 3", reloj: "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z M12 7v5l3 2",
  izquierda: "M15 18l-6-6 6-6", derecha: "M9 18l6-6-6-6",
};
const ic = n => `<svg class="ic" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="${n === "mas" ? 3.2 : 2}" stroke-linecap="round" stroke-linejoin="round"><path d="${TRAZOS[n]}"/></svg>`;
document.querySelectorAll("[data-i]").forEach(el => { el.outerHTML = ic(el.dataset.i); });
const OSCUROS = new Set(["#B9794A", "#79371D"]);
const VENCE = { vencida: "Vencida", hoy: "Vence hoy", pronto: "Pronto" };
const estado = { q: "", etiquetas: new Set(), orden: "", datos: null, arrastrando: null, pagina: 1, contadores: {} };
const $ = (s, r = document) => r.querySelector(s);

async function api(ruta, cuerpo) {
  const r = await fetch(ruta, cuerpo === undefined ? {} : { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(cuerpo) });
  const datos = await r.json().catch(() => ({}));
  if (!r.ok) throw Object.assign(new Error(datos.error || "Algo salió mal."), { estado: r.status });
  return datos;
}

function aviso(texto, error = false) {
  const t = document.createElement("div");
  t.className = "toast" + (error ? " error" : "");
  t.textContent = texto;
  $("#toasts").append(t);
  setTimeout(() => t.remove(), 3700);
}

async function cargar() {
  const p = new URLSearchParams({ q: estado.q, etiquetas: [...estado.etiquetas].join(","), modo: "todas", orden: estado.orden });
  estado.datos = await api("/api/tablero?" + p);
  pintar();
}

function giro(id) { // cada nota tiene su propia inclinación, siempre la misma
  let h = 0;
  for (const c of id) h = (h * 31 + c.charCodeAt(0)) % 997;
  return ((h % 7) - 3) * 0.7 + "deg";
}

function tarjeta(n) {
  const el = document.createElement("article");
  el.className = "nota";
  el.draggable = true;
  el.dataset.id = n.id;
  el.style.background = n.color;
  el.style.setProperty("--giro", giro(n.id));
  if (OSCUROS.has(n.color)) el.style.color = "#FFF8EF";
  const contenido = n.html !== null ? n.html : escapar(n.contenido || "");
  const prog = n.progreso;
  el.innerHTML = `
    ${n.bloqueada ? `<span class="candado" title="Bloqueada">${ic("candado")}</span>` : ""}
    <div class="herramientas">
      <button data-accion="duplicar" title="Duplicar">${ic("copiar")}</button>
      <button data-accion="bloquear" title="${n.bloqueada ? "Desbloquear" : "Bloquear"}">${ic(n.bloqueada ? "abierto" : "candado")}</button>
      <button data-accion="dispositivos" title="Simular edición en dos dispositivos">${ic("sincronizar")}</button>
    </div>
    <h3>${escapar(n.titulo)}</h3>
    ${contenido ? `<div class="contenido">${contenido}</div>` : ""}
    ${n.checklist && n.checklist.length ? `<div class="check">${n.checklist.map((c, i) =>
      `<label><input type="checkbox" data-indice="${i}" ${c.hecho ? "checked" : ""}> ${escapar(c.texto)}</label>`).join("")}</div>` : ""}
    ${prog ? `<div class="barrita" title="${prog.texto}"><div style="width:${prog.porcentaje}%"></div></div>` : ""}
    <div class="pie">
      <span class="prio" title="Prioridad ${["", "baja", "media", "alta"][n.prioridad || 1]}">${"<b></b>".repeat(n.prioridad || 1)}</span>
      ${VENCE[n.vencimiento] ? `<span class="chip ${n.vencimiento}">${VENCE[n.vencimiento]}</span>` : ""}
      ${(n.etiquetas || []).map(e => `<span class="chip">#${escapar(e)}</span>`).join("")}
      ${n.ciclo !== null && n.ciclo !== undefined ? `<span class="chip ciclo" title="Tiempo de ciclo">${ic("reloj")} ${n.ciclo} h</span>` : ""}
      ${n.iniciales ? `<span class="avatar" title="${escapar(n.responsable)}">${escapar(n.iniciales)}</span>` : ""}
    </div>`;
  return el;
}

function escapar(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
}

function pintar() {
  const d = estado.datos;
  // FLIP: recordar dónde estaba cada nota para animar su nuevo lugar
  const antes = new Map([...document.querySelectorAll(".nota")].map(n => [n.dataset.id, n.getBoundingClientRect()]));
  for (const col of document.querySelectorAll(".columna")) {
    const nombre = col.dataset.columna;
    const notas = d.columnas[nombre];
    const caja = $(".notas", col);
    caja.replaceChildren(...notas.map(tarjeta));
    const cuenta = $(".cuenta", col);
    if (estado.contadores[nombre] !== undefined && estado.contadores[nombre] !== notas.length) {
      cuenta.classList.remove("salto"); void cuenta.offsetWidth; cuenta.classList.add("salto");
    }
    estado.contadores[nombre] = notas.length;
    cuenta.textContent = notas.length;
  }
  for (const el of document.querySelectorAll(".nota")) {
    const r0 = antes.get(el.dataset.id);
    if (!r0) continue;
    el.style.animation = "none";
    const r1 = el.getBoundingClientRect();
    const dx = r0.left - r1.left, dy = r0.top - r1.top;
    if (dx || dy) el.animate([{ transform: `translate(${dx}px, ${dy}px)` }, { transform: `rotate(${el.style.getPropertyValue("--giro")})` }],
      { duration: 450, easing: "cubic-bezier(.34,1.56,.64,1)" });
  }
  const r = d.resumen;
  $("#progreso-barra").style.width = r ? r.porcentaje_hecho + "%" : "0";
  $("#resumen-texto").textContent = r ? `${r.porcentaje_hecho}% hecho · ${r.total} notas${d.archivadas ? ` · ${d.archivadas} archivadas` : ""}` : "Resumen pendiente (t15)";
  $("#filtros").replaceChildren(...d.etiquetas.map(e => {
    const b = document.createElement("button");
    b.className = "filtro" + (estado.etiquetas.has(e) ? " activo" : "");
    b.textContent = "#" + e;
    b.onclick = () => { estado.etiquetas.has(e) ? estado.etiquetas.delete(e) : estado.etiquetas.add(e); cargar(); };
    return b;
  }));
  $("#reglas").textContent = `Reglas encendidas: ${d.reglas.activas.length}/${d.reglas.total}`;
}

function confeti(x, y) {
  const colores = Object.values(COLORES);
  for (let i = 0; i < 26; i++) {
    const c = document.createElement("i");
    c.className = "confeti";
    c.style.left = x + "px"; c.style.top = y + "px";
    c.style.background = colores[i % colores.length];
    c.style.setProperty("--dx", (Math.random() * 240 - 120) + "px");
    c.style.setProperty("--dy", (Math.random() * -200 - 40) + "px");
    document.body.append(c);
    setTimeout(() => c.remove(), 1000);
  }
}

async function mover(id, destino, posicion, motivo) {
  const nota = Object.values(estado.datos.columnas).flat().find(n => n.id === id);
  try {
    await api("/api/mover", { id, destino, posicion, version: nota.version, motivo });
    await cargar();
    const el = $(`.nota[data-id="${id}"]`);
    if (el) { el.classList.add("cae"); if (destino === "hecho" && nota.columna !== "hecho") { const r = el.getBoundingClientRect(); confeti(r.left + r.width / 2, r.top); } }
  } catch (e) {
    if (e.estado === 423) {
      const m = prompt("Esta nota está bloqueada. ¿Por qué la mueves?");
      if (m !== null) return mover(id, destino, posicion, m);
    }
    aviso(e.message, true);
    const col = $(`.columna[data-columna="${destino}"]`);
    col.classList.remove("rechazo"); void col.offsetWidth; col.classList.add("rechazo");
    cargar();
  }
}

// ---------- Arrastrar y soltar ----------
document.addEventListener("dragstart", e => {
  const n = e.target.closest?.(".nota");
  if (!n) return;
  estado.arrastrando = n.dataset.id;
  e.dataTransfer.effectAllowed = "move";
  requestAnimationFrame(() => n.classList.add("levantada"));
});
document.addEventListener("dragend", e => e.target.closest?.(".nota")?.classList.remove("levantada"));
for (const col of document.querySelectorAll(".columna")) {
  col.addEventListener("dragover", e => { e.preventDefault(); col.classList.add("sobre"); });
  col.addEventListener("dragleave", e => { if (!col.contains(e.relatedTarget)) col.classList.remove("sobre"); });
  col.addEventListener("drop", e => {
    e.preventDefault();
    col.classList.remove("sobre");
    const otras = [...col.querySelectorAll(".nota")].filter(n => n.dataset.id !== estado.arrastrando);
    const posicion = otras.filter(n => n.getBoundingClientRect().top + n.offsetHeight / 2 < e.clientY).length;
    mover(estado.arrastrando, col.dataset.columna, posicion);
  });
}

// ---------- Acciones de cada nota ----------
document.addEventListener("click", async e => {
  const b = e.target.closest(".herramientas button");
  if (!b) return;
  const id = b.closest(".nota").dataset.id;
  const nota = Object.values(estado.datos.columnas).flat().find(n => n.id === id);
  try {
    if (b.dataset.accion === "duplicar") { await api("/api/duplicar", { id }); aviso("Nota duplicada"); }
    if (b.dataset.accion === "bloquear") await api("/api/bloquear", { id, bloqueada: !nota.bloqueada });
    if (b.dataset.accion === "dispositivos") {
      const r = await api("/api/dispositivos", { id });
      aviso(r.conflictos.length ? `Fusión: conflicto en ${r.conflictos.join(", ")}; ganó el cambio más reciente` : "Fusión sin conflictos");
    }
    cargar();
  } catch (err) { aviso(err.message, true); }
});
document.addEventListener("change", async e => {
  if (!e.target.matches(".check input")) return;
  await api("/api/checklist", { id: e.target.closest(".nota").dataset.id, indice: e.target.dataset.indice });
  cargar();
});

// ---------- Barra ----------
let espera;
$("#q").addEventListener("input", e => { clearTimeout(espera); espera = setTimeout(() => { estado.q = e.target.value; cargar(); }, 200); });
$("#btn-orden").onclick = e => { estado.orden = estado.orden ? "" : "prioridad"; e.target.classList.toggle("principal"); cargar(); };
async function deshacer() {
  try { await api("/api/deshacer", {}); aviso("Movimiento deshecho"); cargar(); } catch (err) { aviso(err.message, true); }
}
$("#btn-deshacer").onclick = deshacer;
document.addEventListener("keydown", e => { if ((e.ctrlKey || e.metaKey) && e.key === "z" && !e.target.matches("input, textarea")) { e.preventDefault(); deshacer(); } });
$("#btn-mas").onclick = () => { $("#menu-mas").hidden = !$("#menu-mas").hidden; };
$("#menu-mas").addEventListener("click", async e => {
  const accion = e.target.dataset.accion;
  if (!accion) return;
  $("#menu-mas").hidden = true;
  try {
    if (accion === "archivar") { const r = await api("/api/archivar", {}); aviso(`${r.archivadas} notas archivadas`); cargar(); }
    if (accion === "archivadas") { estado.pagina = 1; await verArchivadas(); $("#dlg-archivadas").showModal(); }
    if (accion === "exportar") {
      const r = await fetch("/api/exportar");
      if (!r.ok) throw new Error((await r.json()).error);
      const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(await r.blob()), download: "notitas.json" });
      a.click();
    }
  } catch (err) { aviso(err.message, true); }
});
$("#importar").addEventListener("change", async e => {
  const archivo = e.target.files[0];
  if (!archivo) return;
  $("#menu-mas").hidden = true;
  const r = await fetch("/api/importar", { method: "POST", body: await archivo.text() });
  const d = await r.json();
  r.ok ? (aviso("Tablero importado"), cargar()) : aviso(d.error, true);
  e.target.value = "";
});
async function verArchivadas() {
  const r = await api("/api/archivadas?pagina=" + estado.pagina);
  $("#lista-archivadas").innerHTML = r.items.map(n => `<li><i class="punto" style="background:${n.color}"></i> <span style="color:var(--tinta)">${escapar(n.titulo)}</span></li>`).join("") || "<li>No hay notas archivadas.</li>";
  $("#pag-txt").textContent = `${r.pagina} / ${Math.max(r.total_paginas, 1)}`;
  $("#pag-ant").disabled = r.pagina <= 1;
  $("#pag-sig").disabled = !r.hay_siguiente;
}
$("#pag-ant").onclick = () => { estado.pagina--; verArchivadas(); };
$("#pag-sig").onclick = () => { estado.pagina++; verArchivadas(); };
$("#cerrar-arch").onclick = () => $("#dlg-archivadas").close();

// ---------- Nueva notita ----------
$(".colores").append(...Object.entries(COLORES).map(([nombre, hex], i) => {
  const l = document.createElement("label");
  l.style.background = hex;
  l.title = nombre;
  l.innerHTML = `<input type="radio" name="color" value="${nombre}" ${i === 1 ? "checked" : ""}>`;
  return l;
}));
$("#btn-nueva").onclick = () => { $("#form-nueva").reset(); $("#dlg-nueva").showModal(); };
$("#dlg-nueva").addEventListener("close", async () => {
  if ($("#dlg-nueva").returnValue !== "ok") return;
  const f = new FormData($("#form-nueva"));
  const lista = s => (s || "").split(",").map(x => x.trim()).filter(Boolean);
  try {
    await api("/api/notas", { titulo: f.get("titulo"), contenido: f.get("contenido"), color: f.get("color"), prioridad: f.get("prioridad"),
      vence: f.get("vence"), responsable: f.get("responsable"), etiquetas: lista(f.get("etiquetas")), checklist: lista(f.get("checklist")) });
    aviso("¡Notita pegada!");
    cargar();
  } catch (err) { aviso(err.message, true); }
});

cargar().catch(() => aviso("No se pudo conectar con el servidor. ¿Corriste python backend/servidor.py?", true));
