import streamlit as st
# import graficos

# Título de la página
st.title("Contenido")

# Menú de opciones desplegables
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Opción 1", "Opción 2", "Opción 3"])

# Mostrar contenido según la opción seleccionada
if opcion == "Opción 1":
    st.write("Este es el contenido de la Opción 1.")
    #graficos.mostrar_opcion_1()
elif opcion == "Opción 2":
    st.write("Este es el contenido de la Opción 2.")
elif opcion == "Opción 3":
    st.write("Este es el contenido de la Opción 3.")
