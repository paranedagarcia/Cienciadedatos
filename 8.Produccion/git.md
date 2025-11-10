# Git
Git es un sistema de control de versiones distribuido que permite a los desarrolladores rastrear cambios en el código fuente durante el desarrollo de software. Fue creado por Linus Torvalds en 2005 para gestionar el desarrollo del kernel de Linux. Git permite a múltiples desarrolladores trabajar en un proyecto simultáneamente, facilitando la colaboración y la gestión de diferentes versiones del código.

Git fue desarrollado por Linus Torvalds en 2005. Fue creado para gestionar el desarrollo del kernel de Linux, ya que las herramientas de control de versiones existentes en ese momento no cumplían con los requisitos del proyecto.
## Características principales de Git
1. **Distribuido**: Cada desarrollador tiene una copia completa del repositorio, lo que permite trabajar de manera independiente y sin conexión.
2. **Rendimiento**: Git está diseñado para ser rápido y eficiente, incluso con proyectos grandes.
3. **Ramas y fusiones**: Git facilita la creación y gestión de ramas, lo que permite a los desarrolladores trabajar en características o correcciones de errores de manera aislada antes de fusionarlas con la rama principal.
4. **Integridad de datos**: Git utiliza un sistema de hash SHA-1 para asegurar la integridad de los datos y rastrear los cambios en el código.
5. **Historial completo**: Git mantiene un historial completo de todos los cambios realizados en el código, lo que permite a los desarrolladores revertir a versiones anteriores si es necesario.




## Instalación de Git
### instalar en Mac OS
```bash
brew install git
```
### instalar en Windows
```bash
choco install git
```
### instalar en Linux (Debian/Ubuntu)
```bash
sudo apt-get install git
```
### instalar en Linux (Fedora)
```bash
sudo dnf install git
```
### instalar en Linux (Fedora)
```bash
sudo dnf install git
```
### instalar en Linux (Arch)
```bash
sudo pacman -S git
```
### Verificar instalación de Git
Independientemente del sistema operativo, para verificar que Git se haya instalado correctamente, puedes ejecutar el siguiente comando en la terminal:
```bash
git --version
```

## Comandos básicos de Git
- `git init`: Inicializa un nuevo repositorio Git en el directorio actual.
- `git add .`: Agrega todos los archivos nuevos y modificados al área de preparación (staging area).
- `git commit -m "Mensaje del commit"`: Crea un commit con los cambios en el área de preparación y un mensaje descriptivo.
- `git branch -M main`: Cambia el nombre de la rama actual a "main".
- `git remote add   origin <REMOTE_REPOSITORY_URL>`: Agrega un repositorio remoto llamado "origin".
- `git push -u origin main`: Sube los cambios a la rama "main" del repositorio remoto "origin".
- `git pull`: Descarga y fusiona los cambios desde el repositorio remoto a tu rama local.
- `git status`: Muestra el estado de los archivos en el repositorio.
- `git log`: Muestra el historial de commits del repositorio.

## Flujo de trabajo típico
1. Clona el repositorio remoto (si es necesario).
2. Realiza cambios en los archivos del proyecto.
3. Usa `git add .` para agregar los cambios al área de preparación.
4. Usa `git commit -m "Mensaje del commit"` para crear un commit con los cambios.
5. Usa `git push` para subir los cambios al repositorio remoto.

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <REMOTE_REPOSITORY_URL>
git push -u origin main

# para actualizar cambios
git add .
git commit -m "Update files"
git push
```

## Ramas en Git
Las ramas en Git permiten a los desarrolladores trabajar en diferentes características o correcciones de errores de manera aislada. Cada rama es una línea independiente de desarrollo que puede fusionarse con otras ramas cuando sea necesario.

![](https://git-scm.com/book/en/v2/images/two-branches.png)


### Crear una nueva rama 'testing' y trabajar en ella
```bash
git checkout -b testing
# hacer cambios en los archivos
git add .
git commit -m "Add testing feature"
git push -u origin testing
```
![](https://git-scm.com/book/en/v2/images/head-to-testing.png)

Se han realizado los cambios en la rama 'testing'
```bash
git commit -a -m 'Make a change'
```

![](https://git-scm.com/book/en/v2/images/advance-testing.png)

Se han verificado los cambios en la rama 'testing' y ahora esta rama 'testing' se encuentra más actualizada que la master y queremos por tanto que se fusione con 'master'. Para ello activamos la rama 'master'.

```bash
git checkout master
```
![](https://git-scm.com/book/en/v2/images/checkout-master.png)

Ahora el puntero HEAD está en la rama 'master' y todos los cambios que hagamos se aplicarán a esta rama 'master'. Las modificaciones de archivos que hemos hecho en la rama 'testing' no se ven reflejadas en la rama 'master' todavía.

Ahora fusionamos la rama 'testing' con la rama 'master'
```bash
git merge testing
```
![](https://git-scm.com/book/en/v2/images/merge-testing-into-master.png)

---
## Script para automatizar commits y push
```sh
#!/bin/sh
git add .
git commit -m "Update files"
git push
```


# Github
GitHub es una plataforma de alojamiento de código fuente y control de versiones que utiliza Git. Permite a los desarrolladores colaborar en proyectos, gestionar versiones de código y compartir su trabajo con la comunidad.
## Crear un repositorio en GitHub
1. Inicia sesión en tu cuenta de GitHub.
2. Haz clic en el botón "New" o "Nuevo" para crear un nuevo repositorio.
3. Proporciona un nombre para tu repositorio y una descripción opcional.
4. Elige si deseas que el repositorio sea público o privado.
5. Haz clic en "Create repository" o "Crear repositorio".
## Clonar un repositorio
```bash
git clone <REMOTE_REPOSITORY_URL>
```
