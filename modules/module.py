import time
import random

def initialize_species_grid(rows, cols, rand_func=random.uniform):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            rand_num = rand_func(0, 100)
            if rand_num <= 25:
                row.append("Cymodocea nodosa")
            elif rand_num <= 60:
                row.append("Posidonia oceanica")
            elif rand_num <= 75:
                row.append("Halophila stipulacea")
            elif rand_num <= 90:
                row.append("Espacio vacío")
            else:
                row.append("Materia muerta")
        grid.append(row)
    return grid


def simulate_step(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == "Cymodocea nodosa":
                new_row.append("Cymodocea nodosa")  # Permanece
            elif cell == "Posidonia oceanica":
                new_row.append("Posidonia oceanica")  # Permanece
            elif cell == "Halophila stipulacea":
                new_row.append(random.choice(["Halophila stipulacea", "Espacio vacío"]))  # Puede volverse vacío
            elif cell == "Materia muerta":
                new_row.append(random.choice(["Materia muerta", "Espacio vacío"]))  # Puede volverse vacío
            else:
                new_row.append(cell)  # Espacio vacío permanece
        new_grid.append(new_row)
    return new_grid

def run_simulation(grid, steps):
    for step in range(steps):
        grid = simulate_step(grid)
        yield grid  # Usar yield para permitir la visualización paso a paso

def visualize_simulation(grid, steps, delay):
    for step in range(steps):
        grid = simulate_step(grid)
        print(f"Paso {step + 1}:")
        for row in grid:
            print(" | ".join(row))
        print("\n")
        time.sleep(delay)  # Esperar antes de continuar al siguiente paso

def set_simulation_speed(speed):
    if speed <= 0:
        raise ValueError("La velocidad debe ser un valor positivo.")
    return speed

# Configura la velocidad de la simulación (en segundos)
simulation_speed = set_simulation_speed(1)  # Tiempo de pausa entre pasos, ajustable

# Configuración inicial
rows, cols = 5, 5  # Tamaño de la cuadrícula
steps = 10  # Número de pasos de simulación

# Inicializa la cuadrícula de especies
species_grid = initialize_species_grid(rows, cols)

# Visualiza la simulación en tiempo real con la velocidad configurada
visualize_simulation(species_grid, steps=steps, delay=simulation_speed)