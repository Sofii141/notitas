from notitas.t13 import exportar, importar
T = {"notas": [{"id": "1", "titulo": "Canción", "columna": "hecho"}]}
def test_ida_y_vuelta():
    assert importar(exportar(T)) == T
def test_sin_escapar_tildes():
    assert "Canción" in exportar(T)
