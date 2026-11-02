# Notitas · caso base del proyecto final

Caso base del proyecto final de Ágiles 2026-2 (tema 3, pair programming) de Ana Sofía Arango Yanza y Juan José Arias Chacua. **Notitas** es un tablero kanban de notas adhesivas: las notas se pegan en tres columnas (*Por hacer · En curso · Hecho*) y se mueven entre ellas.

**Lo que se mide** es el desarrollo de las 24 reglas del backend: cada una es una función o clase de Python que hoy está vacía y hay que programar. **Lo que no se mide** es el frontend, que ya está hecho y solo muestra lo que responde el backend.

## Estructura
```
backend/
  notitas/t01.py … t24.py   ← las 24 tareas: aquí, y solo aquí, se escribe la lógica
  tests/visibles/           ← pruebas que guían el desarrollo de cada tarea
  tests/ocultas/            ← pruebas que miden los errores que se escapan (no se abren antes de terminar)
  servidor.py               ← API sencilla: guarda las notas en un JSON y llama a las funciones de las tareas
  datos_iniciales.json      ← notas de ejemplo
frontend/
  index.html, estilo.css, app.js, fuentes/   ← el tablero con animaciones (paleta Macarons)
agente/      ← configuración del agente para los ciclos (OpenCode)
registro/    ← salida del sorteo y notas de cada sesión
TAREAS.md    ← enunciado y criterios de aceptación de cada tarea
sorteo.py    ← asigna las tareas a cada condición
```

Cada archivo `backend/notitas/tNN.py` trae la firma de la función y un `raise NotImplementedError`. Programar la tarea es **reemplazar esa línea por la lógica**. No hay que tocar ni el servidor ni el frontend: en cuanto una función funciona, el tablero empieza a usarla ("Reglas encendidas: N/24").

## Uso
Solo necesita Python 3.10+ y pytest.
```bash
pip install pytest
python -m pytest -k t05                            # pruebas visibles de una tarea (por defecto NO corre las ocultas)
python -m pytest backend/tests/ocultas -k t05      # pruebas ocultas: SOLO después de declarar "terminado"
python backend/servidor.py                         # el tablero en http://localhost:8000
```

## Tamaño de las tareas y en qué se basa
| Tamaño | Tiempo estimado | Criterio |
|---|---|---|
| **S** (pequeña) | 15–25 min | Una función que valida o transforma un dato, con reglas independientes entre sí |
| **M** (mediana) | 25–45 min | Varias reglas que interactúan, manejo de fechas o zonas horarias, o una clase con estado |
| **L** (grande) | 45–70 min | Concurrencia o un algoritmo de varios pasos con casos de conflicto |

Es una **estimación por juicio** de quien diseñó las tareas, revisada por la pareja antes de congelar. No se usa como dato: solo sirve para que cada condición reciba una mezcla parecida de tareas. El número de criterios de aceptación no sirve para distinguir los tamaños (todas tienen entre 3 y 5). La duración real la da el cronómetro, y si un tamaño no se cumple, se reporta.

## Reglas de cada tarea (son las que hacen válida la medición)
1. **Antes de empezar:** anotar cuántos minutos creen que les tomará (pronóstico).
2. **Arrancar el cronómetro** al abrir el enunciado en `TAREAS.md` y hacer el commit vacío: `git commit --allow-empty -m "tNN: inicio"`.
3. **Trabajar** solo con las pruebas visibles.
   - **Línea base:** pareja humana en llamada, sin IA; en cada tarea uno escribe en su computador (conductor) y el otro revisa y guía (navegante). El conductor se alterna por tarea, mitad y mitad. Solo se permite documentación y búsquedas puntuales en la web; ninguna IA.
   - **Ciclos:** una persona sola con el agente, y una fila de bitácora por cada uso.
4. **Declarar "terminado"** cuando pasan las visibles. Parar el cronómetro y hacer el commit `tNN: terminado`.
5. **Correr las ocultas.** Cada prueba que falle es un **error escapado**. Si lo corrigen, el tiempo cuenta aparte como **retrabajo**, con el commit `tNN: retrabajo`.
6. **Codewalk:** 5 preguntas sin mirar el código, de 0 a 5, al autor y al compañero.
7. Llenar la hoja *Medicion por caso* de la bitácora.

> **No abrir `backend/tests/ocultas` antes de terminar.** Si alguien las abre por error, la tarea se marca `[C]` y se reemplaza por una de repuesto.
> **El tablero no se toca durante una sesión cronometrada.** Sus datos se guardan en `backend/datos.json` (no se sube); para empezar de cero, se borra ese archivo.

## Asignación por sorteo
```bash
python sorteo.py <semilla> > registro/sorteo_<semilla>.txt
```
Cupos fijos por tamaño: la línea base recibe 5 S · 4 M · 1 L, la condición con agente 5 S · 6 M · 1 L, y quedan 2 M de repuesto. Las tareas difíciles se reparten alternando entre condiciones, el orden de las tareas también se sortea y, con agente, cada persona conduce 6 tareas. Anoten la semilla: cualquiera puede repetir el sorteo y obtener lo mismo.

## Validación del caso
Las 113 pruebas (41 visibles y 72 ocultas) **fallan** con las funciones vacías y **pasan** con soluciones de referencia, comprobado el 31/10/2026. Esas soluciones **no** están en el repositorio: si estuvieran, la medición no sería a ciegas.
