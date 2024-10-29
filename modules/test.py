import unittest
from unittest.mock import patch, mock_open
import os
from module import initialize_species_grid, simulate_step, run_simulation, generate_report

class TestInitializeSpeciesGrid(unittest.TestCase):

    def test_initialize_species_grid_size(self):
        rows, cols = 5, 5
        grid = initialize_species_grid(rows, cols)
        self.assertEqual(len(grid), rows)
        self.assertTrue(all(len(row) == cols for row in grid))

    def test_initialize_species_grid_content(self):
        rows, cols = 10, 10
        valid_species = {"Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Espacio vacío", "Materia muerta"}
        grid = initialize_species_grid(rows, cols)
        for row in grid:
            for cell in row:
                self.assertIn(cell, valid_species)

class TestSimulateStep(unittest.TestCase):

    def test_simulate_step_transitions(self):
        initial_grid = [
            ["Cymodocea nodosa", "Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío"]
        ]
        expected_grid = [
            ["Posidonia oceanica", "Halophila stipulacea", "Materia muerta", "Espacio vacío", "Espacio vacío"]
        ]
        new_grid = simulate_step(initial_grid)
        self.assertEqual(new_grid, expected_grid)

class TestRunSimulation(unittest.TestCase):

    @patch("builtins.print")  
    @patch("time.sleep", return_value=None)  
    def test_run_simulation_execution(self, mock_sleep, mock_print):
        rows, cols, steps = 5, 5, 2
        grid = initialize_species_grid(rows, cols)
        run_simulation(grid, steps)
        
        # Calcular el número esperado de llamadas a print
        # Cada paso tiene una línea de encabezado y `rows` líneas para las filas de la cuadrícula
        # Agregamos una llamada final para el mensaje "Simulación completada"
        expected_print_calls = (rows + 1) * steps + 2  # +2 para "Simulación completada" y el encabezado final
        self.assertEqual(mock_print.call_count, expected_print_calls)


class TestGenerateReport(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_generate_report_file_creation(self, mock_file):
        report = [
            [["Cymodocea nodosa", "Posidonia oceanica"], ["Halophila stipulacea", "Materia muerta"]],
            [["Posidonia oceanica", "Halophila stipulacea"], ["Materia muerta", "Espacio vacío"]]
        ]
        generate_report(report)
        mock_file.assert_called_once_with("simulation_report.txt", "w")
        
    @patch("builtins.open", new_callable=mock_open)
    def test_generate_report_content(self, mock_file):
        report = [
            [["Cymodocea nodosa", "Posidonia oceanica"], ["Halophila stipulacea", "Materia muerta"]],
            [["Posidonia oceanica", "Halophila stipulacea"], ["Materia muerta", "Espacio vacío"]]
        ]
        generate_report(report)
        
        handle = mock_file()
        expected_calls = [
            "\nCiclo 1:\n", "C P\n", "H M\n",
            "\nCiclo 2:\n", "P H\n", "M E\n"
        ]
        handle.write.assert_has_calls([unittest.mock.call(line) for line in expected_calls], any_order=False)

if __name__ == "__main__":
    unittest.main()