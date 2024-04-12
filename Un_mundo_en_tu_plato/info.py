import streamlit as st

def info():
    # Título del apartado
    st.title("Información Importante")

    # Texto descriptivo
    st.write("¡Bienvenidos a nuestra página web! Aquí encontrarás información relevante sobre nuestro servicio.")

    # Enlaces a secciones específicas
    st.write("Para obtener más detalles, visita las siguientes secciones:")
    st.markdown("- [Política de Privacidad](https://tuempresa.com/politica-de-privacidad)")
    st.markdown("- [Contacto](www.linkedin.com/in/juan-jose-echavarria-araque-a92286296)")

    # Pie de página
    st.write("© 2024 Mi Empresa. Todos los derechos reservados.")
