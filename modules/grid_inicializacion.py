import numpy as np

# Probabilidades por especie
probabilidades = {
    "Cymodocea nodosa": 0.25,
    "Posidonia oceanica": 0.35,
    "Halophila stipulacea": 0.15,
    "Espacio vacío": 0.15,
    "Materia muerta": 0.10
}

def validar_probabilidades(probabilidades):
    """
    Valida que las probabilidades sumen 100%.
    Lanza una excepción si no es así.
    """
    suma = sum(probabilidades.values())
    if not np.isclose(suma, 1.0):
        raise ValueError(f"Las probabilidades deben sumar 100%, pero suman {suma * 100:.2f}%")

def inicializar_cuadricula(tamano):
    """
    Crea una cuadrícula con especies distribuidas aleatoriamente según las probabilidades.
    
    Argumentos:
    tamano -- Un entero que define el tamaño de la cuadrícula (e.g., 50x50).
    
    Retorna:
    Una matriz 2D representando la cuadrícula inicializada.
    """
    validar_probabilidades(probabilidades)

    # Definimos las especies y sus probabilidades
    especies = list(probabilidades.keys())
    pesos = list(probabilidades.values())

    # Generamos la cuadrícula aleatoriamente
    cuadricula = np.random.choice(especies, size=(tamano, tamano), p=pesos)
    return cuadricula
