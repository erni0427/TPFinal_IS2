import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

"""
Este proyecto es un módulo de simulación bioinformática que modela la distribución y evolución de pastos marinos en función de diferentes 
escenarios climáticos. Las especies consideradas son Cymodocea nodosa, Posidonia oceanica y Halophila stipulacea, con la opción de 
agregar nuevas especies. El sistema permite analizar cómo el aumento de temperatura y salinidad afecta la dinámica de estas especies 
a lo largo del tiempo.
"""
# Parámetros de las especies: tasa de crecimiento, tasa de mortalidad
species_params = {
    #caso con halop caso 2, compt 10
    #"Posidonia oceanica": {"growth_rate": 0.05, "mortality_rate": 0.02, "competitiveness": 3},
    #"Cymodocea nodosa": {"growth_rate": 0.08, "mortality_rate": 0.03, "competitiveness": 2},

    "Cymodocea nodosa": {"growth_rate": 0.05, "mortality_rate": 0.02, "competitiveness": 3}, #caso 1
    "Posidonia oceanica": {"growth_rate": 0.08, "mortality_rate": 0.03, "competitiveness": 2}#, #caso 1
    #"Halophila stipulacea": {"growth_rate": 0.12, "mortality_rate": 0.04, "competitiveness": 10} 
}

# Escenarios climáticos
climate_scenarios = {
    "RCP 2.6": {"temp_increase": 1.0, "salinity_increase": 0.1},
    "RCP 8.5": {"temp_increase": 3.5, "salinity_increase": 0.4}
}

# Inicialización de la cuadrícula hexagonal de tamaño region_size con especies distribuidas aleatoriamente, primer caso sin halophila

def initialize_grid(region_size, initial_density):
    species_list = list(species_params.keys()) + ['empty', 'dead_matte']
    
    # Especificar las probabilidades de inicialización
    probabilities = {
        "Posidonia oceanica": 0.35, #sin: 35 y con:35
        "Cymodocea nodosa": 0.40, #sin:40 y con:25
        #"Halophila stipulacea": 0.15,
        "empty": 0.15,
        "dead_matte": 0.10
    }
    
    if not np.isclose(sum(probabilities.values()), 1.0):
        raise ValueError("Probabilities do not sum to 1")
    
    grid = np.random.choice(species_list, size=(region_size, region_size), p=[probabilities[species] for species in species_list])
    return grid
    
# Función para aplicar los efectos de los escenarios climáticos
def apply_climate_scenario(scenario):
    for species in species_params.keys():
        species_params[species]["growth_rate"] *= (1 - scenario["temp_increase"] * 0.01)
        species_params[species]["mortality_rate"] *= (1 + scenario["salinity_increase"] * 0.01)

# Aplicar un escenario climático específico 
apply_climate_scenario(climate_scenarios["RCP 2.6"])
#apply_climate_scenario(climate_scenarios["RCP 8.5"])

# Simplificación de la regla de actualización
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] in species_params.keys():
                species = grid[i, j]
                
                # Mortalidad
                if np.random.rand() < species_params[species]["mortality_rate"]:
                    if species == "Posidonia oceanica":
                        new_grid[i, j] = 'dead_matte'
                    else:
                        new_grid[i, j] = 'empty'
                
                # Crecimiento y Competencia
                elif np.random.rand() < species_params[species]["growth_rate"]:
                    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    np.random.shuffle(neighbors)
                    for ni, nj in neighbors:
                        if 0 <= ni < grid.shape[0] and 0 <= nj < grid.shape[1]:
                            if new_grid[ni, nj] == 'empty':
                                new_grid[ni, nj] = species
                                break
                            elif new_grid[ni, nj] in species_params.keys():
                                other_species = new_grid[ni, nj]
                                if species_params[species]["competitiveness"] > species_params[other_species]["competitiveness"]:
                                    new_grid[ni, nj] = species
                                    break
    return new_grid

# Ejecución de la simulación a lo largo de un número de años, actualizando la cuadrícula
def run_simulation(grid, years):
    grids = [grid]
    for year in range(years):
        # Incluir eventos destructivos y perturbaciones (Ejemplo: cada 10 años)
        if year % 10 == 0:
            apply_disturbances(grid)
        grid = update_grid(grid)
        grids.append(grid)
    return grids

# Función para aplicar perturbaciones ambientales y eventos destructivos
def apply_disturbances(grid):
    disturbance_rate = 0.1  # Proporción de la cuadrícula que será afectada
    num_cells = int(grid.size * disturbance_rate)
    indices = np.random.choice(grid.size, num_cells, replace=False)
    for idx in indices:
        i, j = divmod(idx, grid.shape[1])
        grid[i, j] = 'empty'  # La perturbación convierte las celdas afectadas en 'empty'

# Inicialización de la cuadrícula
region_size = 50  # tamaño de la región en celdas
initial_density = 0.2 
grid = initialize_grid(region_size, initial_density)

# Simulación bajo el escenario climático RCP 2.6
years = 80
grids_26 = run_simulation(grid, years)
#grids_85 = run_simulation(grid, years)


# Configuración del gráfico de la cuadrícula
fig1, ax1 = plt.subplots(figsize=(12, 12))


