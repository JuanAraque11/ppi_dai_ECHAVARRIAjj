import streamlit as st

def clear_page():
    st.empty()

button = st.button("Borrar página")

if button:
    clear_page()

# Agregar nuevo contenido después de borrar la página
new_content = st.write("Este es el nuevo contenido")
