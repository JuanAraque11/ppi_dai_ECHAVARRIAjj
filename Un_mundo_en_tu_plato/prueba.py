import streamlit as st

# Título y autor
st.title("Un mundo en tu plato")
st.write("Autor: Esta app fue elaborada por Juan Jos")

# Registro de usuarios (inicialmente vacío)
registered_users = {}

# Función para iniciar sesión
def login():
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


# Función para registrar usuario
def register():
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


# Página principal
def main():
    st.write("Bienvenidos a mi app")
    if not login():
        register()

if __name__ == "__main__":
    main()
