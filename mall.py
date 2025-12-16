
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


st.set_page_config(page_title="Segmentación de Clientes (Mall) – Clustering", layout="wide")

st.title("🛍️ Segmentación de Clientes – Mall Customers")
st.caption("Clustering jerárquico (Income + Spending) + comparación K-Means + perfilado + asignación de nuevos clientes + RFM (simulado).")

# ---------- Helpers ----------
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def make_scaler_fit(X: pd.DataFrame) -> StandardScaler:
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler

def plot_scatter_clusters(df: pd.DataFrame, cluster_col: str):
    fig, ax = plt.subplots(figsize=(7, 5))
    clusters = sorted(df[cluster_col].unique())
    for c in clusters:
        sub = df[df[cluster_col] == c]
        ax.scatter(sub["Annual Income (k$)"], sub["Spending Score (1-100)"], label=f"Cluster {c}", alpha=0.85)
    ax.set_xlabel("Annual Income (k$)")
    ax.set_ylabel("Spending Score (1-100)")
    ax.set_title(f"Scatter – {cluster_col}")
    ax.legend()
    st.pyplot(fig)

def plot_dendrogram(Z):
    fig, ax = plt.subplots(figsize=(10, 5))
    dendrogram(Z, ax=ax, no_labels=True, color_threshold=None)
    ax.set_title("Dendrograma – Clusterización Jerárquica (Ward)")
    ax.set_xlabel("Clientes")
    ax.set_ylabel("Distancia")
    st.pyplot(fig)

def plot_box_by_cluster(df: pd.DataFrame, y: str, cluster_col: str, title: str):
    # Simple matplotlib boxplot by group
    fig, ax = plt.subplots(figsize=(7, 4.5))
    clusters = sorted(df[cluster_col].unique())
    data = [df.loc[df[cluster_col] == c, y].values for c in clusters]
    ax.boxplot(data, labels=[str(c) for c in clusters], showmeans=True)
    ax.set_xlabel("Cluster")
    ax.set_ylabel(y)
    ax.set_title(title)
    st.pyplot(fig)

def plot_gender_counts(df: pd.DataFrame, cluster_col: str):
    if "Genre" not in df.columns:
        st.info("La columna 'Genre' no existe en el dataset cargado.")
        return
    # bar chart counts by cluster and gender
    ct = pd.crosstab(df[cluster_col], df["Genre"])
    fig, ax = plt.subplots(figsize=(7, 4.5))
    x = np.arange(len(ct.index))
    width = 0.35
    cols = list(ct.columns)
    if len(cols) == 1:
        ax.bar(x, ct[cols[0]].values, width=0.6)
        ax.set_xticks(x)
        ax.set_xticklabels([str(i) for i in ct.index])
        ax.set_title("Distribución de Género por Cluster")
        ax.set_xlabel("Cluster")
        ax.set_ylabel("N° clientes")
    else:
        ax.bar(x - width/2, ct[cols[0]].values, width=width, label=str(cols[0]))
        ax.bar(x + width/2, ct[cols[1]].values, width=width, label=str(cols[1]))
        ax.set_xticks(x)
        ax.set_xticklabels([str(i) for i in ct.index])
        ax.set_title("Distribución de Género por Cluster")
        ax.set_xlabel("Cluster")
        ax.set_ylabel("N° clientes")
        ax.legend()
    st.pyplot(fig)

def plot_silhouette_curve(X_scaled: np.ndarray, k_min: int, k_max: int, random_state: int = 42):
    ks = list(range(k_min, k_max + 1))
    scores = []
    for k in ks:
        km = KMeans(n_clusters=k, random_state=random_state, n_init="auto")
        labels = km.fit_predict(X_scaled)
        scores.append(silhouette_score(X_scaled, labels))
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(ks, scores, marker="o")
    ax.set_xlabel("k")
    ax.set_ylabel("Silhouette Score")
    ax.set_title("Selección de k (Silhouette) – K-Means")
    st.pyplot(fig)
    return pd.DataFrame({"k": ks, "silhouette": scores})

