import numpy as np
import random

# Tamaño de la cuadrícula
grid_size = (50, 50)  # Ajustable por el usuario

# Probabilidades de aparición para cada especie
probabilities = {
    'Cymodocea': 0.25,
    'Posidonia': 0.35,
    'Halophila': 0.15,
    'Empty': 0.15,
    'DeadMatta': 0.10
}

def validate_probabilities(prob_dict):
    total = sum(prob_dict.values())
    if total != 1.0:
        raise ValueError("Las probabilidades deben sumar 100%.")

validate_probabilities(probabilities)

def initialize_grid(size, probs):
    grid = np.empty(size, dtype=object)
    species = list(probs.keys())
    prob_values = list(probs.values())
    for i in range(size[0]):
        for j in range(size[1]):
            grid[i, j] = random.choices(species, weights=prob_values, k=1)[0]
    return grid

# Inicialización de la cuadrícula con las especies distribuidas aleatoriamente
species_grid = initialize_grid(grid_size, probabilities)