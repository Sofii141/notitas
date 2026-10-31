import pytest
from notitas.t02 import normalizar_color
def test_nombre():
    assert normalizar_color("matcha") == "#BCC86F"
def test_otro_color():
    with pytest.raises(ValueError):
        normalizar_color("#123456")
