import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import streamlit as st

import geopandas as gpd

url = "https://raw.githubusercontent.com/JuanAraque11/ppi_dai_ECHAVARRIAjj/main/Un_mundo_en_tu_plato/Datos/restaurantes.csv"

# Cargar el dataset a partir de la ruta establecida
datos = gpd.read_file(url)

# Convertir las columnas de latitud y longitud a tipo numérico
datos['Latitude'] = pd.to_numeric(datos['Latitude'])
datos['Longitude'] = pd.to_numeric(datos['Longitude'])
datos['Price range'] = pd.to_numeric(datos['Price range'])
datos['Aggregate rating'] = pd.to_numeric(datos['Aggregate rating'])
datos['Votes'] = pd.to_numeric(datos['Votes'])

NewDelhi = datos[datos['City'] == 'New Delhi']


def elegir_restaurantes():
    """ 
    Muestra una interfaz de usuario para elegir una una ciudad.

    Args: None

    Returns: None
    """

    st.title("Elegir ciudad para ver restaurantes.")
    seleccion_ciudad = st.selectbox("Selecciona la ciudad:", ['New Delhi','Gurgaon', 'Noida', 'Faridabad', 'Ghaziabad '])
    st.write(NewDelhi.head(2))
    st.write(NewDelhi[['Restaurant Name', 'City', 'Address', 'Votes']])
    if st.button("Buscar"):
        hallar_restaurantes = datos[datos['City'] == seleccion_ciudad]
        if hallar_restaurantes.empty:
            st.write("No se encontraron recetas.")
        else:
            plt.figure(figsize=(16, 8))
            hallar_restaurantes.plot(kind='bar')
            plt.title('Distribución de la columna City')
            plt.xlabel('City')
            plt.ylabel('Frecuencia')
            plt.xticks(rotation=45)  # Rotar las etiquetas del eje x si son muchas o muy largas
            st.pyplot(plt)