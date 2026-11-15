class NotaBloqueada(Exception):
    pass


def mover_bloqueada(nota: dict, destino: str, motivo: str | None = None) -> dict:
    copia = dict(nota)
    copia["columna"] = destino

    if not nota.get("bloqueada"):
        return copia

    if not motivo or not motivo.strip():
        raise NotaBloqueada()

    copia["bloqueada"] = False
    historial = list(nota.get("historial") or [])
    historial.append({"accion": "desbloqueo", "motivo": motivo.strip()})
    copia["historial"] = historial
    return copia
