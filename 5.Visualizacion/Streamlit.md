# Streamlit
¡Bienvenido al módulo de Streamlit! Aquí aprenderás a crear aplicaciones web interactivas y visualizaciones de datos utilizando la biblioteca Streamlit. Este módulo te guiará a través de los conceptos básicos de Streamlit, desde la instalación hasta la creación de aplicaciones completas que pueden ser compartidas fácilmente con otros. Al finalizar este módulo, estarás equipado con las habilidades necesarias para desarrollar aplicaciones web dinámicas que faciliten la exploración y presentación de datos.
## Qué es streamlit
Streamlit es una biblioteca de Python de código abierto que permite a los desarrolladores crear aplicaciones web interactivas de manera rápida y sencilla. Está especialmente diseñada para científicos de datos y analistas que desean compartir sus análisis y visualizaciones de datos sin necesidad de conocimientos profundos en desarrollo web. Con Streamlit, puedes transformar scripts de Python en aplicaciones web funcionales con solo unas pocas líneas de código.
## Instalación de Streamlit
Para instalar Streamlit, puedes usar pip, el gestor de paquetes de Python. Abre tu terminal o línea de comandos y ejecuta el siguiente comando:
```bash
pip install streamlit
```
Una vez instalado, puedes verificar la instalación ejecutando:
```bash
streamlit hello
```
Esto abrirá una aplicación de demostración en tu navegador web, mostrando algunas de las capacidades de Streamlit.
## Crear tu primera aplicación con Streamlit
Para crear tu primera aplicación con Streamlit, sigue estos pasos:
1. Crea un nuevo archivo Python, por ejemplo, `app.py`.
2. Abre el archivo en tu editor de texto favorito y agrega el siguiente código:
```python
import streamlit as st

st.title("¡Hola, Streamlit!")
st.write("Esta es mi primera aplicación con Streamlit.")
```
3. Guarda el archivo y vuelve a tu terminal. Navega hasta el directorio donde guardaste `app.py` y ejecuta el siguiente comando:
```bash
streamlit run app.py
``` 
4. Esto abrirá tu aplicación en el navegador web, donde verás el título y el texto que agregaste.
## Componentes básicos de Streamlit
Streamlit ofrece una variedad de componentes que puedes usar para construir tu aplicación. Aquí hay algunos ejemplos básicos:
- **Texto y Títulos:** Usa `st.title()`, `st.header()`, y `st.write()` para agregar texto y títulos.
- **Entradas de Usuario:** Usa `st.text_input()`, `st.slider()`, y `st.selectbox()` para recibir entradas de usuario.
- **Visualizaciones:** Usa `st.line_chart()`, `st.bar_chart()`, y `st.map()` para mostrar gráficos y mapas.
- **Interactividad:** Usa `st.button()` y `st.checkbox()` para agregar interactividad a tu aplicación.
## Despliegue de aplicaciones Streamlit
Una vez que hayas creado tu aplicación, puedes desplegarla para que otros la puedan usar. Streamlit ofrece una plataforma llamada Streamlit Cloud que facilita el despliegue de aplicaciones. También puedes desplegar tu aplicación en servicios como Heroku, AWS, o Google Cloud.
Para desplegar en Streamlit Cloud, sigue estos pasos:
1. Crea una cuenta en [Streamlit Cloud](https://streamlit.io/cloud).
2. Conecta tu repositorio de GitHub que contiene tu aplicación Streamlit.
3. Sigue las instrucciones para desplegar tu aplicación directamente desde el repositorio.
¡Felicidades! Ahora tienes una comprensión básica de Streamlit y cómo crear aplicaciones web interactivas. Explora más funciones y componentes en la [documentación oficial de Streamlit](https://docs.streamlit.io/) para seguir mejorando tus habilidades.

# Despliegue de streamlit en Azure
Para desplegar una aplicación Streamlit en Microsoft Azure, puedes seguir estos pasos básicos. Asegúrate de tener una cuenta de Azure y haber instalado la [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) en tu máquina local.
## Paso 1: Preparar tu aplicación Streamlit
Asegúrate de que tu aplicación Streamlit esté lista para ser desplegada. Crea un archivo `requirements.txt` en el mismo directorio que tu aplicación para listar todas las dependencias necesarias. Por ejemplo:
```streamlit
pandas
numpy
streamlit
```
## Paso 2: Crear un recurso de App Service en Azure
1. Inicia sesión en tu cuenta de Azure desde la terminal:
```bash
az login
```
2. Crea un grupo de recursos:
```bash
az group create --name myResourceGroup --location eastus
```
3. Crea un plan de App Service:
```bash
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux
```
4. Crea una aplicación web:
```bash
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name myStreamlitApp --runtime "PYTHON|3.8"
```
## Paso 3: Desplegar tu aplicación Streamlit
1. Instala la extensión de Azure App Service para despliegue:
```bash
az webapp deployment source config-local-git --name myStreamlitApp --resource-group myResourceGroup
```
2. Obtén la URL del repositorio Git proporcionada por Azure.
3. Agrega el repositorio remoto a tu proyecto local:
```bash
git remote add azure <URL_DEL_REPOSITORIO_GIT>
```
4. Realiza un commit de tus cambios y empuja tu código al repositorio remoto de Azure:
```bash
git add .
git commit -m "Desplegando aplicación Streamlit"
git push azure master
```
## Paso 4: Configurar la aplicación Streamlit en Azure
1. Ve al portal de Azure y navega hasta tu aplicación web.
2. En la sección "Configuración", agrega una nueva configuración de aplicación con el nombre `WEBSITES_PORT` y el valor `8501` (el puerto predeterminado de Streamlit).
3. Guarda los cambios y reinicia la aplicación web.
## Paso 5: Acceder a la aplicación Streamlit
Después de que la aplicación se haya desplegado y reiniciado, puedes acceder a ella utilizando la URL proporcionada por Azure, que generalmente tiene el formato `https://<nombre_de_taplicación>.azurewebsites.net`.
Ahora has desplegado con éxito tu aplicación Streamlit en Microsoft Azure.

