import pytest
from notitas.t05 import insertar_en_posicion
def test_no_modifica_la_original():
    ids = ["a", "b", "c"]
    insertar_en_posicion(ids, "c", 0)
    assert ids == ["a", "b", "c"]
def test_mas_alla_del_final():
    assert insertar_en_posicion(["a", "b"], "a", 99) == ["b", "a"]
def test_negativa():
    with pytest.raises(ValueError):
        insertar_en_posicion(["a"], "b", -1)
