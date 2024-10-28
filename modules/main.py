from collections import Counter
import random

# Inicializa una cuadrícula con especies al azar para simular
def initialize_species_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            rand_num = random.uniform(0, 100)
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

# Simula los pasos de la cuadrícula
def run_simulation(grid, steps):
    for step in range(steps):
        grid = simulate_step(grid)
    return grid

# Simula un paso en la cuadrícula
def simulate_step(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            # Ejemplo de lógica de interacción simple
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

# Genera el reporte final de la simulación
def generate_simulation_report(grid):
    flattened_grid = [cell for row in grid for cell in row]
    species_count = Counter(flattened_grid)
    report = "Reporte Final de Simulación:\n"
    report += "\n".join([f"{species}: {count}" for species, count in species_count.items()])
    return report

# Configuración inicial
rows, cols = 10, 10  # Tamaño de la cuadrícula
steps = 5  # Número de ciclos de simulación

# Inicializa la cuadrícula y ejecuta la simulación
species_grid = initialize_species_grid(rows, cols)
final_grid = run_simulation(species_grid, steps)

# Genera y muestra el reporte de resultados después de la simulación
report = generate_simulation_report(final_grid)
print(report)