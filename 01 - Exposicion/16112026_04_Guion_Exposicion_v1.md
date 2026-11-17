# Guion de la exposición

Diapositivas: `01 - Exposicion/Diapositivas/16112026_01_Diapositivas_v5.html` (flechas para avanzar, **F** para pantalla completa).

**Cómo usar este guion:** no es para leerlo en voz alta. Léanlo varias veces, quédense con la idea de cada diapositiva y díganla con sus palabras. Lo que está entre comillas es un ejemplo de cómo decirlo. Los tiempos suman 10 minutos de tema y 8 de proyecto.

Quién habla en cada parte sigue `16112026_03_Division_Revision_y_Exposicion_v1.md`. Cámbienlo si lo prefieren, pero **los dos deben saberse todo**.

---

## PARTE 1 · EL TEMA (10 min)

### 1 · Portada · los dos · 20 s
"Hola, somos Ana Sofía y Juan José. Nuestro tema es pair programming, pero con una pregunta de hoy: ¿qué pasa cuando el compañero es un agente de IA?"

### 2 · El problema · Ana Sofía · 1:30
- La idea del pair programming: **dos personas, un mismo código**. Las dos lo entienden.
- Hoy el compañero puede ser un agente: escribe rápido y no se cansa, **pero no necesita entender lo que hace**.
- Cerrar con la pregunta del tema: "Si el compañero ya no aprende, ¿qué aprendizaje desaparece? Y si nosotros dejamos de pensar porque el agente lo hace, ¿qué perdemos?"

### 3 · Cómo funciona · Ana Sofía · 1:30
- Dos roles: el **conductor** escribe y piensa en voz alta; el **navegante** revisa cada línea, piensa en los casos raros y en el diseño.
- Cambian de rol seguido para que los dos entiendan todo.
- Origen: viene de Extreme Programming, finales de los noventa (Beck, 1999).
- "En la animación se ve cómo el teclado pasa de uno a otro: eso es lo importante, que los dos lo toquen."

### 4 · Qué dice la evidencia · Juan José · 2:00
Decir **quién lo midió**, no opiniones:
- "Programar en pareja no siempre gana: depende de la complejidad de la tarea" (Hannay y otros, 2009, revisaron muchos estudios).
- "Su mayor valor es que el conocimiento se comparte" (Plonka y otros, 2015).
- "Con IA, estudiantes terminaron 35 % más rápido, pero no entendían por qué funcionaba" (Shihab y otros, 2025).
- "Las sugerencias de la IA se revisan menos que las de un compañero, y quien no escribe cree que entiende" (Welter, 2025; Prather, 2024).
- Conclusión: "Por eso medimos tiempo, pero también comprensión."

### 5 · Pruébenlo así · Juan José · 1:40
Hablarle al curso, como una receta para que lo prueben:
1. Lean la tarea y digan cuánto creen que se van a demorar.
2. Escriban en dos líneas cómo lo harían, **antes** de abrir el agente.
3. Elijan el rol del agente: que revise o que escriba.
4. Cada cosa que proponga: aceptar, corregir o rechazar, y anoten por qué.
5. Al final, expliquen el código sin mirarlo. "Si no pueden, no lo entendieron."

### 6 · Crítica · Ana Sofía · 3:00
Lo que más pesa en la nota de crítica. Decirlo con ejemplos propios:
- **Qué no resuelve:** el agente no aprende con ustedes ni les enseña si no le preguntan. La gran ganancia del pair programming, compartir lo que se sabe, se pierde.
- **Cuándo no conviene:** cuando la tarea es para aprender, cuando el código es confidencial o cuando nadie va a revisar lo que acepta.
- **Qué cuesta:** revisar bien lleva tiempo, y la sensación de ir rápido engaña. "El costo real es una deuda de conocimiento: código que funciona y que nadie entiende."

---

## PARTE 2 · EL PROYECTO (8 min)

### 7 · Notitas · Juan José · 25 s
"Para medir hicimos nuestro propio caso: Notitas, un tablero tipo kanban con 24 funciones vacías. Diez son difíciles a propósito. Lo clave: cada tarea tiene pruebas ocultas que ni nosotros ni el agente vemos hasta terminar."

### 8 · Cómo medimos · Juan José · 25 s
"Medimos cinco cosas: cuánto tardamos, cuántas pruebas ocultas fallan, cuánto tiempo corregimos, si entendemos el código (el codewalk) y si nuestra sensación de tiempo acierta."

### 9 · Línea base · Juan José · 25 s
"Primero medimos sin IA: 5 tareas en pareja, con video y cronómetro. La mediana fue de 38 minutos."

