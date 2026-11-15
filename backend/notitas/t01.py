import re
import unicodedata

MAX_TITULO = 80
_ESPACIOS_REPETIDOS = re.compile(r" {2,}")

def validar_titulo(s: str) -> str:
    """Ver TAREAS.md, tarea t01."""
    titulo = " ".join(s.split())
    titulo = unicodedata.normalize("NFC", titulo)

    if not titulo:
        raise ValueError("el título no puede quedar vacío")
    if len(titulo) > MAX_TITULO:
        raise ValueError(f"el título supera los {MAX_TITULO} caracteres")
    return titulo