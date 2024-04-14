import streamlit as st
import info
import login
import register

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
    elif opcion == "Registrarse":
        register.register_user()
        if st.button("Ver lista de usuarios"):
            register.show_registered_users()
    elif opcion == "Inicio":
        info.info2()

    info.info1()


if __name__ == "__main__":
    main()
