import pytest
from notitas.t22 import mover_bloqueada, NotaBloqueada
def test_libre():
    assert mover_bloqueada({"id": "1", "columna": "por_hacer"}, "en_curso")["columna"] == "en_curso"
def test_bloqueada_sin_motivo():
    with pytest.raises(NotaBloqueada):
        mover_bloqueada({"id": "1", "columna": "por_hacer", "bloqueada": True}, "en_curso")
