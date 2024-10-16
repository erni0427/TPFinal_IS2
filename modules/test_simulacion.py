import unittest
from simulacion import initialize_grid, apply_climate_scenario
from parametros import climate_scenarios, species_params


class TestSimulacion(unittest.TestCase):
    def test_initialize_grid(self):
        grid = initialize_grid(10, {"Cymodocea nodosa": 0.3, "Posidonia oceanica": 0.3,
                                    "Halophila stipulacea": 0.2, "empty": 0.1, "dead_matte": 0.1})
        self.assertEqual(grid.shape, (10, 10))

    def test_apply_climate_scenario(self):
        original_growth = species_params["Halophila stipulacea"]["growth_rate"]
        apply_climate_scenario(climate_scenarios["RCP 8.5"])
        self.assertNotEqual(original_growth, species_params["Halophila stipulacea"]["growth_rate"])

if __name__ == '__main__':
    unittest.main()
