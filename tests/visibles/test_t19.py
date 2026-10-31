from notitas.t19 import progreso_checklist
def test_basico():
    items = [{"texto": "a", "hecho": True}, {"texto": "b", "hecho": False}]
    assert progreso_checklist(items) == {"hechos": 1, "total": 2, "porcentaje": 50, "texto": "1 de 2"}
