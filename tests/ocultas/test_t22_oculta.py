import pytest
from notitas.t22 import mover_bloqueada, NotaBloqueada
def test_motivo_en_blanco():
    with pytest.raises(NotaBloqueada):
        mover_bloqueada({"id": "1", "columna": "por_hacer", "bloqueada": True}, "en_curso", "   ")
def test_desbloqueo_con_historial():
    r = mover_bloqueada({"id": "1", "columna": "por_hacer", "bloqueada": True}, "en_curso", "  ya respondió ")
    assert r["bloqueada"] is False and r["columna"] == "en_curso"
    assert r["historial"] == [{"accion": "desbloqueo", "motivo": "ya respondió"}]
def test_no_modifica_original():
    nota = {"id": "1", "columna": "por_hacer", "bloqueada": True, "historial": [{"accion": "creada"}]}
    r = mover_bloqueada(nota, "en_curso", "ok")
    assert len(r["historial"]) == 2 and nota["historial"] == [{"accion": "creada"}] and nota["bloqueada"] is True
