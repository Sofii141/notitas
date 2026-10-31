from datetime import date
from notitas.t10 import notas_para_archivar
def test_basico():
    notas = [{"id": "1", "columna": "hecho", "fecha_hecho": "2026-10-01"}, {"id": "2", "columna": "hecho", "fecha_hecho": "2026-10-30"}]
    assert notas_para_archivar(notas, date(2026, 11, 2)) == ["1"]
