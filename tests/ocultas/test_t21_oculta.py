from notitas.t21 import fusionar
BASE = {"id": "1", "titulo": "Pan", "columna": "por_hacer", "color": "#BCC86F"}
def ed(titulo, fecha, disp, **extra):
    n = {"id": "1", "titulo": titulo, "columna": "por_hacer", "color": "#BCC86F", "modificado": {"titulo": fecha}, "dispositivo": disp}
    n.update(extra)
    return n
def test_zonas_horarias_distintas():
    a = ed("A", "2026-11-02T10:00:00-05:00", "celular")
    b = ed("B", "2026-11-02T14:00:00+00:00", "portatil")
    assert fusionar(BASE, a, b)["titulo"] == "A"
def test_empate_por_dispositivo():
    a = ed("A", "2026-11-02T15:00:00+00:00", "zeta")
    b = ed("B", "2026-11-02T10:00:00-05:00", "alfa")
    assert fusionar(BASE, a, b)["titulo"] == "B"
def test_mismo_valor_y_campo_borrado():
    a = ed("Igual", "2026-11-02T10:00:00-05:00", "celular")
    b = ed("Igual", "2026-11-02T11:00:00-05:00", "portatil")
    del a["color"]
    r = fusionar(BASE, a, b)
    assert r["titulo"] == "Igual" and r["conflictos"] == [] and "color" not in r
