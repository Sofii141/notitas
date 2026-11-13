def ordenar(notas: list[dict]) -> list[dict]:
    return sorted(
        notas,
        key=lambda n: (
            -n["prioridad"],
            n["vence"] is None,
            n["vence"] or "",
        ),
    )