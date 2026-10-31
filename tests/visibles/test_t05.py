from notitas.t05 import insertar_en_posicion
def test_insertar_nueva():
    assert insertar_en_posicion(["a", "b"], "x", 1) == ["a", "x", "b"]
def test_mover_existente():
    assert insertar_en_posicion(["a", "b", "c"], "a", 2) == ["b", "c", "a"]
