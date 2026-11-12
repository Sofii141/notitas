def resumen_columnas(notas: list[dict]) -> dict:
    
    resumen = {"por_hacer": 0, "en_curso": 0, "hecho": 0, "total": 0, "porcentaje_hecho": 0}

    for nota in notas:

        try:
            isArchivada = nota["archivada"]
        except KeyError:
            isArchivada = False
            
        if isArchivada is False:
            match nota["columna"]:
                case "por_hacer":
                    resumen["por_hacer"] += 1
                case "en_curso":
                    resumen["en_curso"] += 1
                case "hecho":
                    resumen["hecho"] += 1
                case _:
                    raise ValueError(f"Columna desconocida: {nota['columna']}")

    resumen["total"] = resumen["por_hacer"] + resumen["en_curso"] + resumen["hecho"]

    if resumen["total"] == 0:
        resumen["porcentaje_hecho"] = 0
    else:
        resumen["porcentaje_hecho"] = (float(resumen["hecho"])/float(resumen["total"])) * 100
        print(resumen["porcentaje_hecho"])
        if resumen["porcentaje_hecho"] - int(resumen["porcentaje_hecho"]) >= 0.5:
            int(resumen["porcentaje_hecho"]) + 1
        else:
            int(resumen["porcentaje_hecho"])    

                    
    return resumen

