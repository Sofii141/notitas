# Notitas · caso base del proyecto final

Este es el caso base del proyecto final de Ágiles 2026-2 (tema 3, pair programming). **Notitas** es un tablero kanban de notas adhesivas (*Por hacer · En curso · Hecho*), con un front animado y un backend sencillo en Python.

- **Lo que se mide:** 24 tareas del backend (10 S · 12 M · 2 L, de las cuales 10 son difíciles). Cada una es una regla del tablero escrita como función o clase pura, con **pruebas visibles** (41) y **pruebas ocultas** (72). Enunciados: [`TAREAS.md`](TAREAS.md).
- **Lo que no se mide:** el front (`demo/`). Ya está hecho, solo muestra lo que responde el backend y se va "encendiendo" a medida que se implementan las tareas.

> Este repositorio antes tenía CAMEIA-lite. Se reemplazó el 31/10/2026 con aprobación del profesor (plazo del caso base ampliado al 3/11). La versión anterior sigue en el historial y en el tag `congelado-v1`.

Solo necesita Python 3.10+ y pytest.

## Uso
```bash
pip install pytest
python -m pytest -k t05                    # pruebas visibles de una tarea (por defecto NO corre las ocultas)
python -m pytest tests/ocultas -k t05      # pruebas ocultas: SOLO después de declarar "terminado"
python demo/servidor.py                    # el tablero en http://localhost:8000
```

## Reglas de cada tarea (son las que hacen válida la medición)
1. **Antes de empezar:** anotar cuántos minutos creen que les tomará (pronóstico).
2. **Arrancar el cronómetro** al abrir el enunciado en `TAREAS.md` y hacer el commit `tNN: inicio`.
3. **Trabajar** solo con las pruebas visibles.
   - **Línea base:** pareja humana sin IA; uno conduce, el otro navega, y cambian cada 15 min.
   - **Ciclos:** una persona con el agente copiloto, y una fila de bitácora por cada uso.
4. **Declarar "terminado"** cuando pasan las visibles. Parar el cronómetro y hacer el commit `tNN: terminado`.
5. **Correr las ocultas.** Cada prueba que falle es un **error escapado**. Si lo corrigen, el tiempo cuenta aparte como **retrabajo**, con el commit `tNN: retrabajo`.
6. **Codewalk:** 5 preguntas sin mirar el código, de 0 a 5, al autor y al compañero.
7. Llenar la hoja *Medicion por caso* de la bitácora.

> **No abrir `tests/ocultas` antes de terminar.** Si alguien las abre por error, la tarea se marca `[C]` y se reemplaza por una de repuesto.
> **La demo no se toca durante una sesión cronometrada.** Los datos de la demo se guardan en `demo/datos.json` (no se sube); para empezar de cero, se borra ese archivo.

## Asignación por sorteo
```bash
python sorteo.py <semilla> > registro/sorteo_<semilla>.txt
```
Cupos fijos por tamaño: la línea base recibe 5 S · 4 M · 1 L, la condición con agente 5 S · 6 M · 1 L, y quedan 2 M de repuesto. Las tareas difíciles se reparten alternando entre condiciones, el orden de las tareas se sortea y, con agente, cada persona conduce 6 tareas. Anoten la semilla en un acta: cualquiera puede repetir el sorteo y obtener lo mismo.

## Estructura
| Carpeta | Qué hay |
|---|---|
| `src/notitas/tNN.py` | Los esqueletos de las 24 tareas (lanzan `NotImplementedError` hasta que se implementen) |
| `tests/visibles`, `tests/ocultas` | Las pruebas de cada tarea |
| `demo/` | `servidor.py` (backend, solo librería estándar), `index.html`, `estilo.css` y `app.js` (front con animaciones, paleta Macarons), y los datos de ejemplo |
| `registro/` | La salida del sorteo y las notas de cada sesión |

## Validación del caso
Las 113 pruebas **fallan** con los esqueletos y **pasan** con las soluciones de referencia, comprobado el 31/10/2026. Las soluciones de referencia **no** están en el repositorio: si estuvieran, la línea base no sería a ciegas.
