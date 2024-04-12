import streamlit as st

def login_user(registered_users):
    st.subheader("Iniciar sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if username in registered_users:
            if registered_users[username] == password:
                st.success("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(username))
                return True
            else:
                st.error("Contraseña incorrecta")
        else:
            st.error("Usuario no registrado")
    return False
