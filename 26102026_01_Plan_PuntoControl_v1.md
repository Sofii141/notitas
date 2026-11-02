# Plan para el punto de control — viernes 30 de octubre

**Lo que hay que mostrar:**
1. Caso base de ≥10 casos con material difícil.
2. Especificación v1 del agente.
3. Línea base **ya medida**.
4. Además, ese día se intercambian 3 casos con otra pareja.

Ojo: el 27 tienen la Entrega 2 y el 28 el Parcial 2. Por eso el trabajo pesado queda para hoy (26) y el 29.

## Lo que ya está listo ✅
| Qué | Dónde |
|---|---|
| Caso base: repo con 24 tareas (11 S, 11 M, 2 L; 10 difíciles ⚠️), pruebas visibles y ocultas validadas, sorteo reproducible, con git | `Repositorio/CAMEIA-lite` (https://github.com/Sofii141/CAMEIA-lite) |
| GQM v1 con 6 métricas y el codewalk | `03 - Linea base/Versiones anteriores/v1/26102026_01_GQM_v1.md` |
| Spec v1 del agente (borrador) | `04 - Especificacion agentes/Versiones anteriores/v1/25102026_01_Spec_Copiloto_v1.md` |
| Bitácora y hoja de medición | `05 - Ciclos y bitacora/Versiones anteriores/v1/25102026_01_Bitacora_v1.xlsx` |
| Cómo miden los estudios + 5 artículos en PDF | `01 - Exposicion/Fuentes/` |

## Lo que tienen que hacer ustedes
### Lunes 26 (hoy) — 1,5 h juntos
- [ ] **Revisar las 24 tareas** en `TAREAS.md`. Si una está mal planteada, se corrige **ahora**: después del congelamiento ya no se toca. Ustedes responden por el caso, no yo.
- [ ] Revisar que las tareas t10, t11, t12, t23 (Juan José) y t15 (Ana Sofía) estén bien marcadas como "ya implementadas".
- [ ] **Congelar:** commit `congelado v1` en el repo y la fecha en el CHANGELOG.
- [ ] **Sorteo:** `python sorteo.py <semilla>`. Guardar la semilla y la salida en `09 - Control de entrega/Actas pareja/`.
- [ ] Elegir la herramienta del agente (Copilot, Claude Code o Cursor) y el modelo exacto, y completar ese campo de la spec v1.
- [ ] Si alcanza: **piloto con 1 tarea de repuesto** para practicar cronómetro, codewalk y hoja. El piloto **no cuenta**: se anota como tal.

### Martes 27 y miércoles 28 — Entrega 2 y Parcial 2
Nada del proyecto, salvo pedirle al profe (por correo o en clase) que confirme **por escrito** que CAMEIA-lite sirve como caso base.

### Jueves 29 — 4 a 5 h juntos: **línea base**
- [ ] Hacer las **10 tareas de "Línea base"** del sorteo en pareja humana, **sin IA**, siguiendo las 7 reglas del README del repo.
- [ ] Grabar la pantalla (OBS o Teams). Es la evidencia de que la línea base es real, como en Shihab 2025.
- [ ] Llenar la hoja *Medicion por caso* **al terminar cada tarea**, no al final del día.
- [ ] Al cerrar: copiar la bitácora con fecha nueva (`29102026_01_Bitacora_v2.xlsx`) y anotarlo en el CHANGELOG.

### Viernes 30 — antes de clase (1 h)
- [ ] Que **la otra persona recalcule** el promedio de duración y de errores escapados. Fue lo que les faltó en la E1.
- [ ] Preparar una página de resumen de la línea base: n, promedios por tamaño, condiciones y qué NO demuestra.
- [ ] **3 casos para la otra pareja:** dependen del tema de esa pareja, así que se arman cuando sepan cuál les toca. Que sean difíciles de verdad.
- [ ] Llevar al profe: el repo, el GQM, la spec v1 y la línea base.
- [ ] En clase: recibir los 3 casos de la otra pareja y guardarlos en `02 - Caso base/Casos recibidos`.

## Riesgos de esta semana
- **No alcanzan las 10 tareas el 29.** Empiecen por las M y la L; las S son rápidas. Si quedan 8, se reporta n = 8 con la marca `[N]`. No se inventa nada.
- **Alguien mira las pruebas ocultas** antes de tiempo: se marca `[C]` y la tarea se reemplaza por una de repuesto.
- **Aprendizaje entre tareas:** con el tiempo van a ir más rápido. Por eso el orden de las tareas también se sortea, y se declara como limitación.
