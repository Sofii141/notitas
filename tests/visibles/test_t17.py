from notitas.t17 import paginar
def test_primera():
    r = paginar(list(range(25)), 1)
    assert r["items"] == list(range(10)) and r["total_paginas"] == 3 and r["hay_siguiente"] is True
