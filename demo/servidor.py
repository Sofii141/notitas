"""Backend de Notitas: un servidor mínimo (solo librería estándar) que usa las funciones de las tareas.

Toda la lógica vive en las tareas t01–t24; este archivo solo guarda las notas en un JSON y las llama.
Si una tarea todavía no está implementada, su regla queda "pendiente" y el tablero sigue funcionando sin ella:
así la demo se va "encendiendo" a medida que avanzan. La página (`index.html`) no valida nada.

Uso:  python demo/servidor.py  y abrir http://localhost:8000
La demo NO se mide y no se toca durante una sesión cronometrada.
"""
import copy
import json
import sys
import threading
import time
import uuid
from datetime import date, datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "src"))

from notitas import (t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t12,  # noqa: E402
                     t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24)

BOGOTA = timezone(timedelta(hours=-5))
COLUMNAS = ("por_hacer", "en_curso", "hecho")
DATOS = AQUI / "datos.json"
INICIALES = AQUI / "datos_iniciales.json"
candado = threading.Lock()
historial = None
limite = None
pendientes = set()


class ErrorRegla(Exception):
    def __init__(self, estado, mensaje):
        super().__init__(mensaje)
        self.estado, self.mensaje = estado, mensaje


def regla(tarea, fn, *args, por_defecto=None):
    """Ejecuta la regla de una tarea; si aún no está implementada, la marca pendiente y usa el valor por defecto."""
    try:
        return fn(*args)
    except NotImplementedError:
        pendientes.add(tarea)
        return por_defecto


def ahora():
    return datetime.now(BOGOTA)


def cargar():
    origen = DATOS if DATOS.exists() else INICIALES
    return json.loads(origen.read_text(encoding="utf-8"))


def guardar(estado):
    DATOS.write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding="utf-8")


def evento(nota, columna):
    nota.setdefault("eventos", []).append({"hacia": columna, "en": ahora().isoformat(timespec="seconds")})
    if columna == "hecho":
        nota["fecha_hecho"] = ahora().date().isoformat()


def vista(estado, q="", etiquetas=(), modo="todas", orden=""):
    """Arma lo que ve la página: notas enriquecidas, filtradas y ordenadas por columna."""
    notas = [n for n in estado["notas"] if not n.get("archivada")]
    if etiquetas:
        notas = regla("t06", t06.filtrar_por_etiquetas, notas, list(etiquetas), modo, por_defecto=notas)
    if q.strip():
        ids = regla("t07", t07.buscar, notas, q, por_defecto=[n["id"] for n in notas if q.lower() in (n["titulo"] + n["contenido"]).lower()])
        notas = [n for n in notas if n["id"] in set(ids)]
    salida = {}
    for col in COLUMNAS:
        en_col = {n["id"]: n for n in notas if n["columna"] == col}
        lista = [en_col[i] for i in estado["orden"][col] if i in en_col]
        if orden == "prioridad":
            lista = regla("t16", t16.ordenar, lista, por_defecto=lista)
        salida[col] = [enriquecer(n) for n in lista]
    todas = estado["notas"]
    resumen = regla("t15", t15.resumen_columnas, todas, por_defecto=None)
    etiquetas_existentes = sorted({e for n in todas if not n.get("archivada") for e in n.get("etiquetas", [])})
    return {"columnas": salida, "resumen": resumen, "etiquetas": etiquetas_existentes,
            "archivadas": sum(1 for n in todas if n.get("archivada"))}


def enriquecer(n):
    v = {k: n.get(k) for k in ("id", "titulo", "contenido", "columna", "color", "etiquetas", "prioridad", "vence", "responsable",
                                "checklist", "bloqueada", "version")}
    v["html"] = regla("t14", t14.limpiar_contenido, n.get("contenido", ""), por_defecto=None)
    v["vencimiento"] = regla("t08", t08.estado_vencimiento, n.get("vence"), ahora(), por_defecto=None)
    v["iniciales"] = regla("t18", t18.iniciales, n.get("responsable", ""), por_defecto=None) if n.get("responsable") else None
    v["progreso"] = regla("t19", t19.progreso_checklist, n.get("checklist", []), por_defecto=None) if n.get("checklist") else None
    v["ciclo"] = regla("t23", t23.tiempo_ciclo, n.get("eventos", []), por_defecto=None) if n["columna"] == "hecho" else None
    return v


