# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation

# def plot_grid(grid, title):
#     plt.imshow(grid, cmap='viridis')
#     plt.title(title)
#     plt.show()

# def plot_species_coverage(grids, years):
#     posidonia_cover = [np.sum(grid == "Posidonia oceanica") / grid.size * 100 for grid in grids]
#     cymodocea_cover = [np.sum(grid == "Cymodocea nodosa") / grid.size * 100 for grid in grids]
#     halophila_cover = [np.sum(grid == "Halophila stipulacea") / grid.size * 100 for grid in grids]

#     plt.plot(years, posidonia_cover, label='Posidonia oceanica', color='green')
#     plt.plot(years, cymodocea_cover, label='Cymodocea nodosa', color='blue')
#     plt.plot(years, halophila_cover, label='Halophila stipulacea', color='red')

#     plt.xlabel('Años')
#     plt.ylabel('Cobertura (%)')
#     plt.title('Cobertura de Pastos Marinos a lo largo de los Años')
#     plt.legend()
#     plt.show()import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_species_coverage(grids, years):
    posidonia_cover = [np.sum(grid == "Posidonia oceanica") / grid.size * 100 for grid in grids]
    cymodocea_cover = [np.sum(grid == "Cymodocea nodosa") / grid.size * 100 for grid in grids]
    halophila_cover = [np.sum(grid == "Halophila stipulacea") / grid.size * 100 for grid in grids]

    plt.plot(years, posidonia_cover, label='Posidonia oceanica', color='green')
    plt.plot(years, cymodocea_cover, label='Cymodocea nodosa', color='blue')
    plt.plot(years, halophila_cover, label='Halophila stipulacea', color='red')

    plt.xlabel('Years')
    plt.ylabel('Coverage (%)')
    plt.title('Seagrass Coverage Over the Years')
    plt.legend()
    plt.show()
    
def plot_grid(grid, title):
    """Function that converts the species grid into a numerical representation for plotting."""
    
    # Mapping species to numbers
    species_to_number = {
        "Posidonia oceanica": 1,
        "Cymodocea nodosa": 2,
        "Halophila stipulacea": 3,
        None: 0  # Representation of empty cells
    }
    
    # Convert the species grid into a numerical grid
    numeric_grid = np.vectorize(species_to_number.get)(grid)
    
    # Plot the numerical grid
    plt.imshow(numeric_grid, cmap='viridis')
    plt.title(title)
    plt.colorbar(label='Species')
    plt.show()