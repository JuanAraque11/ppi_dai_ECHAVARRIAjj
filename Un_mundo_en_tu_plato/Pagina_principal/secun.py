import streamlit as st
import funciones
import pandas as pd
import recetas
#import scipy.stats as stats
#import matplotlib.pyplot as plt

# Menú de opciones desplegables
opcion = st.sidebar.selectbox("Selecciona una opción:", ["Información", "Guardar Recetas", "Consultar Información de los Platos", "Estadísticas de recetas", "Carga recetas", "Elegir recetas", "Distribuciones"])

def main():
    
    # Mostrar contenido según la opción seleccionada
    if opcion == "Información":
        # Título de la página
        st.title("Contenido")
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
    elif opcion == "Estadísticas de recetas":
        st.write("")
        # Crear DataFrame de Pandas con los datos de las recetas
        """df_recetas = pd.DataFrame(funciones.datos_recetas)

        # Calcular estadísticas descriptivas
        descripcion_calorias = stats.describe(df_recetas["Calorías"])
        descripcion_grasas = stats.describe(df_recetas["Grasas (g)"])
        descripcion_proteinas = stats.describe(df_recetas["Proteínas (g)"])

        # Mostrar estadísticas descriptivas
        st.title("Análisis de Ingredientes Nutricionales")
        st.write("Estadísticas de Calorías:")
        st.write(descripcion_calorias)
        st.write("Estadísticas de Grasas:")
        st.write(descripcion_grasas)
        st.write("Estadísticas de Proteínas:")
        st.write(descripcion_proteinas) """

    elif opcion == "Carga tus recetas":
        
        # Widget para cargar archivo CSV o Excel
        archivo = st.file_uploader("Cargar archivo con tus recetas:", type=["csv", "xlsx"])

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

    elif opcion == "Elegir recetas":
        funciones.elegir_receta()
        
    elif opcion == "Distribuciones":
        st.write("")
        # funciones.visualizar_distribucion_recetas(funciones.recetas)


if __name__ == "__main__":
    main()