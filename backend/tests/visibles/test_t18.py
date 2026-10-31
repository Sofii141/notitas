from notitas.t18 import iniciales
def test_dos_palabras():
    assert iniciales("ana sofía") == "AS"
def test_vacio():
    assert iniciales("   ") == "?"
