import streamlit as st
import funciones
import pandas as pd

# Título de la página
st.title("Contenido")

# Menú de opciones desplegables
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Información", "Guardar Recetas", "Consultar Información de los Platos", "Distribuciones Estadísticas", "Carga tus recetas"])

# Mostrar contenido según la opción seleccionada
if opcion == "Información":
    st.write("Este es el contenido de la Opción 1.")
    funciones.mostrar_inicio()
elif opcion == "Guardar Recetas":
    st.write("En proceso...")
elif opcion == "Consultar Información de los Platos":
    # Título de la página
    st.title("Calculadora de Ingredientes")

    # Solicitar información al usuario
    plato = st.selectbox("Selecciona un plato:", list(funciones.recetas.keys()))
    num_personas = st.number_input("Número de personas que van a comer:", min_value=1, value=1)

    # Calcular ingredientes y mostrar resultado
    if st.button("Calcular"):
        cantidad_ingredientes = funciones.calcular_ingredientes(plato, num_personas)
        st.write("Cantidad de Ingredientes Necesarios:")
        for ingrediente, cantidad in cantidad_ingredientes.items():
            st.write(f"- {ingrediente}: {cantidad} gramos")
elif opcion == "Distribuciones Estadísticas":
    st.write("")
elif opcion == "Carga tus recetas":
    
    # Widget para cargar archivo CSV o Excel
    archivo = st.file_uploader("Cargar archivo de datos adicionales:", type=["csv", "xlsx"])

    # Si se carga un archivo, leer los datos y mostrarlos
    if archivo is not None:
        # Leer los datos del archivo
        if archivo.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":  # Excel
            df_datos_adicionales = pd.read_excel(archivo)
        else:  # CSV
            df_datos_adicionales = pd.read_csv(archivo)
        
        # Mostrar los datos cargados
        st.write("Datos adicionales cargados:")
        st.write(df_datos_adicionales)