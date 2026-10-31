import pytest
from notitas.t02 import normalizar_color
def test_mayusculas_y_espacios():
    assert normalizar_color("  FRESA ") == "#FFABA9"
def test_hex_sin_numeral_y_minusculas():
    assert normalizar_color("79371d") == "#79371D"
    assert normalizar_color("#f68578") == "#F68578"
def test_formatos_invalidos():
    for malo in ["", "BCC86", "##BCC86F", "verde"]:
        with pytest.raises(ValueError):
            normalizar_color(malo)
