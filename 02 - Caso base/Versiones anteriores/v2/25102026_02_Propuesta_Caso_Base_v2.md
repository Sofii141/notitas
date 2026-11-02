# Propuesta de caso base — v2 `[P]`: comparación de alternativas

> La v1 proponía solo "repetir PR de CAMEIA". Esta v2 compara alternativas buscando **el proceso más sencillo** que siga siendo aceptable para el profe.
> Dato nuevo: Juan José también está en CAMEIA (`likelion5010`). Los dos conocen el proyecto, así que **ningún PR de CAMEIA sería código ajeno** para la pareja.

## Lo que necesita cualquier opción
- ~22–24 tareas pequeñas (30–90 min), **parecidas entre sí**, porque una tarea no se repite.
- Cada tarea con criterios de aceptación y pruebas, para medir tiempo, retrabajo y errores sin discutir.
- Que se pueda abrir y correr en minutos. Si cada tarea exige montar Docker, Firebase o PostgreSQL, el cronómetro mide la configuración y no la práctica.
- Al menos 4 tareas difíciles, más los 3 casos de la otra pareja.

## Alternativas

| | Opción | Sencillez | ¿Real? | Comparabilidad | Riesgo con el profe |
|---|---|---|---|---|---|
| **A** | Repetir PR cerrados de CAMEIA (v1) | 🔴 Baja: microservicios Spring/Firebase/Postgres; los PR son grandes porque los escribió un agente | Alta | Baja: tamaños muy dispares | Bajo |
| **B** | Tareas pendientes del backlog de CAMEIA | 🔴 Baja: mismo entorno pesado y sin solución de referencia | Muy alta | Muy baja | Bajo, pero cuesta medir |
| **C** | Repo pequeño propio con tareas inventadas | 🟢 Alta | Baja | Alta | Medio: "construyeron justo el caso que el agente resuelve bien" |
| **D** | Ejercicios públicos (Exercism, katas) | 🟢 Muy alta | Muy baja | Alta | Alto: parece tutorial y los modelos ya los conocen |
| **E ⭐** | **"CAMEIA-lite"**: repo pequeño propio con requisitos **reales** de CAMEIA | 🟢 Alta | Media-alta | Alta | Bajo-medio |

## Recomendación: E, "CAMEIA-lite"
Es un repo nuevo, pequeño y sin infraestructura (TypeScript o Python, solo con pruebas unitarias). Cada tarea implementa **una regla real del backlog de CAMEIA** como función o módulo aislado.

Ejemplos de reglas reales que sirven:
- Nombre y apellido solo con letras, espacios, apóstrofo y guion; recorte y conteo por puntos de código NFC (CM-36).
- Validar el celular en E.164 con 6–15 dígitos (CM-36).
- Política de contraseñas con lista de contraseñas comunes (CM-36).
- Cupo de perfiles por plan → 403 `PLAN_LIMIT` o 409 según el caso (CM-271, CM-270, CM-298).
- Mapear el `code` del ProblemDetail a mensajes por campo (CM-298, CM-336).
- Fecha de nacimiento fuera de rango, más de 110 años (CM-279).
- Nivel de log según el estado HTTP: 5xx, 404 y otros 4xx (CM-184).
- Reintentos que solo cuentan los fallos de la IA (CM-217).
- Evitar la doble creación por doble clic, con un *guard* de concurrencia (CM-270).

**Por qué es la más sencilla:**
- Se clona y se corre con un solo comando (`npm test` o `pytest`), sin configurar nada.
- Las tareas se pueden igualar en tamaño (S/M/L) y repartir por sorteo.
- La solución real del PR de CAMEIA sirve como referencia para juzgar errores y retrabajo.

**Por qué el profe lo aceptaría:**
- Los requisitos salen de su proyecto real, con su ID de Jira y su criterio de aceptación, y no se inventaron para el agente.
- Los casos difíciles salen de defectos que de verdad ocurrieron: NFC, el doble clic, el cupo 409 contra 403, el *falso obvio* `production` contra `prod`.

**Límites que hay que declarar en el reporte:**
- Las tareas se sacan de su entorno (sin Docker ni integración), así que no miden el costo de integrar.
- Los dos conocen CAMEIA, y algunas reglas las implementó uno de ellos o un agente: para no recordar la solución, **excluir las tareas que cada uno escribió**.

## Si quieren todavía más simple: C con una salvaguarda
Repo propio con tareas inventadas, pero **la otra pareja escribe 3 casos** (ya es obligatorio) y ustedes **le piden a un compañero de CAMEIA** que proponga 4 tareas difíciles sin decirles la solución. Es más rápido de montar, pero más fácil de criticar.

## Decisión pendiente (pareja)
- [ ] Elegir opción (recomendada: E).
- [ ] Elegir lenguaje (el que mejor manejen los dos).
- [ ] Confirmar con el profe **por escrito** antes o el día del 30/10 y guardar la respuesta en `09 - Control de entrega`.
