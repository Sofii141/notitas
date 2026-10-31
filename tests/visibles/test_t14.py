from notitas.t14 import limpiar_contenido
def test_negrita():
    assert limpiar_contenido("**hola** mundo") == "<strong>hola</strong> mundo"
def test_salto():
    assert limpiar_contenido("a\nb") == "a<br>b"
