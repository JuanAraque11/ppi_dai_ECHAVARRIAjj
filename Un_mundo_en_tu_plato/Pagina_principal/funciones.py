import streamlit as st
import numpy as np
from recetas import data, reemplazar_nulos
# import geopandas as gpd
# import matplotlib.pyplot as plt


def mostrar_inicio():
    """
    Muestra el contenido de la página de inicio.

    Args: None

    Returns: None
    """
    st.write("Bienvenido al Inicio")
    st.write("Aquí encontrarás información sobre las funciones de la página:")
    st.write("- Guardar Recetas: Permite a los usuarios guardar nuevas recetas\
    en la base de datos.")
    st.write("- Consultar Información de los Platos: Proporciona información\
    detallada sobre los platos disponibles.")
    st.write("- Ver Distribuciones Estadísticas: Muestra distribuciones\
    estadísticas sobre los platos.")


""" def mostrar_grafico_popularidad(platos, popularidad):
    # Crear gráfico de barras
    plt.bar(platos, popularidad)
    plt.xlabel("Plato")
    plt.ylabel("Popularidad")
    plt.title("Popularidad de Platos")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Mostrar gráfico en Streamlit
    st.pyplot() """


"""def visualizar_distribucion_recetas(recetas):
    # Cargar datos geoespaciales de los países
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Contar la cantidad de recetas por país
    recetas_por_pais = {}
    for receta, pais in recetas.items():
        recetas_por_pais[pais] = recetas_por_pais.get(pais, 0) + 1

    # Agregar los datos de recetas por país al dataframe de los países
    world['recetas'] = world['name'].map(recetas_por_pais)

    # Crear un mapa interactivo
    st.title("Distribución Geográfica de Recetas")

    # Mostrar el mapa interactivo
    fig, ax = plt.subplots(figsize=(10, 6))
    world.plot(column='recetas', cmap='YlGn', linewidth=0.8, ax=ax, 
    edgecolor='0.8', legend=True)
    ax.set_title('Distribución Geográfica de Recetas')
    ax.set_axis_off()

    # Mostrar el mapa en Streamlit
    st.pyplot(fig) """


# Ejemplo de uso:
recetas = {
    "Tacos al Pastor": "México",
    "Pizza Margarita": "Italia",
    "Pad Thai": "Tailandia",

    # Agregar más recetas con sus países de origen
}

# Ejemplo de uso:
platos = ["Tacos al Pastor", "Pizza Margarita", "Pad Thai"]
popularidad = [100, 75, 50]

# Diccionario de recetas con ingredientes por porción
recetas = {
    "Tacos al Pastor": {"Carne de cerdo": 100, "Piña": 50, "Cebolla": 30,
                        "Cilantro": 10, "Tortillas de maíz": 2},
    "Pizza Margarita": {"Masa de pizza": 200, "Tomate": 100, "Mozzarella": 150,
                        "Albahaca": 5},
    "Pad Thai": {"Fideos de arroz": 100, "Tofu": 50, "Huevo": 30, "Brotes de\
                       soja": 20, "Cacahuetes": 10, "Salsa de tamarindo": 50}
}

# Datos de ejemplo de recetas
datos_recetas = {
    "Nombre": ["Tacos al Pastor", "Pizza Margarita", "Pad Thai"],
    "Calorías": [300, 250, 400],
    "Grasas (g)": [15, 10, 20],
    "Proteínas (g)": [20, 15, 25]
}

def calcular_ingredientes(plato, num_personas):
    ingredientes = recetas.get(plato, {})
    cantidad_por_porcion = np.array(list(ingredientes.values()))
    cantidad_total = cantidad_por_porcion * num_personas
    return dict(zip(ingredientes.keys(), cantidad_total))


def elegir_receta():

    reemplazar_nulos()

    st.title("Elegir recetas")
    seleccion_tipo = st.sidebar.selectbox("Selecciona el tipo de receta:", ["Acompañamiento", "Cena", "Cumpleaños", "Desayuno", "Entrante", "Merienda", "Plato principal", "Postre"])
    seleccion_difi = st.sidebar.selectbox("Selecciona la dificultad de la receta:", ["muy bajo", "bajo", "medio", "alto", "muy alto"])

    if st.button("Buscar"):
        recetas = data[(data['Tipo'] == seleccion_tipo) & (data['Dificultad'] == seleccion_difi)]
        if recetas.empty:
            st.write("No se encontraron recetas.")
        else:
            st.write("Recetas encontradas:")
            st.write(recetas[['Nombre', 'Tipo', 'Ingredientes', 'Dificultad','Link_receta']])