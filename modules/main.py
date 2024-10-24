from simulation import Simulacion
from visualization import mostrar_simulacion, mostrar_grafico_cobertura
from species import Especie

def correr_escenario_climatico(nombre_escenario, especies):
    # Inicializa la simulación
    sim = Simulacion(50, especies)

    # # Corre la simulación por 80 años
    # sim.correr_simulacion(80)

    # Muestra la simulación con gráfico de barras simultáneo
    mostrar_simulacion(sim.grid_historial, especies, nombre_escenario)

    # Muestra el gráfico final de cobertura
    mostrar_grafico_cobertura(sim.grid_historial, especies)

if __name__ == "__main__":
    # Definimos las especies
    cymodocea = Especie("Cymodocea nodosa", 0.05, 0.02, 3)
    posidonia = Especie("Posidonia oceanica", 0.08, 0.03, 2)
    halophila = Especie("Halophila stipulacea", 0.12, 0.04, 10)

    # Simulación con Cymodocea y Posidonia (dejando Halophila comentada)
    especies_dos = [cymodocea, posidonia]
    correr_escenario_climatico("Escenario RCP 2.6", especies_dos)

    # Simulación con Cymodocea, Posidonia y Halophila
    especies_tres = [cymodocea, posidonia, halophila]
    correr_escenario_climatico("Escenario RCP 8.5", especies_tres)