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
    almacen_recetas = []

    def agregar_receta(nombre, pais, ingredientes, pasos):
        receta = Receta(nombre, pais, ingredientes, pasos)
        almacen_recetas.append(receta)

    agregar_receta("Tacos al pastor", "México", ["Carne de cerdo", "Piña", "Cebolla", "Cilantro", "Tortillas de maíz"], ["Marinar la carne", "Asar la carne en trompo", "Servir en tortillas con piña y cebolla"])
    agregar_receta("Pizza Margarita", "Italia", ["Masa de pizza", "Tomate", "Mozzarella", "Albahaca"], ["Extender la masa de pizza", "Agregar salsa de tomate y mozzarella", "Hornear y agregar albahaca fresca"])
    agregar_receta("Pad Thai", "Tailandia", ["Fideos de arroz", "Tofu", "Huevo", "Brotes de soja", "Cacahuetes", "Salsa de tamarindo"], ["Saltear tofu y huevo", "Agregar fideos y salsa de tamarindo", "Incorporar brotes de soja y cacahuetes"])
    agregar_receta("Pasta Carbonara", "Italia", ["Espaguetis", "Bacon", "Huevo", "Queso Parmesano", "Pimienta negra"], ["Cocinar la pasta al dente", "Freír el bacon", "Mezclar los huevos con el queso", "Agregar la mezcla de huevo y queso a la pasta", "Añadir el bacon y la pimienta"])
    agregar_receta("Risotto de Champiñones", "Italia", ["Arroz Arborio", "Champiñones", "Cebolla", "Caldo de pollo", "Vino blanco", "Queso Parmesano"], ["Sofreír la cebolla y los champiñones", "Añadir el arroz y el vino blanco", "Cocinar añadiendo caldo de pollo poco a poco", "Agregar queso parmesano al final"])
    agregar_receta("Pesto Genovese", "Italia", ["Albahaca", "Piñones", "Ajo", "Queso Parmesano", "Aceite de oliva", "Sal", "Pimienta"], ["Triturar la albahaca, los piñones y el ajo", "Agregar el queso parmesano", "Añadir aceite de oliva hasta obtener la consistencia deseada", "Sazonar con sal y pimienta"])
    agregar_receta("Tiramisú", "Italia", ["Café", "Licor de café", "Huevos", "Azúcar", "Mascarpone", "Bizcochos de soletilla", "Cacao en polvo"], ["Mojar los bizcochos en café y licor", "Hacer una crema con los huevos, el azúcar y el mascarpone", "Montar el postre alternando capas de bizcocho y crema", "Refrigerar y espolvorear con cacao en polvo antes de servir"])
    agregar_receta("Pizza Margarita", "Italia", ["Masa de pizza", "Tomate", "Mozzarella", "Albahaca"], ["Extender la masa de pizza", "Agregar salsa de tomate y mozzarella", "Hornear y agregar albahaca fresca"])

    return almacen_recetas
    # Convertir las recetas a un arreglo de NumPy
   
''' recetas = np.empty((3, 4), dtype=object)
    recetas[0, :] = [receta1.nombre, receta1.pais, ", ".join(receta1.ingredientes), "\n".join(receta1.pasos)]
    recetas[1, :] = [receta2.nombre, receta2.pais, ", ".join(receta2.ingredientes), "\n".join(receta2.pasos)]
    recetas[2, :] = [receta3.nombre, receta3.pais, ", ".join(receta3.ingredientes), "\n".join(receta3.pasos)]
'''

    

# Función para imprimir las recetas encontradas
def imprimir_recetas(recetas):
    if not recetas:
        st.write("No se encontraron recetas para el término de búsqueda.")
    else:
        st.write("Recetas encontradas:")
        for i, receta in enumerate(recetas, start=1):
            st.write(f"Receta {i}: {receta.nombre} ({receta.pais})")
            st.write("Ingredientes:", ", ".join(receta.ingredientes))
            st.write("Pasos:")
            for j, paso in enumerate(receta.pasos, start=1):
                st.write(f"  {j}. {paso}")
            st.write()