| ID | P1 | P2 | P3 | P4 | P5 | Total | Motivo breve de cada 0 |
|---|---:|---:|---:|---:|---:|---:|---|
| R01 | 1 | 0 | 1 | 1 | 0 | 3 | P2: no ubica el desempate en el código. P5: mantiene el desempate por nombre en vez de elegir `valor_base`. |
| R02 | 1 | 1 | 1 | 1 | 1 | 5 | — |
| R03 | 1 | 0 | 0 | 1 | 1 | 3 | P2: el `if` citado usa una comparación de identidad que no detecta la lista vacía. P3: justificación genérica, sin explicar el enfoque. |
| R04 | 1 | 1 | 0 | 0 | 0 | 2 | P3: aceptar la sugerencia de la IA no justifica el diseño. P4: señala el destino, no la comprobación de la columna actual. P5: propone contar Hecho, pero no concreta el límite de 10 ni su validación por columna. |
| R05 | 1 | 0 | 0 | 1 | 1 | 3 | P2: no ubica los casos borde. P3: describe la aceptación de la propuesta, sin justificar la estructura elegida. |
| R06 | 1 | 0 | 1 | 1 | 1 | 4 | P2: no ubica la validación de columnas inexistentes. |
| R07 | 1 | 0 | 1 | 1 | 0 | 3 | P2: no ubica el bloqueo ni la copia profunda. P5: no concreta cómo incorporar la versión actual a la excepción al lanzarla. |
| R08 | 1 | 0 | 0 | 1 | 1 | 3 | P2: no ubica las comprobaciones. P3: relata la investigación, sin justificar las decisiones de implementación. |
| R09 | 1 | 0 | 0 | 1 | 1 | 3 | P2: no ubica las validaciones. P3: justificación genérica basada en aceptar la sugerencia. |
| R10 | 1 | 0 | 0 | 1 | 1 | 3 | P2: no ubica la comprobación del motivo. P3: menciona evitar duplicación, pero no explica qué decisión concreta lo consigue. |
| R11 | 1 | 0 | 0 | 0 | 0 | 1 | P2: no ubica el tratamiento de empates. P3: no justifica la ordenación. P4: no concreta qué comprobar en la clave de ordenación. P5: no identifica el criterio que debe invertir para adelantar las notas sin fecha. |
| R12 | 1 | 0 | 1 | 1 | 0 | 3 | P2: el `if` inicial no detecta correctamente etiquetas vacías; tampoco ubica la validación del modo. P5: no concreta la rama ni la condición para excluir notas con alguna etiqueta solicitada. |
| R13 | 1 | 0 | 1 | 1 | 0 | 3 | P2: no ubica la comprobación de total cero. P5: modificaría también el total general; debe cambiar solo el denominador del porcentaje. |
| R14 | 1 | 0 | 0 | 1 | 1 | 3 | P2: no ubica la validación de nombres. P3: afirmar que es funcional no justifica el enfoque. |
| R15 | 1 | 0 | 1 | 1 | 0 | 3 | P2: no ubica la comprobación de total cero. P5: eliminar la clave no ajusta correctamente el denominador y puede provocar `KeyError`. |
| R16 | 1 | 1 | 1 | 1 | 1 | 5 | — |
| R17 | 1 | 0 | 0 | 1 | 0 | 2 | P2: no ubica las comprobaciones. P3: afirma menor coste sin explicar el motivo. P5: conserva retornos y comprobaciones de En curso que impedirían validar correctamente Hecho. |
| R18 | 1 | 0 | 0 | 0 | 1 | 2 | P2: no ubica el criterio para fechas ausentes. P3: afirma eficiencia sin justificarla. P4: usar el índice negativo invertiría el orden que se debe conservar. |
| R19 | 1 | 0 | 1 | 1 | 0 | 3 | P2: no ubica la validación de límites. P5: devolver anticipadamente las tres primeras puede omitir la validación de 20 caracteres. |
| R20 | 1 | 1 | 1 | 1 | 1 | 5 | — |
