from datetime import date
from notitas.t10 import notas_para_archivar
HOY = date(2026, 11, 10)
def test_siete_exactos_no():
    assert notas_para_archivar([{"id": "1", "columna": "hecho", "fecha_hecho": "2026-11-03"}], HOY) == []
def test_ocho_si():
    assert notas_para_archivar([{"id": "1", "columna": "hecho", "fecha_hecho": "2026-11-02"}], HOY) == ["1"]
def test_otras_columnas_y_sin_fecha():
    notas = [{"id": "1", "columna": "en_curso", "fecha_hecho": "2026-01-01"}, {"id": "2", "columna": "hecho"}]
    assert notas_para_archivar(notas, HOY) == []
