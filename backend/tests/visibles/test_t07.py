from notitas.t07 import buscar
N = [{"id": "1", "titulo": "Canción del lunes", "contenido": ""}, {"id": "2", "titulo": "Pan", "contenido": "comprar pan"}]
def test_tildes_y_mayusculas():
    assert buscar(N, "CANCION") == ["1"]
def test_en_contenido():
    assert buscar(N, "comprar") == ["2"]
