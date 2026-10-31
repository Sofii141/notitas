# Especificación del agente Copiloto — v1 (caso Notitas, 31/10/2026)

> Es la misma v1 del 29/10 (`29102026_01_Spec_Copiloto_v1.md`, que se conserva), ajustada al caso base **Notitas**. El agente todavía no se ha usado: por eso sigue siendo v1. Desde aquí, cada cambio es una versión nueva (v2, v3…) en un archivo nuevo, con el dato de la bitácora que la motivó.

**De dónde sale esta especificación.** Los **8 campos** son los que exige el enunciado del proyecto (Paso 3: rol y alcance, entradas, salidas, herramientas y permisos, prohibiciones, criterio de validación, punto de control humano y versión). El **contenido** de cada campo se apoya en la literatura que estudiamos para el tema y en la guía de riesgos de IA generativa que vimos en el curso; la columna *Fundamento* dice en qué. Las referencias completas, con DOI, están en `01 - Exposicion/Fuentes/29102026_01_Fuentes_v2.md`.

| Campo | Contenido | Fundamento |
|---|---|---|
| **Rol y alcance** | Hace de *navegante* en el desarrollo de **una** tarea de Notitas: propone un enfoque, el código y los casos borde que conviene probar. La persona es el *conductor* y decide. No asiste otras prácticas ni otras tareas. | Roles de conductor y navegante del pair programming (Williams et al., 2000; Bryant et al., 2008): el agente ocupa el lugar del compañero que navega. |
| **Entradas** | Solo tres cosas: (1) el enunciado y los criterios de aceptación de la tarea en `TAREAS.md`; (2) su archivo `backend/notitas/tNN.py`; (3) sus pruebas visibles `backend/tests/visibles/test_tNN.py`. Nada más del repositorio. | Darle al agente solo lo necesario (minimizar los datos que se comparten), como recomienda NIST AI 600-1 (2024) para la confidencialidad, y darles a las dos condiciones la misma información. |
| **Salidas** | En formato fijo de markdown: (1) un plan de 3 a 6 pasos; (2) el diff propuesto, solo en `tNN.py`; (3) la lista de supuestos que hizo; (4) los casos borde que cree que faltan, como **texto**, no como pruebas escritas. | El enunciado: "una salida sin formato definido es imposible de evaluar". Pedir los supuestos hace visibles los requisitos que el agente inventó. |
| **Herramientas y permisos** | **OpenCode** con el modelo gratuito **DeepSeek V4.1 Flash**, el mismo para los dos durante todo el ciclo. El nombre del modelo y la versión de OpenCode (`opencode --version`) se anotan en la hoja *Sesiones* en el primer uso. Trabaja en una **copia del repo sin `backend/tests/ocultas`**, con el `opencode.json` del repo (`agente/opencode.json`): le niega leer las ocultas y `.env`, editar las pruebas, hacer commit, push o merge, salir de la carpeta y buscar en internet; todo lo demás lo **pregunta** antes. | Mínimo privilegio (NIST AI 600-1, 2024). No se usa un modelo de la familia Claude porque con Claude se construyó el caso base. |
| **Prohibiciones explícitas** | No hacer commit, push ni merge (los hace la persona). No modificar `backend/tests/` ni otros archivos fuera de `tNN.py`. No leer ni pedir las pruebas ocultas. No desactivar, saltar ni "ajustar" pruebas para que pasen. No inventar requisitos que no estén en el enunciado. No pegar ni leer credenciales o datos personales. | Que la medición sea válida: las pruebas ocultas solo miden errores escapados si nadie las ve antes (Ko et al., 2015). Perry et al. (2023) muestran que con IA se escribe código menos seguro sin notarlo. |
| **Criterio de validación** | Una salida se acepta solo si se cumplen las tres condiciones: pasan las pruebas visibles de la tarea, cumple cada criterio de aceptación del enunciado, y el conductor puede explicar cada línea **sin mirar al agente**. Si falla una, se corrige o se rechaza. | Welter et al. (2025): las sugerencias de la IA se aceptan con menos escrutinio que las de un compañero. Shihab et al. (2025): los estudiantes no entendían por qué funcionaban. Exigir la explicación contrarresta las dos cosas. |
| **Punto de control humano** | (1) **Antes de cada commit**, el conductor decide *aceptar*, *corregir* o *rechazar* y lo registra en la hoja *Bitacora* con su **razón**. (2) **Al declarar terminado**, la persona corre las pruebas ocultas, no el agente. (3) **Después**, el codewalk con el compañero. Responsable: quien conduce esa tarea. | Human-in-the-loop (sesión 3 del curso; NIST AI 600-1, 2024): una persona decide y queda registro de su decisión. |
| **Versión** | v1 · 31/10/2026 · Ana Sofía Arango Yanza y Juan José Arias Chacua. | El enunciado: numerar las versiones y conservar las anteriores. |

## Historial de cambios
| Versión | Fecha | Qué cambió | Por qué |
|---|---|---|---|
| v1 (borrador) | 25/10/2026 | Creación | — |
| v1 | 29/10/2026 | Entradas reales del caso, salidas sin pruebas escritas, exclusión explícita de las pruebas ocultas y punto de control al declarar "terminado" | Inconsistencias detectadas en una revisión; todavía no había datos de bitácora |
| v1 (Notitas) | 31/10/2026 | Caso base Notitas y rutas `backend/…`. Herramienta: OpenCode con DeepSeek V4.1 Flash, con permisos en `agente/opencode.json`. Columna *Fundamento* | Cambio de caso base; modelo gratuito para los dos y que no es Claude. El agente aún no se ha usado |

## (Solo si agregan un segundo agente en el ciclo 2, p. ej. "Revisor")
Media página: qué recibe del Copiloto, quién tiene la última palabra (siempre la persona), qué hacen cuando discrepan, y por qué coincidir no prueba nada si ambos usan el mismo modelo o leen la misma fuente.

## Referencias de esta especificación
- Bryant, S., Romero, P., & du Boulay, B. (2008). Pair programming and the mysterious role of the navigator. *International Journal of Human-Computer Studies, 66*(7), 519–529. https://doi.org/10.1016/j.ijhcs.2007.03.005
- Ko, A. J., LaToza, T. D., & Burnett, M. M. (2015). A practical guide to controlled experiments of software engineering tools with human participants. *Empirical Software Engineering, 20*(1), 110–141. https://doi.org/10.1007/s10664-013-9279-3
- NIST (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1). https://doi.org/10.6028/NIST.AI.600-1
- Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023). Do users write more insecure code with AI assistants? *ACM CCS 2023*, 2785–2799. https://doi.org/10.1145/3576915.3623157
- Shihab, M. I. H., Hundhausen, C., Tariq, A., Haque, S., Qiao, Y., & Mulanda, B. (2025). The effects of GitHub Copilot on computing students' programming effectiveness, efficiency, and processes in brownfield coding tasks. *ICER 2025*, 407–420. https://doi.org/10.1145/3702652.3744219
- Welter, A., Schneider, N., Dick, T., Weis, K., Tinnes, C., & Wyrich, M. (2025). An empirical study of knowledge transfer in AI pair programming. *ASE 2025*, 166–177. https://doi.org/10.1109/ASE63991.2025.00022
- Williams, L., Kessler, R. R., Cunningham, W., & Jeffries, R. (2000). Strengthening the case for pair programming. *IEEE Software, 17*(4), 19–25. https://doi.org/10.1109/52.854064
