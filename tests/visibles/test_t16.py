from notitas.t16 import ordenar
def test_prioridad_y_fecha():
    n = [{"id": "a", "prioridad": 1, "vence": None}, {"id": "b", "prioridad": 3, "vence": "2026-11-09"},
         {"id": "c", "prioridad": 3, "vence": "2026-11-03"}]
    assert [x["id"] for x in ordenar(n)] == ["c", "b", "a"]
