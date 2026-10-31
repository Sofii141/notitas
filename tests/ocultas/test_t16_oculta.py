from notitas.t16 import ordenar
def test_sin_fecha_al_final_del_grupo():
    n = [{"id": "a", "prioridad": 2, "vence": None}, {"id": "b", "prioridad": 2, "vence": "2026-12-31"}]
    assert [x["id"] for x in ordenar(n)] == ["b", "a"]
def test_estable():
    n = [{"id": str(i), "prioridad": 1, "vence": None} for i in range(5)]
    assert [x["id"] for x in ordenar(n)] == ["0", "1", "2", "3", "4"]
def test_no_modifica():
    n = [{"id": "a", "prioridad": 1, "vence": None}, {"id": "b", "prioridad": 3, "vence": None}]
    ordenar(n)
    assert n[0]["id"] == "a"
