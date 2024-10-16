import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def plot_grid(grid, title):
    plt.imshow(grid, cmap='viridis')
    plt.title(title)
    plt.show()

def plot_species_coverage(grids, years):
    posidonia_cover = [np.sum(grid == "Posidonia oceanica") / grid.size * 100 for grid in grids]
    cymodocea_cover = [np.sum(grid == "Cymodocea nodosa") / grid.size * 100 for grid in grids]
    halophila_cover = [np.sum(grid == "Halophila stipulacea") / grid.size * 100 for grid in grids]

    plt.plot(years, posidonia_cover, label='Posidonia oceanica', color='green')
    plt.plot(years, cymodocea_cover, label='Cymodocea nodosa', color='blue')
    plt.plot(years, halophila_cover, label='Halophila stipulacea', color='red')

    plt.xlabel('Años')
    plt.ylabel('Cobertura (%)')
    plt.title('Cobertura de Pastos Marinos a lo largo de los Años')
    plt.legend()
    plt.show()
