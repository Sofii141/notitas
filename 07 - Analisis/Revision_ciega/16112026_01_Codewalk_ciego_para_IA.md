# Revisión a ciegas de respuestas de codewalk

Eres un evaluador. Vas a calificar respuestas escritas por estudiantes que explicaron, de memoria y sin mirar, un código que ellos mismos escribieron o aceptaron.
Cada caso trae el enunciado de la tarea, el código final, las 5 preguntas y las 5 respuestas.

## Regla de calificación (aplícala igual a todos)
- 1 punto si la respuesta es correcta y concreta; 0 si es vaga o incorrecta.
- Pregunta 2: además de nombrar el caso borde, debe decir DÓNDE está en el código (qué parte, qué condición o qué función). Si no lo ubica, vale 0.
- Preguntas 4 y 5: deben señalar la parte correcta del código y explicar por qué. "Volvería a leer todo" vale 0.
- No premies la extensión ni la ortografía; solo si es correcta y concreta.

## Formato de tu respuesta
Devuelve SOLO una tabla con estas columnas: ID | P1 | P2 | P3 | P4 | P5 | Total | Motivo breve de cada 0.
Una fila por caso, en el mismo orden. No agregues nada más.

---
## Caso R01

### Enunciado
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

### Código final
```python
from datetime import datetime, timezone

_CAMPOS_IGNORADOS = {"modificado", "dispositivo"}
def _instante(valor):
    """Convierte la decha a un mismo estandar comparable"""
    if not isinstance(valor, str):
        return None
    texto = valor.strip()
    if texto.endswith(("Z","z")):
        texto = texto[:-1] + "+00:00"
    try:
        instante = datetime.fromisoformat(texto)
    except ValueError:
        return None
    if instante.tzinfo is None:
        instante = instante.replace(tzinfo = timezone.utc)
    return instante

def _fecha(version, campo):
    modificado = version.get("modificado") or ""
    return _instante(modificado.get(campo))

def _dispositivo(version):
    return version.get("dispositivo") or ""

def fusionar(base: dict, a: dict, b: dict) -> dict:

    campos = (set(base) | set (a) | set(b)) - _CAMPOS_IGNORADOS
    resultado = {}
    conflictos = []

    for campo in sorted(campos):
        valor_base = base.get(campo)
        valor_a = a.get(campo)
        valor_b = b.get(campo)

        if valor_a == valor_b:
            #ambos lados coiniciden
            elegido = valor_a
        elif valor_a == valor_base:
            #cambio solo a
            elegido = valor_b
        elif valor_b == valor_base:
            #cambio solo b
            elegido = valor_a
        else:
            #ambos lados cambiaron
            conflictos.append(campo)
            fecha_a = _fecha(a,campo)
            fecha_b = _fecha(b,campo)

            if fecha_a is not None and fecha_b is not None and fecha_a != fecha_b:
                #se elige la fecha mas reciente
                elegido= valor_a if fecha_a > fecha_b else valor_b
            elif fecha_a is not None and fecha_b is None:
                #Se elige la fecha a
                elegido= valor_a
            elif fecha_b is not None and fecha_a is None:
                #Se elige la fecha b
                elegido= valor_b
            else:
                #si ambas fechas son exactamente iguales o si ninguna tiene fecha
                elegido = (
                    valor_a if _dispositivo(a) <= _dispositivo(b)
                    else valor_b
                )
        if elegido is not None:
            resultado[campo] = elegido
    resultado["conflictos"] = sorted(conflictos)
    return resultado
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Compara los cambios sobre una misma nota desde 2 dispositivos y resuleve conflictos para dejar un resultado final

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: Maneja el caso borde de si al resolver un conflicto por fecha están empatados, entonces desempata por el nombre de los dispositivos y elimina aquello campos none.

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: En su mayoría se siguió la lógica del agente guía, dios y explico funciones muy útiles de ordenamiento y decidir las columnas set y torted, que d eotra manera hubiera hecho iterativamente muy probablemente, y me ayudo a elegir una librería de fechas adecuada

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: 10:00-05:00 frente a 14:00+00:00 gana el de las 14:00**
Respuesta: miraría la función _instant que es el lugar donde de algún modo obtenemos todas las fechas y las ponemos en un formato comparable volviéndolas un objeto especializaod en fechas

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: ante un empate, gana el valor de base**
Respuesta: Probablemente cambiaria solo el condicional final la linea donde asignamos el valor del resultado y cambiaria bastante la comparación final, dando un escenario por si el desempate por nombre lo gana a, o lo gana b y un else de entonces el resultado base, ya que igual se debe regisytrar el conflicto.

---
## Caso R02

### Enunciado
## t07 · Buscar sin tildes ni mayúsculas (M) ⚠️

Archivo: `backend/notitas/t07.py`

Firma: `def buscar(notas: list[dict], texto: str) -> list[str]`

Cada nota tiene `"id"`, `"titulo"` y `"contenido"`. Devuelve los `id` de las notas que coinciden, en el orden original.
- CA1: coincide si `texto` aparece en el título **o** en el contenido.
- CA2: no importan las mayúsculas ni las marcas diacríticas: `"CANCIÓN"` encuentra `"cancion"`, y `"nino"` encuentra `"niño"`.
- CA3: se usa *case folding* completo de Unicode: `"strasse"` encuentra `"Straße"`.
- CA4: si `texto` está vacío o solo tiene espacios, se devuelven todos los `id`.

### Código final
```python
from unidecode import unidecode

def buscar(notas: list[dict], texto: str) -> list[str]:
    if texto == "" or texto is None or texto.isspace():
        return [nota["id"] for nota in notas]
    
    textoNormalizado = unidecode(texto.casefold())
    coincidencias = []
    for nota in notas:
        if textoNormalizado in unidecode(nota["titulo"].casefold()) or textoNormalizado in unidecode(nota["contenido"].casefold()):
            coincidencias.append(nota["id"])
    return coincidencias;
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Le permite al usuario buscar coincidencias en sus notas de la frase que se desee

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: Si la persona manda un texto vacio o con espacios se retornan todos los id, se maneja en la primera validación con esa funcionalidad de python isspace y una condición para ver si esta vacio.

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Una forma fácil de entender el problema y adicionalmente al buscar en google encontramos funcioanlidades de pyhton que ya realizaban estas validaciones entre ellas una librería Unicode asi que decidimos aprovechar estas ventajas del lenguaje para hacer mas sencillo el ejercicio

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: "nino" no encuentra "niño"**
Respuesta: Miraria en el for que recorre todas las notas y a ver si en las validaciones de texto y contenido se aplican las normalizaciones correspondientes o en el texto de entrada del usuario

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: también se busca dentro de las etiquetas**
Respuesta: en el condicional aparte de texto y contenido buscaría en las etiquetas y tmb se le aplicarían las mismas funciones que a texto y contenido

