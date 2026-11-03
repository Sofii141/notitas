import threading
class Conflicto(Exception):
    pass


class Tablero:
    notas: list[dict]
    lock_acceso_tablero: threading.Lock
    def __init__(self, notas: list[dict]):
        Tablero.notas = notas
        Tablero.lock_acceso_tablero = threading.Lock()
    def get_notas(self):
        return self.notas
    def set_notas(self, notas: list[dict]):
        self.notas = notas

    def mover(self, nota_id: str, destino: str, version: int) -> dict:
        nota_a_mover = None
        for nota in Tablero.notas:
            if nota["id"] == nota_id:
                nota_a_mover = nota
                break
        if nota_a_mover is None:
            raise KeyError(f"No se encontró la nota con id {nota_id}")
        
        Tablero.lock_acceso_tablero.acquire()
        if nota_a_mover["version"] == version:
            nota_a_mover["version"] += 1
            nota_a_mover["columna"] = destino
            Tablero.lock_acceso_tablero.release()
            return nota_a_mover.copy()
        else:
            Tablero.lock_acceso_tablero.release()
            raise Conflicto(
                f"Conflicto de versión: la nota ya ha sido movida."
            )
    
