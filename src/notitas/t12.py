class Conflicto(Exception):
    pass


class Tablero:
    """Ver TAREAS.md, tarea t12."""

    def __init__(self, notas: list[dict]):
        raise NotImplementedError

    def mover(self, nota_id: str, destino: str, version: int) -> dict:
        raise NotImplementedError
