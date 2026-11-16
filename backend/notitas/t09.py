def normalizar_etiquetas(etiquetas: list[str]) -> list[str]:
    """Ver TAREAS.md, tarea t09."""
    normalizadas = (" ".join(etiqueta.split()).lower() for etiqueta in etiquetas)
    resultado: list[str] = []
    for etiqueta in normalizadas:
        if etiqueta and etiqueta not in resultado:
            resultado.append(etiqueta)
    if len(resultado) > 5 or any(len(etiqueta) > 20 for etiqueta in resultado):
        raise ValueError("etiquetas fuera de rango")
    return resultado