def crear(estado, d):
    if not regla("t24", limite.permitir, "demo", time.monotonic(), por_defecto=True):
        raise ErrorRegla(429, "Vas muy rápido: máximo 5 notas por minuto.")
    try:
        titulo = regla("t01", t01.validar_titulo, d.get("titulo", ""), por_defecto=d.get("titulo", "").strip() or "Sin título")
        color = regla("t02", t02.normalizar_color, d.get("color") or "semolina", por_defecto="#F5CB99")
        etiquetas = regla("t09", t09.normalizar_etiquetas, d.get("etiquetas", []), por_defecto=d.get("etiquetas", []))
    except ValueError as e:
        raise ErrorRegla(400, {"titulo": "El título debe tener entre 1 y 80 caracteres.", "color": "Ese color no está en la paleta.",
                               "etiqueta larga": "Cada etiqueta puede tener máximo 20 caracteres.",
                               "demasiadas": "Máximo 5 etiquetas."}.get(str(e), "Revisa los datos de la nota."))
    nota = {"id": uuid.uuid4().hex[:8], "titulo": titulo, "contenido": d.get("contenido", ""), "columna": "por_hacer",
            "color": color, "etiquetas": etiquetas, "prioridad": int(d.get("prioridad") or 2), "vence": d.get("vence") or None,
            "responsable": d.get("responsable", ""), "checklist": [{"texto": t, "hecho": False} for t in d.get("checklist", []) if t.strip()],
            "bloqueada": False, "version": 1}
    evento(nota, "por_hacer")
    estado["notas"].append(nota)
    estado["orden"]["por_hacer"].insert(0, nota["id"])
    return nota


def buscar_nota(estado, nota_id):
    nota = next((n for n in estado["notas"] if n["id"] == nota_id), None)
    if nota is None:
        raise ErrorRegla(404, "Esa nota ya no existe.")
    return nota


def mover(estado, d, registrar=True):
    nota = buscar_nota(estado, d["id"])
    destino, origen = d["destino"], nota["columna"]
    if nota.get("bloqueada"):
        try:
            movida = regla("t22", t22.mover_bloqueada, nota, destino, d.get("motivo"), por_defecto=None)
        except t22.NotaBloqueada:
            raise ErrorRegla(423, "Esta nota está bloqueada: escribe un motivo para moverla.")
        if movida:
            nota.update(bloqueada=False, historial=movida.get("historial", []))
    if not regla("t03", t03.puede_mover, origen, destino, por_defecto=True):
        raise ErrorRegla(409, "Ese movimiento no se permite: una nota no se salta \"En curso\".")
    try:
        regla("t04", t04.validar_wip, [n for n in estado["notas"] if not n.get("archivada")], nota["id"], destino)
    except t04.WipExcedido:
        raise ErrorRegla(409, "\"En curso\" ya tiene 3 notas (límite WIP). Termina una antes.")
    if "version" in d:
        try:
            movida = regla("t12", lambda: t12.Tablero([nota]).mover(nota["id"], destino, int(d["version"])), por_defecto=None)
        except t12.Conflicto:
            raise ErrorRegla(409, "Alguien movió esta nota antes que tú. Se recargó el tablero.")
        nota["version"] = movida["version"] if movida else nota["version"] + 1
    else:
        nota["version"] += 1
    estado["orden"][origen] = [i for i in estado["orden"][origen] if i != nota["id"]]
    estado["orden"][destino] = regla("t05", t05.insertar_en_posicion, estado["orden"][destino], nota["id"], int(d.get("posicion", 0)),
                                     por_defecto=[nota["id"]] + [i for i in estado["orden"][destino] if i != nota["id"]])
    nota["columna"] = destino
    if origen != destino:
        evento(nota, destino)
        if registrar:
            regla("t11", historial.registrar, {"nota_id": nota["id"], "desde": origen, "hacia": destino})
    return nota


def deshacer(estado):
    inverso = regla("t11", historial.deshacer, por_defecto=None)
    if not inverso:
        raise ErrorRegla(400, "No hay nada que deshacer.")
    nota = buscar_nota(estado, inverso["nota_id"])
    nota["bloqueada"] = False
    return mover(estado, {"id": nota["id"], "destino": inverso["hacia"]}, registrar=False)


