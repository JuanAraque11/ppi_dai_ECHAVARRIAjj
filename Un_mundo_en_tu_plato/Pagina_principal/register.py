import streamlit as st

registered_users = {}


def register_user():
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
    st.write(list(registered_users.keys()))


def change_password():
    user = st.text_input("Usuario:")
    contraseña_actual = st.text_input("Contraseña actual:", type="password")
    nueva_contraseña = st.text_input("Nueva contraseña:", type="password")

    if st.button("Actualizar"):
        # Aquí puedes colocar el código para verificar la contraseña actual y actualizarla
        st.success("¡Contraseña actualizada con éxito!")
