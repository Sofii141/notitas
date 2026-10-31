# Codewalk: las 5 preguntas y la X y la Y de cada tarea — v1 (31/10/2026)

**Para qué:** el codewalk (métrica M4 del GQM v3) mide si quien programó la tarea, y su compañero, **entienden** el código. Las 5 preguntas son **siempre las mismas** y sirven para cualquier tarea, porque preguntan por comprensión (qué hace, casos borde, por qué, cómo depurar, cómo cambiar) y no por una tarea en particular.

Lo único que cambia por tarea son la **X** (pregunta 4) y la **Y** (pregunta 5). Quedan **fijas aquí** para que sean idénticas en la línea base y con el agente, y para que no dependan de lo que se le ocurra al evaluador en el momento.

> **Solo lo abre quien evalúa.** Quien va a programar la tarea no lo lee antes: si conoce la X y la Y, el codewalk deja de medir comprensión.

## Las 5 preguntas (1 punto cada una; máximo 5 minutos por persona)
Quien responde **no** mira el código ni al agente. Quien evalúa **sí** tiene el código abierto y da 1 punto si la respuesta es correcta y concreta, y 0 si es vaga o incorrecta.
1. ¿Qué hace la función, en una frase?
2. ¿Qué caso borde maneja y dónde?
3. ¿Por qué se eligió esta forma y no otra?
4. Si mañana falla con la entrada **X**, ¿dónde mirarías primero?
5. ¿Qué cambiarías si el requisito cambia en **Y**?

**Cómo se puntúan la 4 y la 5:** 1 punto si la persona señala la parte correcta del código (la línea, la condición o el bloque que habría que mirar o cambiar) y explica por qué. "Volvería a leer todo" vale 0.

## X e Y por tarea
| Tarea | X (pregunta 4: "si falla con…") | Y (pregunta 5: "si el requisito cambia a…") |
|---|---|---|
| t01 | `" Hola "` devuelve el título con espacios | el máximo pasa de 80 a 120 caracteres |
| t02 | `"#bcc86f"` lanza error | se agrega el color "crema" `#FFF8EF` a la paleta |
| t03 | `"Hecho"` (con mayúscula) no lanza error | también se permite pasar de *Por hacer* directo a *Hecho* |
| t04 | reordenar dentro de *En curso* con 3 notas lanza `WipExcedido` | el límite también aplica a *Hecho* (máximo 10) |
| t05 | mover `"a"` a la posición 2 en `["a","b","c"]` da `["b","a","c"]` | una posición negativa significa "contar desde el final" |
| t06 | `["CASA"]` no encuentra la etiqueta `"casa"` | se agrega el modo `"ninguna"` (notas sin esas etiquetas) |
| t07 | `"nino"` no encuentra `"niño"` | también se busca dentro de las etiquetas |
| t08 | a las 22:00 de Bogotá (03:00 UTC del día siguiente) devuelve `"vencida"` | "pronto" pasa a ser de 1 a 7 días |
| t09 | `["a","A"]` devuelve dos etiquetas | el máximo pasa a 3 etiquetas y se descartan las sobrantes en vez de dar error |
| t10 | una nota hecha hace exactamente 7 días se archiva | se archivan también las notas de *Por hacer* sin cambios en 30 días |
| t11 | después de 21 movimientos, el primero todavía se puede deshacer | se agrega "rehacer" |
| t12 | dos hilos con la misma versión mueven la nota los dos | el conflicto devuelve también la versión actual de la nota |
| t13 | importar dos notas con el mismo `id` no da error | el formato exportado incluye la fecha de exportación |
| t14 | `"**<b>**"` deja pasar la etiqueta `<b>` | se permite también `*cursiva*` |
| t15 | 1 hecha de 8 notas da 12 % en vez de 13 % | el porcentaje se calcula sin contar *Por hacer* |
| t16 | dos notas iguales cambian de orden entre sí | las notas sin fecha van al principio de su grupo |
| t17 | la página 0 no lanza error | el tamaño de página máximo es 50 |
| t18 | `"María de los Ángeles"` devuelve `"ML"` | se devuelven hasta 3 iniciales |
| t19 | `[{"texto": "a", "hecho": 1}]` no lanza error | el porcentaje se redondea al más cercano |
| t20 | cambiar las etiquetas de la copia cambia también las de la original | la copia conserva la columna de la original |
| t21 | `10:00-05:00` frente a `14:00+00:00` gana el de las 14:00 | ante un empate, gana el valor de `base` |
| t22 | un motivo de solo espacios desbloquea la nota | también se guarda quién desbloqueó la nota |
| t23 | una nota reabierta cuenta solo la última vez en *En curso* | se descuentan las horas de fin de semana |
| t24 | el intento rechazado en el segundo 30 cuenta en la ventana | el límite es por minuto calendario (de :00 a :59), no por ventana deslizante |

## Ejemplo (t08, Fecha de vencimiento)
- *P4:* "Si mañana a las 10 p. m. una nota que vence hoy aparece como vencida, ¿dónde mirarías?" → 1 punto si dice: "donde se convierte `ahora` a la hora de Bogotá antes de sacar la fecha", y explica por qué.
- *P5:* "Si 'pronto' pasa a ser de 1 a 7 días, ¿qué cambiarías?" → 1 punto si señala la condición que decide cuándo una nota está "pronto".
