import unittest
from unittest.mock import patch
from collections import Counter
from module import initialize_species_grid, simulate_step, run_simulation, generate_simulation_report

class TestSpeciesSimulation(unittest.TestCase):

    def test_initialize_species_grid(self):
        rows, cols = 5, 5
        grid = initialize_species_grid(rows, cols)
        
        # Verifica que el tamaño de la cuadrícula sea correcto
        self.assertEqual(len(grid), rows)
        self.assertTrue(all(len(row) == cols for row in grid))
        
        # Verifica que cada celda tenga uno de los valores esperados
        valid_species = {"Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Espacio vacío", "Materia muerta"}
        for row in grid:
            for cell in row:
                self.assertIn(cell, valid_species)

    def test_simulate_step_transitions(self):
        initial_grid = [
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío"],
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío"]
        ]
        
        with patch('random.choice', side_effect=lambda x: x[0]):  # Controlamos `random.choice` para el primer valor posible
            result_grid = simulate_step(initial_grid)
        
        # Verifica condiciones específicas
        for i, row in enumerate(result_grid):
            for j, cell in enumerate(row):
                if initial_grid[i][j] == "Cymodocea nodosa":
                    self.assertEqual(cell, "Cymodocea nodosa")
                elif initial_grid[i][j] == "Posidonia oceanica":
                    self.assertEqual(cell, "Posidonia oceanica")
                elif initial_grid[i][j] == "Halophila stipulacea":
                    self.assertIn(cell, ["Halophila stipulacea", "Espacio vacío"])
                elif initial_grid[i][j] == "Materia muerta":
                    self.assertIn(cell, ["Materia muerta", "Espacio vacío"])
                elif initial_grid[i][j] == "Espacio vacío":
                    self.assertEqual(cell, "Espacio vacío")




    def test_run_simulation(self):
        initial_grid = [
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea"],
            ["Materia muerta", "Espacio vacío", "Cymodocea nodosa"]
        ]
        
        # Ejecuta la simulación con 2 pasos
        final_grid = run_simulation(initial_grid, 2)
        
        # Verifica que la cuadrícula final tenga el tamaño correcto y valores válidos
        self.assertEqual(len(final_grid), len(initial_grid))
        self.assertEqual(len(final_grid[0]), len(initial_grid[0]))
        
        valid_species = {"Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Espacio vacío", "Materia muerta"}
        for row in final_grid:
            for cell in row:
                self.assertIn(cell, valid_species)

    def test_generate_simulation_report(self):
        final_grid = [
            ["Cymodocea nodosa", "Posidonia oceanica", "Espacio vacío"],
            ["Materia muerta", "Cymodocea nodosa", "Halophila stipulacea"]
        ]
        
        # Genera el reporte
        report = generate_simulation_report(final_grid)
        
        # Define el conteo esperado de cada especie
        expected_counts = Counter({
            "Cymodocea nodosa": 2,
            "Posidonia oceanica": 1,
            "Halophila stipulacea": 1,
            "Espacio vacío": 1,
            "Materia muerta": 1
        })
        
        # Verifica que el reporte contenga la cantidad correcta de cada especie
        for species, count in expected_counts.items():
            self.assertIn(f"{species}: {count}", report)

# Ejecuta las pruebas
if __name__ == "__main__":
    unittest.main()