---
## Caso R03

### Enunciado
## t06 · Filtrar por etiquetas (S)

Archivo: `backend/notitas/t06.py`

Firma: `def filtrar_por_etiquetas(notas: list[dict], etiquetas: list[str], modo: str = "todas") -> list[dict]`

Cada nota tiene `"etiquetas"` (lista de textos).
- CA1: `modo="todas"`: quedan las notas que tienen **todas** las etiquetas pedidas. `modo="alguna"`: las que tienen **al menos una**.
- CA2: la comparación no distingue mayúsculas.
- CA3: si `etiquetas` está vacía, se devuelven todas las notas. Se conserva el orden original.
- CA4: otro `modo` → `ValueError`.

### Código final
```python
def filtrar_por_etiquetas(notas: list[dict], etiquetas: list[str], modo: str = "todas") -> list[dict]:
    if etiquetas is len(etiquetas) == 0:
        return notas
    
    resultado_final = []
    etiquetas = list(map(str.lower, etiquetas))
    
    if modo == "todas":
        for nota in notas:
            nota_valida = True
            for etiqueta_evaluada in etiquetas:
                if etiqueta_evaluada.lower() not in list(map(str.lower, nota["etiquetas"])):
                    nota_valida = False
                    break
            if nota_valida:
                resultado_final.append(nota)
    elif modo == "alguna":
        for nota in notas:
            for etiqueta_evaluada in nota["etiquetas"]:
                if etiqueta_evaluada.lower() in etiquetas:
                    resultado_final.append(nota)
                    break
    else:
        raise ValueError("Modo inválido. Debe ser 'todas' o 'alguna'.")
    return resultado_final
#N = [{"id": "1", "etiquetas": ["casa", "urgente"]}, {"id": "2", "etiquetas": ["casa"]}, {"id": "3", "etiquetas": []}]
#filtrar_por_etiquetas(N, ["casa", "urgente"])
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Traer las notas que se adaptan al filtro de etiquetas segun el modo solicitado

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: Maneja el caso en que no haya etiquetas por las cuales filtar al inicio en un if para ver si esta vacia la lista de etiquetas

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: es la manera mas adecuada de solucionar la tarea con los conocimientos que poseemos de python a pesar de no ser tal vez la mas optima

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: ["CASA"] no encuentra la etiqueta "casa"**
Respuesta: en donde se normalizan las listas de string a minuscula para que no afecte la comparación

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: se agrega el modo "ninguna" (notas sin esas etiquetas)**
Respuesta: Añadiria un elif en el if principal y haria otro bucle invirtiendo la logica y descartar las notas que tengan algunas de las etiquetas del filtro.

---
## Caso R04

### Enunciado
## t04 · Límite WIP de "En curso" (M) ⚠️

Archivo: `backend/notitas/t04.py`

Firma: `def validar_wip(notas: list[dict], nota_id: str, destino: str, limite: int = 3) -> None`

Cada nota es un diccionario con al menos `"id"` y `"columna"`. El módulo ya define la excepción `WipExcedido`.
- CA1: si mover la nota a `"en_curso"` dejaría **más de `limite`** notas en esa columna, se lanza `WipExcedido`. Si no, no devuelve nada.
- CA2: el límite solo aplica a `"en_curso"`; las otras columnas no tienen tope.
- CA3: si la nota **ya está** en `"en_curso"` (solo se reordena), no cuenta como una nota más.
- CA4: si `nota_id` no existe, `KeyError`.

### Código final
```python
class WipExcedido(Exception):
    pass


def validar_wip(notas: list[dict], nota_id: str, destino: str, limite: int = 3) -> None:
    """Ver TAREAS.md, tarea t04."""
    nota = next((n for n in notas if n.get("id") == nota_id), None)
    if nota is None:
        raise KeyError(nota_id)
    
    if destino != "en_curso":
        return None

    if nota.get("columna") == "en_curso":
        return None

    en_curso = sum(1 for n in notas if n.get("columna") == "en_curso")

    if en_curso + 1 > limite:
        raise WipExcedido(
            f'"{destino}" admite como máximo {limite} notas; ya hay {en_curso}.'
        )

    return None
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Al usuario no se le permite exceder el limite definido de tareas que pueden estar en la columna en curso

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: si el id de la nota no existe lanza un error y eso al inicio con un keyerror primero se busca en todas las notas si existe ese id

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Fue la que open code sugirió y estuvimos de acuerdo algo distinto a lo imaginado porque yo no conocía esa funcio sum o next de python

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: reordenar dentro de En curso con 3 notas lanza WipExcedido**
Respuesta: eso significa que esta contando mal y que en la validación de que si el destino es en curso esta haciendo algo distinto a lo esperado entonces revisaría ese if a ver que esta haciendo

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: el límite también aplica a Hecho (máximo 10)**
Respuesta: pues ya no evaluaria solamente en curso y sumaria adicionalmente lo que esta en hecho fuera bueno hacer una función que devuelva según la columna que yo necesite la cantidad de tareas para que no se acumulen variables que sumen de arriba y abajo y centralizar ese comportamiento

---
## Caso R05

### Enunciado
## t11 · Deshacer movimientos (M)

Archivo: `backend/notitas/t11.py`

Clase: `Historial` con `registrar(movimiento: dict) -> None` y `deshacer() -> dict | None`

Un movimiento es `{"nota_id": ..., "desde": ..., "hacia": ...}`.
- CA1: `deshacer()` devuelve el movimiento **inverso** del último registrado (`desde` y `hacia` intercambiados) y lo saca del historial.
- CA2: si no hay nada que deshacer, devuelve `None`.
- CA3: solo se guardan los **últimos 20** movimientos; los más viejos se descartan.

