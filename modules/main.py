import random

class ParametrosClimaticos:
    def __init__(self):
        self.temperatura = None
        self.salinidad = None

    def configurar_parametros(self, temperatura, salinidad):
        """Configura los parámetros climáticos necesarios para la simulación."""
        if not (0 <= temperatura <= 40):
            raise ValueError("La temperatura debe estar entre 0 y 40 grados.")
        if not (0 <= salinidad <= 50):
            raise ValueError("La salinidad debe estar entre 0 y 50 ppt.")
        
        self.temperatura = temperatura
        self.salinidad = salinidad
        print(f"Parámetros climáticos configurados: Temperatura={temperatura}°C, Salinidad={salinidad} ppt")

class Celda:
    def __init__(self, tipo):
        self.tipo = tipo  # Tipo de especie en la celda (e.g., "Cymodocea nodosa", "Posidonia oceanica", etc.)
        self.salud = 100  # Salud inicial de la celda
        
    def actualizar_salud(self, temperatura, salinidad):
        """Actualiza la salud de la celda según los parámetros climáticos."""
        if self.tipo == "Cymodocea nodosa":
            # Ejemplo de lógica de impacto de temperatura y salinidad en la salud
            if temperatura > 30 or salinidad > 40:
                self.salud -= 10
            else:
                self.salud -= 1
        elif self.tipo == "Posidonia oceanica":
            if temperatura > 35 or salinidad < 20:
                self.salud -= 15
            else:
                self.salud -= 2
        elif self.tipo == "Halophila stipulacea":
            if temperatura < 15 or salinidad > 30:
                self.salud -= 5
            else:
                self.salud -= 1

        # Evitar que la salud caiga por debajo de cero
        self.salud = max(self.salud, 0)
        print(f"Celda {self.tipo} actualizada, salud actual: {self.salud}")

class GridSimulacion:
    def __init__(self, tamaño, parametros_climaticos):
        self.tamaño = tamaño  # Tamaño de la cuadrícula, e.g., 50x50
        self.cuadricula = []
        self.parametros_climaticos = parametros_climaticos
        self.inicializar_cuadricula()

    def inicializar_cuadricula(self):
        """Inicializa la cuadrícula con especies en función de las probabilidades definidas."""
        especies = ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Espacio vacío", "Materia muerta"]
        probabilidades = [0.25, 0.35, 0.15, 0.15, 0.10]
        self.cuadricula = [
            [Celda(random.choices(especies, probabilidades)[0]) for _ in range(self.tamaño)]
            for _ in range(self.tamaño)
        ]

    def aplicar_parametros_climaticos(self):
        """Aplica los parámetros climáticos a cada celda en la cuadrícula."""
        temperatura = self.parametros_climaticos.temperatura
        salinidad = self.parametros_climaticos.salinidad
        
        for fila in self.cuadricula:
            for celda in fila:
                celda.actualizar_salud(temperatura, salinidad)

# Ejemplo de uso:
# Inicializar y configurar los parámetros climáticos
parametros_climaticos = ParametrosClimaticos()
parametros_climaticos.configurar_parametros(temperatura=28, salinidad=35)

# Crear la cuadrícula de simulación y aplicar parámetros climáticos
simulacion = GridSimulacion(tamaño=50, parametros_climaticos=parametros_climaticos)
simulacion.aplicar_parametros_climaticos()