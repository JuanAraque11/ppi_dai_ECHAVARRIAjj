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

# Página principal
def main():
    if not login.login_user():
        register.register_user()
    else:
        # Una vez iniciada la sesión, mostrar otro tipo de contenido
        st.write("¡Bienvenido! Aquí hay contenido especial para usuarios autenticados.")
        # Por ejemplo, puedes mostrar el contenido de otro archivo o módulo
        info()

if __name__ == "__main__":
    main()
