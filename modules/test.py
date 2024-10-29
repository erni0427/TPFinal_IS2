import unittest
import numpy as np
from module import initialize_grid, validate_probabilities
class TestSeagrassGrid(unittest.TestCase):
    
    def setUp(self):
        self.grid_size = (50, 50)
        self.probabilities = {
            'Cymodocea': 0.25,
            'Posidonia': 0.35,
            'Halophila': 0.15,
            'Empty': 0.15,
            'DeadMatta': 0.10
        }

    def test_validate_probabilities(self):
        # Verifica que las probabilidades sumen 1.0
        total = sum(self.probabilities.values())
        self.assertAlmostEqual(total, 1.0, msg="Las probabilidades no suman 100%")

    def test_initialize_grid_size(self):
        # Verifica que la cuadrícula generada tenga el tamaño especificado
        grid = initialize_grid(self.grid_size, self.probabilities)
        self.assertEqual(grid.shape, self.grid_size, msg="La cuadrícula no tiene el tamaño correcto")

    def test_initialize_grid_species(self):
        # Verifica que todas las especies estén presentes en la cuadrícula generada
        grid = initialize_grid(self.grid_size, self.probabilities)
        unique_species = set(np.unique(grid))
        expected_species = set(self.probabilities.keys())
        self.assertTrue(unique_species.issubset(expected_species), msg="No todas las especies están presentes en la cuadrícula")

    def test_invalid_probabilities(self):
        # Verifica que se genere un error si las probabilidades no suman 1.0
        invalid_probabilities = {
            'Cymodocea': 0.3,
            'Posidonia': 0.3,
            'Halophila': 0.2,
            'Empty': 0.1,
            'DeadMatta': 0.2
        }
        with self.assertRaises(ValueError, msg="Las probabilidades no suman 100%"):
            validate_probabilities(invalid_probabilities)

if __name__ == '__main__':
    unittest.main()
