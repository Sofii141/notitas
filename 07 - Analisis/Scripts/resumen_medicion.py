"""Resume la bitácora: las 5 métricas del GQM v3 por condición y tamaño, más las decisiones sobre el agente.

Uso:
  python "07 - Analisis/Scripts/resumen_medicion.py" "05 - Ciclos y bitacora/31102026_01_Bitacora_v3.xlsx"
  python "07 - Analisis/Scripts/resumen_medicion.py" <bitacora.xlsx> --html "<documento>.html"
      → además reemplaza la sección de línea base del HTML (entre <!-- LB:INICIO --> y <!-- LB:FIN -->) y regenera el PDF.

Métricas (GQM v3, todas directas): M1 minutos · M2 ocultas que fallan · M3 minutos de retrabajo · M4 codewalk 0–5 · M5 pronóstico.
Calcula desde los datos crudos (inicio, fin, pausas…), no desde las fórmulas del Excel: así la hoja Resumen y este script son
dos cálculos independientes. Igual, una persona recalcula a mano al menos una mediana (regla de la E1).
"""
import datetime as dt
import html
import re
import statistics
import subprocess
import sys
from collections import Counter
from pathlib import Path

from openpyxl import load_workbook

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parents[2]
CONDICIONES = ("Línea base", "Ciclo 1", "Ciclo 2")
TAMANOS = ("S", "M", "L")
# Columnas de la hoja "Medicion por caso" (bitácora v3), contando desde 0
PRON, INI, FIN, PAUSA, FALLA, TOTAL, RETR, CW_A, CW_C, MARCA = 7, 8, 9, 10, 12, 13, 14, 15, 16, 18


def minutos(v):
    """Convierte una hora de Excel (time, datetime, fracción de día o texto hh:mm) a minutos desde medianoche."""
    if v is None or v == "":
        return None
    if isinstance(v, (dt.time, dt.datetime)):
        return v.hour * 60 + v.minute
    if isinstance(v, (int, float)):
        return round(v * 1440)
    m = re.match(r"\s*(\d{1,2}):(\d{2})", str(v))
    return int(m[1]) * 60 + int(m[2]) if m else None


def numero(v):
    try:
        return float(v) if v not in (None, "") else None
    except (TypeError, ValueError):
        return None


def leer(xlsx):
    hoja = load_workbook(xlsx, data_only=True)["Medicion por caso"]
    filas = []
    for r in hoja.iter_rows(min_row=2, values_only=True):
        ini, fin = minutos(r[INI]), minutos(r[FIN])
        if not r[4] or ini is None or fin is None or (r[MARCA] or "").strip() == "[C]":
            continue
        filas.append(dict(caso=r[0], tarea=r[1], tam=r[2] or "?", dif=r[3] == "Sí", cond=r[4], pron=numero(r[PRON]),
                          dur=fin - ini - (numero(r[PAUSA]) or 0), falla=numero(r[FALLA]) or 0, total=numero(r[TOTAL]) or 0,
                          retr=numero(r[RETR]) or 0, cw_a=numero(r[CW_A]), cw_c=numero(r[CW_C])))
    return filas


def leer_sesiones(xlsx, etapa="Línea base"):
    hoja = load_workbook(xlsx, data_only=True)["Sesiones"]
    cab = [c.value for c in hoja[1]]
    filas = []
    for r in hoja.iter_rows(min_row=2, values_only=True):
        if r[2] == etapa and r[1]:  # solo sesiones que ya ocurrieron (con fecha)
            filas.append({k: ("" if v is None else v.strftime("%d/%m/%Y") if isinstance(v, dt.datetime) and v.time() == dt.time(0) else v.strftime("%H:%M") if isinstance(v, (dt.time, dt.datetime)) else str(v))
                          for k, v in zip(cab, r)})
    return filas


def decisiones(xlsx):
    hoja = load_workbook(xlsx, data_only=True)["Bitacora"]
    return Counter(str(r[6]).strip().lower() for r in hoja.iter_rows(min_row=2, values_only=True) if r[6])


def med(valores):
    v = [x for x in valores if x is not None]
    if not v:
        return "—"
    m = statistics.median(v)
    txt = f"{m:g}" if float(m).is_integer() else f"{m:.1f}"
    return txt if len(v) == 1 else f"{txt} [{min(v):g}–{max(v):g}]"


def resumen(filas):
    salida = []
    for cond in CONDICIONES:
        fc = [f for f in filas if f["cond"] == cond]
        for tam in TAMANOS + ("Total",):
            g = fc if tam == "Total" else [f for f in fc if f["tam"] == tam]
            if not g:
                continue
            con_retr = [f["retr"] for f in g if f["retr"] > 0]
            con_pron = [f for f in g if f["pron"]]
            salida.append(dict(
                cond=cond, tam=tam, n=len(g),
                m1=med(f["dur"] for f in g),
                m2=f"{sum(f['falla'] for f in g):g} de {sum(f['total'] for f in g):g}",
                m3=f"{len(con_retr)} de {len(g)}" + (f" ({med(con_retr)} min)" if con_retr else ""),
                m4=f"{med(f['cw_a'] for f in g)} / {med(f['cw_c'] for f in g)}",
                m5=f"{sum(f['dur'] > f['pron'] for f in con_pron)} de {len(con_pron)}" if con_pron else "—"))
    return salida


