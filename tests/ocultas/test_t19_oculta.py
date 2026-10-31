import pytest
from notitas.t19 import progreso_checklist
def test_redondeo_hacia_abajo_y_vacios():
    items = [{"texto": "a", "hecho": True}, {"texto": "b", "hecho": True}, {"texto": "c", "hecho": False}, {"texto": "  ", "hecho": True}]
    r = progreso_checklist(items)
    assert r["porcentaje"] == 66 and r["texto"] == "2 de 3"
def test_sin_items():
    assert progreso_checklist([]) == {"hechos": 0, "total": 0, "porcentaje": 0, "texto": "0 de 0"}
def test_hecho_no_booleano():
    with pytest.raises(ValueError):
        progreso_checklist([{"texto": "a", "hecho": 1}])
