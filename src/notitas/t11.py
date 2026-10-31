class Historial:
    """Ver TAREAS.md, tarea t11."""

    def registrar(self, movimiento: dict) -> None:
        raise NotImplementedError

    def deshacer(self) -> dict | None:
        raise NotImplementedError