### Código final
```python
class Historial:
    """Ver TAREAS.md, tarea t11."""

    MAX_MOVIMIENTOS = 20

    def __init__(self) -> None:
        self._movimientos: list[dict] = []

    def registrar(self, movimiento: dict) -> None:
        self._movimientos.append(movimiento)
        if len(self._movimientos) > self.MAX_MOVIMIENTOS:
            self._movimientos.pop(0)

    def deshacer(self) -> dict | None:
        if not self._movimientos:
            return None
        movimiento = self._movimientos.pop()
        return {
            "nota_id": movimiento["nota_id"],
            "desde": movimiento["hacia"],
            "hacia": movimiento["desde"],
        }
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: la clase le permite al usuario registrar un movimiento de las notas o deschacer un movimiento si este existe

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: si el movimiento anterior no existe se devuelve none y adicionalmente solo guarda 20 movimientos ya en el 21 borra el primero el mas viejo

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: tambien pense inicialmente en guardar en una lista los movimientos y esto que sea parte del constructor se acepto todo lo del junior opencode con deepsek y tambien se le pidio a claude en opus5.5 revisar entonces alfinal se acepto este enfoque y considero que es bastante entendible, no se hizo de otra forma porque no experimente otras alternativas y decidi quedarme con esta primera version, no vi nada mal y llegue a un acuerdo con el cliente senior.

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: después de 21 movimientos, el primero todavía se puede deshacer**
Respuesta: esta mal definido la variable que tenemos con los limites de movimientos porque debe decir 20 para que se haga bien la validacion y saque el movimiento mas viejo

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: se agrega "rehacer"**
Respuesta: agrego un nuevo metodo a la clase, actualmente deshacer elimina lo que se iba a hacer entonces tocaria no borrarlo y guardarse el historia para que cuando se deshaga ese movimiento poder rehacerlo aunque ahi tocaria ocmo tener otro atributo en el diccionario diferenciador de cuando se deshace algo porque si no podria haber problemas con el metodo deshacer o hacer en el contructor una lista de diccionario pero esta vez para lo de deshacer osea que en la de movimiento se elimine tal cual como se anda haciendo y pues antes de eliminar el ultimo que se iba a hacer guardarlo en esa lista para que el metodo rehacer pueda tener ese historial.

---
## Caso R06

### Enunciado
## t03 · Transiciones entre columnas (M) ⚠️

Archivo: `backend/notitas/t03.py`

Firma: `def puede_mover(origen: str, destino: str) -> bool`

Las columnas son `"por_hacer"`, `"en_curso"` y `"hecho"`.
- CA1: permitido: `por_hacer → en_curso`, `en_curso → hecho`, `en_curso → por_hacer` (devolver) y `hecho → en_curso` (reabrir).
- CA2: **no** permitido: `por_hacer → hecho` (no se salta "En curso") ni `hecho → por_hacer`.
- CA3: mover dentro de la misma columna (reordenar) siempre es permitido.
- CA4: si alguna columna no existe (los nombres son exactos, en minúscula), `ValueError`.

### Código final
```python
from unittest import result

from sqlalchemy import case


def puede_mover(origen: str, destino: str) -> bool:

    value = origen
    columnas_permitidas = ["por_hacer", "en_curso", "hecho"]

    if destino not in columnas_permitidas or origen not in columnas_permitidas:
        raise ValueError("La columna no existe")

    match value:
        case "por_hacer":

            if destino == "en_curso" or destino == "por_hacer":
                return True
            else:
                return False

        case "en_curso":
            
            if destino == "por_hacer" or destino == "hecho" or destino == "en_curso":
                return True
            else:
                return False

        case "hecho":
            if destino == "en_curso" or destino == "hecho":
                return True
            else:
                return False
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Validar si es permitido la navegación entre las columnas definidas

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: en caso tal de que alguna columna no existe sea de origen o destino lanza una excepción

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: muchos if anidados no nos parecía adecuado asi que elegimos una alternativa que nos sugirió una pagina de google al switch case que no tiene python

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: "Hecho" (con mayúscula) no lanza error**
Respuesta: pues tocaria al inicio en el origen y destino poner todo en minúsculas si ese criterio se define para que valga mayuscula o minúscula si no pues miraría al inicio en las columnas que me permite el código

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: también se permite pasar de Por hacer directo a Hecho**
Respuesta: voy al caso del por hacer y permito ese movimiento en el condicional

---
## Caso R07

### Enunciado
## t12 · Dos personas mueven la misma nota (L) ⚠️

Archivo: `backend/notitas/t12.py`

Clase: `Tablero(notas: list[dict])` con `mover(nota_id: str, destino: str, version: int) -> dict`. El módulo ya define la excepción `Conflicto`.

Cada nota tiene `"id"`, `"columna"` y `"version"` (entero). Es **bloqueo optimista**: el cliente manda la versión que vio.
- CA1: si `version` coincide con la de la nota, la nota pasa a `destino`, su versión sube en 1 y se devuelve **una copia** de la nota actualizada.
- CA2: si no coincide (alguien la movió antes), `Conflicto`, y la nota no cambia.
- CA3: si `nota_id` no existe, `KeyError`.
- CA4: es seguro con **hilos**: si varias llamadas llegan al mismo tiempo con la misma versión, exactamente **una** gana y las demás reciben `Conflicto`.
- CA5: el `Tablero` no comparte las notas con la lista que recibió (modificar la lista original después no lo afecta).

