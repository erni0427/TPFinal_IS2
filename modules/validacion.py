def validar_probabilidades(probabilidades):
    """
    Valida que las probabilidades de aparición de las especies sumen 100%.
    """
    suma_probabilidades = sum(probabilidades.values())
    if suma_probabilidades != 1.0:
        raise ValueError("Las probabilidades deben sumar 100%.")
