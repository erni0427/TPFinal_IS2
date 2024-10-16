import numpy as np
from parametros import species_params

def initialize_grid(region_size, probabilities):
    species_list = list(species_params.keys()) + ['empty', 'dead_matte']
    grid = np.random.choice(species_list, size=(region_size, region_size),
                            p=[probabilities[species] for species in species_list])
    return grid

def apply_climate_scenario(scenario):
    for species in species_params:
        species_params[species]["growth_rate"] *= (1 - scenario["temp_increase"] * 0.01)
        species_params[species]["mortality_rate"] *= (1 + scenario["salinity_increase"] * 0.01)
