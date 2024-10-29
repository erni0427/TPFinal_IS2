import unittest
from module import ParametrosClimaticos, Celda, GridSimulacion

class TestParametrosClimaticos(unittest.TestCase):
    
    def setUp(self):
        self.parametros_climaticos = ParametrosClimaticos()

    def test_configurar_parametros_validos(self):
        # Verifica que la configuración válida de temperatura y salinidad funcione sin errores
        self.parametros_climaticos.configurar_parametros(temperatura=25, salinidad=30)
        self.assertEqual(self.parametros_climaticos.temperatura, 25)
        self.assertEqual(self.parametros_climaticos.salinidad, 30)

    def test_configurar_parametros_invalidos(self):
        # Verifica que se levante un ValueError para valores de temperatura fuera de rango
        with self.assertRaises(ValueError):
            self.parametros_climaticos.configurar_parametros(temperatura=45, salinidad=30)
        
        # Verifica que se levante un ValueError para valores de salinidad fuera de rango
        with self.assertRaises(ValueError):
            self.parametros_climaticos.configurar_parametros(temperatura=25, salinidad=60)

class TestCelda(unittest.TestCase):

    def setUp(self):
        self.celda_cymodocea = Celda("Cymodocea nodosa")
        self.celda_posidonia = Celda("Posidonia oceanica")
        self.celda_halophila = Celda("Halophila stipulacea")

    def test_actualizar_salud_cymodocea(self):
        # Prueba la actualización de salud para Cymodocea nodosa con valores normales y extremos
        self.celda_cymodocea.actualizar_salud(temperatura=25, salinidad=35)
        self.assertEqual(self.celda_cymodocea.salud, 99)
        self.celda_cymodocea.actualizar_salud(temperatura=35, salinidad=45)
        self.assertEqual(self.celda_cymodocea.salud, 89)  # Salud disminuye 10 con alta temperatura y salinidad

    def test_actualizar_salud_posidonia(self):
        # Prueba la actualización de salud para Posidonia oceanica con valores normales y extremos
        self.celda_posidonia.actualizar_salud(temperatura=25, salinidad=30)
        self.assertEqual(self.celda_posidonia.salud, 98)
        self.celda_posidonia.actualizar_salud(temperatura=40, salinidad=15)
        self.assertEqual(self.celda_posidonia.salud, 83)  # Salud disminuye 15 con alta temperatura y baja salinidad

    def test_actualizar_salud_halophila(self):
        # Prueba la actualización de salud para Halophila stipulacea con valores normales y extremos
        self.celda_halophila.actualizar_salud(temperatura=20, salinidad=25)
        self.assertEqual(self.celda_halophila.salud, 99)
        self.celda_halophila.actualizar_salud(temperatura=10, salinidad=35)
        self.assertEqual(self.celda_halophila.salud, 94)  # Salud disminuye 5 con baja temperatura y alta salinidad

    def test_salud_minima(self):
        # Verifica que la salud no caiga por debajo de cero
        for _ in range(20):  # Aplicar múltiples actualizaciones de salud
            self.celda_cymodocea.actualizar_salud(temperatura=40, salinidad=45)
        self.assertEqual(self.celda_cymodocea.salud, 0)

class TestGridSimulacion(unittest.TestCase):

    def setUp(self):
        self.parametros_climaticos = ParametrosClimaticos()
        # Ajustar los parámetros climáticos para forzar un cambio en la salud
        self.parametros_climaticos.configurar_parametros(temperatura=35, salinidad=45)
        self.simulacion = GridSimulacion(tamaño=10, parametros_climaticos=self.parametros_climaticos)

    def test_aplicar_parametros_climaticos(self):
        # Guarda el estado de salud inicial de todas las celdas
        salud_inicial = [[celda.salud for celda in fila] for fila in self.simulacion.cuadricula]
        
        # Aplica los parámetros climáticos y verifica si hubo algún cambio
        self.simulacion.aplicar_parametros_climaticos()
        
        cambio_encontrado = any(
            salud_inicial[i][j] != self.simulacion.cuadricula[i][j].salud
            for i in range(self.simulacion.tamaño)
            for j in range(self.simulacion.tamaño)
        )
        
        self.assertTrue(cambio_encontrado, "La salud de las celdas no se actualizó correctamente con los parámetros climáticos")


if __name__ == '__main__':
    unittest.main()
