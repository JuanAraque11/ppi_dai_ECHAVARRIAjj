import streamlit as st

registered_users = {}


def register_user(registered_users):
    st.subheader("Registro de usuario")
    new_username = st.text_input("Nuevo usuario")
    new_password = st.text_input("Nueva contraseña", type="password")
    if st.button("Registrarse"):
        if new_username in registered_users:
            st.error("El usuario ya existe. Por favor, elige otro.")
        else:
            registered_users[new_username] = new_password
            st.success("Usuario registrado exitosamente. Por favor, inicia sesión.")

# Función para mostrar usuarios registrados
def show_registered_users():
    st.subheader("Usuarios registrados")
    st.write(list(st.session_state.registered_users.keys()))