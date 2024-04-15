import streamlit as st
import numpy as np
#import matplotlib.pyplot as plt


def mostrar_inicio():
    st.write("Bienvenido al Inicio")
    st.write("Aquí encontrarás información sobre las funciones de la página:")
    st.write("- Guardar Recetas: Permite a los usuarios guardar nuevas recetas en la base de datos.")
    st.write("- Consultar Información de los Platos: Proporciona información detallada sobre los platos disponibles.")
    st.write("- Ver Distribuciones Estadísticas: Muestra distribuciones estadísticas sobre los platos.")

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

# Ejemplo de uso:
platos = ["Tacos al Pastor", "Pizza Margarita", "Pad Thai"]
popularidad = [100, 75, 50]
# Diccionario de recetas con ingredientes por porción
recetas = {
    "Tacos al Pastor": {"Carne de cerdo": 100, "Piña": 50, "Cebolla": 30, "Cilantro": 10, "Tortillas de maíz": 2},
    "Pizza Margarita": {"Masa de pizza": 200, "Tomate": 100, "Mozzarella": 150, "Albahaca": 5},
    "Pad Thai": {"Fideos de arroz": 100, "Tofu": 50, "Huevo": 30, "Brotes de soja": 20, "Cacahuetes": 10, "Salsa de tamarindo": 50}
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