### Código final
```python
import threading
import copy
class Conflicto(Exception):
    pass


class Tablero:
    _notas: list[dict]
    lock_acceso_tablero: threading.Lock
    def __init__(self, notas: list[dict]):
        self._notas = copy.deepcopy(notas)
        self.lock_acceso_tablero = threading.Lock()
    
    def get_notas(self):
        return self._notas
    def set_notas(self, notas: list[dict]):
        self._notas = copy.deepcopy(notas)

    def mover(self, nota_id: str, destino: str, version: int) -> dict:
        nota_a_mover = None
        for nota in self.get_notas():
            if nota["id"] == nota_id:
                nota_a_mover = nota
                break
        if nota_a_mover is None:
            raise KeyError(f"No se encontró la nota con id {nota_id}")
        
        self.lock_acceso_tablero.acquire()
        if nota_a_mover["version"] == version:
            nota_a_mover["version"] += 1
            nota_a_mover["columna"] = destino
            self.lock_acceso_tablero.release()
            return copy.deepcopy(nota_a_mover)
        else:
            self.lock_acceso_tablero.release()
            raise Conflicto(
                f"Conflicto de versión: la nota ya ha sido movida."
            )
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Validar multiples cambios a un solo tablero con las mismas notas aplicando conceptos de concurrencia y referencias en memoria.

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: Maneja el caso en que varios hilos al mismo tiempo intentes modificar la misma nota y si una copia por referencia externa hace un cambio afecte a las notas del tablero

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Se tuvo que estudiar muy bien diferentes conceptos de mutex y copias profundas al ser estructuras de varios niveles(un diccionario de listas), para llegar a la version que funcionara para multiples usuarios a la vez.

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: dos hilos con la misma versión mueven la nota los dos**
Respuesta: Miraria el atributo lock de la clase tablero que maneja la concurrencia de varios hilos, bloqueando los cambios hasta que termine el primer hilo.

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: el conflicto devuelve también la versión actual de la nota**
Respuesta: Iria a la clase conflicto y devolveria tambien una copia de la nota actual.

---
## Caso R08

### Enunciado
## t12 · Dos personas mueven la misma nota (L) ⚠️

Archivo: `backend/notitas/t12.py`

Clase: `Tablero(notas: list[dict])` con `mover(nota_id: str, destino: str, version: int) -> dict`. El módulo ya define la excepción `Conflicto`.

Cada nota tiene `"id"`, `"columna"` y `"version"` (entero). Es **bloqueo optimista**: el cliente manda la versión que vio.
- CA1: si `version` coincide con la de la nota, la nota pasa a `destino`, su versión sube en 1 y se devuelve **una copia** de la nota actualizada.
- CA2: si no coincide (alguien la movió antes), `Conflicto`, y la nota no cambia.
- CA3: si `nota_id` no existe, `KeyError`.
- CA4: es seguro con **hilos**: si varias llamadas llegan al mismo tiempo con la misma versión, exactamente **una** gana y las demás reciben `Conflicto`.
- CA5: el `Tablero` no comparte las notas con la lista que recibió (modificar la lista original después no lo afecta).

### Código final
```python
import threading
import copy
class Conflicto(Exception):
    pass


class Tablero:
    _notas: list[dict]
    lock_acceso_tablero: threading.Lock
    def __init__(self, notas: list[dict]):
        self._notas = copy.deepcopy(notas)
        self.lock_acceso_tablero = threading.Lock()
    
    def get_notas(self):
        return self._notas
    def set_notas(self, notas: list[dict]):
        self._notas = copy.deepcopy(notas)

    def mover(self, nota_id: str, destino: str, version: int) -> dict:
        nota_a_mover = None
        for nota in self.get_notas():
            if nota["id"] == nota_id:
                nota_a_mover = nota
                break
        if nota_a_mover is None:
            raise KeyError(f"No se encontró la nota con id {nota_id}")
        
        self.lock_acceso_tablero.acquire()
        if nota_a_mover["version"] == version:
            nota_a_mover["version"] += 1
            nota_a_mover["columna"] = destino
            self.lock_acceso_tablero.release()
            return copy.deepcopy(nota_a_mover)
        else:
            self.lock_acceso_tablero.release()
            raise Conflicto(
                f"Conflicto de versión: la nota ya ha sido movida."
            )
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Control de conflictos en caso tal de que dos usuarios muevan la misma nota

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: si no existe una nota y también si alguien ya movio la nota anteriormente

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: nos ayudamos de internet para la parte de hilos que no teníamos mucho conocimiento y para recordar la encapsulación y la parte de las copias. se que hay version mas eficiente pero asi fue como se entendio y se uso google y nuestros conocimientos para armar la respuesta

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: dos hilos con la misma versión mueven la nota los dos**
Respuesta: pues estamos manejando la concurrencia con eso de aquire y lock entonces pues iría a esa parte para ver si se esta permitiendo solo un usuario cuando se accede a ese recurso por asi decir para ver si realmente esa función sirve y se esta validando correctamente

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: el conflicto devuelve también la versión actual de la nota**
Respuesta: pues antes de lanzar la excepción imprimo la version actual de la nota y no se si se pueda mandar esos datos como parámetro de la excepción personalizada, no recuerdo pero pensaría algo asi si eso se refiere

---
## Caso R09

### Enunciado
## t01 · Validar el título de una nota (S)

Archivo: `backend/notitas/t01.py`

Firma: `def validar_titulo(s: str) -> str`

Devuelve el título limpio o lanza `ValueError`.
- CA1: se quitan los espacios al inicio y al final (incluye tabulaciones, saltos de línea y el espacio duro ` `).
- CA2: los espacios internos repetidos se dejan en uno solo (`"Comprar   pan"` → `"Comprar pan"`).
- CA3: el texto se normaliza a Unicode **NFC**.
- CA4: si queda vacío o tiene **más de 80 caracteres** (puntos de código, después de normalizar), `ValueError`.

