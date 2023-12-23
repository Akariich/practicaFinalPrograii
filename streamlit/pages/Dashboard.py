import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg
import requests
import seaborn as sns

@st.cache_data
def load_data(url: str):
    df = pd.read_csv('/home/pablo/repositorios/repos/practicaFinalPrograii/fastapi/videojuegos_ventas.csv', sep=',')
    return df

# Personalización de la interfaz
def info_box (texto, color=None):
    st.markdown(f'<div style = "background-color:#B8F393;opacity:70%"><p style="text-align:center;color:#8cb6fa;font-size:30px;">{texto}</p></div>', unsafe_allow_html=True)

# Configuración de matplotlib
matplotlib.use("agg")
st.set_option('deprecation.showPyplotGlobalUse', False)

df_merged = load_data('http://fastapi:8000/retrieve_data')

sns.set_palette("pastel")

# Cajas con información general del dashboard
st.header("Información general")

columns1 = st.columns(3)
col1 = columns1[0]
col2 = columns1[1]

columns2 = st.columns(3)
col3 = columns2[0]
col4 = columns2[1]

with col1:
    col1.subheader('Videojuegos')
    num_videojuegos = df_merged['name'].nunique()
    info_box(num_videojuegos)

with col2:
    col2.subheader('Plataformas')
    num_platform = df_merged['platform'].nunique()
    info_box(num_platform)

with col3:
    col3.subheader('Géneros')
    num_genre = df_merged['genre'].nunique()
    info_box(num_genre)

with col4:
    col4.subheader('Millones de ventas')
    globalsales = df_merged['global_sales'].astype(float).sum()
    info_box(f"${globalsales:.2f}")

# Configuración de los gráficos
# Primero voy a colocar los gráficos de ventas en cada región con el paso de los años.
st.header("Análisis de ventas a lo largo de los años.")

fig_global_sales = px.bar(df_merged, x='year', y='global_sales', title='Ventas Globales a lo largo de los años.')
st.plotly_chart(fig_global_sales, use_container_width=True)

# Gráfico de ventas europeas a lo largo de los años
fig_eu_sales = px.bar(df_merged, x='year', y='eu_sales', title='Ventas Europeas a lo largo de los años.')
st.plotly_chart(fig_eu_sales, use_container_width=True)

# Gráfico de ventas japonesas a lo largo de los años
fig_jp_sales = px.bar(df_merged, x='year', y='jp_sales', title='Ventas Japonesas a lo largo de los años.')
st.plotly_chart(fig_jp_sales, use_container_width=True)

# Y ahora veremos las comparaciones de las ventas entre plataformas
st.header("Análisis de ventas por plataforma.")

fig_global_sales = px.bar(df_merged, x='platform', y='global_sales', title='Ventas globales por plataforma.')
st.plotly_chart(fig_global_sales, use_container_width=True)

# Gráfico de ventas europeas por plataformas
fig_eu_sales = px.bar(df_merged, x='platform', y='eu_sales', title='Ventas Europeas por cada plataforma.')
st.plotly_chart(fig_eu_sales, use_container_width=True)

# Gráfico de ventas japonesas por plataforma
fig_jp_sales = px.bar(df_merged, x='platform', y='jp_sales', title='Ventas Japonesas por plataforma.')
st.plotly_chart(fig_jp_sales, use_container_width=True)
