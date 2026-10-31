from notitas.t11 import Historial
def test_deshacer():
    h = Historial()
    h.registrar({"nota_id": "a", "desde": "por_hacer", "hacia": "en_curso"})
    assert h.deshacer() == {"nota_id": "a", "desde": "en_curso", "hacia": "por_hacer"}
def test_vacio():
    assert Historial().deshacer() is None
