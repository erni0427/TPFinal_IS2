import numpy as np
from species import DeadMatta, Especie

class Simulacion:
    """Clase que maneja la simulación del ecosistema marino."""

    def __init__(self, tamano_grid, especies, clima):
        self.tamano_grid = tamano_grid
        self.clima = clima
        self.especies = especies
        self.grid = self.inicializar_grid()
        self.grid_historial = []  # Historial de estados del grid

    def inicializar_grid(self):
        """Inicializa el grid con especies, celdas vacías y materia muerta."""
        total_celdas = self.tamano_grid * self.tamano_grid
        celdas_vacias = [None] * (total_celdas // 3)
        celdas_especies = np.random.choice(self.especies, size=(total_celdas // 3)).tolist()
        celdas_muertas = [DeadMatta()] * (total_celdas - len(celdas_vacias) - len(celdas_especies))

        combinado = celdas_vacias + celdas_especies + celdas_muertas
        np.random.shuffle(combinado)

        grid = np.array(combinado).reshape((self.tamano_grid, self.tamano_grid))

        # Depuración: Verificar las cantidades iniciales de cada tipo
        #print(f"Especies Inicializadas: {len(celdas_especies)}, Celdas Vacías: {len(celdas_vacias)}, Materia Muerta: {len(celdas_muertas)}")
        #print(f"Initialized Grid:\n{grid}")
        return grid

    def correr_simulacion(self, anios):
        """Corre la simulación por un número determinado de años."""
        for anio in range(anios):
            self.grid_historial.append(self.grid.copy())
            self.grid = self.actualizar_grid()
            #print(f"Grid después del año {anio+1}:\n{self.grid}")  # Debugging adicional

    def actualizar_grid(self):
        """Actualiza el grid aplicando las reglas de crecimiento, mortalidad y competencia."""
        nuevo_grid = self.grid.copy()

        for i in range(self.tamano_grid):
            for j in range(self.tamano_grid):
                especie = self.grid[i, j]

                # Verificamos si la celda contiene una especie válida (no DeadMatta ni None)
                if especie and isinstance(especie, Especie):
                    # Mortalidad
                    if np.random.rand() < especie.tasa_mortalidad:
                        nuevo_grid[i, j] = DeadMatta()  # La especie muere
                    else:
                        # Crecimiento en celdas vacías o colonización de Dead Matta
                        vecinos = self.obtener_vecinos(i, j)
                        espacios_libres = [v for v in vecinos if v is None or isinstance(v, DeadMatta)]

                        # Si hay espacios libres (arena o Dead Matta), intenta colonizar
                        if espacios_libres:
                            for espacio in espacios_libres:
                                if np.random.rand() < especie.tasa_crecimiento:
                                    nuevo_grid[i, j] = especie

                        # Interacción y competencia con especies vecinas
                        for vecino in vecinos:
                            if vecino and isinstance(vecino, Especie):
                                # Si la especie actual es más competitiva, reemplaza al vecino
                                if especie.competitividad > vecino.competitividad:
                                    nuevo_grid[i, j] = especie
                # Si la celda está vacía (None) o contiene Dead Matta, permite la colonización
                elif especie is None or isinstance(especie, DeadMatta):
                    vecinos = self.obtener_vecinos(i, j)
                    # Seleccionamos la especie con mayor competitividad entre los vecinos
                    mejor_vecino = max((v for v in vecinos if isinstance(v, Especie)), 
                                       key=lambda e: e.competitividad, 
                                       default=None)
                    if mejor_vecino and np.random.rand() < mejor_vecino.tasa_crecimiento:
                        nuevo_grid[i, j] = mejor_vecino

        # Debug para verificar la actualización correcta del grid
        #print(f"Updated Grid:\n{nuevo_grid}")
        return nuevo_grid    

    def obtener_vecinos(self, x, y):
        """Obtiene los vecinos válidos alrededor de una celda."""
        vecinos = []
        for i in range(max(0, x - 1), min(self.tamano_grid, x + 2)):
            for j in range(max(0, y - 1), min(self.tamano_grid, y + 2)):
                if (i, j) != (x, y):
                    vecinos.append(self.grid[i, j])
        return vecinos