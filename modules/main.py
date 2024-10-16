# from simulacion import initialize_grid, apply_climate_scenario

from clima import Climate
from especies import SpeciesFactory
from simulacion import Simulation
from visualizacion import plot_species_coverage, plot_grid

# Set up the simulation parameters
climate = Climate(1.0, 0.1)
species_list = [
    SpeciesFactory.create_species("Posidonia oceanica"),
    SpeciesFactory.create_species("Cymodocea nodosa"),
    SpeciesFactory.create_species("Halophila stipulacea")
]

# Initialize and run the simulation
simulation = Simulation(50, species_list, climate)
simulation.run_simulation(80)

# Visualize species coverage and grid
# Check if simulation.grids is populated
if simulation.grids:
    plot_species_coverage(simulation.grids, list(range(2020, 2020 + 80)))
    plot_grid(simulation.grid, "Final Distribution of Seagrasses")
else:
    print("No grid data to visualize.")