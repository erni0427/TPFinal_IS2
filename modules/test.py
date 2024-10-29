from module import set_simulation_speed, simulate_step, initialize_species_grid, run_simulation
import unittest
from unittest.mock import patch
import random
from collections import Counter



class TestSpeciesSimulation(unittest.TestCase):
    
    def test_initialize_species_grid(self):
        rows, cols = 5, 5
        total_cells = rows * cols
        
        # Controla los valores aleatorios para un patrón específico
        with patch('random.uniform', side_effect=[10, 30, 65, 80, 95] * total_cells):
            grid = initialize_species_grid(rows, cols, lambda *args: random.uniform(*args))
        
        # Verifica que el grid tenga el tamaño correcto
        self.assertEqual(len(grid), rows)
        self.assertTrue(all(len(row) == cols for row in grid))
        
        # Contar las especies generadas
        flat_grid = [cell for row in grid for cell in row]
        species_counts = Counter(flat_grid)
        
        # Contenidos esperados (proporciones basadas en el patrón en side_effect)
        expected_counts = {
            "Cymodocea nodosa": 5,
            "Posidonia oceanica": 5,
            "Halophila stipulacea": 5,
            "Espacio vacío": 5,
            "Materia muerta": 5
        }
        
        self.assertEqual(species_counts, expected_counts)
    
    def test_simulate_step(self):
        initial_grid = [
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío"],
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío"]
        ]
        
        # Controla random.choice para Halophila y Materia muerta
        with patch('random.choice', side_effect=["Halophila stipulacea", "Materia muerta", "Espacio vacío", "Espacio vacío"]):
            result_grid = simulate_step(initial_grid)
        
        expected_grid = [
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío"],
            ["Cymodocea nodosa", "Posidonia oceanica", "Espacio vacío", "Espacio vacío", "Espacio vacío"]
        ]
        self.assertEqual(result_grid, expected_grid)

    def test_run_simulation(self):
        initial_grid = [
            ["Cymodocea nodosa", "Posidonia oceanica"],
            ["Halophila stipulacea", "Materia muerta"]
        ]
        steps = 2
        
        # Controla random.choice para las transiciones
        with patch('random.choice', side_effect=["Espacio vacío", "Materia muerta"] * steps):
            simulation_generator = run_simulation(initial_grid, steps)
            result_grids = list(simulation_generator)
        
        # Verifica que la simulación devuelve el número correcto de pasos
        self.assertEqual(len(result_grids), steps)
        self.assertEqual(result_grids[-1], [
            ["Cymodocea nodosa", "Posidonia oceanica"],
            ["Espacio vacío", "Espacio vacío"]
        ])

    def test_set_simulation_speed(self):
        # Verifica que set_simulation_speed devuelve la velocidad configurada cuando es válida
        self.assertEqual(set_simulation_speed(1), 1)
        
        # Verifica que set_simulation_speed lanza ValueError para velocidad no positiva
        with self.assertRaises(ValueError):
            set_simulation_speed(0)
        with self.assertRaises(ValueError):
            set_simulation_speed(-1)

if __name__ == "__main__":
    unittest.main()

