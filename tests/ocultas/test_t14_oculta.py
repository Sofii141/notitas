from notitas.t14 import limpiar_contenido
def test_script():
    assert limpiar_contenido("<script>alert(1)</script>") == "&lt;script&gt;alert(1)&lt;/script&gt;"
def test_formato_no_abre_la_puerta():
    assert limpiar_contenido("**<b>**") == "<strong>&lt;b&gt;</strong>"
def test_comillas_ampersand_y_sin_pareja():
    assert limpiar_contenido("a & b \"c\" 'd' **x") == "a &amp; b &quot;c&quot; &#x27;d&#x27; **x"
