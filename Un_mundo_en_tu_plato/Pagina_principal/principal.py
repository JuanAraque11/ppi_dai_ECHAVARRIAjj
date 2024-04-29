import streamlit as st
import info
import login
import recetas
import register
# import streamlit_authenticator as stauth


# Función principal
def main():
    """
    Función principal del programa.

    Args: None

    Returns: None
    """

    info.terminos_condiciones()
    # Verificar si el usuario acepta los términos y condiciones
    aceptado = st.checkbox("Acepto los Términos y Condiciones")

    if aceptado:
        # Menú desplegable para elegir entre iniciar sesión y registrar usuario
        opcion = st.sidebar.selectbox("Menú:", ["Inicio", "Registrarse", "Actualizar contraseña", "Buscar recetas", "Receta al azar", "Buscar por valoración","Información y contacto"])


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

            st.title("Buscar por valoración")
            valoracion = st.number_input("Ingrese la valoración a buscar", min_value=1.0, max_value=5.0, step=0.1, value=3.0)
            opcion_buscar = st.radio("Selecciona una opción:", ['mayores', 'menores', 'iguales', 'sin valoración'])

            if st.button("Buscar"):
                recetas_valoradas = recetas.buscar_por_valoracion(valoracion, opcion_buscar)
                if recetas_valoradas.empty:
                    st.write("No se encontraron recetas.")
                else:
                    st.write("Recetas encontradas:")
                    st.write(recetas_valoradas[['Nombre', 'Tiempo', 'Ingredientes', 'Valoracion','Link_receta']])
    else:
        # Mostrar mensaje indicando que el usuario debe aceptar los términos y condiciones
        st.warning("Debe aceptar los Términos y Condiciones para utilizar la aplicación.")



if __name__ == "__main__":
    main()
