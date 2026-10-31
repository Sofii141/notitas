import pytest
from notitas.t04 import validar_wip, WipExcedido
def nota(i, c):
    return {"id": i, "columna": c}
def test_cabe():
    notas = [nota("a", "en_curso"), nota("b", "en_curso"), nota("c", "por_hacer")]
    assert validar_wip(notas, "c", "en_curso") is None
def test_excede():
    notas = [nota("a", "en_curso"), nota("b", "en_curso"), nota("x", "en_curso"), nota("c", "por_hacer")]
    with pytest.raises(WipExcedido):
        validar_wip(notas, "c", "en_curso")
