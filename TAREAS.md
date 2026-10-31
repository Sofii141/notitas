# Tareas de Notitas

Notitas es un tablero kanban de notas adhesivas (columnas **Por hacer · En curso · Hecho**). Cada tarea es **una regla del backend**, escrita como una función o clase pura de Python, con pruebas visibles y ocultas. El front (la página con animaciones) ya está hecho y **no se mide**: usa estas funciones a través de `backend/servidor.py`. Programar una tarea es reemplazar el `raise NotImplementedError` de su archivo por la lógica.

Tamaño (estimado por juicio; ver el README): **S** pequeña ≈ 15–25 min · **M** mediana ≈ 25–45 min · **L** grande ≈ 45–70 min. Lo real lo dirá el cronómetro.
Columnas válidas en todas las tareas: `"por_hacer"`, `"en_curso"` y `"hecho"`.

| ID | Tarea | Tamaño | Difícil |
|---|---|---|---|
| t01 | Validar el título de una nota | S |  |
| t02 | Color de la nota | S |  |
| t03 | Transiciones entre columnas | M | ⚠️ sí |
| t04 | Límite WIP de "En curso" | M | ⚠️ sí |
| t05 | Insertar en una posición | M |  |
| t06 | Filtrar por etiquetas | S |  |
| t07 | Buscar sin tildes ni mayúsculas | M | ⚠️ sí |
| t08 | Estado de vencimiento | M | ⚠️ sí |
| t09 | Normalizar etiquetas | S |  |
| t10 | Qué notas se archivan | S |  |
| t11 | Deshacer movimientos | M |  |
| t12 | Dos personas mueven la misma nota | L | ⚠️ sí |
| t13 | Exportar e importar el tablero | M |  |
| t14 | Contenido seguro (sin inyectar HTML) | M | ⚠️ sí |
| t15 | Resumen por columna | S |  |
| t16 | Ordenar por prioridad y fecha | S |  |
| t17 | Paginar el listado | S |  |
| t18 | Iniciales del responsable | S |  |
| t19 | Progreso de la checklist | M |  |
| t20 | Duplicar una nota | S | ⚠️ sí |
| t21 | Fusionar cambios de dos dispositivos | L | ⚠️ sí |
| t22 | Notas bloqueadas | M |  |
| t23 | Tiempo de ciclo | M | ⚠️ sí |
| t24 | Límite de notas por minuto | M | ⚠️ sí |

## t01 · Validar el título de una nota (S)

Archivo: `backend/notitas/t01.py`

Firma: `def validar_titulo(s: str) -> str`

Devuelve el título limpio o lanza `ValueError`.
- CA1: se quitan los espacios al inicio y al final (incluye tabulaciones, saltos de línea y el espacio duro ` `).
- CA2: los espacios internos repetidos se dejan en uno solo (`"Comprar   pan"` → `"Comprar pan"`).
- CA3: el texto se normaliza a Unicode **NFC**.
- CA4: si queda vacío o tiene **más de 80 caracteres** (puntos de código, después de normalizar), `ValueError`.

## t02 · Color de la nota (S)

Archivo: `backend/notitas/t02.py`

Firma: `def normalizar_color(c: str) -> str`

Las notitas solo pueden tener un color de la paleta del tablero:

| Nombre | Hex |
|---|---|
| matcha | `#BCC86F` |
| semolina | `#F5CB99` |
| fresa | `#FFABA9` |
| rosa | `#F68578` |
| mani | `#B9794A` |
| chocolate | `#79371D` |

- CA1: se acepta el **nombre** (sin importar mayúsculas ni espacios alrededor) o el **hex** de 6 dígitos, con o sin `#`, en mayúsculas o minúsculas.
- CA2: devuelve siempre el hex canónico: `#` + 6 dígitos en mayúsculas.
- CA3: cualquier otro valor (otro color, formato inválido) → `ValueError`.

## t03 · Transiciones entre columnas (M) ⚠️

Archivo: `backend/notitas/t03.py`

Firma: `def puede_mover(origen: str, destino: str) -> bool`

