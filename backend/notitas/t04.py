class WipExcedido(Exception):
    pass


def validar_wip(notas: list[dict], nota_id: str, destino: str, limite: int = 3) -> None:
    """Ver TAREAS.md, tarea t04."""
    nota = next((n for n in notas if n.get("id") == nota_id), None)
    if nota is None:
        raise KeyError(nota_id)
    
    if destino != "en_curso":
        return None

    if nota.get("columna") == "en_curso":
        return None

    en_curso = sum(1 for n in notas if n.get("columna") == "en_curso")

    if en_curso + 1 > limite:
        raise WipExcedido(
            f'"{destino}" admite como máximo {limite} notas; ya hay {en_curso}.'
        )

    return None