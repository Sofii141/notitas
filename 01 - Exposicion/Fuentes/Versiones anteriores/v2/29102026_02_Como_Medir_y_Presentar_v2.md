# Cómo medir y cómo presentar los resultados — v2 (29/10/2026)

Reemplaza a `26102026_01_Como_Miden_Estudios_v1.md` (se conserva). **Qué cambió:** cada decisión se apoya ahora en artículos **revisados por pares** (la lista completa, con DOI, está en `29102026_01_Fuentes_v2.md`). Se agregó la parte que faltaba: **cómo presentar resultados con pocas tareas**, sin afirmar más de lo que los datos permiten.

---

## 1. Qué medimos y de dónde sale cada métrica

| Métrica (GQM) | Definición operacional | Respaldo revisado por pares |
|---|---|---|
| **M1 Duración** | Minutos de cronómetro desde abrir el enunciado hasta que pasan las pruebas visibles, menos las pausas | Hannay 2009 (A1); Arisholm 2007 (A2); Shihab 2025 (B3) |
| **M2 Esfuerzo** | Duración × personas: pareja humana = 2, persona + agente = 1 | Hannay 2009 (A1); Arisholm 2007 (A2): las parejas usaron 84 % más esfuerzo |
| **M3 Errores escapados** | Pruebas **ocultas** que fallan al declarar "terminado", reportadas como *fallan / total* (3 por tarea; t23 tiene 2) | Arisholm 2007 (A2): corrección medida con pruebas que el desarrollador no ve; Dakhel 2023 (B8) |
| **M4 Retrabajo** | Minutos y commits `tNN: retrabajo` después del primer "terminado" | Enunciado del curso ("retrabajo"); medición propia |
| **M5 Comprensión** | Codewalk de 5 preguntas (0–5) al autor y al compañero, sin mirar el código | Plonka 2015 (A5) y Welter 2025 (B1): transferencia de conocimiento; Shihab 2025 (B3): no entendían las sugerencias |
| **M6 Percepción** | Pronóstico en minutos antes de empezar y ayuda percibida (−2 a +2) al terminar; se reporta *real / pronóstico* | Perry 2023 (B5): más confianza y menos seguridad; Lee 2025 (B6). (METR 2025 va como contexto: es preprint) |

## 2. Cómo tomar el dato para que valga (Ko, LaToza y Burnett, 2015 — C1)

1. **Criterio de éxito definido antes**: la tarea termina cuando pasan las pruebas visibles. Nada de "ya casi".
2. **Tiempo hasta el éxito**, con el cronómetro corriendo desde que se abre el enunciado (la lectura cuenta, en las dos condiciones igual). Si hay interrupciones, se restan en *Pausas*.
3. **Una tarea de práctica (piloto)** antes de empezar, que no cuenta. Sirve para practicar el cronómetro y el codewalk. Si no hay tiempo, se declara.
4. **Orden sorteado**: `sorteo.py` ya imprime el orden de cada condición. Con eso se reduce el sesgo por aprendizaje entre tareas.
5. **Evidencia**: grabación de pantalla, commits `tNN: inicio / terminado / retrabajo`, salida de `pytest`.
6. **Llenar la hoja al terminar cada tarea**, no de memoria.

## 3. Cómo presentar los resultados (Kitchenham et al., 2017 — C2; Vargha y Delaney, 2000 — C3)

Con unas 10 tareas por condición, los datos son pocos y no siguen una normal (hay tareas de 10 minutos y de 60). Por eso:

| En lugar de… | Hacemos… | Por qué |
|---|---|---|
| Promedio | **Mediana [mínimo–máximo]** | Una sola tarea larga no arrastra el resultado (C2) |
| Un solo número global | **Por tamaño (S, M, L)** y el total | El efecto depende de la complejidad (A1, A2) |
| "Fue X % más rápido" | **A12** (probabilidad de que una tarea con agente tarde más que una de la línea base; 0,5 = iguales) | Se entiende sin saber estadística y aguanta muestras pequeñas (C3) |
| p-valor y "es significativo" | **No** se afirma significancia ni causalidad | Con n ≈ 10 no hay potencia; se reporta como descriptivo (C2, C4) |
| Solo el resumen | **Tabla completa por tarea** en el anexo (la bitácora) | Que cualquiera pueda recalcular (C4) |
| Duración cruda | Además, **real / pronóstico** | Mide la "sensación de velocidad" y compensa que unas tareas sean más largas |

**Gráfico recomendado para el reporte y las diapositivas:** un gráfico de puntos con una fila por tamaño (S, M, L), un punto por tarea y un color por condición (Semolina para la línea base, Matcha para el agente), y una raya en la mediana. Se ven todos los datos, no solo el promedio.

**Plantilla de frase para cada resultado** (así lo premia el profe):
> "En la línea base (n = 10), la mediana de duración en tareas M fue **X min [mín–máx]**; con el agente (n = 6), **Y min [mín–máx]**; A12 = 0,xx. **Qué no demuestra:** no prueba que el agente cause la diferencia (n pequeño, tareas distintas en cada condición, aprendizaje entre semanas)."

**Recálculo independiente (lo que faltó en la E1):** el script `07 - Analisis/Scripts/resumen_medicion.py` calcula desde los datos crudos, la hoja *Resumen* del Excel calcula con sus fórmulas, y **la otra persona recalcula a mano** al menos una mediana. Si los tres coinciden, la cifra lleva `[R]`.

## 4. Amenazas a la validez que hay que declarar (Wohlin et al., 2012 — C5)

| Tipo | Amenaza en *nuestro* caso | Qué hacemos |
|---|---|---|
| Interna | Aprendizaje: la línea base va primero (29/10) y el agente después (noviembre) | Se sortea el orden dentro de cada etapa y se declara |
| Interna | Ana Sofía generó las tareas y las pruebas con Claude Code: conoce el diseño | Declararlo. Propuesta (lo decide la pareja): en la línea base, que Juan José conduzca primero en cada tarea |
| Interna | 5 tareas ya las implementó uno de los dos en CAMEIA | Van solo con agente y las hace la otra persona (`sorteo.py`) |
| De constructo | M2 favorece al agente "por diseño" (2 personas frente a 1) | Se reporta M1 y M2 por separado y se dice explícitamente |
| De constructo | M5 del compañero: en la línea base participó; con el agente, no | Lo que se compara es **la transferencia de conocimiento** (A5, B1): es justo la pregunta del tema, y se aclara |
| De constructo | M3 es gruesa (0 a 3 por tarea) | Se reporta como suma *fallan / total* por condición |
| Externa | Tareas aisladas (funciones puras) de un solo proyecto, con 2 personas | No se generaliza; se compara con lo que dice la literatura |
| De conclusión | n ≈ 10 por condición | Solo estadística descriptiva y A12; nada de causalidad |
