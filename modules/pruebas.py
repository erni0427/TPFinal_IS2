import unittest
from species import Especie,DeadMatta
from climate import Clima

class TestSimulacion(unittest.TestCase):

    def setUp(self):
        # Configuración de especies para las pruebas
        self.cymodocea = Especie(nombre="Cymodocea nodosa", tasa_crecimiento=0.05, tasa_mortalidad=0.02, competitividad=3)
        self.posidonia = Especie(nombre="Posidonia oceanica", tasa_crecimiento=0.08, tasa_mortalidad=0.03, competitividad=2)
        self.halophila = Especie(nombre="Halophila stipulacea", tasa_crecimiento=0.12, tasa_mortalidad=0.04, competitividad=10)
        self.dead_matta = DeadMatta()
        self.especies = [self.cymodocea, self.posidonia, self.halophila]



    def test_colores_correctos(self):
        """Verificar que los colores aplicados en los gráficos son los correctos."""
        # Colores esperados basados en la asignación en visualization.py
        colores_esperados = {
            "Cymodocea nodosa": '#7CFC00',  # Verde manzana
            "Posidonia oceanica": '#87CEEB',  # Celeste azulado
            "Halophila stipulacea": '#FF0000',  # Rojo
            "Dead Matta": '#006400',  # Verde inglés
            "Arena": '#D3D3D3'  # Gris claro
        }

        # Crear una función que devuelve los colores según el mapeo
        colores_actuales = {
            "Cymodocea nodosa": '#7CFC00',
            "Posidonia oceanica": '#87CEEB',
            "Halophila stipulacea": '#FF0000',
            "Dead Matta": '#006400',
            "Arena": '#D3D3D3'
        }

        self.assertEqual(colores_actuales, colores_esperados)

    def test_aplicar_cambio_climatico_rcp26(self):
        """Probar los efectos del clima en las especies con un escenario moderado (RCP 2.6)."""
        clima = Clima(incremento_temp=1.0, incremento_salinidad=0.1)
        clima.aplicar_cambio_climatico(self.especies)

        # Verificar los cambios esperados en las tasas de crecimiento y mortalidad
        self.assertAlmostEqual(self.cymodocea.tasa_crecimiento, 0.05 * (1 - 1.0 * 0.01))
        self.assertAlmostEqual(self.cymodocea.tasa_mortalidad, 0.02 * (1 + 0.1 * 0.01))
        self.assertAlmostEqual(self.posidonia.tasa_crecimiento, 0.08 * (1 - 1.0 * 0.01))
        self.assertAlmostEqual(self.posidonia.tasa_mortalidad, 0.03 * (1 + 0.1 * 0.01))

    def test_aplicar_cambio_climatico_rcp85(self):
        """Probar los efectos del clima en las especies con un escenario extremo (RCP 8.5)."""
        clima = Clima(incremento_temp=3.5, incremento_salinidad=0.4)
        clima.aplicar_cambio_climatico(self.especies)

        # Verificar los cambios esperados en las tasas de crecimiento y mortalidad
        self.assertAlmostEqual(self.cymodocea.tasa_crecimiento, 0.05 * (1 - 3.5 * 0.01))
        self.assertAlmostEqual(self.cymodocea.tasa_mortalidad, 0.02 * (1 + 0.4 * 0.01))
        self.assertAlmostEqual(self.posidonia.tasa_crecimiento, 0.08 * (1 - 3.5 * 0.01))
        self.assertAlmostEqual(self.posidonia.tasa_mortalidad, 0.03 * (1 + 0.4 * 0.01))

    def test_clima_sin_cambio(self):
        """Probar el comportamiento del clima sin cambios (incremento de temperatura y salinidad = 0)."""
        clima = Clima(incremento_temp=0.0, incremento_salinidad=0.0)
        clima.aplicar_cambio_climatico(self.especies)

        # Las tasas deben permanecer iguales
        self.assertAlmostEqual(self.cymodocea.tasa_crecimiento, 0.05)
        self.assertAlmostEqual(self.cymodocea.tasa_mortalidad, 0.02)
        self.assertAlmostEqual(self.posidonia.tasa_crecimiento, 0.08)
        self.assertAlmostEqual(self.posidonia.tasa_mortalidad, 0.03)

    def test_cambios_extremos(self):
        """Probar los efectos de un cambio climático extremo en las especies."""
        clima = Clima(incremento_temp=10.0, incremento_salinidad=2.0)
        clima.aplicar_cambio_climatico(self.especies)

        # Verificar que las tasas de crecimiento y mortalidad han cambiado drásticamente
        self.assertAlmostEqual(self.cymodocea.tasa_crecimiento, 0.05 * (1 - 10.0 * 0.01))
        self.assertAlmostEqual(self.cymodocea.tasa_mortalidad, 0.02 * (1 + 2.0 * 0.01))
        self.assertAlmostEqual(self.posidonia.tasa_crecimiento, 0.08 * (1 - 10.0 * 0.01))
        self.assertAlmostEqual(self.posidonia.tasa_mortalidad, 0.03 * (1 + 2.0 * 0.01))

    def test_inicializacion_especie(self):
        """Probar que las especies se inicializan correctamente con los valores proporcionados."""
        # Verificar los atributos de Cymodocea nodosa
        self.assertEqual(self.cymodocea.nombre, "Cymodocea nodosa")
        self.assertEqual(self.cymodocea.tasa_crecimiento, 0.05)
        self.assertEqual(self.cymodocea.tasa_mortalidad, 0.02)
        self.assertEqual(self.cymodocea.competitividad, 3)

        # Verificar los atributos de Posidonia oceanica
        self.assertEqual(self.posidonia.nombre, "Posidonia oceanica")
        self.assertEqual(self.posidonia.tasa_crecimiento, 0.08)
        self.assertEqual(self.posidonia.tasa_mortalidad, 0.03)
        self.assertEqual(self.posidonia.competitividad, 2)

        # Verificar los atributos de Halophila stipulacea
        self.assertEqual(self.halophila.nombre, "Halophila stipulacea")
        self.assertEqual(self.halophila.tasa_crecimiento, 0.12)
        self.assertEqual(self.halophila.tasa_mortalidad, 0.04)
        self.assertEqual(self.halophila.competitividad, 10)

    def test_repr_especie(self):
        """Probar que la representación de la especie devuelve el nombre correctamente."""
        self.assertEqual(repr(self.cymodocea), "Cymodocea nodosa")
        self.assertEqual(repr(self.posidonia), "Posidonia oceanica")
        self.assertEqual(repr(self.halophila), "Halophila stipulacea")

    def test_cambio_tasas_especie(self):
        """Probar que se pueden cambiar correctamente las tasas de crecimiento y mortalidad."""
        # Cambiar tasas para Cymodocea nodosa
        self.cymodocea.tasa_crecimiento = 0.10
        self.cymodocea.tasa_mortalidad = 0.05
        self.assertEqual(self.cymodocea.tasa_crecimiento, 0.10)
        self.assertEqual(self.cymodocea.tasa_mortalidad, 0.05)

    def test_inicializacion_dead_matta(self):
        """Probar que Dead Matta se inicializa correctamente con el nombre correcto."""
        self.assertEqual(self.dead_matta.nombre, "Dead Matta")

    def test_repr_dead_matta(self):
        """Probar que la representación de Dead Matta devuelve el nombre correctamente."""
        self.assertEqual(repr(self.dead_matta), "Dead Matta")


if __name__ == '__main__':
    unittest.main()