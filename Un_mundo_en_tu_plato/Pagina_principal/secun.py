import streamlit as st
import funciones

# Título de la página
st.title("Contenido")

# Menú de opciones desplegables
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Información", "Guardar Recetas", "Consultar Información de los Platos", "Distribuciones Estadísticas"])

# Mostrar contenido según la opción seleccionada
if opcion == "Información":
    st.write("Este es el contenido de la Opción 1.")
    funciones.mostrar_inicio()
elif opcion == "Guardar Recetas":
    st.write("En proceso...")
elif opcion == "Consultar Información de los Platos":
    # Título de la página
    st.title("Calculadora de Ingredientes")

    # Solicitar información al usuario
    plato = st.selectbox("Selecciona un plato:", list(funciones.recetas.keys()))
    num_personas = st.number_input("Número de personas que van a comer:", min_value=1, value=1)

    # Calcular ingredientes y mostrar resultado
    if st.button("Calcular"):
        cantidad_ingredientes = funciones.calcular_ingredientes(plato, num_personas)
        st.write("Cantidad de Ingredientes Necesarios:")
        for ingrediente, cantidad in cantidad_ingredientes.items():
            st.write(f"- {ingrediente}: {cantidad} gramos")
elif opcion == "Distribuciones Estadísticas":
    st.write("")