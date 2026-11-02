# Guía para el 5,0 — Proyecto final + Exposición (Tercer corte)

**Tema 3 · Pair programming:** programar en pareja con una persona vs. con un agente: qué se gana, qué se pierde y qué aprendizaje desaparece cuando el compañero no necesita entender.
**Práctica que asiste el agente (la fija el PDF):** desarrollo de una tarea con el agente como copiloto. **Qué medir:** tiempo, retrabajo y errores detectados a tiempo.

> Vale el 100 % del corte = 70 % reporte/proyecto + 30 % exposición. Lo único que anula todo el trabajo: **inventar datos de línea base o de bitácora.**

---

## 1. Lo que más pesa en la nota

| Reporte y proyecto (70 %) | Peso | Para el máximo |
|---|---|---|
| Medición y evidencia | **35 %** | ≥10 casos con material difícil, línea base real (antes del 30/10), comparación honesta |
| Gobernanza y bitácora | 25 % | Cada uso con decisión (aceptar/corregir/rechazar), **razón** y responsable |
| Especificación de agentes | 20 % | Prohibiciones explícitas, criterio de validación, versiones v1→v2 con su porqué |
| Fallos y riesgos | 20 % | 3 fallos reales + riesgos de *su* caso, no genéricos |

| Exposición (30 %) | Peso | Para el máximo |
|---|---|---|
| Dominio del tema | 30 % | Responder lo que no está en las diapositivas — **los dos saben todo** |
| Demo del proyecto | 25 % | En vivo, sobre su caso real, + video de respaldo de 2 min |
| Crítica del enfoque | 20 % | Límites y costos reales, con datos propios |
| Conexión tema–proyecto | 15 % | Una sola historia: el tema explica lo que midieron |
| Tiempo y claridad | 10 % | 10 + 8 min exactos, sin leer |

**Un resultado negativo bien medido saca mejor nota que uno positivo sin evidencia** (lo dice el PDF). No tienen que demostrar que el agente sirve; tienen que demostrar *qué pasó*.

---

## 2. Lo que este profe premia (sacado de la retro de la E1, donde sacaron 3/3 en medición y gobernanza)

1. **Las marcas `[V] [R] [P] [N] [C]`.** Lo que más le impresionó. Úsenlas en todo el reporte, también para las fuentes.
2. **Decir qué NO demuestra cada número** ("qué no representa esta métrica", "no podemos afirmar causalidad").
3. **Descartar métricas con datos** y explicar por qué.
4. **Que una segunda persona recalcule** al menos una cifra de forma independiente (fue lo que les faltó en la E1).
5. **Ir a la fuente primaria, no releer el texto de la IA** (el caso CM-25).
6. **Confirmar por escrito** cualquier adaptación con el profe y guardar esa confirmación en `09 - Control de entrega`.
7. **Lo que les quitó puntos en la E1 (C5):** se repartieron la sustentación por roles y se equivocaron citando cifras. Aquí: **cada uno debe poder explicar todo**, y llevar escritas las 5–6 cifras clave.
8. Tiene línea de investigación en **deuda de proceso / deuda técnica en ágil**. El ángulo "el agente genera *deuda de conocimiento* invisible en la velocidad" le va a sonar.

---

## 3. Diseño recomendado del proyecto

**La idea:** comparar la misma práctica en dos condiciones, sobre tareas reales del mismo proyecto:

| | Línea base (antes del 30/10) | Ciclos 1 y 2 (2–13 nov) |
|---|---|---|
| Condición | **Pareja humana** (driver/navigator, sin IA) | **Pareja con agente** (una persona + agente copiloto) |
| Casos | ≥10 tareas | ≥5 tareas por ciclo (≥10 en total) |

**Caso base (actualizado el 31/10):** **Notitas**, un tablero kanban de notas adhesivas con 24 tareas de backend (10 S · 12 M · 2 L, 10 difíciles), aprobado por el profe en reemplazo de CAMEIA-lite (que quedó en el tag `congelado-v1`). Plazo del caso base: martes 3/11.
- Incluyan **difíciles a propósito** (≥4 de 12): código que ninguno escribió, requisito ambiguo, API/librería que no conocen, bug difícil de reproducir, una tarea con un riesgo de seguridad escondido, una parte con factor de camión 0.
- **Clasifiquen por tamaño (S/M/L) y asignen condición por sorteo dentro de cada tamaño** (así se hizo en el estudio de METR; Hannay et al. 2009 muestran que el efecto del pairing depende de la complejidad).
- Congelen el caso (fecha en cada ficha) **antes** de medir. Lo que falte después va como limitación.
- Revisen datos sensibles antes de dárselos al agente (y si el repo es del Proyecto II, que el equipo esté de acuerdo).

**GQM (actualizado el 31/10):** son 5 métricas directas: minutos, ocultas que fallan, minutos de retrabajo, codewalk 0–5 y pronóstico. El detalle está en `03 - Linea base/31102026_01_GQM_v3.md`.

El codewalk es lo que conecta todo con el tema. La literatura revisada por pares dice que con IA se acepta con **menos escrutinio** (Welter et al. 2025), que los estudiantes **no entendían por qué funcionaban** las sugerencias (Shihab et al. 2025) y que hay **más confianza con menos seguridad** (Perry et al. 2023); en contra, Kazemitabaar et al. (2023) no encontró menos retención. Ustedes lo comprueban o lo refutan con su propio caso.

**Agentes:** empiecen con **uno solo** (Copiloto/navegante): **OpenCode con DeepSeek V4.1 Flash**, el mismo modelo para los dos. Agreguen un "Revisor" en el ciclo 2 **solo si** la bitácora del ciclo 1 muestra un problema que el primero no resolvía, y expliquen qué pasa cuando discrepan. Plantilla de spec ya creada en `04 - Especificacion agentes`.