def plot_feature_importance(feature_names, importances):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    order = np.argsort(importances)
    ax.barh(np.array(feature_names)[order], np.array(importances)[order])
    ax.set_title("Importancia de Variables (RandomForest)")
    st.pyplot(fig)


# ---------- Sidebar controls ----------
st.sidebar.header("⚙️ Configuración")

data_path = st.sidebar.text_input("Ruta del CSV", value="Mall_Customers.csv", help="Por defecto busca el archivo en el mismo directorio.")
n_clusters = st.sidebar.slider("N° clusters (Jerárquico y K-Means)", min_value=2, max_value=8, value=5, step=1)

show_dendro = st.sidebar.checkbox("Mostrar dendrograma", value=True)
show_kmeans = st.sidebar.checkbox("Comparar con K-Means", value=True)
show_external_validation = st.sidebar.checkbox("Validación externa (Age/Genre)", value=True)
show_predictor = st.sidebar.checkbox("Modelo para asignar clusters a nuevos clientes", value=True)
show_rfm = st.sidebar.checkbox("Segmentación RFM (simulada)", value=True)

st.sidebar.divider()
st.sidebar.subheader("🧪 Ajustes de simulación RFM")
rfm_seed = st.sidebar.number_input("Seed", min_value=0, max_value=10_000, value=42, step=1)
rfm_recency_max = st.sidebar.slider("Recency máx.", 30, 365, 100)
rfm_freq_max = st.sidebar.slider("Frequency máx.", 5, 100, 20)

# ---------- Load data ----------
try:
    df = load_data(data_path)
except Exception as e:
    st.error(f"No pude cargar el archivo '{data_path}'. Error: {e}")
    st.stop()

required_cols = {"Annual Income (k$)", "Spending Score (1-100)"}
missing = required_cols - set(df.columns)
if missing:
    st.error(f"Faltan columnas requeridas: {missing}")
    st.stop()

st.write("### Vista rápida del dataset")
st.dataframe(df.head(15), use_container_width=True)

# ---------- Core clustering (Hierarchical) ----------
X = df[["Annual Income (k$)", "Spending Score (1-100)"]].copy()
scaler = make_scaler_fit(X)
X_scaled = scaler.transform(X)

Z = linkage(X_scaled, method="ward")
df = df.copy()
df["Cluster_H"] = fcluster(Z, t=n_clusters, criterion="maxclust")

c1, c2 = st.columns([1, 1])
with c1:
    st.write("## 1) Clusterización Jerárquica")
    st.write(f"**Corte configurado:** {n_clusters} clusters")
    if show_dendro:
        plot_dendrogram(Z)
    plot_scatter_clusters(df, "Cluster_H")

with c2:
    st.write("## 2) Perfilado automático (Jerárquico)")
    agg = {
        "Annual Income (k$)": "mean",
        "Spending Score (1-100)": "mean",
    }
    if "Age" in df.columns:
        agg["Age"] = "mean"
    if "CustomerID" in df.columns:
        agg["CustomerID"] = "count"
    profile = df.groupby("Cluster_H").agg(agg).rename(columns={"CustomerID": "N_Clientes"})
    st.dataframe(profile.round(2), use_container_width=True)

    st.write("**Interpretación rápida (reglas simples):**")
    # Heurística simple para etiquetar clusters por centroides
    tmp = profile.copy()
    inc = tmp["Annual Income (k$)"]
    sp = tmp["Spending Score (1-100)"]
    inc_q = inc.quantile([0.33, 0.66]).values
    sp_q = sp.quantile([0.33, 0.66]).values

    def bucket(v, q):
        if v <= q[0]: return "Bajo"
        if v <= q[1]: return "Medio"
        return "Alto"

    labels = []
    for idx, row in tmp.iterrows():
        inc_b = bucket(row["Annual Income (k$)"], inc_q)
        sp_b = bucket(row["Spending Score (1-100)"], sp_q)
        if inc_b == "Alto" and sp_b == "Alto":
            lab = "Premium (alto ingreso, alto gasto)"
        elif inc_b == "Alto" and sp_b == "Bajo":
            lab = "Potencial no explotado (alto ingreso, bajo gasto)"
        elif inc_b == "Bajo" and sp_b == "Alto":
            lab = "Impulsivo (bajo ingreso, alto gasto)"
        elif inc_b == "Bajo" and sp_b == "Bajo":
            lab = "Bajo valor (bajo ingreso, bajo gasto)"
        else:
            lab = "Cliente promedio / mixto"
        labels.append(lab)

    label_df = pd.DataFrame({"Cluster_H": tmp.index, "Etiqueta sugerida": labels})
    st.dataframe(label_df, use_container_width=True)

