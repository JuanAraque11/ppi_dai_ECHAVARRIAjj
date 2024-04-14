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

    # Devolvemos las recetas creadas
    return [receta1, receta2, receta3]

# Función para imprimir las recetas creadas
def imprimir_recetas(recetas):
    print("Recetas creadas:")
    for i, receta in enumerate(recetas, start=1):
        print(f"Receta {i}: {receta.get_nombre()} ({receta.get_pais()})")
        print("Ingredientes:", ", ".join(receta.get_ingredientes()))
        print("Pasos:")
        for j, paso in enumerate(receta.get_pasos(), start=1):
            print(f"  {j}. {paso}")
        print()