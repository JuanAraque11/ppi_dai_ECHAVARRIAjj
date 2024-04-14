import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título de la opción
st.title("Opción 1: Distribución Geográfica y Popularidad de Platos")

# Generar datos de ejemplo
paises = ['México', 'Italia', 'Tailandia', 'India', 'Japón']
popularidad = np.random.randint(100, 1000, size=len(paises))

# Crear gráfico de barras
fig, ax = plt.subplots()
ax.bar(paises, popularidad)
ax.set_ylabel('Popularidad')
ax.set_title('Distribución Geográfica y Popularidad de Platos')
plt.xticks(rotation=45)

# Mostrar gráfico interactivo
st.pyplot(fig)