# ---------- KMeans comparison ----------
if show_kmeans:
    st.write("---")
    st.write("## 3) Comparación con K-Means")
    left, right = st.columns([1, 1])

    with left:
        st.write("### 3.1 Silhouette para elegir k")
        sil_df = plot_silhouette_curve(X_scaled, k_min=2, k_max=8, random_state=42)
        st.dataframe(sil_df, use_container_width=True)

    with right:
        st.write("### 3.2 K-Means con k configurado")
        km = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
        df["Cluster_KM"] = km.fit_predict(X_scaled)
        # para comparar con jerárquico, hacemos 1..k en vez de 0..k-1
        df["Cluster_KM"] = df["Cluster_KM"] + 1
        plot_scatter_clusters(df, "Cluster_KM")

        km_profile = df.groupby("Cluster_KM")[["Annual Income (k$)", "Spending Score (1-100)"]].mean()
        st.write("Centroides promedio (K-Means):")
        st.dataframe(km_profile.round(2), use_container_width=True)

        st.write("Tabla cruzada (Jerárquico vs K-Means):")
        st.dataframe(pd.crosstab(df["Cluster_H"], df["Cluster_KM"]), use_container_width=True)

# ---------- External validation ----------
if show_external_validation:
    st.write("---")
    st.write("## 4) Validación externa (Age y Genre)")
    cols = st.columns([1, 1])
    with cols[0]:
        if "Age" in df.columns:
            plot_box_by_cluster(df, y="Age", cluster_col="Cluster_H", title="Distribución de Edad por Cluster (Jerárquico)")
        else:
            st.info("El dataset no contiene 'Age'.")
    with cols[1]:
        if "Genre" in df.columns:
            plot_gender_counts(df, "Cluster_H")
        else:
            st.info("El dataset no contiene 'Genre'.")

# ---------- Predictor for new customers ----------
if show_predictor:
    st.write("---")
    st.write("## 5) Modelo para asignar clusters a nuevos clientes (operacionalización)")
    st.caption("Entrenamos un modelo supervisado para predecir el **cluster jerárquico** usando Age + Income + Spending (si 'Age' existe).")

    feature_cols = ["Annual Income (k$)", "Spending Score (1-100)"]
    if "Age" in df.columns:
        feature_cols = ["Age"] + feature_cols

    X_sup = df[feature_cols].copy()
    y_sup = df["Cluster_H"].copy()

    scaler_sup = StandardScaler()
    X_sup_scaled = scaler_sup.fit_transform(X_sup)

    X_train, X_test, y_train, y_test = train_test_split(
        X_sup_scaled, y_sup, test_size=0.25, random_state=42, stratify=y_sup
    )

    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.write("### 5.1 Métricas (test set)")
        st.text(classification_report(y_test, y_pred))
        st.write("Matriz de confusión:")
        st.dataframe(pd.DataFrame(confusion_matrix(y_test, y_pred)), use_container_width=True)

    with c2:
        st.write("### 5.2 Importancia de variables")
        plot_feature_importance(feature_cols, clf.feature_importances_)

    st.write("### 5.3 Asignación de un nuevo cliente")
    form_cols = st.columns([1, 1, 1])
    with form_cols[0]:
        age_val = st.slider("Age", 15, 80, 35) if "Age" in df.columns else None
    with form_cols[1]:
        income_val = st.slider("Annual Income (k$)", int(df["Annual Income (k$)"].min()), int(df["Annual Income (k$)"].max()), int(df["Annual Income (k$)"].median()))
    with form_cols[2]:
        spend_val = st.slider("Spending Score (1-100)", int(df["Spending Score (1-100)"].min()), int(df["Spending Score (1-100)"].max()), int(df["Spending Score (1-100)"].median()))

    new_row = {"Annual Income (k$)": income_val, "Spending Score (1-100)": spend_val}
    if age_val is not None:
        new_row["Age"] = age_val

    new_df = pd.DataFrame([new_row])[feature_cols]
    new_scaled = scaler_sup.transform(new_df)
    pred_cluster = int(clf.predict(new_scaled)[0])
    st.success(f"✅ Cluster jerárquico predicho para el nuevo cliente: **{pred_cluster}**")

