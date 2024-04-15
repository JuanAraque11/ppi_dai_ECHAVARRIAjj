import numpy as np
import streamlit as st

class Receta:
    """Representa una receta de cocina.

    Esta clase almacena información sobre una receta, incluyendo su nombre,
    país de origen, ingredientes y pasos para prepararla.

    Args:
        nombre (str): El nombre de la receta.
        pais (str): El país de origen de la receta.
        ingredientes (list): Una lista de ingredientes necesarios para la receta.
        pasos (list): Una lista de pasos para preparar la receta.

    Attributes:
        nombre (str): El nombre de la receta.
        pais (str): El país de origen de la receta.
        ingredientes (list): Una lista de ingredientes necesarios para la receta.
        pasos (list): Una lista de pasos para preparar la receta.

    """
    def __init__(self, nombre, pais, ingredientes, pasos):
        """Inicializa una nueva instancia de la clase Receta.

        Args:
            nombre (str): El nombre de la receta.
            pais (str): El país de origen de la receta.
            ingredientes (list): Una lista de ingredientes necesarios para la receta.
            pasos (list): Una lista de pasos para preparar la receta.

        """
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
    """
    Crea una lista de recetas.
    
    Args: None

    Returns: list de recetas
    """
    almacen_recetas = []

    def agregar_receta(nombre, pais, ingredientes, pasos):
        """
        Agrega una receta a la lista de recetas.

        Args: str, str, list, list

        Returns: None
        """
        receta = Receta(nombre, pais, ingredientes, pasos)
        almacen_recetas.append(receta)

    agregar_receta("Tacos al pastor", "México", ["Carne de cerdo", "Piña", "Cebolla", "Cilantro", "Tortillas de maíz"], ["Marinar la carne", "Asar la carne en trompo", "Servir en tortillas con piña y cebolla"])
    agregar_receta("Enchiladas", "México", ["Tortillas de maíz", "Pollo deshebrado", "Salsa roja", "Queso fresco", "Crema", "Cebolla", "Aguacate"], ["Calentar las tortillas", "Rellenarlas con pollo deshebrado", "Doblarlas y cubrirlas con salsa roja", "Espolvorear queso fresco y cebolla picada", "Servir con crema y aguacate"])
    agregar_receta("Tacos de Carnitas", "México", ["Tortillas de maíz", "Carnitas de cerdo", "Cebolla", "Cilantro", "Salsa verde", "Limón"], ["Calentar las tortillas", "Rellenarlas con carnitas de cerdo", "Agregar cebolla y cilantro picados", "Rociar con salsa verde y exprimir limón", "Servir caliente"])
    agregar_receta("Mole Poblano", "México", ["Pollo", "Chiles secos", "Chocolate", "Plátano", "Sésamo", "Canela", "Almendras", "Cacahuetes"], ["Cocinar los chiles y molerlos con chocolate y especias", "Freír la salsa resultante", "Agregar trozos de pollo cocido", "Cocinar a fuego lento hasta que esté bien mezclado", "Servir con arroz y tortillas"])
    agregar_receta("Guacamole", "México", ["Aguacate", "Tomate", "Cebolla", "Cilantro", "Limón", "Sal", "Chile serrano"], ["Machacar los aguacates", "Agregar tomate, cebolla y cilantro picados", "Exprimir limón y sazonar con sal", "Añadir chile serrano al gusto", "Mezclar bien y servir con totopos"])

    agregar_receta("Bandeja Paisa", "Colombia", ["Arroz", "Frijoles", "Carne molida", "Chicharrón", "Plátano maduro", "Huevo frito", "Aguacate", "Arepa"], ["Freír la carne molida", "Freír el chicharrón", "Freír el plátano maduro", "Preparar el arroz y los frijoles", "Freír el huevo", "Servir todo junto con aguacate y arepa"])
    agregar_receta("Ajiaco", "Colombia", ["Pollo", "Papa criolla", "Papa común", "Mazorca", "Cilantro", "Aguacate", "Crema de leche", "Alcaparras"], ["Cocinar el pollo con las papas criollas y la mazorca", "Agregar las papas comunes y cocinar hasta que estén tiernas", "Servir con cilantro, aguacate, crema de leche y alcaparras"])
    agregar_receta("Empanadas Colombianas", "Colombia", ["Masa de maíz", "Carne molida", "Cebolla", "Papa", "Comino", "Achiote", "Huevo", "Aceite"], ["Preparar el relleno con carne molida, cebolla, papa y especias", "Armar las empanadas con la masa y el relleno", "Freír las empanadas hasta que estén doradas"])
    agregar_receta("Sancocho", "Colombia", ["Pollo", "Costilla de cerdo", "Yuca", "Plátano", "Mazorca", "Cilantro", "Cebolla", "Tomate", "Ajo"], ["Cocinar el pollo y la costilla de cerdo en una olla grande con agua", "Agregar las verduras y cocinar hasta que estén tiernas", "Servir caliente con cilantro, cebolla y tomate picados"])
    agregar_receta("Bunuelos Colombianos", "Colombia", ["Queso costeño rallado", "Harina de maíz", "Huevos", "Azúcar", "Sal", "Aceite"], ["Mezclar el queso costeño rallado con harina de maíz, huevos, azúcar y sal", "Formar bolitas y freírlas en aceite caliente hasta que estén doradas"])

    agregar_receta("Pad Thai", "Tailandia", ["Fideos de arroz", "Tofu", "Huevo", "Brotes de soja", "Cacahuetes", "Salsa de tamarindo"], ["Saltear tofu y huevo", "Agregar fideos y salsa de tamarindo", "Incorporar brotes de soja y cacahuetes"])
    agregar_receta("Pad Thai", "Tailandia", ["Fideos de arroz", "Tofu", "Huevo", "Brotes de soja", "Cacahuetes", "Salsa de tamarindo"], ["Saltear tofu y huevo", "Agregar fideos y salsa de tamarindo", "Incorporar brotes de soja y cacahuetes"])
    agregar_receta("Curry Rojo Tailandés", "Tailandia", ["Pechuga de pollo", "Leche de coco", "Pasta de curry rojo", "Bambú", "Pimientos", "Berengena", "Hoja de lima kaffir"], ["Cocinar la pasta de curry rojo con la leche de coco", "Agregar el pollo y cocinar hasta que esté tierno", "Añadir las verduras y cocinar hasta que estén tiernas", "Servir caliente con arroz jazmín"])
    agregar_receta("Tom Yum Goong", "Tailandia", ["Langostinos", "Setas", "Hierba de limón", "Chiles", "Galanga", "Hoja de lima kaffir", "Pasta de tamarindo"], ["Hervir las hierbas y especias en caldo de pollo", "Agregar langostinos y setas y cocinar hasta que estén cocidos", "Añadir pasta de tamarindo y ajustar el sabor con salsa de pescado y limón"])
    agregar_receta("Mango Sticky Rice", "Tailandia", ["Arroz glutinoso", "Mango", "Leche de coco", "Azúcar", "Sal"], ["Cocinar el arroz glutinoso al vapor", "Mezclar la leche de coco con azúcar y sal para hacer el jarabe", "Servir el arroz con rodajas de mango y jarabe de leche de coco"])

    agregar_receta("Pasta Carbonara", "Italia", ["Espaguetis", "Bacon", "Huevo", "Queso Parmesano", "Pimienta negra"], ["Cocinar la pasta al dente", "Freír el bacon", "Mezclar los huevos con el queso", "Agregar la mezcla de huevo y queso a la pasta", "Añadir el bacon y la pimienta"])
    agregar_receta("Risotto de Champiñones", "Italia", ["Arroz Arborio", "Champiñones", "Cebolla", "Caldo de pollo", "Vino blanco", "Queso Parmesano"], ["Sofreír la cebolla y los champiñones", "Añadir el arroz y el vino blanco", "Cocinar añadiendo caldo de pollo poco a poco", "Agregar queso parmesano al final"])
    agregar_receta("Pesto Genovese", "Italia", ["Albahaca", "Piñones", "Ajo", "Queso Parmesano", "Aceite de oliva", "Sal", "Pimienta"], ["Triturar la albahaca, los piñones y el ajo", "Agregar el queso parmesano", "Añadir aceite de oliva hasta obtener la consistencia deseada", "Sazonar con sal y pimienta"])
    agregar_receta("Tiramisú", "Italia", ["Café", "Licor de café", "Huevos", "Azúcar", "Mascarpone", "Bizcochos de soletilla", "Cacao en polvo"], ["Mojar los bizcochos en café y licor", "Hacer una crema con los huevos, el azúcar y el mascarpone", "Montar el postre alternando capas de bizcocho y crema", "Refrigerar y espolvorear con cacao en polvo antes de servir"])
    agregar_receta("Pizza Margarita", "Italia", ["Masa de pizza", "Tomate", "Mozzarella", "Albahaca"], ["Extender la masa de pizza", "Agregar salsa de tomate y mozzarella", "Hornear y agregar albahaca fresca"])

    return almacen_recetas


# Función para imprimir las recetas encontradas
def imprimir_recetas(recetas):
    """
    imprime las recetas encontradas

    Args:  recetas (list): lista de recetas

    Returns: None
    """
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