# Graficación de la cuadrícula
def plot_grid(grid, title="Distribución de Pastos Marinos"):
    species_to_num = {species: idx for idx, species in enumerate(species_params.keys(), start=1)}
    species_to_num['empty'] = 0
    species_to_num['dead_matte'] = len(species_params) + 1
    num_grid = np.vectorize(species_to_num.get)(grid)
    
    #cmap = sns.color_palette(["#bdc3c7", "#3498db", "#77dd77", "#e74c3c", "#2e8b57"], as_cmap=True) #e74c3c para halophila
    cmap = sns.color_palette(["#bdc3c7", "#3498db", "#77dd77", "#2e8b57"], as_cmap=True) #sinhalophila
    im = sns.heatmap(num_grid, cbar=False, cmap=cmap, annot=False, linewidths=.5, linecolor='gray', ax=ax1)
    ax1.set_title(title)
    return im

# Configuración del gráfico de cantidad de especies
fig2, ax2 = plt.subplots(figsize=(6, 6))

# Función para contar especies
def count_species(grid):
    counts = {species: np.sum(grid == species) for species in species_params.keys()}
    counts['empty'] = np.sum(grid == 'empty')
    counts['dead_matte'] = np.sum(grid == 'dead_matte')
    return counts

# Obtener colores del colormap usado en el heatmap
species_to_num = {species: idx for idx, species in enumerate(species_params.keys(), start=1)}
species_to_num['empty'] = 0
species_to_num['dead_matte'] = len(species_params) + 1

#cmap = ["#bdc3c7", "#3498db","#77dd77", "#e74c3c", "#2e8b57"] #con rojo halophila
cmap = ["#bdc3c7",  "#3498db","#77dd77", "#2e8b57"]
colors = [cmap[species_to_num[species]] for species in species_params.keys()] + [cmap[species_to_num['empty']], cmap[species_to_num['dead_matte']]]

# Actualización para animación
def update(frame):
    ax1.clear()
    ax2.clear()
    
    plot_grid(grids_26[frame], f"Distribución de Pastos Marinos en {2020 + frame} (RCP 2.6)")
    #plot_grid(grids_85[frame], f"Distribución de Pastos Marinos en {2020 + frame} (RCP 8.5)")
    
    counts = count_species(grids_26[frame])
    #counts = count_species(grids_85[frame])

    species_names = list(counts.keys())
    species_counts = list(counts.values())
    
    bars = ax2.bar(species_names, species_counts, color=colors)
    ax2.set_ylim(0, region_size * region_size)
    ax2.set_ylabel('Cantidad')
    ax2.set_title(f"Cantidad de cada especie en {2020 + frame}")
    
    # Ajustar el tamaño de las etiquetas
    ax2.tick_params(axis='x', labelsize=8)  # Tamaño de las etiquetas de las especies
    ax2.tick_params(axis='y', labelsize=8)  # Tamaño de las etiquetas de la cantidad

# Grafica el estado inicial de la cuadrícula y crea una barra de colores para identificar las especies
im = plot_grid(grids_26[0], "Distribución de Pastos Marinos en 2020 (RCP 2.6)")
#im = plot_grid(grids_85[0], "Distribución de Pastos Marinos en 2020 (RCP 8.5)")

colorbar = fig1.colorbar(im.collections[0], ax=ax1, use_gridspec=True, location="right")
colorbar.set_ticks(range(len(species_params) + 2))
colorbar.set_ticklabels(['empty'] + list(species_params.keys()) + ['dead_matte'])

# Animación que actualiza la gráfica cada 500 milisegundos
ani1 = FuncAnimation(fig1, update, frames=len(grids_26), repeat=False, interval=500)
#ani1 = FuncAnimation(fig1, update, frames=len(grids_85), repeat=False, interval=500)
plt.show(block=False)

# Animación para la cantidad de especies
ani2 = FuncAnimation(fig2, update, frames=len(grids_26), repeat=False, interval=500)
#ani2 = FuncAnimation(fig2, update, frames=len(grids_85), repeat=False, interval=500)
plt.show()


# Adición del gráfico de cobertura de pastos marinos
fig3, ax3 = plt.subplots(figsize=(8, 6))

# Calcular la cobertura de las especies en función de los años
posidonia_cover = [np.sum(grid == "Posidonia oceanica") / grid.size * 100 for grid in grids_26]
cymodocea_cover = [np.sum(grid == "Cymodocea nodosa") / grid.size * 100 for grid in grids_26]
#halophila_cover = [np.sum(grid == "Halophila stipulacea") / grid.size * 100 for grid in grids_85]
years_range = list(range(2020, 2020 + years + 1))

# Especificar los colores deseados
color_posidonia = 'green'
color_cymodocea = 'blue'
#color_halophila = 'red'

# Graficar las líneas con los colores especificados
ax3.plot(years_range, posidonia_cover, label='Posidonia oceanica', color=color_posidonia)
ax3.plot(years_range, cymodocea_cover, label='Cymodocea nodosa', color=color_cymodocea)
#ax3.plot(years_range, halophila_cover, label='Halophila stipulacea', color=color_halophila)

ax3.set_xlabel('Años')
ax3.set_ylabel('Cobertura (%)')
ax3.set_title('Cobertura de Pastos Marinos a lo largo de los Años RCP 2.6')
ax3.legend()

plt.show()