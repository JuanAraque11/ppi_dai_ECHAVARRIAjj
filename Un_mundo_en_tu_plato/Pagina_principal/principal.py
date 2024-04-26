import streamlit as st
import info
import login
import recetas
import register
from usuario import Usuario

# Menú desplegable para elegir entre iniciar sesión y registrar usuario
opcion = st.sidebar.selectbox("Menú:", ["Inicio", "Registrarse", "Actualizar contraseña", "Buscar recetas", "Receta al azar", "Buscar por valoración","Información y contacto"])

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

    # estado_politi = info.mostrar_ventana_emergente()

    # if estado_politi:

    if opcion == "Información y contacto":

        info.info1()
    elif opcion == "Registrarse":
        register.register_user()
        # if st.button("Ver lista de usuarios"):
            # register.show_registered_users()
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
        # Interfaz de usuario
        st.title("Buscar recetas por ingredientes")
        ingrediente_busqueda = st.text_input("Ingrese un ingrediente:")
        buscar_button = st.button("Buscar recetas")
        if buscar_button:
            recetas_encontradas = recetas.buscar_receta_por_ingrediente(ingrediente_busqueda)
            if recetas_encontradas.empty:
                st.write("No se encontraron recetas con ese ingrediente.")
            else:
                st.write("Recetas encontradas:")
                st.write(recetas_encontradas[['Nombre', 'Tiempo', 'Ingredientes', 'Link_receta']])

    # else:
        # st.stop()
    elif opcion == "Receta al azar":
        st.title("Receta al azar")
        recetas.mostrar_receta_aleatoria()

    elif opcion == "Buscar por valoración":
        # Ejemplo de uso
        # Suponiendo que 'data' es tu DataFrame de recetas
        st.title("Buscar por valoración")
        valoracion = st.number_input("Ingrese la valoración a buscar", min_value=0.0, max_value=5.0, step=0.1, value=3.0)
        opcion_buscar = st.radio("Selecciona una opción:", ['mayores', 'menores', 'iguales'])

        if st.button("Buscar"):
            recetas_valoradas = recetas.buscar_por_valoracion(valoracion, opcion_buscar)
            if recetas_valoradas.empty:
                st.write("No se encontraron recetas.")
            else:
                st.write("Recetas encontradas:")
                st.write(recetas_valoradas[['Nombre', 'Tiempo', 'Ingredientes', 'Valoracion','Link_receta']])



if __name__ == "__main__":
    main()
