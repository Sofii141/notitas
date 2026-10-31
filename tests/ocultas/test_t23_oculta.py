from notitas.t23 import tiempo_ciclo
def test_reabierta_suma_las_dos_veces():
    ev = [{"hacia": "en_curso", "en": "2026-11-02T09:00:00-05:00"}, {"hacia": "hecho", "en": "2026-11-02T10:00:00-05:00"},
          {"hacia": "en_curso", "en": "2026-11-03T09:00:00-05:00"}, {"hacia": "hecho", "en": "2026-11-03T11:00:00-05:00"}]
    assert tiempo_ciclo(ev) == 3.0
def test_desordenados_y_zonas():
    ev = [{"hacia": "hecho", "en": "2026-11-02T16:00:00+00:00"}, {"hacia": "en_curso", "en": "2026-11-02T09:00:00-05:00"}]
    assert tiempo_ciclo(ev) == 2.0
def test_devuelta_a_por_hacer_no_cuenta_y_redondeo():
    ev = [{"hacia": "en_curso", "en": "2026-11-02T09:00:00-05:00"}, {"hacia": "por_hacer", "en": "2026-11-02T09:20:00-05:00"},
          {"hacia": "en_curso", "en": "2026-11-02T12:00:00-05:00"}, {"hacia": "hecho", "en": "2026-11-02T12:10:00-05:00"}]
    assert tiempo_ciclo(ev) == 0.5
