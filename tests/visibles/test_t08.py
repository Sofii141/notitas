from datetime import datetime, timedelta, timezone
from notitas.t08 import estado_vencimiento
BOG = timezone(timedelta(hours=-5))
def test_basicos():
    ahora = datetime(2026, 11, 2, 9, 0, tzinfo=BOG)
    assert estado_vencimiento("2026-11-01", ahora) == "vencida"
    assert estado_vencimiento("2026-11-02", ahora) == "hoy"
    assert estado_vencimiento("2026-11-04", ahora) == "pronto"
def test_sin_fecha():
    assert estado_vencimiento(None, datetime(2026, 11, 2, tzinfo=BOG)) == "sin_fecha"
