import pytest
from notitas.t17 import paginar
def test_ultima_y_mas_alla():
    assert paginar(list(range(25)), 3)["items"] == [20, 21, 22, 23, 24]
    r = paginar(list(range(25)), 4)
    assert r["items"] == [] and r["hay_siguiente"] is False
def test_vacia():
    assert paginar([], 1)["total_paginas"] == 0
def test_invalidos():
    with pytest.raises(ValueError):
        paginar([1], 0)
    with pytest.raises(ValueError):
        paginar([1], 1, 0)
