import random
import time

# Función para inicializar la cuadrícula de especies según los porcentajes de probabilidad
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

# Función que simula un paso en la cuadrícula, actualizando de acuerdo a reglas de interacción (simplificado)
def simulate_step(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            # Ejemplo de interacción simple: placeholder
            if cell == "Cymodocea nodosa":
                new_row.append("Posidonia oceanica")  # simplificación: evolución de especies
            elif cell == "Posidonia oceanica":
                new_row.append("Halophila stipulacea")  # simplificación
            elif cell == "Halophila stipulacea":
                new_row.append("Materia muerta")  # simplificación
            elif cell == "Materia muerta":
                new_row.append("Espacio vacío")  # simplificación
            else:
                new_row.append(cell)  # Espacio vacío permanece vacío
        new_grid.append(new_row)
    return new_grid

# Función que ejecuta la simulación mostrando en tiempo real y generando reporte final
def run_simulation(grid, steps):
    report = []
    for step in range(steps):
        try:
            grid = simulate_step(grid)
            print(f"\nCiclo {step + 1}:")
            for row in grid:
                print(" ".join(cell[0] for cell in row))  # Muestra visualización del ciclo en tiempo real
            report.append(grid)
            time.sleep(1)  # Pausa para simular "tiempo real" en cada ciclo
        except Exception as e:
            print(f"Error en la actualización de la cuadrícula en el ciclo {step + 1}: {e}")
            break
    print("\nSimulación completada. Generando reporte...")
    generate_report(report)

# Función de generación de reporte final de la simulación
def generate_report(report):
    try:
        with open("simulation_report.txt", "w") as file:
            for step, grid in enumerate(report, start=1):
                file.write(f"\nCiclo {step}:\n")
                for row in grid:
                    file.write(" ".join(cell[0] for cell in row) + "\n")
        print("Reporte generado exitosamente: 'simulation_report.txt'")
    except IOError:
        print("Error: No se pudo generar el reporte.")

# Configuración de simulación
rows, cols = 10, 10  # Tamaño de la cuadrícula
steps = 5  # Número de ciclos de simulación, configurable por el usuario

# Inicializa la cuadrícula y ejecuta la simulación
species_grid = initialize_species_grid(rows, cols)
run_simulation(species_grid, steps)
