def simulate_step(grid):
    next_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            species = grid[i, j]
            # Aquí implementarías la lógica de interacción entre especies
            # Ejemplo de reglas: si es 'Cymodocea', cambiar a 'Posidonia' bajo ciertas condiciones
            # ...
    return next_grid

# Ejecución de varios pasos de simulación
steps = 10  # Número de ciclos de simulación
for step in range(steps):
    species_grid = simulate_step(species_grid)