Las columnas son `"por_hacer"`, `"en_curso"` y `"hecho"`.
- CA1: permitido: `por_hacer → en_curso`, `en_curso → hecho`, `en_curso → por_hacer` (devolver) y `hecho → en_curso` (reabrir).
- CA2: **no** permitido: `por_hacer → hecho` (no se salta "En curso") ni `hecho → por_hacer`.
- CA3: mover dentro de la misma columna (reordenar) siempre es permitido.
- CA4: si alguna columna no existe (los nombres son exactos, en minúscula), `ValueError`.

## t04 · Límite WIP de "En curso" (M) ⚠️

Archivo: `backend/notitas/t04.py`

Firma: `def validar_wip(notas: list[dict], nota_id: str, destino: str, limite: int = 3) -> None`

Cada nota es un diccionario con al menos `"id"` y `"columna"`. El módulo ya define la excepción `WipExcedido`.
- CA1: si mover la nota a `"en_curso"` dejaría **más de `limite`** notas en esa columna, se lanza `WipExcedido`. Si no, no devuelve nada.
- CA2: el límite solo aplica a `"en_curso"`; las otras columnas no tienen tope.
- CA3: si la nota **ya está** en `"en_curso"` (solo se reordena), no cuenta como una nota más.
- CA4: si `nota_id` no existe, `KeyError`.

## t05 · Insertar en una posición (M)

Archivo: `backend/notitas/t05.py`

Firma: `def insertar_en_posicion(ids: list[str], nota_id: str, posicion: int) -> list[str]`

`ids` es el orden de las notas de una columna, de arriba a abajo.
- CA1: devuelve una **lista nueva** con `nota_id` en `posicion` (contando desde 0 en la lista resultante). **No** modifica `ids`.
- CA2: si `nota_id` ya estaba en la lista, primero se quita de donde estaba (no queda repetida).
- CA3: si `posicion` es mayor que el largo, la nota va al final; si es negativa, `ValueError`.

## t06 · Filtrar por etiquetas (S)

Archivo: `backend/notitas/t06.py`

Firma: `def filtrar_por_etiquetas(notas: list[dict], etiquetas: list[str], modo: str = "todas") -> list[dict]`

Cada nota tiene `"etiquetas"` (lista de textos).
- CA1: `modo="todas"`: quedan las notas que tienen **todas** las etiquetas pedidas. `modo="alguna"`: las que tienen **al menos una**.
- CA2: la comparación no distingue mayúsculas.
- CA3: si `etiquetas` está vacía, se devuelven todas las notas. Se conserva el orden original.
- CA4: otro `modo` → `ValueError`.

## t07 · Buscar sin tildes ni mayúsculas (M) ⚠️

Archivo: `backend/notitas/t07.py`

Firma: `def buscar(notas: list[dict], texto: str) -> list[str]`

Cada nota tiene `"id"`, `"titulo"` y `"contenido"`. Devuelve los `id` de las notas que coinciden, en el orden original.
- CA1: coincide si `texto` aparece en el título **o** en el contenido.
- CA2: no importan las mayúsculas ni las marcas diacríticas: `"CANCIÓN"` encuentra `"cancion"`, y `"nino"` encuentra `"niño"`.
- CA3: se usa *case folding* completo de Unicode: `"strasse"` encuentra `"Straße"`.
- CA4: si `texto` está vacío o solo tiene espacios, se devuelven todos los `id`.

## t08 · Estado de vencimiento (M) ⚠️

Archivo: `backend/notitas/t08.py`

Firma: `def estado_vencimiento(vence: str | None, ahora: datetime) -> str`

`vence` es una fecha `"AAAA-MM-DD"` o `None`. `ahora` es un `datetime` **con zona horaria** (puede venir en UTC u otra).
- CA1: "hoy" es la fecha de `ahora` **en Bogotá** (UTC−5 fijo, sin horario de verano).
- CA2: devuelve `"sin_fecha"` si `vence` es `None`; `"vencida"` si `vence` es anterior a hoy; `"hoy"` si es hoy; `"pronto"` si faltan de 1 a 3 días; `"a_tiempo"` si faltan más de 3.
- CA3: si `ahora` no tiene zona horaria (*naive*), `ValueError`.

