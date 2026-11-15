class Historial:
    """Ver TAREAS.md, tarea t11."""

    MAX_MOVIMIENTOS = 20

    def __init__(self) -> None:
        self._movimientos: list[dict] = []

    def registrar(self, movimiento: dict) -> None:
        self._movimientos.append(movimiento)
        if len(self._movimientos) > self.MAX_MOVIMIENTOS:
            self._movimientos.pop(0)

    def deshacer(self) -> dict | None:
        if not self._movimientos:
            return None
        movimiento = self._movimientos.pop()
        return {
            "nota_id": movimiento["nota_id"],
            "desde": movimiento["hacia"],
            "hacia": movimiento["desde"],
        }
