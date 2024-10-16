from simulacion import initialize_grid, apply_climate_scenario
from visualizacion import plot_grid, plot_species_coverage
from parametros import climate_scenarios

region_size = 50
probabilities = {
    "Cymodocea nodosa": 0.25,
    "Posidonia oceanica": 0.35,
    "Halophila stipulacea": 0.15,
    "empty": 0.15,
    "dead_matte": 0.10
}

grid = initialize_grid(region_size, probabilities)
apply_climate_scenario(climate_scenarios["RCP 8.5"])

plot_grid(grid, "Distribución inicial de pastos marinos")
