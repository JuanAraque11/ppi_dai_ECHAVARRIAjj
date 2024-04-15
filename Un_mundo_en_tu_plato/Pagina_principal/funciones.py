import streamlit as st
import numpy as np

def mostrar_inicio():
    st.write("Bienvenido al Inicio")
    st.write("Aquí encontrarás información sobre las funciones de la página:")
    st.write("- Guardar Recetas: Permite a los usuarios guardar nuevas recetas en la base de datos.")
    st.write("- Consultar Información de los Platos: Proporciona información detallada sobre los platos disponibles.")
    st.write("- Ver Distribuciones Estadísticas: Muestra distribuciones estadísticas sobre los platos.")


# Diccionario de recetas con ingredientes por porción
recetas = {
    "Tacos al Pastor": {"Carne de cerdo": 100, "Piña": 50, "Cebolla": 30, "Cilantro": 10, "Tortillas de maíz": 2},
    "Pizza Margarita": {"Masa de pizza": 200, "Tomate": 100, "Mozzarella": 150, "Albahaca": 5},
    "Pad Thai": {"Fideos de arroz": 100, "Tofu": 50, "Huevo": 30, "Brotes de soja": 20, "Cacahuetes": 10, "Salsa de tamarindo": 50}
}

def calcular_ingredientes(plato, num_personas):
    ingredientes = recetas.get(plato, {})
    cantidad_por_porcion = np.array(list(ingredientes.values()))
    cantidad_total = cantidad_por_porcion * num_personas
    return dict(zip(ingredientes.keys(), cantidad_total))

# Título de la página
st.title("Calculadora de Ingredientes")

# Solicitar información al usuario
plato = st.selectbox("Selecciona un plato:", list(recetas.keys()))
num_personas = st.number_input("Número de personas que van a comer:", min_value=1, value=1)

# Calcular ingredientes y mostrar resultado
if st.button("Calcular"):
    cantidad_ingredientes = calcular_ingredientes(plato, num_personas)
    st.write("Cantidad de Ingredientes Necesarios:")
    for ingrediente, cantidad in cantidad_ingredientes.items():
        st.write(f"- {ingrediente}: {cantidad} gramos")