## t09 · Normalizar etiquetas (S)

Archivo: `backend/notitas/t09.py`

Firma: `def normalizar_etiquetas(etiquetas: list[str]) -> list[str]`

- CA1: cada etiqueta se recorta, se pasa a minúsculas y sus espacios internos repetidos quedan en uno.
- CA2: se descartan las vacías y las repetidas, conservando el orden de la **primera** aparición.
- CA3: si quedan **más de 5** etiquetas, o alguna tiene **más de 20** caracteres, `ValueError`.

## t10 · Qué notas se archivan (S)

Archivo: `backend/notitas/t10.py`

Firma: `def notas_para_archivar(notas: list[dict], hoy: date) -> list[str]`

Cada nota tiene `"id"`, `"columna"` y, si está hecha, `"fecha_hecho"` (`"AAAA-MM-DD"`).
- CA1: se archivan las notas de `"hecho"` que llevan **más de 7 días** hechas (8 o más; con 7 exactos todavía no).
- CA2: las notas sin `"fecha_hecho"` o de otras columnas no se archivan.
- CA3: devuelve los `id` en el orden original.

## t11 · Deshacer movimientos (M)

Archivo: `backend/notitas/t11.py`

Clase: `Historial` con `registrar(movimiento: dict) -> None` y `deshacer() -> dict | None`

Un movimiento es `{"nota_id": ..., "desde": ..., "hacia": ...}`.
- CA1: `deshacer()` devuelve el movimiento **inverso** del último registrado (`desde` y `hacia` intercambiados) y lo saca del historial.
- CA2: si no hay nada que deshacer, devuelve `None`.
- CA3: solo se guardan los **últimos 20** movimientos; los más viejos se descartan.

## t12 · Dos personas mueven la misma nota (L) ⚠️

Archivo: `backend/notitas/t12.py`

Clase: `Tablero(notas: list[dict])` con `mover(nota_id: str, destino: str, version: int) -> dict`. El módulo ya define la excepción `Conflicto`.

Cada nota tiene `"id"`, `"columna"` y `"version"` (entero). Es **bloqueo optimista**: el cliente manda la versión que vio.
- CA1: si `version` coincide con la de la nota, la nota pasa a `destino`, su versión sube en 1 y se devuelve **una copia** de la nota actualizada.
- CA2: si no coincide (alguien la movió antes), `Conflicto`, y la nota no cambia.
- CA3: si `nota_id` no existe, `KeyError`.
- CA4: es seguro con **hilos**: si varias llamadas llegan al mismo tiempo con la misma versión, exactamente **una** gana y las demás reciben `Conflicto`.
- CA5: el `Tablero` no comparte las notas con la lista que recibió (modificar la lista original después no lo afecta).

## t13 · Exportar e importar el tablero (M)

Archivo: `backend/notitas/t13.py`

Firmas: `def exportar(tablero: dict) -> str` y `def importar(texto: str) -> dict`

Un tablero es `{"notas": [ {...}, ... ]}`.
- CA1: `exportar` produce JSON **estable**: claves ordenadas, sangría de 2 espacios y sin escapar tildes (`ensure_ascii=False`). Dos tableros iguales dan exactamente el mismo texto.
- CA2: `importar(exportar(t)) == t`.
- CA3: `importar` valida y lanza `ValueError` si: el texto no es JSON; no hay una lista `"notas"`; alguna nota no tiene `"id"` y `"titulo"` como texto; su `"columna"` no es `por_hacer`, `en_curso` o `hecho`; o hay `id` repetidos.

## t14 · Contenido seguro (sin inyectar HTML) (M) ⚠️

Archivo: `backend/notitas/t14.py`

Firma: `def limpiar_contenido(texto: str) -> str`

