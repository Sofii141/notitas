from notitas.t23 import tiempo_ciclo
def test_simple():
    ev = [{"hacia": "por_hacer", "en": "2026-11-02T08:00:00-05:00"}, {"hacia": "en_curso", "en": "2026-11-02T09:00:00-05:00"},
          {"hacia": "hecho", "en": "2026-11-02T12:30:00-05:00"}]
    assert tiempo_ciclo(ev) == 3.5
def test_sin_hecho():
    assert tiempo_ciclo([{"hacia": "en_curso", "en": "2026-11-02T09:00:00-05:00"}]) is None
