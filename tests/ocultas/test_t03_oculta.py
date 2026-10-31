import pytest
from notitas.t03 import puede_mover
def test_no_se_salta_en_curso():
    assert puede_mover("por_hacer", "hecho") is False
    assert puede_mover("hecho", "por_hacer") is False
def test_misma_columna():
    assert puede_mover("hecho", "hecho") is True
def test_columna_desconocida_exacta():
    with pytest.raises(ValueError):
        puede_mover("Hecho", "en_curso")