El contenido de una nota se muestra como HTML en el tablero. No se puede permitir que alguien inyecte HTML o JavaScript (XSS).
- CA1: se escapan `&`, `<`, `>`, `"` y `'` exactamente como lo hace `html.escape(texto, quote=True)` (el apóstrofo queda `&#x27;`).
- CA2: se permite una sola marca de formato: `**texto**` → `<strong>texto</strong>` (sin anidar; un `**` sin pareja se deja tal cual).
- CA3: los saltos de línea `\n` se convierten en `<br>`.
- CA4: el formato no debe abrir la puerta: `**<b>**` da `<strong>&lt;b&gt;</strong>`.

## t15 · Resumen por columna (S)

Archivo: `backend/notitas/t15.py`

Firma: `def resumen_columnas(notas: list[dict]) -> dict`

- CA1: devuelve `{"por_hacer": n, "en_curso": n, "hecho": n, "total": n, "porcentaje_hecho": p}`.
- CA2: las notas con `"archivada": True` no cuentan.
- CA3: `porcentaje_hecho` es un entero redondeado al más cercano, y los empates (.5) suben (`1 de 8` = 12,5 % → 13). Si no hay notas, es 0.

## t16 · Ordenar por prioridad y fecha (S)

Archivo: `backend/notitas/t16.py`

Firma: `def ordenar(notas: list[dict]) -> list[dict]`

Cada nota tiene `"prioridad"` (1 baja, 2 media, 3 alta) y `"vence"` (`"AAAA-MM-DD"` o `None`).
- CA1: primero la prioridad más alta; entre iguales, la fecha de vencimiento más cercana; las que no tienen fecha van al final de su grupo.
- CA2: si todo empata, se conserva el orden original (orden estable).
- CA3: devuelve una lista nueva; no modifica `notas`.

## t17 · Paginar el listado (S)

Archivo: `backend/notitas/t17.py`

Firma: `def paginar(items: list, pagina: int, tamano: int = 10) -> dict`

- CA1: devuelve `{"items": [...], "pagina": pagina, "total_paginas": n, "hay_siguiente": bool}`. Las páginas empiezan en **1**.
- CA2: `total_paginas` es el techo de `len(items) / tamano` (0 si no hay items).
- CA3: una página más allá del final devuelve `items` vacío y `hay_siguiente` en `False`.
- CA4: `pagina < 1` o `tamano < 1` → `ValueError`.

## t18 · Iniciales del responsable (S)

Archivo: `backend/notitas/t18.py`

Firma: `def iniciales(nombre: str) -> str`

Para el circulito del responsable en cada nota.
- CA1: la inicial de la **primera** y de la **última** palabra, en mayúsculas (`"juan josé arias"` → `"JA"`).
- CA2: se ignoran las partículas `de`, `del`, `la`, `las`, `los` e `y` (en cualquier mayúscula), salvo que sean la única palabra.
- CA3: una sola palabra da una sola inicial. Respeta las tildes y la ñ (`"ñandú"` → `"Ñ"`).
- CA4: si el nombre está vacío o solo tiene espacios, `"?"`.

## t19 · Progreso de la checklist (M)

Archivo: `backend/notitas/t19.py`

Firma: `def progreso_checklist(items: list[dict]) -> dict`

Cada ítem es `{"texto": str, "hecho": bool}`.
- CA1: devuelve `{"hechos": k, "total": n, "porcentaje": p, "texto": "k de n"}`; `porcentaje` es entero, redondeado **hacia abajo**.
- CA2: los ítems cuyo texto queda vacío al recortar no cuentan.
- CA3: si `"hecho"` no es `True` ni `False` (por ejemplo `"sí"` o `1`), `ValueError`.
- CA4: sin ítems: `{"hechos": 0, "total": 0, "porcentaje": 0, "texto": "0 de 0"}`.

## t20 · Duplicar una nota (S) ⚠️

Archivo: `backend/notitas/t20.py`

Firma: `def duplicar(nota: dict, nuevo_id: str) -> dict`

- CA1: devuelve una nota nueva igual a la original, pero con `"id": nuevo_id`, `"version": 1` y `"columna": "por_hacer"`.
- CA2: el título lleva el sufijo ` (copia)`. Si ya terminaba en ` (copia)`, pasa a ` (copia 2)`; si terminaba en ` (copia N)`, pasa a ` (copia N+1)`.
- CA3: la copia **no comparte** listas ni diccionarios con la original (etiquetas, checklist…): cambiar una no cambia la otra. La original no se modifica.

