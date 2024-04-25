import streamlit as st
import info
import login
import recetas
import register
from usuario import Usuario

# Menú desplegable para elegir entre iniciar sesión y registrar usuario
opcion = st.sidebar.selectbox("Menú:", ["Inicio", "Iniciar sesión",
                    "Registrarse", "Actualizar contraseña","Buscar recetas"])

# Función para buscar recetas por nombre y país
def buscar_recetas(recetas, termino_busqueda):
    """
    Busca recetas por nombre o país en una lista de recetas.

    Args: recetas (list): Una lista de recetas., termino_busqueda (str): El termino de búsqueda.

    Returns: Una lista de recetas que coincidan con el termino de búsqueda.
    """
    recetas_encontradas = []
    for receta in recetas:

        # Convertimos los atributos de la receta a minúsculas para una búsqueda
        # insensible a mayúsculas y minúsculas
        nombre = receta.nombre.lower()
        pais = receta.pais.lower()

        # Verificamos si el término de búsqueda está en el nombre o país de 
        # la receta
        if termino_busqueda.lower() in nombre or termino_busqueda.lower() in pais:
            
            # Si encontramos una coincidencia, agregamos la receta a la lista
            recetas_encontradas.append(receta)
    return recetas_encontradas


# Función principal
def main():
    """
    Función principal del programa.

    Args: None

    Returns: None
    """

    # Creación
    comidas = recetas.crear_recetas()

    if opcion == "Iniciar sesión":
        estado, en_sesion = login.login_user()
        if not estado:
            st.info("Por favor, inicie sesión.")
        else:
            
            # Redirigir al usuario a un enlace externo después de iniciar sesión
            st.markdown("[Ir al enlace](https://unmundoentuplato-funciones.streamlit.app/)")
            st.write("La sesion pertenece a ", en_sesion.get_username())
    elif opcion == "Registrarse":
        register.register_user()
        if st.button("Ver lista de usuarios"):
            register.show_registered_users()
    elif opcion == "Inicio":
        info.info2()
        estado, en_sesion = login.login_user()
        if not estado:
            st.info("Por favor, inicie sesión.")
        else:
            
            # Redirigir al usuario a un enlace externo después de iniciar sesión
            st.markdown("[Ir al enlace](https://unmundoentuplato-funciones.streamlit.app/)")
            st.write("La sesion pertenece a ", en_sesion.get_username())
    elif opcion == "Actualizar contraseña":
        register.change_password()
    elif opcion == "Buscar recetas":
        termino_busqueda = st.sidebar.text_input("Buscar recetas por nombre o país:")
        recetas_filtradas = buscar_recetas(comidas, termino_busqueda)
        if recetas_filtradas:
            st.subheader("Recetas (Los países disponibles por el momento son Colombia, Italia, México y Tailandia)")
            if termino_busqueda:
                recetas.imprimir_recetas(recetas_filtradas)
            else:
                pass
        else:
            st.subheader("No se encontraron recetas para el término de búsqueda.")

    info.info1()


if __name__ == "__main__":
    main()
