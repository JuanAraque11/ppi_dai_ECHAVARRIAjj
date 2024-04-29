import streamlit as st
from register import registered_users

def login_user():
    """
    Iniciar sesión de usuario.

    Args: None'

    Returns:  True si el inicio de sesión fue exitoso, False en caso contrario.
    """
    st.subheader("Iniciar sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if username in registered_users:
            if registered_users[username] == password:
                st.success("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(username))  
                actual = crear_usuario(username, password)  
                return True, actual
            else:
                st.error("Contraseña incorrecta")
        else:
            st.error("Usuario no registrado")
    return False, None


def crear_usuario(userna, passwo):
    user = Usuario(userna, passwo)
    return user