### 10 · Escenarios · Ana Sofía · 20 s
"Después pusimos al agente en cuatro roles: revisando lo que escribimos, escribiendo y nosotros revisando, como tercero entre los dos, y con un agente junior que escribe y uno senior que revisa."

### 11 · Antes y después · Ana Sofía · 35 s
"En las tareas pequeñas y medianas fuimos más rápidos con el agente. En la única tarea grande fuimos más lentos. **Son pocas tareas: esto describe lo que pasó, no prueba que el agente sea la causa.**"

### 12 · Lo demás · Ana Sofía · 20 s
"Las pruebas ocultas fallaron igual o menos con el agente. Pero cuando otra IA calificó a ciegas nuestras explicaciones, la comprensión fue de 3 sobre 5, con y sin agente, y en el trío bajó a 2. Y nos habíamos calificado 1,6 puntos más alto de lo que de verdad entendíamos."

### 13 · Bitácora · Juan José · 20 s
"Registramos cada respuesta del agente: de 29, aceptamos 24. Lo más común fue aceptar después de pedirle que se explicara. Solo una traía un error real, y no lo vimos nosotros: lo atrapó una prueba oculta."

### 14 · Tres fallos · Juan José · 25 s
1. "Supuso algo que el enunciado no decía y lo aceptamos."
2. "Cuando no pudo leer las pruebas ocultas, intentó leerlas por la consola. Lo bloqueamos."
3. "Se salió de su tarea: leyó otras tareas y una solución ya hecha."

### 15 · Riesgos · Juan José · 15 s
"Lo que cambiaríamos: darle solo los archivos de la tarea, pedirle sus supuestos antes del código y escribir al menos una prueba nuestra en cada tarea."

### 16 · Demo en vivo · conduce y navega · 4:30
Seguir `16112026_02_Guia_Demo_v2.md`. Lo que se va diciendo:
- "Esta es t20, duplicar una nota. Creemos que nos va a tomar __ minutos."
- Navegante: "Antes de abrir el agente, escribimos cómo lo haríamos."
- Conductor pega el prompt: "El agente es el navegante: solo propone."
- Leer lo que propone y **decidir en voz alta**: "Lo aceptamos porque… / Lo corregimos porque…"
- Correr las pruebas: "Pasan las visibles. Ahora las ocultas, que el agente nunca vio."
- Mostrar el tablero.
- Si algo falla: "Tenemos el video de respaldo" y lo ponen sin perder tiempo.

---

## CIERRE

### 17 · La frase · Ana Sofía · 20 s
"Lo que nos dijo el tema sobre nuestro proyecto: el valor del pair programming no era escribir más rápido, era que dos personas entendieran el código. El agente no hace eso solo; hay que exigirlo con puntos de control."

### 18 · Dos preguntas para el curso · Juan José · 20 s
Leerlas y **esperar respuestas**:
1. "Si un agente escribe el código y ustedes lo aceptan porque pasa las pruebas, ¿de quién es la responsabilidad cuando falla?"
2. "¿Qué prefieren: un compañero que va más lento pero aprende con ustedes, o un agente rápido que mañana no recuerda nada?"

### 19 · Declaración de uso de IA · los dos
Dejarla en pantalla durante las preguntas. Si les preguntan: "Claude Code nos ayudó a construir el caso, organizar los datos y armar los documentos; nosotros programamos y medimos todo, decidimos cada respuesta del agente y revisamos cada documento. Ningún número está escrito a mano."

---

## Preguntas que les pueden hacer (y una respuesta corta)

- **¿Por qué tan pocas tareas?** "Por tiempo hicimos 13. Por eso no afirmamos causas: describimos lo que pasó y lo comprobamos con la revisión a ciegas."
- **¿El agente fue mejor o peor?** "Más rápido en tareas pequeñas, no en la grande; los errores, iguales; la comprensión, igual de baja con y sin agente. Lo que sí vimos es que aceptamos casi todo."
- **¿Por qué la tríada (E3) salió más baja?** "Con dos personas y un agente, cada uno confió en que el otro o el agente revisaba. Es una hipótesis: con 2 tareas no lo podemos asegurar."
- **¿Cómo saben que no se inventaron los datos?** "Cada número sale de la bitácora: cronómetros, commits, videos y las conversaciones exportadas. Y el codewalk lo recalificó otra IA a ciegas."
- **¿Qué cambiarían?** "Pedirle al agente sus supuestos antes del código, darle solo los archivos de la tarea y escribir una prueba propia en cada tarea."
