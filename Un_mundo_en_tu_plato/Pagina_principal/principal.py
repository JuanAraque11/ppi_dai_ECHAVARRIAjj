import streamlit as st
import info
import login
import register

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

# Menú desplegable para elegir entre iniciar sesión y registrar usuario
opcion = st.sidebar.selectbox("Menú:", ["Inicio", "Iniciar sesión", "Registrarse"])
# Función principal
def main():
    if opcion == "Iniciar sesión":
        if not login.login_user():
            st.info("Por favor, inicie sesión.")
        else:
            # Redirigir al usuario a un enlace externo después de iniciar sesión
            st.markdown("[Ir al enlace](https://www.youtube.com/watch?v=FusIKjztap8&ab_channel=TheBeatlesVEVO)")
    elif opcion == "Registrar usuario":
        register.register_user()
    elif opcion == "Inicio":
        info.info()

    if st.button("Ver lista de usuarios"):
        register.show_registered_users()
    info.info()


if __name__ == "__main__":
    main()
