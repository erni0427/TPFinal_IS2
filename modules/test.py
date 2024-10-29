from module import set_interaction_parameters
import unittest

class TestInteractionParameters(unittest.TestCase):

    def test_valid_interaction_parameters(self):
        """Prueba con parámetros válidos dentro del rango 0 a 1."""
        params = {
            'Cymodocea_vs_Posidonia': 0.5,
            'Cymodocea_vs_Halophila': 0.3,
            'Posidonia_vs_Halophila': 0.4,
        }
        result = set_interaction_parameters(params)
        self.assertEqual(result, params)  # Verifica que el resultado coincide con los parámetros dados

    def test_invalid_interaction_parameters_negative(self):
        """Prueba que lanza ValueError si algún parámetro es menor que 0."""
        params = {
            'Cymodocea_vs_Posidonia': -0.1,
            'Cymodocea_vs_Halophila': 0.3,
            'Posidonia_vs_Halophila': 0.4,
        }
        with self.assertRaises(ValueError) as context:
            set_interaction_parameters(params)
        self.assertIn("debe estar entre 0 y 1", str(context.exception))

    def test_invalid_interaction_parameters_above_one(self):
        """Prueba que lanza ValueError si algún parámetro es mayor que 1."""
        params = {
            'Cymodocea_vs_Posidonia': 0.5,
            'Cymodocea_vs_Halophila': 1.2,
            'Posidonia_vs_Halophila': 0.4,
        }
        with self.assertRaises(ValueError) as context:
            set_interaction_parameters(params)
        self.assertIn("debe estar entre 0 y 1", str(context.exception))

    def test_empty_interaction_parameters(self):
        """Prueba que retorna un diccionario vacío si se pasan parámetros vacíos."""
        params = {}
        result = set_interaction_parameters(params)
        self.assertEqual(result, {})  # Verifica que retorna un diccionario vacío sin errores

# Ejecución de las pruebas
if __name__ == '__main__':
    unittest.main()
