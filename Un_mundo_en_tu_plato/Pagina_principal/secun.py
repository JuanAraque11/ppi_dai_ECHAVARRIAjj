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
    st.write("Este es el contenido de la Opción 2.")
elif opcion == "Consultar Información de los Platos":
    st.write("Este es el contenido de la Opción 3.")
elif opcion == "Distribuciones Estadísticas":
    st.write("")