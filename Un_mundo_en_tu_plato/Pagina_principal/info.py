import streamlit as st

def info1():
    # Título del apartado
    st.title("Información Importante")

    # Texto descriptivo
    st.write("Bienvenido a mi página web, Aquí encontrarás información relevante sobre mi servicio.")

    # Enlaces a secciones específicas
    st.write("Para obtener más detalles, visita las siguientes secciones:")
    st.markdown("- [Política de Privacidad](https://tuempresa.com/politica-de-privacidad)")
    st.markdown("- [Contacto](https://www.linkedin.com/in/juan-jose-echavarria-araque-a92286296)")

    # Botón para mostrar/ocultar política de privacidad
    if "show_privacy_policy" not in st.session_state:
        st.session_state.show_privacy_policy = False  # Establecer el estado inicial del botón
    
    if st.button("Política de Privacidad"):
        st.session_state.show_privacy_policy = not st.session_state.show_privacy_policy  # Alternar el estado del botón
    
    if st.session_state.show_privacy_policy:
        st.write("Aquí puedes escribir tu política de privacidad.")
    
    # Pie de página
    st.write("© 2024 Mi Empresa. Todos los derechos reservados.")

def info2():
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
