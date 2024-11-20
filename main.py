from rutas import crear_grafo_transmilenio, ruta_mas_corta, mostrar_ruta

def main():
    print("Bienvenido al sistema de rutas de TransMilenio.\n")

    # Crear el grafo completo
    grafo = crear_grafo_transmilenio()

    # Solicitar origen y destino
    origen = input("Ingrese la estación de origen: ").strip()
    destino = input("Ingrese la estación de destino: ").strip()

    # Validar estaciones
    if origen not in grafo.nodes or destino not in grafo.nodes:
        print("Error: Una o ambas estaciones no existen en el sistema.")
        return

    # Calcular la mejor ruta
    ruta, tiempo = ruta_mas_corta(grafo, origen, destino)

    if ruta:
        print("\nLa mejor ruta encontrada es:")
        print(f" -> {' -> '.join(ruta)}")
        print(f"Tiempo estimado: {tiempo} minutos.\n")

        # Mostrar detalles de las rutas utilizadas
        detalles = mostrar_ruta(grafo, ruta)
        print("Detalles del trayecto:")
        for detalle in detalles:
            print(f"- {detalle}")
    else:
        print("\nNo se encontró una ruta válida entre las estaciones especificadas.\n")

if __name__ == "__main__":
    main()
