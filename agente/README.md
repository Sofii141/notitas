# Cómo preparar Claude Code para los ciclos (no se usa en la línea base)

La spec v1 dice que el agente trabaja en una **copia del repo sin `tests/ocultas`** y que **no puede hacer commit ni push ni leer las ocultas**. Para cumplirlo:

1. Crear la copia de trabajo de la tarea, fuera de esta carpeta:
   ```bash
   git clone https://github.com/Sofii141/CAMEIA-lite.git notitas-agente
   cd notitas-agente
   rm -rf tests/ocultas
   mkdir .claude
   cp agente/settings.json .claude/settings.json
   ```
2. Abrir Claude Code **en esa carpeta** (`claude`) y anotar en la hoja *Sesiones* el modelo (`/model`) y la versión (`claude --version`).
3. Pegarle solo lo que dice la spec: el enunciado de la tarea en `TAREAS.md`, `src/notitas/tNN.py` y `tests/visibles/test_tNN.py`.
4. Cada propuesta del agente es una fila de la bitácora: aceptar, corregir o rechazar, con su razón.
5. Al declarar "terminado", **la persona** copia `tNN.py` al repo original, hace el commit y corre ahí las pruebas ocultas.

`settings.json` le niega a Claude Code: hacer commit, push o merge; leer `tests/ocultas`; editar las pruebas; leer `.env`; y salir de la carpeta.
