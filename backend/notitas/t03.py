from unittest import result

from sqlalchemy import case


def puede_mover(origen: str, destino: str) -> bool:

    value = origen
    columnas_permitidas = ["por_hacer", "en_curso", "hecho"]

    if destino not in columnas_permitidas or origen not in columnas_permitidas:
        raise ValueError("La columna no existe")

    match value:
        case "por_hacer":

            if destino == "en_curso" or destino == "por_hacer":
                return True
            else:
                return False

        case "en_curso":
            
            if destino == "por_hacer" or destino == "hecho" or destino == "en_curso":
                return True
            else:
                return False

        case "hecho":
            if destino == "en_curso" or destino == "hecho":
                return True
            else:
                return False
