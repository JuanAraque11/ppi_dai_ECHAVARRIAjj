import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import streamlit as st

import geopandas as gpd

url = "https://raw.githubusercontent.com/JuanAraque11/ppi_dai_ECHAVARRIAjj/main/Un_mundo_en_tu_plato/Datos/restaurantes.csv"

# Cargar el dataset a partir de la ruta establecida
datos = gpd.read_file(url, sep=",")

# Convertir las columnas de latitud y longitud a tipo numérico
datos['Latitude'] = pd.to_numeric(datos['Latitude'])
datos['Longitude'] = pd.to_numeric(datos['Longitude'])
datos['Price range'] = pd.to_numeric(datos['Price range'])
datos['Aggregate rating'] = pd.to_numeric(datos['Aggregate rating'])
datos['Votes'] = pd.to_numeric(datos['Votes'])
datos['Restaurant Name'] = datos['Restaurant Name'].astype('string')
datos['Address'] = datos['Address'].astype('string')

NewDelhi = datos[datos['City'] == 'New Delhi']
Gurgaon = datos[datos['City'] == 'Gurgaon']
Noida = datos[datos['City'] == 'Noida']
Faridabad = datos[datos['City'] == 'Faridabad']
Ghaziabad = datos[datos['City'] == 'Ghaziabad']


def elegir_restaurantes():
    """ 
    Muestra una interfaz de usuario para elegir una una ciudad.

    Args: None

    Returns: None
    """

    st.title("Elegir ciudad para ver restaurantes.")
    seleccion_ciudad = st.selectbox("Selecciona la ciudad:", ['New Delhi','Gurgaon', 'Noida', 'Faridabad', 'Ghaziabad'])
    st.write(NewDelhi[['Restaurant Name', 'City', 'Address', 'Votes']])
    if st.button("Buscar"):
        hallar_restaurantes = datos[datos['City'] == seleccion_ciudad]
