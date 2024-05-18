import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from recetas import data

def distri_categorias():
    """
    Muestra una gráfica de barras de las categorías de las recetas.

    Args: None

    Returns: None
    """
    
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Categoria', data=data, order=data['Categoria'].value_counts().index)
    plt.title('Distribución de Categorías')
    plt.xlabel('Frecuencia')
    plt.ylabel('Categoría')
    
    st.pyplot(plt)

    # Limpiar la figura para evitar problemas con gráficos futuros
    plt.clf()