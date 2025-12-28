import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ace_tools_open as tools

def eda_null(df: pd.DataFrame) -> pd.DataFrame:
    null_counts = df.isnull().sum()
    null_percentages = (null_counts / len(df)) * 100
    # mostrar null_percentages con 2 decimales
    null_percentages = null_percentages.round(2)
    missing_data = pd.DataFrame({
        'Valores nulos': null_counts,
        'Porcentaje (%)': null_percentages
    })
    return missing_data

def normalize_name(name: str) -> str:
    """Pasa a minúsculas y reemplaza espacios por guion bajo, colapsando guiones repetidos."""
    name = name.strip().lower().replace(' ', '_')
    name = re.sub(r'_+', '_', name)
    return name

def fechas_notime(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte columnas que inician con 'Fecha' a tipo fecha con formato 'dd-mm-yyyy' sin el tiempo."""
    for col in df.columns:
        if col.startswith('Fecha'):
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.date
    return df

def todate(s: pd.Series) -> pd.Series:
    '''Convierte una serie de tipo datetime a solo fecha (date) sin la parte de tiempo.'''
    return pd.to_datetime(s, errors='coerce').dt.date

def tointeger(series: pd.Series) -> pd.Series:
    '''Convierte una serie a tipo numérico entero (Int64) si contiene valores no NaN.'''
    if series.notna().any():
        nonnull = pd.to_numeric(series.dropna(), errors='coerce').astype(float)
        frac = (nonnull % 1).abs()
        if (frac < 1e-8).all():
            return pd.to_numeric(series, errors='coerce').astype('Int64')
        else:
            return pd.to_numeric(series, errors='coerce').round().astype('Int64')
    return series

def decimal_round(series: pd.Series, decimals=2) -> pd.Series:
    """Redondea un valor decimal al número especificado de decimales."""
    # if series.notna().any():
    #     return series.apply(lambda x: float(Decimal(x).quantize(Decimal('1.' + '0' * decimals), rounding=ROUND_HALF_UP)) if pd.notna(x) else x)
    # return series
    factor = 10 ** decimals
    return series.apply(lambda x: round(x * factor) / factor if pd.notna(x) else x)

def eda_full(df):
    """
    Docstring para eda_full
    
    :param df: Descripción
    """

    # Asegurar el formato de fechas
    for col in ["Fecha_promesa", "Fecha_Escritura", "Fecha pactada"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Variables numéricas y categóricas
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include='object').columns

    # Resumen de valores nulos
    null_counts = df.isnull().sum()
    null_percentages = (null_counts / len(df)) * 100
    missing_data = pd.DataFrame({
        'Valores nulos': null_counts,
        'Porcentaje (%)': null_percentages
    })
    tools.display_dataframe_to_user(name="Resumen de Valores Nulos", dataframe=missing_data)

    # Verificar duplicados
    print(f"Cantidad de filas duplicadas: {df.duplicated().sum()}")

    # Matriz de correlación
    correlation_matrix = df[num_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Matriz de Correlación entre Variables Numéricas")
    plt.tight_layout()
    plt.show()

    # Distribuciones de variables numéricas
    for col in num_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f"Distribución de: {col}")
        plt.xlabel(col)
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.show()

    # Distribuciones de variables categóricas (Top 10)
    for col in cat_cols:
        top_categories = df[col].value_counts().nlargest(10)
        plt.figure(figsize=(6, 4))
        sns.barplot(x=top_categories.values, y=top_categories.index)
        plt.title(f"Frecuencia de categorías en: {col}")
        plt.xlabel("Frecuencia")
        plt.ylabel(col)
        plt.tight_layout()
        plt.show()

    # Outliers por variable numérica (IQR)
    outliers_summary = {}
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
        outliers_summary[col] = {
            "Cantidad de outliers": outliers.shape[0],
            "Porcentaje": (outliers.shape[0] / df.shape[0]) * 100
        }

    outliers_df = pd.DataFrame(outliers_summary).T
    tools.display_dataframe_to_user(name="Resumen de Outliers por Variable Numérica", dataframe=outliers_df)

    # Agrupación por Estado_Contable si existe
    if 'Estado_Contable' in df.columns:
        grouped_estado = df.groupby("Estado_Contable")[num_cols].agg(["mean", "median", "count", "std"])
        tools.display_dataframe_to_user(name="Resumen por Estado Contable", dataframe=grouped_estado)

