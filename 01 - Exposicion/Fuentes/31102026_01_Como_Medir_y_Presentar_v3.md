# Cómo medir y cómo presentar los resultados — v3 (31/10/2026, caso Notitas)

Reemplaza a `Versiones anteriores/v2/29102026_02_Como_Medir_y_Presentar_v2.md` (se conserva). **Qué cambió:** el caso base es ahora **Notitas** y las métricas se redujeron a las **5 directas del GQM v3**: sin esfuerzo, sin ayuda percibida y sin tamaño de efecto. Las fuentes con DOI están en `29102026_01_Fuentes_v2.md`.

---

## 1. Qué medimos y de dónde sale cada métrica

| Métrica (GQM v3) | Definición operacional | Respaldo revisado por pares |
|---|---|---|
| **M1 Minutos** | Desde que se abre el enunciado hasta que pasan las pruebas visibles, menos las pausas | Hannay 2009 (A1); Arisholm 2007 (A2); Shihab 2025 (B3) |
| **M2 Ocultas que fallan** | Pruebas ocultas que fallan al declarar "terminado" (de 3 por tarea) | Arisholm 2007 (A2): corrección medida con pruebas que el desarrollador no ve; Dakhel 2023 (B8) |
| **M3 Minutos de retrabajo** | Minutos de corrección después del primer "terminado" (0 si no hubo) | Enunciado del curso ("retrabajo") |
| **M4 Codewalk 0–5** | 5 preguntas al autor y al compañero, sin mirar el código | Plonka 2015 (A5) y Welter 2025 (B1): transferencia de conocimiento; Shihab 2025 (B3) |
| **M5 Pronóstico** | Minutos que creen que tardarán, anotados antes de empezar; se compara con M1 | Perry 2023 (B5); Lee 2025 (B6). METR 2025 solo como contexto (es un preprint) |

## 2. Cómo tomar el dato para que valga (Ko, LaToza y Burnett, 2015 — C1)

1. **Criterio de éxito definido antes**: la tarea termina cuando pasan las pruebas visibles. Nada de "ya casi".
2. **Tiempo hasta el éxito**, con el cronómetro corriendo desde que se abre el enunciado (la lectura cuenta, en las dos condiciones igual). Si hay interrupciones, se restan en *Pausas*.
3. **Una tarea de práctica (piloto)** antes de empezar, que no cuenta. Sirve para practicar el cronómetro y el codewalk. Si no hay tiempo, se declara.
4. **Orden sorteado**: `sorteo.py` ya imprime el orden de cada condición. Con eso se reduce el sesgo por aprendizaje entre tareas.
5. **Evidencia**: grabación de pantalla, commits `tNN: inicio / terminado / retrabajo`, salida de `pytest`.
6. **Llenar la hoja al terminar cada tarea**, no de memoria.

## 3. Cómo presentar los resultados (Kitchenham et al., 2017 — C2)

Con unas 10 tareas por condición, los datos son pocos y no siguen una distribución normal (hay tareas de 10 minutos y de 60). Por eso el análisis es **descriptivo y directo**:

| En lugar de… | Hacemos… | Por qué |
|---|---|---|
| Promedio | **Mediana [mínimo–máximo]** de M1 y M4 | Una sola tarea larga no arrastra el resultado (C2) |
| Un solo número global | **Por tamaño (S, M, L)** y el total | El efecto depende de la complejidad (A1, A2) |
| Porcentajes de mejora | **Conteos**: "se escaparon 4 de 30 errores", "3 de 10 tareas con retrabajo", "en 7 de 12 tardamos más de lo pronosticado" | Se entienden y se recalculan fácil |
| p-valor y "es significativo" | **No** se afirma significancia ni causalidad | Con n ≈ 10 no hay potencia estadística (C2, C4) |
| Solo el resumen | **Tabla completa por tarea** en el anexo (la bitácora) | Que cualquiera pueda recalcular (C4) |

**Gráfico recomendado:** uno de puntos, con una fila por tamaño, un punto por tarea y un color por condición (Semolina para la línea base, Matcha para el agente), y una raya en la mediana.

**Plantilla de frase para cada resultado:**
> "En la línea base (n = 10), la mediana en tareas M fue **X min [mín–máx]**; con el agente (n = 6), **Y min [mín–máx]**. Se escaparon **a de b** errores frente a **c de d**. **Qué no demuestra:** no prueba que el agente cause la diferencia (n pequeño, tareas distintas en cada condición, aprendizaje entre días)."

**Recálculo independiente:** el script `07 - Analisis/Scripts/resumen_medicion.py` calcula desde los datos crudos, la hoja *Resumen* con sus fórmulas, y la otra persona a mano al menos una mediana. Si coinciden, la cifra lleva `[R]`.

## 4. Amenazas a la validez que hay que declarar (Wohlin et al., 2012 — C5)

| Tipo | Amenaza en *nuestro* caso | Qué hacemos |
|---|---|---|
| Interna | Aprendizaje: la línea base va primero (29/10) y el agente después (noviembre) | Se sortea el orden dentro de cada etapa y se declara |
| Interna | Las tareas, las pruebas y la demo se generaron con Claude Code | El agente de los ciclos es otro modelo (DeepSeek V4.1 Flash en OpenCode); nadie ve las ocultas ni las soluciones de referencia (`_Privado/`) antes de terminar |
| De constructo | En la línea base trabajan 2 personas y con el agente 1: el costo en persona-tiempo es distinto | Se comenta en el análisis (M1 × 2 en la línea base), sin convertirlo en una métrica aparte |
| De constructo | M4 del compañero: en la línea base participó; con el agente, no | Lo que se compara es **la transferencia de conocimiento** (A5, B1): es justo la pregunta del tema, y se aclara |
| De constructo | M2 es gruesa (0 a 3 por tarea) | Se reporta como suma *fallan / total* por condición |
| Externa | Notitas es un caso diseñado para el experimento, con tareas aisladas y 2 personas | No se generaliza; se compara con lo que dice la literatura |
| De conclusión | n ≈ 10 por condición | Solo estadística descriptiva (medianas y conteos); nada de causalidad |
