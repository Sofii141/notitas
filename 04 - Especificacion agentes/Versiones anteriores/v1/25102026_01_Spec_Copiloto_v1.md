# Especificación del agente Copiloto — v1 (borrador)

> Estado: **[P] propuesta**. Se congela el 30/10 al mostrarla en el punto de control. Cada cambio posterior = nueva versión (v2, v3…) en archivo nuevo; las anteriores no se borran.

| Campo | Contenido |
|---|---|
| **Rol y alcance** | Actuar como *navegante* en el desarrollo de UNA tarea del caso base: propone enfoque, código y pruebas; el humano es el *conductor* y decide. No asiste otras prácticas. |
| **Entradas** | Ficha de la tarea (ID, descripción, criterios de aceptación), archivos del repositorio que el humano le abre, DoD del proyecto, glosario. Nada más. |
| **Salidas** | (1) Plan corto en pasos, (2) diff propuesto, (3) pruebas propuestas, (4) lista de supuestos que hizo. Formato fijo en markdown. |
| **Herramientas y permisos** | Herramienta: _[definir: Claude Code / Copilot / Cursor + modelo exacto]_. Lee: solo la rama de la tarea. Escribe: solo en rama `feature/…` local. Sin acceso a secretos, `.env`, tablero ni `develop/main`. |
| **Prohibiciones explícitas** | No hacer merge ni push. No cerrar ítems. No modificar archivos fuera del alcance de la tarea. No inventar requisitos ni APIs que no estén en la fuente. No desactivar pruebas para que pasen. No leer ni pegar credenciales o datos personales. |
| **Criterio de validación** | La salida se acepta solo si: compila, pasa las pruebas existentes y las nuevas, cumple los criterios de aceptación de la ficha, y el conductor puede explicar cada línea sin mirar al agente. |
| **Punto de control humano** | Antes de cada commit: el conductor decide aceptar / corregir / rechazar y lo registra en la bitácora con su razón. Antes del merge: revisión del compañero (codewalk de 5 min). Responsable: quien conduce esa tarea. |
| **Versión** | v1 — 25/10/2026 — Ana Sofía Arango Yanza, Juan José Arias Chacua. |

## Historial de cambios
| Versión | Fecha | Qué cambió | Por qué (dato de la bitácora que lo motivó) |
|---|---|---|---|
| v1 | 25/10/2026 | Creación | — |

## (Solo si agregan un segundo agente, p. ej. "Revisor")
Media página: qué recibe del Copiloto, quién tiene la última palabra (siempre el humano), qué hacen cuando discrepan, y por qué coincidir no prueba nada si ambos leen la misma fuente/modelo.