## t21 · Fusionar cambios de dos dispositivos (L) ⚠️

Archivo: `backend/notitas/t21.py`

Firma: `def fusionar(base: dict, a: dict, b: dict) -> dict`

Una nota se editó sin conexión en dos dispositivos. `base` es la versión común; `a` y `b` son las dos versiones editadas. Cada una de `a` y `b` trae además:
- `"modificado"`: un diccionario `campo → fecha ISO 8601 con zona horaria` de cuándo se cambió cada campo;
- `"dispositivo"`: un texto con el nombre del dispositivo.

Reglas, **campo por campo** (todos los campos de `base`, `a` y `b`, menos `"modificado"` y `"dispositivo"`; un campo que falta cuenta como `None`):
- CA1: si solo cambió uno de los dos respecto a `base`, gana ese cambio. Si ninguno cambió, queda el de `base`.
- CA2: si los dos cambiaron al mismo valor, ese valor (no es conflicto).
- CA3: si cambiaron a valores distintos, es **conflicto**: gana el cambio con la fecha `"modificado"` **más reciente**, comparando instantes reales (`"2026-11-02T10:00:00-05:00"` es **posterior** a `"2026-11-02T14:00:00+00:00"`). Si las fechas son el mismo instante, gana el dispositivo cuyo nombre va **primero** en orden alfabético.
- CA4: el resultado incluye `"conflictos"`: la lista ordenada alfabéticamente de los campos que tuvieron conflicto. Los campos que quedan en `None` no se incluyen en el resultado.

## t22 · Notas bloqueadas (M)

Archivo: `backend/notitas/t22.py`

Firma: `def mover_bloqueada(nota: dict, destino: str, motivo: str | None = None) -> dict`. El módulo ya define la excepción `NotaBloqueada`.

Una nota puede estar bloqueada (`"bloqueada": True`), por ejemplo porque espera a alguien.
- CA1: si **no** está bloqueada, devuelve una copia con `"columna": destino` (el motivo se ignora).
- CA2: si está bloqueada, solo se mueve con un `motivo` que no quede vacío al recortar; si no, `NotaBloqueada`.
- CA3: al moverla con motivo, la copia queda con `"bloqueada": False` y agrega al final de `"historial"` (que se crea si no existe) `{"accion": "desbloqueo", "motivo": <motivo recortado>}`.
- CA4: nunca modifica la nota original (tampoco su historial).

## t23 · Tiempo de ciclo (M) ⚠️

Archivo: `backend/notitas/t23.py`

Firma: `def tiempo_ciclo(eventos: list[dict]) -> float | None`

Cada evento es `{"hacia": columna, "en": fecha ISO 8601 con zona horaria}`: el momento en que la nota llegó a esa columna.
- CA1: el tiempo de ciclo es el total de **horas** que la nota pasó en `"en_curso"`, sumando todas las veces que estuvo ahí, hasta su **última** llegada a `"hecho"`.
- CA2: los eventos pueden venir desordenados: se ordenan por fecha (instante real).
- CA3: si la nota nunca llegó a `"hecho"`, `None`.
- CA4: el resultado se redondea a 2 decimales.

## t24 · Límite de notas por minuto (M) ⚠️

Archivo: `backend/notitas/t24.py`

Clase: `LimiteCreacion(max_por_minuto: int = 5)` con `permitir(usuario: str, ahora: float) -> bool`

`ahora` es el tiempo en segundos (un número que solo crece). Evita que alguien llene el tablero de notas sin querer.
- CA1: cada usuario puede crear como máximo `max_por_minuto` notas en cualquier ventana de 60 segundos: se cuentan las creaciones con tiempo `t` tal que `ahora - 60 < t <= ahora`.
- CA2: si se permite, la creación se registra y devuelve `True`; si no, devuelve `False` y el intento **no** cuenta.
- CA3: cada usuario tiene su propio límite.
