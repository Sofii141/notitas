from notitas.t21 import fusionar
BASE = {"id": "1", "titulo": "Pan", "columna": "por_hacer"}
def test_sin_conflicto():
    a = {"id": "1", "titulo": "Pan integral", "columna": "por_hacer", "modificado": {"titulo": "2026-11-02T10:00:00-05:00"}, "dispositivo": "celular"}
    b = {"id": "1", "titulo": "Pan", "columna": "en_curso", "modificado": {"columna": "2026-11-02T11:00:00-05:00"}, "dispositivo": "portatil"}
    assert fusionar(BASE, a, b) == {"id": "1", "titulo": "Pan integral", "columna": "en_curso", "conflictos": []}
def test_conflicto_gana_el_mas_reciente():
    a = {"id": "1", "titulo": "A", "columna": "por_hacer", "modificado": {"titulo": "2026-11-02T10:00:00-05:00"}, "dispositivo": "celular"}
    b = {"id": "1", "titulo": "B", "columna": "por_hacer", "modificado": {"titulo": "2026-11-02T09:00:00-05:00"}, "dispositivo": "portatil"}
    r = fusionar(BASE, a, b)
    assert r["titulo"] == "A" and r["conflictos"] == ["titulo"]
