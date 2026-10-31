from datetime import datetime, timedelta, timezone
import pytest
from notitas.t08 import estado_vencimiento
def test_noche_en_bogota_es_otro_dia_en_utc():
    ahora = datetime(2026, 11, 1, 3, 0, tzinfo=timezone.utc)
    assert estado_vencimiento("2026-10-31", ahora) == "hoy"
def test_limite_pronto_a_tiempo():
    ahora = datetime(2026, 11, 2, 12, 0, tzinfo=timezone.utc)
    assert estado_vencimiento("2026-11-05", ahora) == "pronto"
    assert estado_vencimiento("2026-11-06", ahora) == "a_tiempo"
def test_naive():
    with pytest.raises(ValueError):
        estado_vencimiento("2026-11-02", datetime(2026, 11, 2, 9, 0))