def duplicar(estado, d):
    nota = buscar_nota(estado, d["id"])
    nueva = regla("t20", t20.duplicar, nota, uuid.uuid4().hex[:8], por_defecto=None)
    if nueva is None:
        raise ErrorRegla(501, "Duplicar todavía no está disponible (tarea t20 pendiente).")
    nueva["eventos"] = []
    evento(nueva, "por_hacer")
    estado["notas"].append(nueva)
    estado["orden"]["por_hacer"].insert(0, nueva["id"])
    return nueva


def archivar(estado):
    ids = regla("t10", t10.notas_para_archivar, estado["notas"], ahora().date(), por_defecto=[])
    for n in estado["notas"]:
        if n["id"] in ids:
            n["archivada"] = True
    return {"archivadas": len(ids)}


def simular_dos_dispositivos(estado, d):
    """Muestra la fusión de t21: la misma nota editada sin conexión en el celular y en el portátil."""
    nota = buscar_nota(estado, d["id"])
    base = {k: v for k, v in nota.items() if k in ("titulo", "color", "prioridad")}
    hace = lambda m: (ahora() - timedelta(minutes=m)).isoformat(timespec="seconds")  # noqa: E731
    a = dict(base, titulo=base["titulo"] + " (editada en el celular)", prioridad=3, modificado={"titulo": hace(5), "prioridad": hace(5)}, dispositivo="celular")
    b = dict(base, titulo=base["titulo"] + " (editada en el portátil)", color="#FFABA9", modificado={"titulo": hace(2), "color": hace(2)}, dispositivo="portatil")
    r = regla("t21", t21.fusionar, base, a, b, por_defecto=None)
    if r is None:
        raise ErrorRegla(501, "La fusión todavía no está disponible (tarea t21 pendiente).")
    nota.update({k: v for k, v in r.items() if k in base})
    nota["version"] += 1
    return r


def estado_reglas():
    """Prueba cada tarea con una llamada mínima para saber cuáles ya están implementadas."""
    pruebas = {
        "t01": lambda: t01.validar_titulo("a"), "t02": lambda: t02.normalizar_color("matcha"),
        "t03": lambda: t03.puede_mover("por_hacer", "en_curso"), "t04": lambda: t04.validar_wip([{"id": "a", "columna": "hecho"}], "a", "hecho"),
        "t05": lambda: t05.insertar_en_posicion([], "a", 0), "t06": lambda: t06.filtrar_por_etiquetas([], []),
        "t07": lambda: t07.buscar([], "a"), "t08": lambda: t08.estado_vencimiento(None, ahora()),
        "t09": lambda: t09.normalizar_etiquetas([]), "t10": lambda: t10.notas_para_archivar([], date.today()),
        "t11": lambda: t11.Historial().deshacer(), "t12": lambda: t12.Tablero([]),
        "t13": lambda: t13.exportar({"notas": []}), "t14": lambda: t14.limpiar_contenido(""),
        "t15": lambda: t15.resumen_columnas([]), "t16": lambda: t16.ordenar([]), "t17": lambda: t17.paginar([], 1),
        "t18": lambda: t18.iniciales("a"), "t19": lambda: t19.progreso_checklist([]),
        "t20": lambda: t20.duplicar({"titulo": "a"}, "b"), "t21": lambda: t21.fusionar({}, {}, {}),
        "t22": lambda: t22.mover_bloqueada({}, "hecho"), "t23": lambda: t23.tiempo_ciclo([]),
        "t24": lambda: t24.LimiteCreacion(),
    }
    activas = []
    for tarea, fn in pruebas.items():
        try:
            fn()
            activas.append(tarea)
        except NotImplementedError:
            pass
        except Exception:  # implementada, aunque la llamada mínima no le guste
            activas.append(tarea)
    return {"activas": activas, "total": len(pruebas)}


def iniciar_estado_global():
    global historial, limite
    try:
        historial = t11.Historial()
    except NotImplementedError:
        historial = None
    try:
        limite = t24.LimiteCreacion()
    except NotImplementedError:
        limite = None


