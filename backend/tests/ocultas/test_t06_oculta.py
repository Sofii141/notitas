import pytest
from notitas.t06 import filtrar_por_etiquetas
N = [{"id": "1", "etiquetas": ["Casa", "urgente"]}, {"id": "2", "etiquetas": ["casa"]}, {"id": "3", "etiquetas": []}]
def test_mayusculas():
    assert [n["id"] for n in filtrar_por_etiquetas(N, ["CASA"])] == ["1", "2"]
def test_vacia_devuelve_todas():
    assert [n["id"] for n in filtrar_por_etiquetas(N, [])] == ["1", "2", "3"]
def test_modo_invalido():
    with pytest.raises(ValueError):
        filtrar_por_etiquetas(N, ["casa"], "ninguna")
