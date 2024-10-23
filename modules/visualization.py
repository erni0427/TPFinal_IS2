import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap

def mostrar_simulacion(historial_grids, especies, nombre_escenario):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [3, 1]})

    # Mapeo de especies a números
    species_to_num = {
        "Cymodocea nodosa": 1,
        "Posidonia oceanica": 2,
        "Halophila stipulacea": 3,
        "Dead Matta": 4,
        None: 0  # Espacios vacíos (arena)
    }

    # Colores exactos basados en la presentación
    cmap = ListedColormap(['#D3D3D3', '#7CFC00', '#87CEEB', '#FF0000', '#006400'])  # Gris claro, Verde manzana, Celeste azulado, Rojo, Verde inglés

    # Dibujar grid inicial con celdas más grandes
    grid = historial_grids[0]
    numeric_grid = np.vectorize(lambda x: species_to_num.get(x.nombre if x else None))(grid)
    im = ax1.imshow(numeric_grid, cmap=cmap, interpolation='none')

    # Mostrar las líneas de cuadrícula para cada celda (resaltar cada celda)
    ax1.set_xticks(np.arange(-0.5, grid.shape[1], 1), minor=True)
    ax1.set_yticks(np.arange(-0.5, grid.shape[0], 1), minor=True)
    ax1.grid(which="minor", color="black", linestyle='-', linewidth=0.5)
    ax1.tick_params(which="minor", size=0)

    # Barra de color
    cbar = fig.colorbar(im, ax=ax1, ticks=[0, 1, 2, 3, 4])
    cbar.ax.set_yticklabels(['Arena', 'Cymodocea', 'Posidonia', 'Halophila', 'Dead Matta'])
    ax1.set_title(f"{nombre_escenario} - Año: 2020")

    # Colores del gráfico de barras: corregido para Dead Matta (verde inglés) y None (gris claro)
    colores_barras = {
        "Cymodocea nodosa": '#7CFC00',  # Verde manzana
        "Posidonia oceanica": '#87CEEB',  # Celeste azulado
        "Halophila stipulacea": '#FF0000',  # Rojo
        "Dead Matta": '#006400',  # Verde inglés
        "Arena": '#D3D3D3'  # Gris claro para None (arena)
    }

    # Convertir None a "Arena" para evitar problemas en matplotlib
    conteo_especies_inicial = contar_especies(grid, especies)
    conteo_especies_inicial["Arena"] = conteo_especies_inicial.pop(None)  # Renombrar 'None' a 'Arena'
    species_names = list(colores_barras.keys())  # Especies en orden para el gráfico de barras
    barras = ax2.bar(species_names, [conteo_especies_inicial.get(species, 0) for species in species_names],
                     color=[colores_barras[species] for species in species_names])
    ax2.set_ylim(0, max(conteo_especies_inicial.values()) * 1.1)
    ax2.set_title("Cobertura de especies")
    ax2.set_xlabel("Especies")
    ax2.set_ylabel("Cantidad")
    ax2.set_xticklabels(species_names, rotation=45, ha="right")

    def actualizar(frame):
        # Actualización del grid
        grid = historial_grids[frame]
        numeric_grid = np.vectorize(lambda x: species_to_num.get(x.nombre if x else None))(grid)
        im.set_array(numeric_grid)
        ax1.set_title(f"{nombre_escenario} - Año: {2020 + frame}")

        # Actualizar las alturas de las barras sin redibujar todo el gráfico de barras
        conteo_especies = contar_especies(grid, especies)
        conteo_especies["Arena"] = conteo_especies.pop(None)  # Renombrar 'None' a 'Arena'
        for bar, species in zip(barras, species_names):
            bar.set_height(conteo_especies.get(species, 0))
        ax2.set_ylim(0, max(conteo_especies.values()) * 1.1)

    anim = FuncAnimation(fig, actualizar, frames=len(historial_grids), repeat=False, interval=1000)
    plt.tight_layout()
    plt.show()

def contar_especies(grid, especies):
    """Cuenta la cantidad de cada especie en el grid."""
    conteo = {especie.nombre: 0 for especie in especies}
    conteo["Dead Matta"] = 0
    conteo[None] = 0  # Espacios vacíos (arena)
    for celda in grid.flatten():
        if celda:
            conteo[celda.nombre] += 1
        else:
            conteo[None] += 1
    return conteo

# def contar_especies(grid, especies):
#     """Cuenta la cantidad de cada especie en el grid."""
#     conteo = {especie.nombre: 0 for especie in especies}
#     conteo["Dead Matta"] = 0
#     conteo["Arena"] = 0  # Espacios vacíos (arena)
    
#     for celda in grid.flatten():
#         if isinstance(celda, especies):  # Si es una instancia de Species
#             conteo[celda.nombre] += 1
#         elif celda == "Dead Matta":  # Si es Dead Matta
#             conteo["Dead Matta"] += 1
#         else:
#             conteo["Arena"] += 1  # Contar los espacios vacíos
#     return conteo

def mostrar_grafico_cobertura(historial_grids, especies):
    """Muestra el gráfico de cobertura al final."""
    fig, ax = plt.subplots()

    # Colores corregidos para el gráfico de cobertura
    colores_cobertura = {
        "Cymodocea nodosa": '#7CFC00',  # Verde manzana
        "Posidonia oceanica": '#87CEEB',  # Celeste azulado
        "Halophila stipulacea": '#FF0000',  # Rojo
        "Dead Matta": '#006400',  # Verde inglés
        "Arena": '#D3D3D3'  # Gris claro
    }

    for especie in especies:
        cobertura = [np.sum(grid == especie) / grid.size * 100 for grid in historial_grids]
        ax.plot(cobertura, label=especie.nombre, color=colores_cobertura[especie.nombre], linewidth=2.5)

    # Cobertura de los espacios vacíos (None)
    cobertura_arena = [np.sum(grid == None) / grid.size * 100 for grid in historial_grids]
    ax.plot(cobertura_arena, label='Arena', color=colores_cobertura["Arena"], linewidth=2.5)

    ax.set_xlabel('Años')
    ax.set_ylabel('Cobertura (%)')
    ax.set_title('Cobertura de especies a lo largo de los años')
    ax.legend()
    plt.show()