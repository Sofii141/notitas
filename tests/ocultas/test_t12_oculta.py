import threading
import pytest
from notitas.t12 import Tablero, Conflicto
def test_concurrencia_un_solo_ganador():
    for _ in range(20):
        t = Tablero([{"id": "a", "columna": "por_hacer", "version": 1}])
        barrera = threading.Barrier(8)
        ganadores, conflictos = [], []
        def intento(destino):
            barrera.wait()
            try:
                ganadores.append(t.mover("a", destino, 1))
            except Conflicto:
                conflictos.append(destino)
        hilos = [threading.Thread(target=intento, args=("en_curso",)) for _ in range(8)]
        [h.start() for h in hilos]
        [h.join() for h in hilos]
        assert len(ganadores) == 1 and len(conflictos) == 7
        assert t.mover("a", "hecho", 2)["version"] == 3
def test_copias_independientes():
    original = [{"id": "a", "columna": "por_hacer", "version": 1}]
    t = Tablero(original)
    original[0]["version"] = 99
    devuelta = t.mover("a", "en_curso", 1)
    devuelta["columna"] = "hecho"
    assert t.mover("a", "por_hacer", 2)["version"] == 3
def test_desconocida_y_conflicto_no_cambia():
    t = Tablero([{"id": "a", "columna": "por_hacer", "version": 5}])
    with pytest.raises(KeyError):
        t.mover("zz", "hecho", 1)
    with pytest.raises(Conflicto):
        t.mover("a", "hecho", 4)
    assert t.mover("a", "en_curso", 5)["version"] == 6
