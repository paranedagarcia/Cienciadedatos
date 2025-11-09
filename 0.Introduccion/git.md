# Git / GitHub — Manual completo (resumen práctico)

## Introducción
Git es un sistema de control de versiones distribuido para gestionar cambios en código y archivos. GitHub es una plataforma que hospeda repositorios Git y facilita colaboración mediante ramas, pull requests y revisión de código.

## Conceptos clave
- Repositorio (repo): carpeta con historial Git.
- Commit: captura puntual del estado del repo.
- Branch (rama): línea paralela de desarrollo.
- Remote: repositorio remoto (ej. GitHub).
- Push / Pull: enviar/traer commits a/de un remote.
- Merge / Rebase: integrar cambios entre ramas.

La documentación oficial de Git: https://git-scm.com/book/es/v2
---

## Inicializar un nuevo repositorio local
1. Crea carpeta o ve a la carpeta del proyecto:
    ```bash
    mkdir mi-proyecto
    cd mi-proyecto
    ```
2. Inicializa Git:
    ```bash
    git init
    ```
3. Añade archivos y haz el primer commit:
    ```bash
    echo "# Mi proyecto" > README.md
    git add .
    git commit -m "Inicio: añadir README"
    ```

---

## Crear un repositorio en GitHub (opciones)
Opción A — Interfaz web:
- Entra a github.com → Nuevo repositorio → especifica nombre, visibilidad y crea.
- Tras crear, GitHub muestra instrucciones para conectar el repo local.

Opción B — CLI `gh` (GitHub CLI):
```bash
gh repo create usuario/mi-proyecto --public --source=. --remote=origin --push
```
(Ajusta visibilidad y opciones según necesidad.)

---

## Conectar un repo local a GitHub y subir (pasos comunes)
1. Añade remote (si no lo hizo `gh`):
    ```bash
    git remote add origin https://github.com/usuario/mi-proyecto.git
    ```
2. Configura rama principal (si es necesario):
    ```bash
    git branch -M main
    ```
3. Empuja al remoto por primera vez:
    ```bash
    git push -u origin main
    ```
4. Para cambios posteriores:
    ```bash
    git add .
    git commit -m "Mensaje claro y conciso"
    git push
    ```

---

## Clonar un repositorio existente
```bash
git clone https://github.com/usuario/mi-proyecto.git
# o vía SSH
git clone git@github.com:usuario/mi-proyecto.git
```

---

## Flujo de trabajo típico (colaboración)
1. Actualizar copia local:
    ```bash
    git fetch origin
    git pull origin main
    ```
2. Crear y moverte a una rama nueva:
    ```bash
    git checkout -b feature/nueva-funcionalidad
    # o
    git switch -c feature/nueva-funcionalidad
    ```
3. Trabajar, commitear y pushear la rama:
    ```bash
    git add .
    git commit -m "feat: descripción de la funcionalidad"
    git push -u origin feature/nueva-funcionalidad
    ```
4. Abrir Pull Request (PR) en GitHub para revisión.
5. Después de revisión, merge a main (puede hacerse en GitHub o localmente).

---

## Gestionar ramas (branch)

![Ramas en Git](https://git-scm.com/book/be/v2/images/remote-branches-1.png)
- Listar ramas locales:
  ```bash
  git branch
  ```
- Listar ramas remotas:
  ```bash
  git branch -r
  ```
- Crear rama:
  ```bash
  git branch nombre-rama
  git checkout nombre-rama
  # o en un paso:
  git checkout -b nombre-rama
  ```
- Cambiar de rama:
  ```bash
  git checkout main
  # o
  git switch main
  ```
- Borrar rama local:
  ```bash
  git branch -d nombre-rama   # seguro (rechaza si no está mergeada)
  git branch -D nombre-rama   # forzar borrado
  ```
- Borrar rama remota:
  ```bash
  git push origin --delete nombre-rama
  ```
- Traer y sincronizar ramas remotas:
  ```bash
  git fetch
  git pull origin nombre-rama
  ```

---

## Integrar cambios entre ramas
- Merge (fusión):
  ```bash
  git checkout main
  git pull origin main
  git merge feature/nombre
  # resolver conflictos si aparecen, luego:
  git add .
  git commit
  git push
  ```
- Rebase (reaplicar commits sobre otra base):
  ```bash
  git checkout feature/nombre
  git fetch origin
  git rebase origin/main
  # resolver conflictos si aparecen, luego:
  git push --force-with-lease
  ```
Nota: usar rebase con precaución en commits ya compartidos.

---

## Manejo de conflictos
1. Al encontrar conflicto, Git marca archivos con <<<<<<<.
2. Edita, resuelve diferencias, guarda.
3. Añade los archivos resueltos:
    ```bash
    git add archivo_resuelto
    git rebase --continue   # si estabas haciendo rebase
    # o
    git commit              # si estabas haciendo merge y falta commit
    ```
4. Continúa el flujo (push, etc.).

---

## Buenas prácticas
- Mensajes de commit claros: tipo(scope): descripción breve. Ej.: feat(auth): añadir login
- Commits pequeños y atómicos.
- Usar .gitignore para evitar subir archivos binarios, credenciales o dependencias.
- Mantener main/main branch protegida: usar PRs, revisiones y CI antes de merge.
- Rebase interactivo para limpiar historial antes de integrar (en ramas locales).
- Evitar forzar push en ramas compartidas; si imprescindible, usar --force-with-lease.

Ejemplo básico de .gitignore:
```
node_modules/
.env
.DS_Store
*.log
```

---

## Comandos útiles adicionales
- Estado actual:
  ```bash
  git status
  ```
- Historial:
  ```bash
  git log --oneline --graph --decorate --all
  ```
- Ver diferencias:
  ```bash
  git diff                # cambios no staged
  git diff --staged       # cambios staged
  ```
- Recuperar archivo de un commit anterior:
  ```bash
  git checkout <commit> -- ruta/al/archivo
  ```
- Renombrar rama local:
  ```bash
  git branch -m viejo-nombre nuevo-nombre
  git push origin :viejo-nombre nuevo-nombre
  git push -u origin nuevo-nombre
  ```

---

## Resumen rápido — comandos esenciales
- Crear local: git init
- Clonar: git clone <url>
- Añadir: git add .
- Commit: git commit -m "mensaje"
- Añadir remote: git remote add origin <url>
- Push inicial: git push -u origin main
- Crear rama: git checkout -b rama
- Push rama: git push -u origin rama
- Merge: git merge rama
- Borrar rama remota: git push origin --delete rama

---



