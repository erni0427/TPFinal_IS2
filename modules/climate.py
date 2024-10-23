# class Climate:
#     """Represents climate change effects."""
#     def __init__(self, temp_increase, salinity_increase):
#         self.temp_increase = temp_increase
#         self.salinity_increase = salinity_increase

class Clima:
    """Define los efectos del clima en las especies."""
    def __init__(self, incremento_temp, incremento_salinidad):
        self.incremento_temp = incremento_temp
        self.incremento_salinidad = incremento_salinidad

    def aplicar_cambio_climatico(self, especies):
        """Modifica las tasas de crecimiento y mortalidad de las especies según el escenario climático."""
        for especie in especies:
            especie.tasa_crecimiento *= (1 - self.incremento_temp * 0.01)
            especie.tasa_mortalidad *= (1 + self.incremento_salinidad * 0.01)