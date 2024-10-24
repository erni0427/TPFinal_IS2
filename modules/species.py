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