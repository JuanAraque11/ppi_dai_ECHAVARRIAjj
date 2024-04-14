import numpy as np
import streamlit as st

class Receta:
    def __init__(self, nombre, pais, ingredientes, pasos):
        self.nombre = nombre
        self.pais = pais
        self.ingredientes = ingredientes
        self.pasos = pasos

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_pais(self):
        return self.pais

    def get_ingredientes(self):
        return self.ingredientes

    def get_pasos(self):
        return self.pasos

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_pais(self, pais):
        self.pais = pais

    def set_ingredientes(self, ingredientes):
        self.ingredientes = ingredientes

    def set_pasos(self, pasos):
        self.pasos = pasos

# Función para crear recetas
def crear_recetas():
    # Creamos tres instancias de la clase Receta
    receta1 = Receta("Tacos al pastor", "México", ["Carne de cerdo", "Piña", "Cebolla", "Cilantro", "Tortillas de maíz"], ["Marinar la carne", "Asar la carne en trompo", "Servir en tortillas con piña y cebolla"])
    receta2 = Receta("Pizza Margarita", "Italia", ["Masa de pizza", "Tomate", "Mozzarella", "Albahaca"], ["Extender la masa de pizza", "Agregar salsa de tomate y mozzarella", "Hornear y agregar albahaca fresca"])
    receta3 = Receta("Pad Thai", "Tailandia", ["Fideos de arroz", "Tofu", "Huevo", "Brotes de soja", "Cacahuetes", "Salsa de tamarindo"], ["Saltear tofu y huevo", "Agregar fideos y salsa de tamarindo", "Incorporar brotes de soja y cacahuetes"])

    # Convertir las recetas a un arreglo de NumPy
    recetas = np.empty((3, 4), dtype=object)
    recetas[0, :] = [receta1.nombre, receta1.pais, ", ".join(receta1.ingredientes), "\n".join(receta1.pasos)]
    recetas[1, :] = [receta2.nombre, receta2.pais, ", ".join(receta2.ingredientes), "\n".join(receta2.pasos)]
    recetas[2, :] = [receta3.nombre, receta3.pais, ", ".join(receta3.ingredientes), "\n".join(receta3.pasos)]

    # Devolvemos las recetas creadas como un arreglo de NumPy
    return recetas

# Función para imprimir las recetas encontradas
def imprimir_recetas(recetas):
    if not recetas:
        st.write("No se encontraron recetas para el término de búsqueda.")
    else:
        st.write("Recetas encontradas:")
        for i, receta in enumerate(recetas, start=1):
            st.write(f"Receta {i}: {receta.get_nombre()} ({receta.get_pais()})")
            st.write("Ingredientes:", ", ".join(receta.get_ingredientes()))
            st.write("Pasos:")
            for j, paso in enumerate(receta.get_pasos(), start=1):
                st.write(f"  {j}. {paso}")
            st.write()