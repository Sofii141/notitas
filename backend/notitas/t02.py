import re

HEX = re.compile(r"#?[0-9A-Fa-f]{6}")

PALETA = {
    "matcha": "#BCC86F",
    "semolina": "#F5CB99",
    "fresa": "#FFABA9",
    "rosa": "#F68578",
    "mani": "#B9794A",
    "chocolate": "#79371D",
}


def normalizar_color(c: str) -> str:
    """Ver TAREAS.md, tarea t02."""
    texto = c.strip()
    nombre = texto.lower()
    if nombre in PALETA:
        return PALETA[nombre]
    if HEX.fullmatch(texto):
        hex_canonico = "#" + texto.lstrip("#").upper()
        if hex_canonico in PALETA.values():
            return hex_canonico
    raise ValueError(f"Color no válido: {c!r}")
