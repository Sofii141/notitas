import pytest
from notitas.t09 import normalizar_etiquetas
def test_espacios_internos_y_vacias():
    assert normalizar_etiquetas(["mi   lista", "", "  ", "MI LISTA"]) == ["mi lista"]
def test_cinco_tras_deduplicar_vale():
    assert len(normalizar_etiquetas(["a", "b", "c", "d", "e", "A", "b "])) == 5
def test_muy_larga():
    with pytest.raises(ValueError):
        normalizar_etiquetas(["x" * 21])
