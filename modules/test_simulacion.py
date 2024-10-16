import unittest
from simulacion import initialize_grid, apply_climate_scenario
from parametros import climate_scenarios, species_params


# class TestSimulacion(unittest.TestCase):
#     def test_initialize_grid(self):
#         grid = initialize_grid(10, {"Cymodocea nodosa": 0.3, "Posidonia oceanica": 0.3,
#                                     "Halophila stipulacea": 0.2, "empty": 0.1, "dead_matte": 0.1})
#         self.assertEqual(grid.shape, (10, 10))

#     def test_apply_climate_scenario(self):
#         original_growth = species_params["Halophila stipulacea"]["growth_rate"]
#         apply_climate_scenario(climate_scenarios["RCP 8.5"])
#         self.assertNotEqual(original_growth, species_params["Halophila stipulacea"]["growth_rate"])

# if __name__ == '__main__':
#     unittest.main()

class TestSimulacion(unittest.TestCase):
    """Pruebas unitarias para validar el sistema."""
    
    def setUp(self):
        self.clima = Clima(1.0, 0.1)
        self.especie = FabricaEspecies.crear_especie("Posidonia oceanica")

    def test_crear_especie(self):
        """Verifica la creación correcta de una especie."""
        self.assertEqual(self.especie.nombre, "Posidonia oceanica")

    def test_ajuste_climatico(self):
        """Verifica el impacto del cambio climático."""
        self.especie.growth_rate = 0.1
        self.clima.temp_increase = 2.0
        self.especie.growth_rate *= (1 - self.clima.temp_increase * 0.01)
        self.assertAlmostEqual(self.especie.growth_rate, 0.098)