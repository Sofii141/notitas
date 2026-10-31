import pytest
from notitas.t01 import validar_titulo
def test_recorta():
    assert validar_titulo("  Comprar pan  ") == "Comprar pan"
def test_vacio():
    with pytest.raises(ValueError):
        validar_titulo("   ")
