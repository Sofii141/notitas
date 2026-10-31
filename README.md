# Entrega final — Ágiles 2026-2 · Tema 3: Pair programming

Ana Sofía Arango Yanza · Juan José Arias Chacua · Prof. César Pardo

**Empiecen por [GUIA_EntregaFinal.md](GUIA_EntregaFinal.md)**. Para el punto de control del 30/10, lean primero la revisión del 29/10: [09 - Control de entrega/29102026_01_Revision_Entrega_v1.pdf](09%20-%20Control%20de%20entrega/29102026_01_Revision_Entrega_v1.pdf). Ahí están el semáforo, lo que se corrigió y los pasos pendientes en orden. **Lo que se envía el 30/10:** [29102026_02_Punto_Control_v2.pdf](09%20-%20Control%20de%20entrega/29102026_02_Punto_Control_v2.pdf). **Cómo medir la línea base, paso a paso:** [29102026_03_Guia_Entrega_y_Medicion_v1.pdf](09%20-%20Control%20de%20entrega/29102026_03_Guia_Entrega_y_Medicion_v1.pdf).

## Carpetas
| Carpeta | Qué va |
|---|---|
| `00 - Info inicial` | PDF del profe (no editar) |
| `01 - Exposicion` | Fuentes, guion, diapositivas del tema |
| `02 - Caso base` | Fichas de casos, 3 recibidos y 3 entregados |
| `Repositorio/CAMEIA-lite` | Código del caso base **Notitas** desde el 31/10 (git) → https://github.com/Sofii141/CAMEIA-lite. CAMEIA-lite quedó en el tag `congelado-v1` |
| `03 - Linea base` | GQM, datos crudos y condiciones de medición |
| `04 - Especificacion agentes` | Spec v1, v2… y prompts finales |
| `05 - Ciclos y bitacora` | Bitácora xlsx + notas de ciclo 1 y 2 |
| `06 - Fallos y riesgos` | 3 fallos documentados + análisis de riesgos |
| `07 - Analisis` | Antes/después, scripts y gráficos. `Scripts/resumen_medicion.py` resume la bitácora y llena la línea base del punto de control |
| `08 - Reporte` | Reporte PDF (6–10 pág.) y sus versiones |
| `09 - Control de entrega` | Checklist, actas de la pareja, confirmaciones del profe por escrito |
| `99 - Videos` | Video de respaldo de la demo (2 min) |
| `_Estilo` | Paleta "Macarons", fuentes, `estilo.css`, plantilla HTML, `html_a_pdf.py` y `estilo_xlsx.py` (para Excel): **todo documento y las diapositivas siguen este estilo** |

> **31/10:** el caso base cambió a **Notitas** (tablero kanban de notas), con aprobación del profe; plazo del caso base hasta el 3/11. Versiones vigentes: [GQM v3](03%20-%20Linea%20base/31102026_01_GQM_v3.md) y [bitácora v3](05%20-%20Ciclos%20y%20bitacora/31102026_01_Bitacora_v3.xlsx). `_Privado/` (soluciones de referencia) no se sube y no se abre antes de medir.

## Ramas del repositorio (https://github.com/Sofii141/CAMEIA-lite)
- `main`: código del caso base (carpeta local `Repositorio/CAMEIA-lite`).
- `documentacion`: esta carpeta (guía, GQM, spec, bitácora, fuentes, reporte…). Para editar: `git pull`, hacer los cambios, `git commit` y `git push`.
- No se suben (ver `.gitignore`): los PDF del profe, los artículos descargados y los videos. El repo es público; esos archivos se comparten por Drive.

## Convención de nombres (la misma de E1/E2)
`DDMMAAAA_NN_Nombre_vX.ext` → p. ej. `30102026_01_Spec_Copiloto_v1.md`.
Aplica a los artefactos que evolucionan (spec, GQM, bitácora, propuestas, plan, fuentes). Los documentos estables y las plantillas (`README`, `GUIA_EntregaFinal`, `CHANGELOG`, `Plantilla_*`, `Registro_Uso_IA`) no llevan fecha.
Nunca sobrescribir una versión entregada o revisada: se copia con fecha nueva y se anota en [CHANGELOG.md](CHANGELOG.md).
