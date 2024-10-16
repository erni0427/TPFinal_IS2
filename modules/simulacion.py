# import numpy as np
# from parametros import species_params

# def initialize_grid(region_size, probabilities):
#     species_list = list(species_params.keys()) + ['empty', 'dead_matte']
#     grid = np.random.choice(species_list, size=(region_size, region_size),
#                             p=[probabilities[species] for species in species_list])
#     return grid

# def apply_climate_scenario(scenario):
#     for species in species_params:
#         species_params[species]["growth_rate"] *= (1 - scenario["temp_increase"] * 0.01)
#         species_params[species]["mortality_rate"] *= (1 + scenario["salinity_increase"] * 0.01)

import numpy as np
from especies import SpeciesFactory

class Simulation:
    """Manages the simulation of the marine ecosystem."""
    
    def __init__(self, grid_size, species_list, climate):
        self.grid_size = grid_size
        self.climate = climate
        self.grid = self.initialize_grid(species_list)
        self.grids = []  # Store the state of the grid for each year

    def initialize_grid(self, species_list):
        """Initializes the grid with species randomly distributed."""
        species_probs = [0.35, 0.40, 0.15, 0.10]

        if len(species_list) > len(species_probs):
            raise ValueError("More species than probabilities defined.")
        
        species_probs = species_probs[:len(species_list)]
        
        total = sum(species_probs)
        if total != 1:
            species_probs = [p / total for p in species_probs]
        
        return np.random.choice(species_list, size=(self.grid_size, self.grid_size), p=species_probs)

    def update_grid(self):
        """Updates the grid according to mortality rates."""
        new_grid = self.grid.copy()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                species = self.grid[i, j]
                if species is not None and np.random.rand() < species.mortality_rate:
                    new_grid[i, j] = None  # The species dies
                elif species is not None:
                    # Apply growth logic (for simplicity, growth is not visualized here)
                    new_grid[i, j] = species  # Keep the species in the grid

        return new_grid

    def run_simulation(self, years):
        """Runs the simulation for the specified number of years."""
        for year in range(years):
            self.grids.append(self.grid.copy())  # Store the current grid state
            self.grid = self.update_grid()
            self.apply_climate_scenario()

    def apply_climate_scenario(self):
        """Applies climate changes to species rates."""
        for species in self.grid.flatten():
            if species:
                species.growth_rate *= (1 - self.climate.temp_increase * 0.01)
                species.mortality_rate *= (1 + self.climate.salinity_increase * 0.01)