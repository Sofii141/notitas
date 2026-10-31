from notitas.t07 import buscar
N = [{"id": "1", "titulo": "Regalo del niño", "contenido": ""}, {"id": "2", "titulo": "Viaje", "contenido": "Hotel en la Straße"},
     {"id": "3", "titulo": "cancion", "contenido": ""}]
def test_enie():
    assert buscar(N, "nino") == ["1"]
def test_casefold_completo():
    assert buscar(N, "strasse") == ["2"]
def test_vacio_y_busqueda_con_tilde():
    assert buscar(N, "   ") == ["1", "2", "3"]
    assert buscar(N, "canción") == ["3"]
