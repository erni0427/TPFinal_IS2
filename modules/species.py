# class Species:
#     """Modelo de una especie de pasto marino."""
    
#     def __init__(self, name, growth_rate, mortality_rate, competitiveness):
#         self.name = name
#         self.growth_rate = growth_rate
#         self.mortality_rate = mortality_rate
#         self.competitiveness = competitiveness

# class DeadMatta:
#     """Represents dead organic matter in the ecosystem."""
#     def __str__(self):
#         return "Dead Matta"
    
# class SpeciesFactory:
#     """Fábrica para crear especies según el nombre."""

#     @staticmethod
#     def create_species(name):
#         species_data = {
#             "Posidonia oceanica": Species("Posidonia oceanica", 0.08, 0.03, 2),
#             "Cymodocea nodosa": Species("Cymodocea nodosa", 0.05, 0.02, 3),
#             "Halophila stipulacea": Species("Halophila stipulacea", 0.12, 0.04, 1),
#         }
#         if name not in species_data:
#             raise ValueError(f"Especie desconocida: {name}")
#         return species_data[name]
class Especie:
    """Clase que define a una especie marina."""
    def __init__(self, nombre, tasa_crecimiento, tasa_mortalidad, competitividad):
        self.nombre = nombre
        self.tasa_crecimiento = tasa_crecimiento
        self.tasa_mortalidad = tasa_mortalidad
        self.competitividad = competitividad

    def __repr__(self):
        return self.nombre

class DeadMatta:
    def __init__(self):
        self.nombre = "Dead Matta"
    def __repr__(self):
        return self.nombre