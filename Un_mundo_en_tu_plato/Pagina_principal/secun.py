import streamlit as st
import funciones

# Título de la página
st.title("Contenido")

# Menú de opciones desplegables
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Opción 1", "Opción 2", "Opción 3"])

# Mostrar contenido según la opción seleccionada
if opcion == "Opción 1":
    st.write("Este es el contenido de la Opción 1.")
    funciones.mostrar_inicio()
elif opcion == "Opción 2":
    st.write("Este es el contenido de la Opción 2.")
elif opcion == "Opción 3":
    st.write("Este es el contenido de la Opción 3.")