# ---------- RFM segmentation (simulated) ----------
if show_rfm:
    st.write("---")
    st.write("## 6) Segmentación RFM (simulada) + comparación")
    st.caption("El dataset no es transaccional. Para ilustrar el enfoque RFM, simulamos Recency/Frequency y definimos Monetary como ingreso×spending.")

    np.random.seed(int(rfm_seed))
    df_rfm = df.copy()
    df_rfm["Recency"] = np.random.randint(1, int(rfm_recency_max) + 1, size=len(df_rfm))
    df_rfm["Frequency"] = np.random.randint(1, int(rfm_freq_max) + 1, size=len(df_rfm))
    df_rfm["Monetary"] = df_rfm["Spending Score (1-100)"] * df_rfm["Annual Income (k$)"]

    rfm = df_rfm[["Recency", "Frequency", "Monetary"]].copy()
    rfm_scaled = StandardScaler().fit_transform(rfm)

    km_rfm = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
    df_rfm["Cluster_RFM"] = km_rfm.fit_predict(rfm_scaled) + 1

    rfm_profile = df_rfm.groupby("Cluster_RFM")[["Recency", "Frequency", "Monetary"]].mean().round(2)
    st.write("Perfil promedio RFM (simulado):")
    st.dataframe(rfm_profile, use_container_width=True)

    st.write("Tabla cruzada: Jerárquico vs RFM (simulado)")
    st.dataframe(pd.crosstab(df_rfm["Cluster_H"], df_rfm["Cluster_RFM"]), use_container_width=True)

    # Simple plot Monetary vs Recency colored by RFM cluster
    fig, ax = plt.subplots(figsize=(7, 5))
    for c in sorted(df_rfm["Cluster_RFM"].unique()):
        sub = df_rfm[df_rfm["Cluster_RFM"] == c]
        ax.scatter(sub["Recency"], sub["Monetary"], label=f"RFM {c}", alpha=0.8)
    ax.set_xlabel("Recency (días) – simulado")
    ax.set_ylabel("Monetary – simulado")
    ax.set_title("RFM (simulado): Monetary vs Recency")
    ax.legend()
    st.pyplot(fig)

st.write("---")
st.write("### ✅ Recomendaciones por segmento (guía rápida)")
st.markdown(
"""
- **Premium (alto ingreso, alto gasto):** VIP, exclusividad, fidelización prioritaria.  
- **Potencial (alto ingreso, bajo gasto):** activación, personalización, bundles/cross-sell.  
- **Impulsivo (bajo ingreso, alto gasto):** promociones acotadas, control de descuentos, foco en alta rotación.  
- **Bajo valor (bajo ingreso, bajo gasto):** automatizar marketing, baja inversión.  
- **Mixto/Promedio:** campañas masivas, programas de puntos y upsell gradual.
"""
)

st.info("Tip: Si cambias el número de clusters en la barra lateral, el pipeline recalcula todo automáticamente.")
