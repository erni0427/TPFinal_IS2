import random
import time

# Inicialización de la cuadrícula de especies con probabilidades específicas
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

# Función para simular un paso de la cuadrícula
def simulate_step(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            # Ejemplo simplificado de evolución de especies
            if cell == "Cymodocea nodosa":
                new_row.append("Posidonia oceanica")
            elif cell == "Posidonia oceanica":
                new_row.append("Halophila stipulacea")
            elif cell == "Halophila stipulacea":
                new_row.append("Materia muerta")
            elif cell == "Materia muerta":
                new_row.append("Espacio vacío")
            else:
                new_row.append(cell)
        new_grid.append(new_row)
    return new_grid

# Función para ejecutar la visualización en tiempo real de la simulación
def run_real_time_simulation(grid, steps):
    report = []
    try:
        for step in range(steps):
            # Actualiza la cuadrícula de especies en cada ciclo
            grid = simulate_step(grid)
            print(f"\nCiclo {step + 1}:")
            for row in grid:
                print(" ".join(cell[0] for cell in row))  # Visualización en tiempo real
            
            # Pausa para la visualización en tiempo real
            time.sleep(1)
            report.append(grid)
    except Exception as e:
        print(f"Error en la visualización en tiempo real: {e}")
        return
    
    # Al finalizar, da opción de guardar resultados
    save_results_option = input("\nSimulación completada. ¿Desea guardar los resultados? (s/n): ")
    if save_results_option.lower() == 's':
        save_simulation_report(report)
    else:
        print("Los resultados no fueron guardados.")

# Función para guardar el reporte de la simulación
def save_simulation_report(report):
    try:
        with open("real_time_simulation_report.txt", "w") as file:
            for step, grid in enumerate(report, start=1):
                file.write(f"\nCiclo {step}:\n")
                for row in grid:
                    file.write(" ".join(cell[0] for cell in row) + "\n")
        print("Reporte guardado exitosamente: 'real_time_simulation_report.txt'")
    except IOError:
        print("Error al guardar el reporte. Cierre la visualización y vuelva a intentarlo.")

# Configuración inicial para la simulación
rows, cols = 10, 10  # Tamaño de la cuadrícula
steps = 5  # Número de ciclos de simulación

# Inicializa y ejecuta la simulación con visualización en tiempo real
species_grid = initialize_species_grid(rows, cols)
run_real_time_simulation(species_grid, steps)
save_simulation_report