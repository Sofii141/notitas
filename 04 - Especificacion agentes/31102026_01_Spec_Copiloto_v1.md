# Especificación del agente Copiloto — v1 (caso Notitas, 31/10/2026)

> Es la misma v1 del 29/10 (`29102026_01_Spec_Copiloto_v1.md`, que se conserva), con las rutas y el nombre del caso base nuevo, **Notitas**. El agente todavía no se ha usado: por eso sigue siendo v1. Antes, la v1 del 29/10 reemplazó al borrador `25102026_01_Spec_Copiloto_v1.md`. Ese borrador y el HTML del punto de control no coincidían: en el borrador había entradas que no existen en el caso (DoD y glosario), pedía "pruebas propuestas" aunque a la vez prohibía tocar pruebas, y no excluía `tests/ocultas`. Desde aquí, cada cambio es una versión nueva (v2, v3…) en un archivo nuevo, con el dato de la bitácora que la motivó.

| Campo | Contenido |
|---|---|
| **Rol y alcance** | Hace de *navegante* en el desarrollo de **una** tarea de Notitas: propone un enfoque, el código y los casos borde que conviene probar. La persona es el *conductor* y decide. No asiste otras prácticas ni otras tareas. |
| **Entradas** | Solo tres cosas: (1) el enunciado y los criterios de aceptación de la tarea en `TAREAS.md`; (2) su archivo `src/notitas/tNN.py`; (3) sus pruebas visibles `tests/visibles/test_tNN.py`. Nada más del repositorio. |
| **Salidas** | En formato fijo de markdown: (1) un plan de 3 a 6 pasos; (2) el diff propuesto, solo en `tNN.py`; (3) la lista de supuestos que hizo; (4) los casos borde que cree que faltan, como **texto**, no como pruebas escritas. |
| **Herramientas y permisos** | **Claude Code** (los dos lo tienen), en una carpeta de trabajo propia por tarea. El modelo exacto (lo muestra `/model`) y la versión (`claude --version`) se anotan en la hoja *Sesiones* en el primer uso y no se cambian durante los ciclos. Permisos: solo lee y edita dentro de una **copia del repo sin la carpeta `tests/ocultas`**, y en `.claude/settings.json` de esa copia se niegan `git commit`, `git push` y el acceso a `tests/ocultas`. Sin acceso a credenciales ni a otros repositorios. **Limitación declarada:** el caso base también se generó con Claude, así que el agente puede tener ventaja ("caso a su medida"). Por eso las pruebas ocultas nadie las ve y se incorporan 3 casos de otra pareja. |
| **Prohibiciones explícitas** | No hacer commit, push ni merge (los hace la persona). No modificar `tests/` ni otros archivos fuera de `tNN.py`. No leer ni pedir `tests/ocultas`. No desactivar, saltar ni "ajustar" pruebas para que pasen. No inventar requisitos que no estén en el enunciado. No pegar ni leer credenciales o datos personales. |
| **Criterio de validación** | Una salida se acepta solo si se cumplen las tres condiciones: pasan las pruebas visibles de la tarea, cumple cada criterio de aceptación del enunciado, y el conductor puede explicar cada línea **sin mirar al agente**. Si falla una, se corrige o se rechaza. |
| **Punto de control humano** | (1) **Antes de cada commit**, el conductor decide *aceptar*, *corregir* o *rechazar* y lo registra en la hoja *Bitacora* con su **razón**. (2) **Al declarar terminado**, la persona corre las pruebas ocultas, no el agente. (3) **Después**, el codewalk con el compañero. Responsable: quien conduce esa tarea. |
| **Versión** | v1 · 29/10/2026 · Ana Sofía Arango Yanza y Juan José Arias Chacua. |

## Historial de cambios
| Versión | Fecha | Qué cambió | Por qué |
|---|---|---|---|
| v1 (borrador) | 25/10/2026 | Creación | — |
| v1 (CAMEIA-lite) | 29/10/2026 | Se unificó con el HTML del punto de control: entradas reales del caso, salidas sin pruebas escritas, exclusión explícita de `tests/ocultas` y punto de control al declarar "terminado". Herramienta fijada: GitHub Copilot con un modelo que no sea Claude | Inconsistencias detectadas en la revisión del 29/10. Todavía no hay datos de bitácora |
| v1 (Notitas) | 31/10/2026 | Cambian el nombre del caso y la ruta `src/notitas/tNN.py`. Herramienta: Claude Code en vez de Copilot | El caso base cambió a Notitas con aprobación del profe; el agente aún no se ha usado. Claude Code porque los dos lo tienen; se declara como limitación que el caso también se generó con Claude |

## (Solo si agregan un segundo agente en el ciclo 2, p. ej. "Revisor")
Media página: qué recibe del Copiloto, quién tiene la última palabra (siempre la persona), qué hacen cuando discrepan, y por qué coincidir no prueba nada si ambos usan el mismo modelo o leen la misma fuente.
