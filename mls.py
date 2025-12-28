# integra_streamlit.py
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd
import numpy as np
from pathlib import Path
import re
import hashlib
import os
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from decimal import Decimal, ROUND_HALF_UP
import millify
from millify import millify, prettify
warnings.filterwarnings('ignore')
#from streamlit_pandas_profiling import st_profile_report


@st.cache_data
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
css_path = Path("./css/style.css")
local_css(css_path)

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Integración Cubit-Mobysuite",
    page_icon="📊",
    layout="wide"
)


decimales = st.session_state['decimales'] if 'decimales' in st.session_state else 2

# Crear directorios si no existen
data_path = Path('./data')


def load_dataset(file_path: Path) -> pd.DataFrame :
    """Carga un dataset desde la ruta especificada."""
    data_path = Path('./data')
    datasets = [f.name for f in data_path.glob('*') if f.is_file()]
    selected_dataset = st.selectbox("Selecciona un dataset:", datasets)
    full_path = data_path / selected_dataset
    df = pd.read_csv(full_path)
    return df




# ------------------------------------------------
# ------------------------------------------------
# Página 1: Inicio
# ------------------------------------------------
# ------------------------------------------------
def pagina_inicio():
    # st.title("📁 Sistema de Integración Cubit-Mobysuite")
    #st.markdown("---")
    
    #st.header("🏠 Bienvenido al Machine Learning supervisado")
    st.markdown(
        """
        Esta aplicación te permite realizar análisis de datos y comparar modelos de machine learning supervisado utilizando tus propios datasets.

        **Instrucciones:**
        1. Selecciona un dataset desde la carpeta `data/`.
        2. Elige la columna objetivo y las columnas predictoras.
        3. Selecciona el modelo de machine learning que deseas utilizar.
        4. Navega entre las páginas para analizar los datos y ver los resultados de comparación.

        ¡Comencemos!
        """
    )
    # muestra el dataset cargado
    st.subheader("Vista previa del dataset seleccionado:")
    if 'dataset_name' in st.session_state:
        dataset = st.session_state['dataset_name']
    else:
        st.warning("Por favor, selecciona un dataset en la barra lateral.")

    st.dataframe(dataset.head())
    
# ------------------------------------------------
# ------------------------------------------------
# Página 2: Análisis
# ------------------------------------------------
# ------------------------------------------------

def pagina_analisis():
    st.header("🔍 Análisis de Proyectos")
    
    
# ------------------------------------------------
# ------------------------------------------------
# Página 3: Resultado
# ------------------------------------------------
# ------------------------------------------------

def pagina_resultado():
    st.header("📈 Resultados de Comparación")
    
with st.sidebar:
    # Navegación en sidebar
    st.title("Aprendizaje supervisado")
    
    # crea un selectbox para seleccionar un dataset desde la carpeta '..data/'
    dataset = load_dataset(data_path)
    # si existe el dataset almacena en una session state el nombre del dataset
    if 'dataset_name' not in st.session_state:
        st.session_state['dataset_name'] = dataset


    # crea variable target con el nombre de la columna objetivo seleccionada por el usuario
    target_column = st.selectbox("Selecciona la columna objetivo:", 
                                 dataset.columns.tolist())
    st.session_state['target_column'] = target_column

    # selecciona las columnas predictoras desde la lista de columnas del dataset
    predictor_columns = st.multiselect("Selecciona las columnas predictoras:", 
                                       dataset.columns.tolist(), 
                                       default=[col for col in dataset.columns if col != target_column])
    st.session_state['predictor_columns'] = predictor_columns

    # crea un selectbox para elegir un modelo de machine learning supervisado
    model_type = st.selectbox("Selecciona el modelo de machine learning:", 
                              ["Regresión Lineal", 
                               "Árbol de Decisión", 
                               "Bosque Aleatorio", 
                               "Máquina de Soporte Vectorial"])    
    st.session_state['model_type'] = model_type


    # actualizar el datset en la session state
    st.session_state['dataset_name'] = dataset

    
    # boton para actualizar la pagina ypagina_inicio() cargar el dataset seleccionado
    if st.button("Cargar Dataset"):
        pagina_inicio()
        st.rerun()

st.subheader("Machine Learning supervisado")
# crea 5 tabs para la navegación entre páginas
tab1, tab2, tab3 = st.tabs(["Inicio", "Análisis", "Resultado"])
with tab1:
    pagina_inicio()
with tab2:
    pagina_analisis()
with tab3:
    pagina_resultado()


st.logo(image="images/streamlit-logo-primary-colormark-lighttext.png", 
        icon_image="images/streamlit-mark-color.png")


    