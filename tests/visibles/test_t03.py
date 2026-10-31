from notitas.t03 import puede_mover
def test_flujo_normal():
    assert puede_mover("por_hacer", "en_curso") is True
    assert puede_mover("en_curso", "hecho") is True
def test_reabrir():
    assert puede_mover("hecho", "en_curso") is True
