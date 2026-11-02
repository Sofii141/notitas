# Cómo preparar el agente para los ciclos (no se usa en la línea base)

**Agente:** OpenCode con el modelo gratuito **DeepSeek V4.1 Flash**. Los dos usan exactamente el mismo modelo durante todo el ciclo.

La spec v1 dice que el agente trabaja en una **copia del repo sin `backend/tests/ocultas`** y que **no puede hacer commit, push ni leer las ocultas**. Para cumplirlo, en cada tarea:

1. Crear la copia de trabajo, fuera de esta carpeta:
   ```bash
   git clone https://github.com/Sofii141/notitas.git notitas-agente
   cd notitas-agente
   rm -rf backend/tests/ocultas
   cp agente/opencode.json opencode.json
   ```
2. Abrir OpenCode **en esa carpeta** (`opencode`), escribir `/models` y elegir **DeepSeek V4.1 Flash**. Anotar en la hoja *Sesiones* el nombre del modelo tal como aparece y la versión de OpenCode (`opencode --version`).
3. Darle solo lo que dice la spec: el enunciado de la tarea en `TAREAS.md`, `backend/notitas/tNN.py` y `backend/tests/visibles/test_tNN.py`.
4. Cada propuesta del agente es una fila de la bitácora: aceptar, corregir o rechazar, con su razón. `opencode.json` hace que **pida permiso** antes de editar un archivo o correr un comando: ese es el punto de control humano.
5. Al declarar "terminado", **la persona** copia `tNN.py` al repo original, hace el commit y corre ahí las pruebas ocultas.

`opencode.json` (sintaxis oficial: https://opencode.ai/docs/permissions/) le niega lo siguiente: leer `backend/tests/ocultas` y `.env`; editar las pruebas; hacer commit, push o merge; salir de la carpeta; y buscar en internet. Todo lo demás lo pregunta antes de hacerlo.

**Antes del ciclo 1:** hagan un piloto con una de las 2 tareas de repuesto que dio el sorteo para comprobar que los permisos funcionan. Pídanle que lea `backend/tests/ocultas`: debe negarse. El piloto no cuenta en la medición.

**Privacidad:** los modelos gratuitos pueden guardar lo que se les envía. Notitas no tiene datos personales ni secretos, así que no hay problema; igual se menciona en el análisis de riesgos (confidencialidad).