### Código final
```python
import re
import unicodedata

MAX_TITULO = 80
_ESPACIOS_REPETIDOS = re.compile(r" {2,}")

def validar_titulo(s: str) -> str:
    """Ver TAREAS.md, tarea t01."""
    titulo = " ".join(s.split())
    titulo = unicodedata.normalize("NFC", titulo)

    if not titulo:
        raise ValueError("el título no puede quedar vacío")
    if len(titulo) > MAX_TITULO:
        raise ValueError(f"el título supera los {MAX_TITULO} caracteres")
    return titulo
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Validar el titulo que ingrese el usuario devolviendoselo limpio y garantizando que este dentro del rango de caracteres y no vacio

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: si el texto es vacio o excede los 80 caracteres

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: basicamente pues fue lo que sugirio opencode y la vd me parecio una forma sencilla de entender y aprovechar python con todas las funcionalidades y atajos que se pueda y si fue entendible.

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: " Hola " devuelve el título con espacios**
Respuesta: de hecho nos paso algo similar y era porque no estabas teniendo en cuenta con el agente todos los tipos de espacios entonces miraria al inicio el join y el split que usamos que basicamente se hizo para eliminar todos los tipos de espacios y volver a juntar todo entonces si algo falla debe ser ahi

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: el máximo pasa de 80 a 120 caracteres**
Respuesta: en la variable global definida cambio de 80 a 120 caracteres

---
## Caso R10

### Enunciado
## t22 · Notas bloqueadas (M)

Archivo: `backend/notitas/t22.py`

Firma: `def mover_bloqueada(nota: dict, destino: str, motivo: str | None = None) -> dict`. El módulo ya define la excepción `NotaBloqueada`.

Una nota puede estar bloqueada (`"bloqueada": True`), por ejemplo porque espera a alguien.
- CA1: si **no** está bloqueada, devuelve una copia con `"columna": destino` (el motivo se ignora).
- CA2: si está bloqueada, solo se mueve con un `motivo` que no quede vacío al recortar; si no, `NotaBloqueada`.
- CA3: al moverla con motivo, la copia queda con `"bloqueada": False` y agrega al final de `"historial"` (que se crea si no existe) `{"accion": "desbloqueo", "motivo": <motivo recortado>}`.
- CA4: nunca modifica la nota original (tampoco su historial).

### Código final
```python
class NotaBloqueada(Exception):
    pass


def mover_bloqueada(nota: dict, destino: str, motivo: str | None = None) -> dict:
    copia = dict(nota)
    copia["columna"] = destino

    if not nota.get("bloqueada"):
        return copia

    if not motivo or not motivo.strip():
        raise NotaBloqueada()

    copia["bloqueada"] = False
    historial = list(nota.get("historial") or [])
    historial.append({"accion": "desbloqueo", "motivo": motivo.strip()})
    copia["historial"] = historial
    return copia
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: La función evalúa el cambiar una nota de columna en base a si esta bloqueda o no

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: El caso borde que maneja es si esta bloqueada pero tiene un motivo para moverse o si esta bloqueada y no tiene motivo para moverse

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Le di correciones por que sentí que era la mejor manera de evitar comentarios innecesario y evitar código duplicado

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: un motivo de solo espacios desbloquea la nota**
Respuesta: miraría el condicional donde se valida si la nota al eliminar los espacios queda vacia

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: también se guarda quién desbloqueó la nota**
Respuesta: Tendría que pedir por los parámetros de la función el id o nombre d ela persona y al escribir un elemento del historial agregar esa información

---
## Caso R11

### Enunciado
## t16 · Ordenar por prioridad y fecha (S)

Archivo: `backend/notitas/t16.py`

Firma: `def ordenar(notas: list[dict]) -> list[dict]`

Cada nota tiene `"prioridad"` (1 baja, 2 media, 3 alta) y `"vence"` (`"AAAA-MM-DD"` o `None`).
- CA1: primero la prioridad más alta; entre iguales, la fecha de vencimiento más cercana; las que no tienen fecha van al final de su grupo.
- CA2: si todo empata, se conserva el orden original (orden estable).
- CA3: devuelve una lista nueva; no modifica `notas`.

### Código final
```python
def ordenar(notas: list[dict]) -> list[dict]:
    return sorted(
        notas,
        key=lambda n: (
            -n["prioridad"],
            n["vence"] is None,
            n["vence"] or "",
        ),
    )
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Reordenar por prioridad las tareas del usuario

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: en los empates no cambia el orden

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: por sugerencia de opencode y fue según lo que me imaginaba que iba a hacer filtrar todo de una en una función

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: dos notas iguales cambian de orden entre sí**
Respuesta: en la función sorted debe estar haciéndose mal una validación debido a que en empates no pasa nada asi que haría prints para ver que pasa y pregutnaria a open code por sugerencias de donde mirar para entender mejor el problema

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: las notas sin fecha van al principio de su grupo**
Respuesta: iría a la función sorted y le cambio la prioridad a las notas sin fecha y repasar mas que puedo hacer con la funcion sorted

---
## Caso R12

### Enunciado
## t06 · Filtrar por etiquetas (S)

Archivo: `backend/notitas/t06.py`

Firma: `def filtrar_por_etiquetas(notas: list[dict], etiquetas: list[str], modo: str = "todas") -> list[dict]`

Cada nota tiene `"etiquetas"` (lista de textos).
- CA1: `modo="todas"`: quedan las notas que tienen **todas** las etiquetas pedidas. `modo="alguna"`: las que tienen **al menos una**.
- CA2: la comparación no distingue mayúsculas.
- CA3: si `etiquetas` está vacía, se devuelven todas las notas. Se conserva el orden original.
- CA4: otro `modo` → `ValueError`.

### Código final
```python
def filtrar_por_etiquetas(notas: list[dict], etiquetas: list[str], modo: str = "todas") -> list[dict]:
    if etiquetas is len(etiquetas) == 0:
        return notas
    
    resultado_final = []
    etiquetas = list(map(str.lower, etiquetas))
    
    if modo == "todas":
        for nota in notas:
            nota_valida = True
            for etiqueta_evaluada in etiquetas:
                if etiqueta_evaluada.lower() not in list(map(str.lower, nota["etiquetas"])):
                    nota_valida = False
                    break
            if nota_valida:
                resultado_final.append(nota)
    elif modo == "alguna":
        for nota in notas:
            for etiqueta_evaluada in nota["etiquetas"]:
                if etiqueta_evaluada.lower() in etiquetas:
                    resultado_final.append(nota)
                    break
    else:
        raise ValueError("Modo inválido. Debe ser 'todas' o 'alguna'.")
    return resultado_final
