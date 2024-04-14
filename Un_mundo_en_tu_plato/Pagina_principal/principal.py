import streamlit as st
import info
import login
import recetas
import register

# Menú desplegable para elegir entre iniciar sesión y registrar usuario
opcion = st.sidebar.selectbox("Menú:", ["Inicio", "Iniciar sesión", "Registrarse", "Buscar Recetas"])

# Función para buscar recetas por nombre y país
def buscar_recetas(recetas, termino_busqueda):
    # Filtrar recetas por nombre o país
    recetas_filtradas = [receta for receta in recetas if termino_busqueda.lower() in receta.get_nombre().lower() or termino_busqueda.lower() in receta.get_pais().lower()]
    return recetas_filtradas

# Función principal
def main():

    # Creación
    comida = recetas.crear_recetas()

    if opcion == "Iniciar sesión":
        if not login.login_user():
            st.info("Por favor, inicie sesión.")
        else:
            # Redirigir al usuario a un enlace externo después de iniciar sesión
            st.markdown("[Ir al enlace](https://www.youtube.com/watch?v=FusIKjztap8&ab_channel=TheBeatlesVEVO)")
    elif opcion == "Registrarse":
        register.register_user()
        if st.button("Ver lista de usuarios"):
            register.show_registered_users()
    elif opcion == "Inicio":
        info.info2()
    elif opcion == "Buscar Recetas":
        termino_busqueda = st.sidebar.text_input("Buscar recetas por nombre o país:")
        recetas_filtradas = buscar_recetas(comida, termino_busqueda)
        if recetas_filtradas:
            st.subheader("Recetas encontradas:")
            recetas.imprimir_recetas(recetas_filtradas)
        else:
            st.subheader("No se encontraron recetas para el término de búsqueda.")

    info.info1()


if __name__ == "__main__":
    main()
