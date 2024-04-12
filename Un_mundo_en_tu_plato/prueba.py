import streamlit as st

# Título y autor
st.title("Un mundo en tu plato")
st.write('''¡Emprende un viaje culinario alrededor del mundo sin salir de casa!
Descubre recetas auténticas de cada rincón del planeta, desde la vibrante cocina mexicana hasta los exóticos sabores tailandeses.

Explora una amplia variedad de platos, desde clásicos familiares hasta innovadoras creaciones de chefs galardonados.

Aprende a preparar platos deliciosos con instrucciones detalladas paso a paso y videos explicativos.

Conoce los ingredientes de cada receta, su origen y sus propiedades nutricionales.

Personaliza tu experiencia con filtros avanzados que te permiten buscar recetas por región, tipo de cocina, ingredientes y preferencias dietéticas.

Guarda tus recetas favoritas para acceder a ellas fácilmente más tarde.

Comparte tus descubrimientos culinarios con amigos y familiares en las redes sociales. ''')

# Inicializamos la sesión para mantener los datos de usuario entre sesiones
if 'registered_users' not in st.session_state:
    st.session_state.registered_users = {}

# Función para iniciar sesión
def login():
    st.subheader("Iniciar sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if username in st.session_state.registered_users:
            if st.session_state.registered_users[username] == password:
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
        if new_username in st.session_state.registered_users:
            st.error("El usuario ya existe. Por favor, elige otro.")
        else:
            st.session_state.registered_users[new_username] = new_password
            st.success("Usuario registrado exitosamente. Por favor, inicia sesión.")

# Función para mostrar usuarios registrados
def show_registered_users():
    st.subheader("Usuarios registrados")
    st.write(list(st.session_state.registered_users.keys()))

# Página principal
def main():
    st.write("Bienvenidos a mi app")
    if not login():
        register()
    if st.button("Ver lista de usuarios"):
        show_registered_users()

if __name__ == "__main__":
    main()
