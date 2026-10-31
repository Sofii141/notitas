class LimiteCreacion:
    """Ver TAREAS.md, tarea t24."""

    def __init__(self, max_por_minuto: int = 5):
        raise NotImplementedError

    def permitir(self, usuario: str, ahora: float) -> bool:
        raise NotImplementedError