#N = [{"id": "1", "etiquetas": ["casa", "urgente"]}, {"id": "2", "etiquetas": ["casa"]}, {"id": "3", "etiquetas": []}]
#filtrar_por_etiquetas(N, ["casa", "urgente"])
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: ayudar al usuario a filtrar una nota que tenga todas las etiquetas seleccionadas o que al menos tenga una.

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: primero si las etiquetas están vacias se devuelven todas las notas, si un modo no esta definido lanza una excepción.

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: pues estamos retomando lo del código de pronto se pudo haber hecho todo con menos if y for y utilizando mas funciones de python pero no nos acordábamos de otras funcionalidades con las que cuenta el lenguaje entonces decidimos hacerlo de forma sencilla la cual es con if anidados y for para recorrer los elementos de la listas.

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: ["CASA"] no encuentra la etiqueta "casa"**
Respuesta: pues miro en el for donde se comparan las etiquetas buscadas con las de las notas a ver si ambas están inicialmente con la función .lower aplciada. nosotros definimos al inicio de una vez tener el arreglo de etiquetas en mayuscula pero faltaría comprobar si en lo de notas se hace bien esa conversion

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: se agrega el modo "ninguna" (notas sin esas etiquetas)**
Respuesta: pues se que no es la mejor solución pero agregaría otro if para que hiciera esa búsqueda de notas sin las etiquetas mencionadas.

---
## Caso R13

### Enunciado
## t15 · Resumen por columna (S)

Archivo: `backend/notitas/t15.py`

Firma: `def resumen_columnas(notas: list[dict]) -> dict`

- CA1: devuelve `{"por_hacer": n, "en_curso": n, "hecho": n, "total": n, "porcentaje_hecho": p}`.
- CA2: las notas con `"archivada": True` no cuentan.
- CA3: `porcentaje_hecho` es un entero redondeado al más cercano, y los empates (.5) suben (`1 de 8` = 12,5 % → 13). Si no hay notas, es 0.

### Código final
```python
def resumen_columnas(notas: list[dict]) -> dict:
    
    resumen = {"por_hacer": 0, "en_curso": 0, "hecho": 0, "total": 0, "porcentaje_hecho": 0}

    for nota in notas:

        try:
            isArchivada = nota["archivada"]
        except KeyError:
            isArchivada = False
            
        if isArchivada is False:
            match nota["columna"]:
                case "por_hacer":
                    resumen["por_hacer"] += 1
                case "en_curso":
                    resumen["en_curso"] += 1
                case "hecho":
                    resumen["hecho"] += 1
                case _:
                    raise ValueError(f"Columna desconocida: {nota['columna']}")

    resumen["total"] = resumen["por_hacer"] + resumen["en_curso"] + resumen["hecho"]

    if resumen["total"] == 0:
        resumen["porcentaje_hecho"] = 0
    else:
        resumen["porcentaje_hecho"] = (float(resumen["hecho"])/float(resumen["total"])) * 100
        if resumen["porcentaje_hecho"] - int(resumen["porcentaje_hecho"]) >= 0.5:
            resumen["porcentaje_hecho"] = int(resumen["porcentaje_hecho"]) + 1
        else:
            resumen["porcentaje_hecho"] = int(resumen["porcentaje_hecho"])    

                    
    return resumen
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: La función da una vista a cuantas notas hay por columna y el porcentaje de las completadas.

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: Maneja el caso borde cuando no hay ninguna nota entonces el porcentaje de completas es 0

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Se considero el mas legible por otros con un match y también s einvestigo la forma de redondear al entero mas cercano

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: 1 hecha de 8 notas da 12 % en vez de 13 %**
Respuesta: en el if que definimos para redondear al entero mas cercano si esta bien la condición para redondear hacia arriba o hacia bajo

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: el porcentaje se calcula sin contar Por hacer**
Respuesta: EN la operación que sacamos el total de notas para sacar el porcentaje quitaría de la suma las notas que están en por_hacer

---
## Caso R14

### Enunciado
## t03 · Transiciones entre columnas (M) ⚠️

Archivo: `backend/notitas/t03.py`

Firma: `def puede_mover(origen: str, destino: str) -> bool`

Las columnas son `"por_hacer"`, `"en_curso"` y `"hecho"`.
- CA1: permitido: `por_hacer → en_curso`, `en_curso → hecho`, `en_curso → por_hacer` (devolver) y `hecho → en_curso` (reabrir).
- CA2: **no** permitido: `por_hacer → hecho` (no se salta "En curso") ni `hecho → por_hacer`.
- CA3: mover dentro de la misma columna (reordenar) siempre es permitido.
- CA4: si alguna columna no existe (los nombres son exactos, en minúscula), `ValueError`.

### Código final
```python
from unittest import result

from sqlalchemy import case


def puede_mover(origen: str, destino: str) -> bool:

    value = origen
    columnas_permitidas = ["por_hacer", "en_curso", "hecho"]

    if destino not in columnas_permitidas or origen not in columnas_permitidas:
        raise ValueError("La columna no existe")

    match value:
        case "por_hacer":

            if destino == "en_curso" or destino == "por_hacer":
                return True
            else:
                return False

        case "en_curso":
            
            if destino == "por_hacer" or destino == "hecho" or destino == "en_curso":
                return True
            else:
                return False

        case "hecho":
            if destino == "en_curso" or destino == "hecho":
                return True
            else:
                return False
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Es una validación de si es posible un cambio de estado de la nota en base a su origen y destino

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: Maneja el caso borde de que los nombres de las columnas de origen y destino, tal cual se pusieron no existan.

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: No es la forma mas optimizada pero para retornar a Python se opto por algo funcional, que cumpla.

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: "Hecho" (con mayúscula) no lanza error**
Respuesta: El condicional al inicio que valida los nombres de las columnas permitidas tal cual.

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: también se permite pasar de Por hacer directo a Hecho**
Respuesta: El if de los estado permitidos de la columna Por hacer y añadiría Hecho al If de los que devuelven true.

---
## Caso R15

### Enunciado
## t15 · Resumen por columna (S)

Archivo: `backend/notitas/t15.py`

Firma: `def resumen_columnas(notas: list[dict]) -> dict`

- CA1: devuelve `{"por_hacer": n, "en_curso": n, "hecho": n, "total": n, "porcentaje_hecho": p}`.
- CA2: las notas con `"archivada": True` no cuentan.
- CA3: `porcentaje_hecho` es un entero redondeado al más cercano, y los empates (.5) suben (`1 de 8` = 12,5 % → 13). Si no hay notas, es 0.