class Manejador(BaseHTTPRequestHandler):
    def _responder(self, estado_http, cuerpo, tipo="application/json; charset=utf-8"):
        datos = cuerpo if isinstance(cuerpo, bytes) else json.dumps(cuerpo, ensure_ascii=False).encode("utf-8")
        self.send_response(estado_http)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)

    def log_message(self, *args):
        pass

    def do_GET(self):
        url = urlparse(self.path)
        p = parse_qs(url.query)
        if url.path == "/api/tablero":
            with candado:
                pendientes.clear()
                r = vista(cargar(), p.get("q", [""])[0], [e for e in p.get("etiquetas", [""])[0].split(",") if e],
                          p.get("modo", ["todas"])[0], p.get("orden", [""])[0])
            r["reglas"] = estado_reglas()
            return self._responder(200, r)
        if url.path == "/api/archivadas":
            notas = [n for n in cargar()["notas"] if n.get("archivada")]
            pag = regla("t17", t17.paginar, notas, int(p.get("pagina", ["1"])[0]), 5,
                        por_defecto={"items": notas, "pagina": 1, "total_paginas": 1, "hay_siguiente": False})
            pag["items"] = [{"id": n["id"], "titulo": n["titulo"], "color": n["color"]} for n in pag["items"]]
            return self._responder(200, pag)
        if url.path == "/api/exportar":
            texto = regla("t13", t13.exportar, cargar(), por_defecto=None)
            if texto is None:
                return self._responder(501, {"error": "Exportar todavía no está disponible (tarea t13 pendiente)."})
            return self._responder(200, texto.encode("utf-8"), "application/json; charset=utf-8")
        archivo = AQUI / ("index.html" if url.path in ("/", "") else url.path.lstrip("/"))
        if archivo.is_file() and AQUI in archivo.resolve().parents:
            tipo = {".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".ttf": "font/ttf", ".svg": "image/svg+xml"}
            return self._responder(200, archivo.read_bytes(), tipo.get(archivo.suffix, "application/octet-stream") + "; charset=utf-8")
        self._responder(404, {"error": "No encontrado"})

    def do_POST(self):
        largo = int(self.headers.get("Content-Length") or 0)
        texto = self.rfile.read(largo).decode("utf-8") if largo else "{}"
        acciones = {"/api/notas": crear, "/api/mover": mover, "/api/duplicar": duplicar, "/api/dispositivos": simular_dos_dispositivos,
                    "/api/deshacer": lambda e, d: deshacer(e), "/api/archivar": lambda e, d: archivar(e),
                    "/api/checklist": lambda e, d: alternar_item(e, d), "/api/bloquear": lambda e, d: bloquear(e, d)}
        try:
            with candado:
                estado = cargar()
                if self.path == "/api/importar":
                    try:
                        nuevo = regla("t13", t13.importar, texto, por_defecto=None)
                    except ValueError:
                        raise ErrorRegla(400, "El archivo no es un tablero válido.")
                    if nuevo is None:
                        raise ErrorRegla(501, "Importar todavía no está disponible (tarea t13 pendiente).")
                    nuevo.setdefault("orden", {c: [n["id"] for n in nuevo["notas"] if n["columna"] == c] for c in COLUMNAS})
                    estado, r = nuevo, {"ok": True}
                elif self.path in acciones:
                    r = acciones[self.path](estado, json.loads(texto))
                else:
                    return self._responder(404, {"error": "No encontrado"})
                guardar(estado)
            self._responder(200, r if isinstance(r, dict) else {"ok": True})
        except ErrorRegla as e:
            self._responder(e.estado, {"error": e.mensaje})


def alternar_item(estado, d):
    nota = buscar_nota(estado, d["id"])
    item = nota["checklist"][int(d["indice"])]
    item["hecho"] = not item["hecho"]
    return {"ok": True}


def bloquear(estado, d):
    nota = buscar_nota(estado, d["id"])
    nota["bloqueada"] = bool(d.get("bloqueada", True))
    return {"ok": True}


if __name__ == "__main__":
    iniciar_estado_global()
    if historial is None:
        historial = type("SinHistorial", (), {"registrar": lambda s, m: pendientes.add("t11"), "deshacer": lambda s: None})()
    if limite is None:
        limite = type("SinLimite", (), {"permitir": lambda s, u, t: True})()
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"Notitas en http://localhost:{puerto}  (Ctrl+C para salir)")
    ThreadingHTTPServer(("127.0.0.1", puerto), Manejador).serve_forever()
