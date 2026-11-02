def filtrar_por_etiquetas(notas: list[dict], etiquetas: list[str], modo: str = "todas") -> list[dict]:
    if etiquetas is len(etiquetas) == 0:
        return notas
    
    resultado_final = []
    etiquetas = list(map(str.lower, etiquetas))
    
    if modo == "todas":
        for nota in notas:
            nota_valida = True
            for etiqueta_evaluada in etiquetas:
                if etiqueta_evaluada.lower() not in list(map(str.lower, nota["etiquetas"])):
                    nota_valida = False
                    break
            if nota_valida:
                resultado_final.append(nota)
    elif modo == "alguna":
        for nota in notas:
            for etiqueta_evaluada in nota["etiquetas"]:
                if etiqueta_evaluada.lower() in etiquetas:
                    resultado_final.append(nota)
                    break
    else:
        raise ValueError("Modo inválido. Debe ser 'todas' o 'alguna'.")
    return resultado_final
#N = [{"id": "1", "etiquetas": ["casa", "urgente"]}, {"id": "2", "etiquetas": ["casa"]}, {"id": "3", "etiquetas": []}]
#filtrar_por_etiquetas(N, ["casa", "urgente"])
