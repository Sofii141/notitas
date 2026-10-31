from notitas.t20 import duplicar
NOTA = {"id": "1", "titulo": "Pan", "columna": "hecho", "version": 4, "etiquetas": ["casa"]}
def test_basico():
    d = duplicar(NOTA, "2")
    assert d["id"] == "2" and d["titulo"] == "Pan (copia)" and d["version"] == 1 and d["columna"] == "por_hacer"
