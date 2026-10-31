from notitas.t11 import Historial
def test_orden_lifo():
    h = Historial()
    h.registrar({"nota_id": "a", "desde": "por_hacer", "hacia": "en_curso"})
    h.registrar({"nota_id": "b", "desde": "en_curso", "hacia": "hecho"})
    assert h.deshacer()["nota_id"] == "b"
    assert h.deshacer()["nota_id"] == "a"
    assert h.deshacer() is None
def test_capacidad_20():
    h = Historial()
    for i in range(21):
        h.registrar({"nota_id": str(i), "desde": "por_hacer", "hacia": "en_curso"})
    ids = [h.deshacer()["nota_id"] for _ in range(20)]
    assert ids[0] == "20" and ids[-1] == "1"
    assert h.deshacer() is None
def test_instancias_independientes():
    a, b = Historial(), Historial()
    a.registrar({"nota_id": "x", "desde": "por_hacer", "hacia": "en_curso"})
    assert b.deshacer() is None
