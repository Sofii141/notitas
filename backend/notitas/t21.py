from datetime import datetime, timezone

_CAMPOS_IGNORADOS = {"modificado", "dispositivo"}
def _instante(valor):
    """Convierte la decha a un mismo estandar comparable"""
    if not isinstance(valor, str):
        return None
    texto = valor.strip()
    if texto.endswith(("Z","z")):
        texto = texto[:-1] + "+00:00"
    try:
        instante = datetime.fromisoformat(texto)
    except ValueError:
        return None
    if instante.tzinfo is None:
        instante = instante.replace(tzinfo = timezone.utc)
    return instante

def _fecha(version, campo):
    modificado = version.get("modificado") or ""
    return _instante(modificado.get(campo))

def _dispositivo(version):
    return version.get("dispositivo") or ""

def fusionar(base: dict, a: dict, b: dict) -> dict:

    campos = (set(base) | set (a) | set(b)) - _CAMPOS_IGNORADOS
    resultado = {}
    conflictos = []

    for campo in sorted(campos):
        valor_base = base.get(campo)
        valor_a = a.get(campo)
        valor_b = b.get(campo)

        if valor_a == valor_b:
            #ambos lados coiniciden
            elegido = valor_a
        elif valor_a == valor_base:
            #cambio solo a
            elegido = valor_b
        elif valor_b == valor_base:
            #cambio solo b
            elegido = valor_a
        else:
            #ambos lados cambiaron
            conflictos.append(campo)
            fecha_a = _fecha(a,campo)
            fecha_b = _fecha(b,campo)

            if fecha_a is not None and fecha_b is not None and fecha_a != fecha_b:
                #se elige la fecha mas reciente
                elegido= valor_a if fecha_a > fecha_b else valor_b
            elif fecha_a is not None and fecha_b is None:
                #Se elige la fecha a
                elegido= valor_a
            elif fecha_b is not None and fecha_a is None:
                #Se elige la fecha b
                elegido= valor_b
            else:
                #si ambas fechas son exactamente iguales o si ninguna tiene fecha
                elegido = (
                    valor_a if _dispositivo(a) <= _dispositivo(b)
                    else valor_b
                )
        if elegido is not None:
            resultado[campo] = elegido
    resultado["conflictos"] = sorted(conflictos)
    return resultado
