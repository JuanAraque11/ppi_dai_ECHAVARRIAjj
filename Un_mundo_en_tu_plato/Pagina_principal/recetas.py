import pandas as pd
import streamlit as st

# Guardar en la variable 'ruta' la url del dataset
ruta = "https://raw.githubusercontent.com/JuanAraque11/ppi_dai_ECHAVARRIAjj/main/Un_mundo_en_tu_plato/Datos/recetas.csv"

# Cargar el dataset a partir de la ruta establecida
data = pd.read_csv(ruta, delimiter="|")

def mostrar_receta_aleatoria():
    # Seleccionar una fila aleatoria del DataFrame
    aleatoria = st.button("Buscar una receta al azar")

    if aleatoria:
        receta_aleatoria = data.sample()

        # Mostrar la información de la receta aleatoria seleccionada
        st.write(f"Nombre: {receta_aleatoria['Nombre'].values[0]}")
        st.write(f"Tiempo: {receta_aleatoria['Tiempo'].values[0]}")
        st.write(f"Ingredientes: {receta_aleatoria['Ingredientes'].values[0]}")
        st.write(f"Link de la Receta: {receta_aleatoria['Link_receta'].values[0]}")


def reemplazar_nulos():
  # Reemplazar los nulos de la columna 'Ingredientes' con una cadena vacía
  data['Ingredientes'] = data['Ingredientes'].fillna('')


def buscar_receta_por_ingrediente(ingrediente):    
    
    reemplazar_nulos()

    recetas_filtradas = data[data['Ingredientes'].str.contains(ingrediente)]
    recetas_filtradas
    return recetas_filtradas