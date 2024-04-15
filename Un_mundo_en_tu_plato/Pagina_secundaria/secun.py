import streamlit as st
# import graficos

# Título de la página
st.title("Contenido")

# Menú de opciones desplegables
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Opción 1", "Opción 2", "Opción 3"])

# Mostrar contenido según la opción seleccionada
if opcion == "Opción 1":
    st.write("Este es el contenido de la Opción 1.")
    #graficos.mostrar_opcion_1()
elif opcion == "Opción 2":
    st.write("Este es el contenido de la Opción 2.")
elif opcion == "Opción 3":
    st.write("Este es el contenido de la Opción 3.")

if st.button("Usuario"):
    # Desplegar menú de opciones
    option = st.selectbox("Selecciona una opción:", ["Actualizar Contraseña", "Ver Perfil"])
    
    # Actuar según la opción seleccionada
    if option == "Actualizar Contraseña":
        st.write("Opción seleccionada: Actualizar Contraseña")
        # Aquí puedes colocar el código para actualizar la contraseña
    elif option == "Ver Perfil":
        st.write("Opción seleccionada: Ver Perfil")
        # Aquí puedes colocar el código para ver el perfil del usuario