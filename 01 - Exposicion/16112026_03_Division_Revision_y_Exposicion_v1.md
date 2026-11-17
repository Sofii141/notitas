# Quién revisa, quién expone y quién prepara la demo

Archivos:
- Reporte: `08 - Reporte/16112026_01_Reporte_Final_v6.pdf`
- Diapositivas: `01 - Exposicion/Diapositivas/16112026_01_Diapositivas_v5.html`
- Demo: `01 - Exposicion/16112026_02_Guia_Demo_v2.md`

> **Importante:** esta división es solo para repartir el trabajo y los turnos para hablar. **Los dos deben poder explicar todo**: el profe pregunta cosas que no están en las diapositivas, y en la entrega anterior se perdieron puntos por repartirse la sustentación por roles. Cada uno lleva escritas las cifras clave (al final de este archivo).

Es una propuesta: cámbienla si lo prefieren.

---

## 1. Revisión del reporte (hoy, antes de entregar)

Cada uno revisa su parte con cuidado y después **lee la del otro** de corrido. Marquen lo que no entiendan o lo que no sea cierto, y me lo mandan.

| Secciones | Revisa primero | Qué mirar |
|---|---|---|
| Portada, 1 Tema, 2 Caso base, 3 Línea base | Ana Sofía | Que los datos de la tabla de la línea base coincidan con las fichas |
| 4 Especificación, 5 Ciclos | Juan José | Que las versiones y los permisos sean como pasó de verdad |
| 6 Antes y después, 7 Tres fallos | Ana Sofía | Que cada fallo cuente lo que pasó (t01, la prueba de permisos, t11 y t09) |
| 8 Riesgos, 9 Conclusión, 10 Uso de IA | Juan José | Que la conclusión no diga más de lo que muestran los datos |
| Fuentes y anexos | Los dos | Que los enlaces abran |

## 2. Exposición: 25 minutos (10 tema + 8 proyecto + 7 preguntas)

| Diapositivas | Parte | Habla | Tiempo |
|---|---|---|---|
| 1 Portada | — | Los dos se presentan | 0:20 |
| 2 El problema · 3 Cómo funciona | Tema | Ana Sofía | 3:00 |
| 4 Qué dice la evidencia · 5 Pruébenlo así | Tema | Juan José | 3:40 |
| 6 Crítica | Tema | Ana Sofía | 3:00 |
| 7 Notitas · 8 Cómo medimos · 9 Línea base | Proyecto | Juan José | 1:15 |
| 10 Escenarios · 11 Antes y después · 12 Lo demás | Proyecto | Ana Sofía | 1:15 |
| 13 Bitácora · 14 Tres fallos · 15 Riesgos | Proyecto | Juan José | 1:00 |
| 16 **Demo en vivo** | Proyecto | Conduce y navega (abajo) | 4:30 |
| 17 Cierre: la frase | Cierre | Ana Sofía | 0:20 |
| 18 Dos preguntas para el curso | Cierre | Juan José | 0:20 |
| 19 Declaración de uso de IA | Cierre | Los dos (a la vista durante las preguntas) | — |

**Ojo con el tiempo:** el proyecto son 8 minutos y la demo se lleva 4:30, así que las diapositivas 7 a 15 tienen unos 3:30. Pasen rápido por la 7, la 8 y la 10, y dediquen el tiempo a la 11 (antes y después) y a la 14 (fallos). Ensayen con cronómetro.

## 3. Demo

| Qué | Quién |
|---|---|
| Preparar el entorno el día anterior: `git pull`, VS Code, OpenCode y el tablero | Juan José |
| Ensayar y **grabar el video de respaldo de 2 minutos** | Los dos (graba quien conduce) |
| Conduce en vivo: escribe y pega el prompt | ________ |
| Navega en vivo: escribe el enfoque, lee lo que propone el agente y ayuda a decidir | ________ |
| En el salón: probar el proyector y el internet antes de la sesión | Los dos |
| Dejar todo limpio después (`git checkout -- backend/notitas/t20.py`) | Quien conduce |

## 4. Cifras clave (cada uno las lleva escritas)

- **13 tareas medidas:** 5 en pareja sin IA y 8 con agente (2 por escenario).
- **Tiempo (mediana de M1):** tareas pequeñas 42.5 min sin IA y 16.5 con agente; medianas 27 y 19; la grande 54 sin IA y 61 con agente.
- **Ocultas que fallaron:** 2 de 15 sin IA y 1 de 24 con agente.
- **Bitácora:** 29 salidas del agente: 24 aceptadas, 3 corregidas y 2 rechazadas.
- **Codewalk a ciegas (ChatGPT · GPT Astra Max):** mediana 3 sin IA y 3 con agente; E3, 2. Nos calificábamos 1,6 puntos más alto. La pregunta 2 solo vale 1 en 4 de 20.
- **En 6 de 8 tareas con agente**, "¿por qué esta forma?" fue "porque la propuso el agente".
