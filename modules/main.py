# Parámetros de interacción entre especies
interaction_parameters = {
    'Cymodocea_vs_Posidonia': 0.5,
    'Cymodocea_vs_Halophila': 0.3,
    'Posidonia_vs_Halophila': 0.4,
    # Otros parámetros de interacción según necesidad
}

def set_interaction_parameters(params):
    for key, value in params.items():
        if not (0 <= value <= 1):
            raise ValueError(f"El parámetro {key} debe estar entre 0 y 1.")
    return params

# Configura parámetros de interacción con validación
interaction_parameters = set_interaction_parameters(interaction_parameters)