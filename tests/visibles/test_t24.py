from notitas.t24 import LimiteCreacion
def test_cinco_y_luego_no():
    lim = LimiteCreacion()
    assert all(lim.permitir("ana", t) for t in range(5))
    assert lim.permitir("ana", 10) is False
