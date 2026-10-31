from notitas.t15 import resumen_columnas
def test_vacio():
    assert resumen_columnas([])["porcentaje_hecho"] == 0
def test_redondeo_hacia_arriba_en_empate():
    notas = [{"columna": "hecho"}] + [{"columna": "por_hacer"}] * 7
    assert resumen_columnas(notas)["porcentaje_hecho"] == 13
def test_archivadas_no_cuentan():
    notas = [{"columna": "hecho", "archivada": True}, {"columna": "por_hacer"}, {"columna": "hecho"}]
    r = resumen_columnas(notas)
    assert r["total"] == 2 and r["porcentaje_hecho"] == 50
