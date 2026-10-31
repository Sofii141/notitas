from notitas.t24 import LimiteCreacion
def test_borde_de_la_ventana():
    lim = LimiteCreacion()
    for t in range(5):
        lim.permitir("ana", t)
    assert lim.permitir("ana", 59.9) is False
    assert lim.permitir("ana", 60) is True
def test_rechazados_no_cuentan():
    lim = LimiteCreacion(max_por_minuto=2)
    assert lim.permitir("ana", 0) and lim.permitir("ana", 1)
    for t in range(2, 50):
        assert lim.permitir("ana", t) is False
    assert lim.permitir("ana", 60.5) is True
def test_por_usuario():
    lim = LimiteCreacion(max_por_minuto=1)
    assert lim.permitir("ana", 0) and lim.permitir("juan", 0)