CAB = ("Condición", "Tam.", "n", "M1 minutos", "M2 ocultas que fallan", "M3 tareas con retrabajo", "M4 codewalk autor / comp.",
       "M5 tardaron más de lo pronosticado")


def imprimir(filas, res, dec):
    print(f"Tareas con datos válidos: {len(filas)}\n")
    print(" | ".join(CAB))
    for r in res:
        print(" | ".join(str(r[k]) for k in ("cond", "tam", "n", "m1", "m2", "m3", "m4", "m5")))
    if dec:
        print(f"\nDecisiones sobre el agente (bitácora): " + ", ".join(f"{k}: {v}" for k, v in sorted(dec.items())))
    print("\nM1 y M4 = mediana [mínimo–máximo]. Las tareas marcadas [C] no se cuentan. Son tendencias, no causas.")


def fragmento_html(filas, res, sesiones):
    e = html.escape
    base = [f for f in filas if f["cond"] == "Línea base"]
    if not base:
        return "<div class='caja alerta'><h4>Sin datos todavía</h4><p>La bitácora aún no tiene tareas de línea base con inicio y fin.</p></div>"
    claves = [k for i, k in enumerate(list(sesiones[0]) if sesiones else []) if i in (1, 3, 4, 5, 6, 7, 8, 9, 11)]
    condiciones = (f"<h3>Condiciones de la medición</h3><table class='pequeno'><thead><tr>{''.join(f'<th>{e(k)}</th>' for k in claves)}</tr></thead>"
                   f"<tbody>{''.join('<tr>' + ''.join(f'<td>{e(s[k])}</td>' for k in claves) + '</tr>' for s in sesiones)}</tbody></table>"
                   if sesiones else "<div class='caja alerta'><h4>Faltan las condiciones</h4><p>La hoja Sesiones no tiene filas de línea base.</p></div>")

    def v(x):
        return "—" if x is None else f"{x:g}"

    dif = "<span class='chip dif'>Sí</span>"
    por_tarea = "".join(
        f"<tr><td><code>{e(str(f['caso']))}</code> {e(str(f['tarea']))}</td><td class='c'><span class='chip {f['tam'].lower()}'>{e(f['tam'])}</span></td>"
        f"<td class='c'>{dif if f['dif'] else ''}</td><td class='c'>{v(f['pron'])}</td><td class='c'>{v(f['dur'])}</td>"
        f"<td class='c'>{v(f['falla'])}/{v(f['total'])}</td><td class='c'>{v(f['retr'])}</td><td class='c'>{v(f['cw_a'])} / {v(f['cw_c'])}</td></tr>"
        for f in base)
    resumen_html = "".join(
        f"<tr><td>{e(r['tam'])}</td><td class='c'>{r['n']}</td><td>{r['m1']}</td><td>{r['m2']}</td><td>{r['m3']}</td><td>{r['m4']}</td><td>{r['m5']}</td></tr>"
        for r in res if r["cond"] == "Línea base")
    return (condiciones + f"<h3>Resultados por tarea (n = {len(base)})</h3><table><thead><tr><th>Tarea</th><th>Tam.</th><th>Difícil</th>"
            "<th>M5 pronóstico</th><th>M1 minutos</th><th>M2 ocultas que fallan</th><th>M3 retrabajo (min)</th><th>M4 codewalk autor / comp.</th></tr></thead>"
            f"<tbody>{por_tarea}</tbody></table><h3>Resumen por tamaño</h3><p class='pequeno'>M1 y M4: mediana [mínimo–máximo]. Son tendencias, no causas.</p>"
            "<table><thead><tr><th>Tamaño</th><th>n</th><th>M1 minutos</th><th>M2 ocultas que fallan</th><th>M3 tareas con retrabajo</th>"
            f"<th>M4 codewalk autor / comp.</th><th>M5 tardaron más de lo pronosticado</th></tr></thead><tbody>{resumen_html}</tbody></table>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    filas = leer(sys.argv[1])
    res = resumen(filas)
    imprimir(filas, res, decisiones(sys.argv[1]))
    if "--html" in sys.argv:
        destino = Path(sys.argv[sys.argv.index("--html") + 1])
        texto = destino.read_text(encoding="utf-8")
        nuevo = re.sub(r"(<!-- LB:INICIO -->).*?(<!-- LB:FIN -->)",
                       lambda m: m[1] + fragmento_html(filas, res, leer_sesiones(sys.argv[1])) + m[2], texto, flags=re.S)
        destino.write_text(nuevo, encoding="utf-8")
        subprocess.run([sys.executable, str(RAIZ / "_Estilo" / "html_a_pdf.py"), str(destino)], check=True)
