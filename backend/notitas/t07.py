from unidecode import unidecode

def buscar(notas: list[dict], texto: str) -> list[str]:
    if texto == "" or texto is None or texto.isspace():
        return [nota["id"] for nota in notas]
    
    textoNormalizado = unidecode(texto.casefold())
    coincidencias = []
    for nota in notas:
        if textoNormalizado in unidecode(nota["titulo"].casefold()) or textoNormalizado in unidecode(nota["contenido"].casefold()):
            coincidencias.append(nota["id"])
    return coincidencias;
