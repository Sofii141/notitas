import pytest
from notitas.t12 import Tablero, Conflicto
def test_mueve_y_sube_version():
    t = Tablero([{"id": "a", "columna": "por_hacer", "version": 1}])
    n = t.mover("a", "en_curso", 1)
    assert n["columna"] == "en_curso" and n["version"] == 2
def test_version_vieja():
    t = Tablero([{"id": "a", "columna": "por_hacer", "version": 1}])
    t.mover("a", "en_curso", 1)
    with pytest.raises(Conflicto):
        t.mover("a", "hecho", 1)
