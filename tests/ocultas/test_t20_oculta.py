from notitas.t20 import duplicar
def test_no_comparte_listas():
    nota = {"id": "1", "titulo": "Pan", "columna": "hecho", "version": 4, "etiquetas": ["casa"], "checklist": [{"texto": "a", "hecho": False}]}
    d = duplicar(nota, "2")
    d["etiquetas"].append("x")
    d["checklist"][0]["hecho"] = True
    assert nota["etiquetas"] == ["casa"] and nota["checklist"][0]["hecho"] is False
def test_copia_de_copia():
    assert duplicar({"id": "1", "titulo": "Pan (copia)", "columna": "hecho", "version": 1}, "2")["titulo"] == "Pan (copia 2)"
    assert duplicar({"id": "1", "titulo": "Pan (copia 9)", "columna": "hecho", "version": 1}, "2")["titulo"] == "Pan (copia 10)"
def test_original_intacta():
    nota = {"id": "1", "titulo": "Pan", "columna": "hecho", "version": 4}
    duplicar(nota, "2")
    assert nota == {"id": "1", "titulo": "Pan", "columna": "hecho", "version": 4}