---

## 4. Checklist por fechas

### ⚠️ Antes de nada (hoy–mañana)
- [ ] Confirmar que el tema 3 quedó registrado en el archivo compartido (cerró el 24/10) y guardar captura en `09`.
- [ ] Ojo con la semana: **Entrega 2 el 27/10 y Parcial 2 el 28/10** del curso, y el punto de control es el **30/10**. Repártanse bien.

### 🔴 Próxima entrega: caso base y línea base hasta el martes 3 de noviembre (el profe amplió el plazo; paso a paso en `09 - Control de entrega/31102026_02_Guia_Entrega_y_Medicion_v2.pdf`)
- [ ] **Caso base**: ≥10 fichas (mejor 12) con difíciles marcadas, congeladas. → `02 - Caso base/Casos propios`
- [ ] **Línea base medida**: ≥10 tareas en pareja humana con la hoja *Medicion por caso* llena + condiciones (quién, cuánto duró, herramientas). → `03 - Linea base`
- [ ] **GQM** escrito. → `03 - Linea base`
- [ ] **Especificación v1** del agente. → `04`
- [ ] **3 casos para entregar** a otra pareja (difíciles de verdad). → `02/Casos entregados`
- [ ] Ese día recibir los 3 de la otra pareja → `02/Casos recibidos` (obligatorio incorporarlos; repórtenlos aparte como "casos no previstos").
- [ ] Preguntarle al profe lo que tengan dudoso y **guardar la respuesta por escrito**.

### Ciclo 1 — 2 al 6 nov
- [ ] ≥5 tareas con el agente, **una fila de bitácora por cada uso** (la columna Razón es la que lee).
- [ ] Al cerrar: revisar la spec → **v2** con el porqué en el historial. Guardar `DDMMAAAA_NN_Bitacora_vX.xlsx`.

### Ciclo 2 — 9 al 13 nov
- [ ] ≥5 tareas más (incluir los 3 recibidos). Bitácora igual.
- [ ] Documentar **3 fallos reales**: qué hizo el agente, cómo lo detectaron, qué habría pasado sin revisión, qué cambiaron (prompt/spec/punto de control). → `06`
- [ ] Grabar el **video de la demo (2 min)**. → `99`

### Entrega — lunes 16 nov (reporte PDF 6–10 pág. + anexos + diapositivas)
1. Portada · 2. Tema, práctica y qué esperaban · 3. Caso base (½ pág.) + 3 recibidos · 4. Línea base (GQM, datos, n, condiciones) · 5. Spec con versiones · 6. Resumen de ciclos y decisiones más frecuentes · 7. Antes/después con interpretación (si no mejoró, decirlo) · 8. 3 fallos + riesgos (confidencialidad, sesgo/omisiones, sobredependencia — *de su caso*) + conclusión honesta · 9. Declaración de uso de IA.
**Anexos:** bitácora completa (xlsx) + specs/prompts finales.
- [ ] Una segunda persona recalcula una cifra clave (anotarlo).

### Exposición — 17 o 18 nov (llegar listos el 17; orden al azar)
- **10 min tema:** problema y contexto (2–3 min) → cómo funciona (driver/navigator vs. agente, para que alguien lo pruebe) → **crítica explícita**: qué no resuelve, cuándo no conviene, qué cuesta.
- **8 min proyecto:** línea base → qué hizo el agente → qué cambió → demo en vivo sobre una tarea de su caso.
- **Cierre:** una frase "qué nos dijo el tema sobre nuestro proyecto" + **2 preguntas para el curso** + diapositiva final de **declaración de uso de IA**.
- Probar el proyector y la red **antes** de la sesión; tener el video listo; no leer diapositivas.

---

## 5. Errores que bajan la nota
- Empezar por el prompt en vez de por la medición.
- Línea base "reconstruida de memoria" después del 30/10.
- Medir tres prácticas a la vez.
- "Nos sentimos más rápidos" como evidencia.
- Un agente que "nunca falló" (= no lo revisaron).
- Afirmar causalidad con n = 10.
- Darle al agente lo que no le darían a un tercero (secretos, datos personales).

## 6. Archivos ya creados (versiones vigentes al 31/10)
- `Repositorio/CAMEIA-lite` (rama `main`): caso base **Notitas** — `TAREAS.md`, `sorteo.py`, `demo/` y `agente/opencode.json`.
- `05 - Ciclos y bitacora/31102026_01_Bitacora_v3.xlsx` — sesiones, medición por caso, codewalk, bitácora y resumen.
- `04 - Especificacion agentes/31102026_01_Spec_Copiloto_v1.md` — spec v1 (OpenCode + DeepSeek V4.1 Flash).
- `03 - Linea base/31102026_01_GQM_v3.md` — GQM con 5 métricas directas.
- `01 - Exposicion/Fuentes/29102026_01_Fuentes_v2.md` y `31102026_01_Como_Medir_y_Presentar_v3.md` — fuentes revisadas por pares y cómo presentar los resultados.
- `09 - Control de entrega/02112026_01_Punto_Control_v5.pdf` — lo que se envía el 3/11; `31102026_02_Guia_Entrega_y_Medicion_v2.pdf` — el paso a paso.
- `02 - Caso base/Guia_Medicion/02112026_01_Guia_General_v5.pdf`: **empiecen aquí para medir**; de ahí pasan a la guía y a las fichas de cada condición.
- `02 - Caso base/Plantilla_Ficha_Caso.md` — ficha de cada caso.