### Código final
```python
def resumen_columnas(notas: list[dict]) -> dict:
    
    resumen = {"por_hacer": 0, "en_curso": 0, "hecho": 0, "total": 0, "porcentaje_hecho": 0}

    for nota in notas:

        try:
            isArchivada = nota["archivada"]
        except KeyError:
            isArchivada = False
            
        if isArchivada is False:
            match nota["columna"]:
                case "por_hacer":
                    resumen["por_hacer"] += 1
                case "en_curso":
                    resumen["en_curso"] += 1
                case "hecho":
                    resumen["hecho"] += 1
                case _:
                    raise ValueError(f"Columna desconocida: {nota['columna']}")

    resumen["total"] = resumen["por_hacer"] + resumen["en_curso"] + resumen["hecho"]

    if resumen["total"] == 0:
        resumen["porcentaje_hecho"] = 0
    else:
        resumen["porcentaje_hecho"] = (float(resumen["hecho"])/float(resumen["total"])) * 100
        if resumen["porcentaje_hecho"] - int(resumen["porcentaje_hecho"]) >= 0.5:
            resumen["porcentaje_hecho"] = int(resumen["porcentaje_hecho"]) + 1
        else:
            resumen["porcentaje_hecho"] = int(resumen["porcentaje_hecho"])    

                    
    return resumen
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Darle a el usuario un resumen de los estados de sus tarjetas con un su porcentaje de tareas terminadas

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: Si no hay tareas el porcentaje es 0

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: a la hora del desarrollo decidimos usar un case en vez de ifs anidados debido a que eran varios casos y en caso de que a futuro aumenten sea mas fácil acomodarlos en el switch y la parte del redondeo la que nos sugirió google porque no encontramos una función especifica de python para eso

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: 1 hecha de 8 notas da 12 % en vez de 13 %**
Respuesta: En la parte del redondeo revisaría ese condicional a ver como se esta haciendo e ir imprimiendo que da en cada paso

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: el porcentaje se calcula sin contar Por hacer**
Respuesta: voy a la parte de mas abajo de la función y quito la clave del diccionario resumen donde esta la clave "Por hacer" y ya no se calcularía con eso en el porcentaje

---
## Caso R16

### Enunciado
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

### Código final
```python
import re

HEX = re.compile(r"#?[0-9A-Fa-f]{6}")

PALETA = {
    "matcha": "#BCC86F",
    "semolina": "#F5CB99",
    "fresa": "#FFABA9",
    "rosa": "#F68578",
    "mani": "#B9794A",
    "chocolate": "#79371D",
}


def normalizar_color(c: str) -> str:
    """Ver TAREAS.md, tarea t02."""
    texto = c.strip()
    nombre = texto.lower()
    if nombre in PALETA:
        return PALETA[nombre]
    if HEX.fullmatch(texto):
        hex_canonico = "#" + texto.lstrip("#").upper()
        if hex_canonico in PALETA.values():
            return hex_canonico
    raise ValueError(f"Color no válido: {c!r}")
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Garantizar que las notitas del usuario solo tengan los colores definidos ya sea en hexadecimal o en palabras

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: Si el color no esta en el diccionario que definidos lanza una excepcion value error y eso se hace despues de haber realizado las otras comparaciones validas asi que si no cumple pues se lanza la excepcion

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: yo en un inicio tambien pense de validarlo desde un diccionario o dos listas pero con opencode mas eficiente es el diccionario y mas entendible el codigo entonces pues si fue algo pensado inicialmente ya lo otro como siempre funciones de python para normalizar la entrada que son entendibles y pues nos ayuda a aprovechar este lenguaje y siento que con mi entendimiento actual y conocimiento decidi aceptar esta forma del agente

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: "#bcc86f" lanza error**
Respuesta: revisaria primero si en el diccionario esta definido, si se encuentra significa que es valido y pues ya es problema de las validaciones asi que iria al if donde miramos que el hex coincida con los valores del diccionario o depronto el # es el problema ahi asi que revisaria, ese es el ultimo if donde se valida lo del hexadecimal entonces hay que mirar ahi primero

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: se agrega el color "crema" #FFF8EF a la paleta**
Respuesta: añado esa clave y valor en el diccionario definido en el codigo

---
## Caso R17

### Enunciado
## t04 · Límite WIP de "En curso" (M) ⚠️

Archivo: `backend/notitas/t04.py`

Firma: `def validar_wip(notas: list[dict], nota_id: str, destino: str, limite: int = 3) -> None`

Cada nota es un diccionario con al menos `"id"` y `"columna"`. El módulo ya define la excepción `WipExcedido`.
- CA1: si mover la nota a `"en_curso"` dejaría **más de `limite`** notas en esa columna, se lanza `WipExcedido`. Si no, no devuelve nada.
- CA2: el límite solo aplica a `"en_curso"`; las otras columnas no tienen tope.
- CA3: si la nota **ya está** en `"en_curso"` (solo se reordena), no cuenta como una nota más.
- CA4: si `nota_id` no existe, `KeyError`.

