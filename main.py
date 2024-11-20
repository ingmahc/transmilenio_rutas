from rutas import crear_grafo_c19, encontrar_mejor_ruta_transmilenio

def main():
    print("Bienvenido al sistema de rutas de TransMilenio (C19).\n")

    # Crear el grafo de la ruta C19
    grafo_c19 = crear_grafo_c19()

    # Definir origen y destino
    origen = 'Portal Sur'
    destino = 'Calle 100'

    # Encontrar la mejor ruta
    encontrar_mejor_ruta_transmilenio(grafo_c19, origen, destino)

if __name__ == "__main__":
    main()
