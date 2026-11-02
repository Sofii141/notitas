# Propuesta de caso base — v1 `[P]` (por confirmar con el profe y con el equipo CAMEIA)

## Qué es un "caso" en nuestro tema
**Un caso = una tarea de programación pequeña (30–90 min)** que tiene:
- un enunciado (qué hay que hacer),
- criterios de aceptación,
- una forma de comprobar que quedó bien (pruebas o una solución de referencia).

## Cuántos necesitamos
Una misma tarea no se puede hacer dos veces: la segunda vez ya sabemos la solución. Por eso necesitamos **tareas distintas pero parecidas** para cada condición:
- 10 para la línea base (pareja humana),
- 10 para los ciclos (pareja con agente),
- 2–3 de repuesto.

**En total, unas 22–24 tareas, más los 3 casos que nos entregue la otra pareja.**

## Fuente recomendada: "repetir" tareas reales ya cerradas de CAMEIA
CAMEIA tiene unos 240 PR fusionados en 9 repos, cada uno con su ítem de Jira, su descripción y sus pruebas (ver `drive-download…/05 - Medicion de flujo/Datos/prs-corte-cameia-*.json`).

**Cómo se arma cada caso:**
1. Escoger un PR cerrado y pequeño.
2. Volver el repo al commit **anterior** a ese PR (`git checkout <commit>^` en una rama nueva).
3. El enunciado = el ítem de Jira + los criterios de aceptación. **No se muestra el PR.**
4. La solución real del PR y sus pruebas sirven de **referencia** para juzgar la tarea: si la terminamos, cuánto retrabajo hubo y qué errores se escaparon.

**Por qué conviene esta fuente:**
- Es material real, no inventado para que el agente quede bien.
- Hay de dónde escoger casos difíciles.
- Cada tarea trae su forma de verificarla.

**Reglas para escoger los casos:**
- **No usar PR escritos por nosotros**, porque recordaríamos la solución. Ana Sofía escribió PR en `cameia-perfil`: evitarlos.
- Mezclar tamaños S, M y L y asignarles condición **por sorteo**.
- Incluir al menos 4 difíciles, por ejemplo:
  - un diagnóstico con causa oculta (tipo CM-177, el 404 del balanceador),
  - código de un servicio con factor de camión 0,
  - una tarea con un requisito ambiguo,
  - una con un riesgo de seguridad o de permisos,
  - una donde la solución "obvia" es la equivocada (tipo el perfil `production` vs `prod`).
- Quitar datos sensibles (credenciales, nombres reales en datos de prueba) antes de dársela al agente.

**Una advertencia que debemos poner en el reporte:** casi todos estos PR ya se hicieron con Claude Code. La solución de referencia puede tener "estilo de agente". Va como limitación.

## Alternativas si la anterior no se aprueba
| Opción | A favor | En contra |
|---|---|---|
| B. Tareas **pendientes** del backlog real (de CAMEIA o del proyecto de Juan José) | Trabajo vivo de verdad | No hay solución de referencia y las tareas son más difíciles de igualar entre condiciones |
| C. Construir un repo pequeño propio con 24 tareas | Control total | El PDF advierte el riesgo de diseñar justo lo que el agente resuelve bien; hay que incluir difíciles y los 3 casos externos |

## Cómo se ejecuta una tarea
**Línea base (pareja humana, sin IA):**
1. Uno conduce y el otro navega; cambian cada 15 min.
2. Cronómetro desde que leen el enunciado hasta que pasan las pruebas y los criterios.
3. Al terminar, *codewalk* de 5 preguntas a cada uno, sin mirar el código.

**Ciclos (pareja con agente):**
1. Una persona + el agente copiloto; el otro no participa.
2. Cronómetro igual, y una fila de bitácora por cada uso del agente.
3. Al terminar, *codewalk* al autor **y** al compañero que no participó. Esto mide si el conocimiento se queda en una sola persona.
4. Se compara contra la solución de referencia: retrabajo y errores escapados.

## Pendiente de decisión (pareja)
- [ ] ¿Fuente A, B o C?
- [ ] Permiso del equipo CAMEIA para usar los repos y el historial.
- [ ] Confirmar con el profe **por escrito** que la "repetición de tareas reales" cuenta como caso base. Guardar la respuesta en `09 - Control de entrega`.
