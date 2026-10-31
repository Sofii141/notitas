import pytest
from notitas.t13 import exportar, importar
def test_estable():
    a = {"notas": [{"titulo": "x", "id": "1", "columna": "hecho"}]}
    b = {"notas": [{"columna": "hecho", "id": "1", "titulo": "x"}]}
    assert exportar(a) == exportar(b)
def test_ids_repetidos_y_columna():
    with pytest.raises(ValueError):
        importar('{"notas": [{"id": "1", "titulo": "a", "columna": "hecho"}, {"id": "1", "titulo": "b", "columna": "hecho"}]}')
    with pytest.raises(ValueError):
        importar('{"notas": [{"id": "1", "titulo": "a", "columna": "Hecho"}]}')
def test_json_invalido_y_campos():
    for malo in ["no es json", '{"notas": {}}', '{"notas": [{"id": 1, "titulo": "a", "columna": "hecho"}]}']:
        with pytest.raises(ValueError):
            importar(malo)
