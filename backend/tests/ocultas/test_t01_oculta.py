import pytest
from notitas.t01 import validar_titulo
def test_espacios_internos_y_duro():
    assert validar_titulo("\u00a0Comprar \t  pan\n") == "Comprar pan"
def test_limite_80_despues_de_nfc():
    assert len(validar_titulo("e\u0301" * 80)) == 80
    with pytest.raises(ValueError):
        validar_titulo("a" * 81)
def test_nfc():
    assert validar_titulo("Cancio\u0301n") == "Canci\u00f3n"
