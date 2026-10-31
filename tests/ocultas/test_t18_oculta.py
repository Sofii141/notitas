from notitas.t18 import iniciales
def test_particulas():
    assert iniciales("María de los Ángeles") == "MÁ"
def test_una_palabra_y_enie():
    assert iniciales("ñandú") == "Ñ"
def test_tres_palabras_y_espacios():
    assert iniciales("  juan   josé arias ") == "JA"