### Código final
```python
class WipExcedido(Exception):
    pass


def validar_wip(notas: list[dict], nota_id: str, destino: str, limite: int = 3) -> None:
    """Ver TAREAS.md, tarea t04."""
    nota = next((n for n in notas if n.get("id") == nota_id), None)
    if nota is None:
        raise KeyError(nota_id)
    
    if destino != "en_curso":
        return None

    if nota.get("columna") == "en_curso":
        return None

    en_curso = sum(1 for n in notas if n.get("columna") == "en_curso")

    if en_curso + 1 > limite:
        raise WipExcedido(
            f'"{destino}" admite como máximo {limite} notas; ya hay {en_curso}.'
        )

    return None
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: La función evalúa el limite wip de la columna en_curso, al pasar una nota de una columna diferente a la de en_curso

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: EL evaluar si la nota a cambiar de columna realmente existe, además de si no se encuentra ya en la nota en la columna en_curso

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Es la manera que nos sugirió la ia y tenia menos costo computacional y estaba mas ordenado que el enfoque que inicialmente planteamos

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: reordenar dentro de En curso con 3 notas lanza WipExcedido**
Respuesta: Validar el er if de la función donde se evalúa si el origen de la nota es la misma columna en curso, debe de retornar none y no lanzar excepciones

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: el límite también aplica a Hecho (máximo 10)**
Respuesta: Eliminar la validación que retorna sin errores si destino es diferentes de en_cruso para que acepte también si el destino es hecho, poner una nueva validación al final si destino es hecho y hay mas de 10 lanzar wip error y mover el return none luego de esta nueva validación

---
## Caso R18

### Enunciado
## t16 · Ordenar por prioridad y fecha (S)

Archivo: `backend/notitas/t16.py`

Firma: `def ordenar(notas: list[dict]) -> list[dict]`

Cada nota tiene `"prioridad"` (1 baja, 2 media, 3 alta) y `"vence"` (`"AAAA-MM-DD"` o `None`).
- CA1: primero la prioridad más alta; entre iguales, la fecha de vencimiento más cercana; las que no tienen fecha van al final de su grupo.
- CA2: si todo empata, se conserva el orden original (orden estable).
- CA3: devuelve una lista nueva; no modifica `notas`.

### Código final
```python
def ordenar(notas: list[dict]) -> list[dict]:
    return sorted(
        notas,
        key=lambda n: (
            -n["prioridad"],
            n["vence"] is None,
            n["vence"] or "",
        ),
    )
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Reordenar las notas de las columnas en base a prioridad y fecha limite

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: El caso en el que la nota no tenga una fecha limite

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Es la manera mas corta y eficiente de solucionar, a pesar de que tla vez no sea la mas fácil de entender a simple vista

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: dos notas iguales cambian de orden entre sí**
Respuesta: La verdad no sabría muy bien si esto es posible con la función sorted, probablemnet puedo añadir otro criterio de ordenamiento obteniendo el índice del objeto y poniendo como criterio el negativo para que asi el que estaba primero lo ponga después y el de sefundo de primero

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: las notas sin fecha van al principio de su grupo**
Respuesta: en el criterio del sorted que dice Nota"fecha" is None le pondría una negación asi pondría con cero o mas prioridad a los que no tienen fecha

---
## Caso R19

### Enunciado
## t09 · Normalizar etiquetas (S)

Archivo: `backend/notitas/t09.py`

Firma: `def normalizar_etiquetas(etiquetas: list[str]) -> list[str]`

- CA1: cada etiqueta se recorta, se pasa a minúsculas y sus espacios internos repetidos quedan en uno.
- CA2: se descartan las vacías y las repetidas, conservando el orden de la **primera** aparición.
- CA3: si quedan **más de 5** etiquetas, o alguna tiene **más de 20** caracteres, `ValueError`.

### Código final
```python
def normalizar_etiquetas(etiquetas: list[str]) -> list[str]:
    """Ver TAREAS.md, tarea t09."""
    normalizadas = (" ".join(etiqueta.split()).lower() for etiqueta in etiquetas)
    resultado: list[str] = []
    for etiqueta in normalizadas:
        if etiqueta and etiqueta not in resultado:
            resultado.append(etiqueta)
    if len(resultado) > 5 or any(len(etiqueta) > 20 for etiqueta in resultado):
        raise ValueError("etiquetas fuera de rango")
    return resultado
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: La función normaliza las etiquetas de una nota volviéndolas minúscula y eliminando espacios innecesario, además de etiquetas repetidas

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: El caso en el que haya mas de 5 etiquetas finales o si alguna excede la longitud de 20 caracteres con el texto ya normalizado

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Es una forma entendible de codificar el flujo si sigue el enfoque inicialmente planteado por mi, aunque con funciones que lo hacen muy ordenado de ver como el Split o join

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: ["a","A"] devuelve dos etiquetas**
Respuesta: Miraria el inicio de la función donde pasamos los caracteres a minúscula, por que significa que no lo esta haciendo bien

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: el máximo pasa a 3 etiquetas y se descartan las sobrantes en vez de dar error**
Respuesta: Iria a la comprobación final y si excede las 3 etiquetas retornaría una copia de la lista pero solo de sus primeras 3 posiciones

---
## Caso R20

### Enunciado
## t07 · Buscar sin tildes ni mayúsculas (M) ⚠️

Archivo: `backend/notitas/t07.py`

Firma: `def buscar(notas: list[dict], texto: str) -> list[str]`

Cada nota tiene `"id"`, `"titulo"` y `"contenido"`. Devuelve los `id` de las notas que coinciden, en el orden original.
- CA1: coincide si `texto` aparece en el título **o** en el contenido.
- CA2: no importan las mayúsculas ni las marcas diacríticas: `"CANCIÓN"` encuentra `"cancion"`, y `"nino"` encuentra `"niño"`.
- CA3: se usa *case folding* completo de Unicode: `"strasse"` encuentra `"Straße"`.
- CA4: si `texto` está vacío o solo tiene espacios, se devuelven todos los `id`.

### Código final
```python
from unidecode import unidecode

def buscar(notas: list[dict], texto: str) -> list[str]:
    if texto == "" or texto is None or texto.isspace():
        return [nota["id"] for nota in notas]
    
    textoNormalizado = unidecode(texto.casefold())
    coincidencias = []
    for nota in notas:
        if textoNormalizado in unidecode(nota["titulo"].casefold()) or textoNormalizado in unidecode(nota["contenido"].casefold()):
            coincidencias.append(nota["id"])
    return coincidencias;
```

### Preguntas y respuestas
**P1. ¿Qué hace la función, en una frase?**
Respuesta: Busca coincidencias de un texto en una lista de notas, ya sea en titulo o contenido, independiente de mayuscualas y minúsculas, ni caracteres especiales

**P2. ¿Qué caso borde maneja y dónde?**
Respuesta: el caso borde si el texto esta vacio o son puros espacios, lo maneja en un condicional al inicio.

**P3. ¿Por qué se eligió esta forma y no otra?**
Respuesta: Se busco en la documentación de Python y foros las mejores maneras de normalizar el texto usando unidecode o casefold para comparar cadenas de forma segura

**P4. Si mañana falla con esto, ¿dónde mirarías primero? Falla: "nino" no encuentra "niño"**
Respuesta: miraría el lugar donde normalizamos el texto con unidecode y donde normalizamos los campos de las notas

**P5. ¿Qué cambiarías si el requisito cambia así? Cambio: también se busca dentro de las etiquetas**
Respuesta: Cambiaria el if dentrodel for donde se busca por cada nota en los campos titulo y contenido agregaría buscar en el campo de etiquetas.

