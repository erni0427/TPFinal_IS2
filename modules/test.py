from module import initialize_species_grid, simulate_step, run_real_time_simulation,save_simulation_report
import unittest
from unittest.mock import patch, mock_open
import os

# Importa el código que deseas probar aquí (si está en otro archivo, usa: from filename import function)

class TestSimulation(unittest.TestCase):

    def test_initialize_species_grid(self):
        rows, cols = 5, 5
        grid = initialize_species_grid(rows, cols)
        
        # Verifica que el tamaño de la cuadrícula sea el esperado
        self.assertEqual(len(grid), rows)
        self.assertTrue(all(len(row) == cols for row in grid))
        
        # Verifica que todas las celdas contengan solo los valores esperados
        valid_species = {"Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Espacio vacío", "Materia muerta"}
        for row in grid:
            for cell in row:
                self.assertIn(cell, valid_species)

    def test_simulate_step(self):
        initial_grid = [
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío"],
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío"]
        ]
        
        expected_grid = [
            ["Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío", "Espacio vacío"],
            ["Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío", "Espacio vacío"]
        ]
        
        result_grid = simulate_step(initial_grid)
        self.assertEqual(result_grid, expected_grid)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_simulation_report(self, mock_file):
        # Simulación de un reporte para guardar
        report = [
            [["Cymodocea nodosa", "Posidonia oceanica"]],
            [["Halophila stipulacea", "Materia muerta"]],
            [["Espacio vacío", "Espacio vacío"]]
        ]
        
        # Llamamos a la función que debería crear el archivo
        save_simulation_report(report)
        
        # Comprueba que el archivo fue abierto en modo escritura
        mock_file.assert_called_once_with("real_time_simulation_report.txt", "w")
        
        # Genera el contenido esperado que debería haber sido escrito en el archivo
        expected_calls = [
            "\nCiclo 1:\n", "C P\n",
            "\nCiclo 2:\n", "H M\n",
            "\nCiclo 3:\n", "E E\n"
        ]
        
        # Verifica que el contenido fue escrito en el orden correcto
        mock_file().write.assert_has_calls([unittest.mock.call(line) for line in expected_calls])


# Ejecuta las pruebas
if __name__ == "__main__":
    unittest.main()
