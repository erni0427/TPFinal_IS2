from grid_inicializacion import inicializar_cuadricula

def main():
    # Definir el tamaño de la cuadrícula
    tamano_region = int(input("Ingrese el tamaño de la región (e.g., 50 para una cuadrícula 50x50): "))

    # Inicialización de la cuadrícula
    try:
        cuadricula = inicializar_cuadricula(tamano_region)
        print(f"Cuadrícula inicializada con éxito. Tamaño: {tamano_region}x{tamano_region}")
        print(cuadricula)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()