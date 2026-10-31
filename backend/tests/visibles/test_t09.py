import pytest
from notitas.t09 import normalizar_etiquetas
def test_limpia_y_deduplica():
    assert normalizar_etiquetas([" Casa ", "casa", "Urgente"]) == ["casa", "urgente"]
def test_mas_de_5():
    with pytest.raises(ValueError):
        normalizar_etiquetas(["a", "b", "c", "d", "e", "f"])
