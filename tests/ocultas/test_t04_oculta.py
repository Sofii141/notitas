import pytest
from notitas.t04 import validar_wip, WipExcedido
def nota(i, c):
    return {"id": i, "columna": c}
LLENA = [nota("a", "en_curso"), nota("b", "en_curso"), nota("c", "en_curso"), nota("d", "por_hacer")]
def test_reordenar_no_cuenta():
    assert validar_wip(LLENA, "a", "en_curso") is None
def test_otras_columnas_sin_tope_y_limite_parametro():
    assert validar_wip(LLENA, "d", "hecho") is None
    with pytest.raises(WipExcedido):
        validar_wip([nota("a", "en_curso"), nota("d", "por_hacer")], "d", "en_curso", limite=1)
def test_id_desconocido():
    with pytest.raises(KeyError):
        validar_wip(LLENA, "zz", "en_curso")
