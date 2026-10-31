from notitas.t15 import resumen_columnas
def test_basico():
    notas = [{"columna": "por_hacer"}, {"columna": "hecho"}, {"columna": "hecho"}, {"columna": "en_curso"}]
    assert resumen_columnas(notas) == {"por_hacer": 1, "en_curso": 1, "hecho": 2, "total": 4, "porcentaje_hecho": 50}
