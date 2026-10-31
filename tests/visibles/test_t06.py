from notitas.t06 import filtrar_por_etiquetas
N = [{"id": "1", "etiquetas": ["casa", "urgente"]}, {"id": "2", "etiquetas": ["casa"]}, {"id": "3", "etiquetas": []}]
def test_todas():
    assert [n["id"] for n in filtrar_por_etiquetas(N, ["casa", "urgente"])] == ["1"]
def test_alguna():
    assert [n["id"] for n in filtrar_por_etiquetas(N, ["urgente", "casa"], "alguna")] == ["1", "2"]
