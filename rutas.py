import networkx as nx

def crear_grafo_c19():
    """Crea el grafo representando la ruta C19 de TransMilenio."""
    G = nx.DiGraph()

    # Estaciones de la ruta C19
    estaciones = [
        'Portal Sur', 'General Santander', 'Calle 40 Sur', 'Venecia',
        'Carrera 30', 'Ricaurte', 'Calle 19', 'Calle 72',
        'Calle 100', 'Portal Norte'
    ]
    G.add_nodes_from(estaciones)

    # Conexiones con tiempos estimados
    conexiones = [
        ('Portal Sur', 'General Santander', {'tiempo': 5, 'linea': 'C19'}),
        ('General Santander', 'Calle 40 Sur', {'tiempo': 4, 'linea': 'C19'}),
        ('Calle 40 Sur', 'Venecia', {'tiempo': 3, 'linea': 'C19'}),
        ('Venecia', 'Carrera 30', {'tiempo': 6, 'linea': 'C19'}),
        ('Carrera 30', 'Ricaurte', {'tiempo': 8, 'linea': 'C19'}),
        ('Ricaurte', 'Calle 19', {'tiempo': 7, 'linea': 'C19'}),
        ('Calle 19', 'Calle 72', {'tiempo': 9, 'linea': 'C19'}),
        ('Calle 72', 'Calle 100', {'tiempo': 5, 'linea': 'C19'}),
        ('Calle 100', 'Portal Norte', {'tiempo': 6, 'linea': 'C19'}),
    ]
    G.add_edges_from(conexiones)

    return G
def ruta_mas_corta(G, origen, destino):
    """Encuentra la ruta más corta en tiempo."""
    try:
        ruta = nx.dijkstra_path(G, origen, destino, weight='tiempo')
        tiempo_total = nx.dijkstra_path_length(G, origen, destino, weight='tiempo')
        return ruta, tiempo_total
    except nx.NetworkXNoPath:
        return None, float('inf')

def encontrar_mejor_ruta_transmilenio(G, origen, destino):
    """Determina la mejor ruta en TransMilenio basada en el tiempo."""
    ruta, tiempo = ruta_mas_corta(G, origen, destino)
    if ruta:
        print(f"La mejor ruta desde {origen} hasta {destino} es:")
        print(f" -> {' -> '.join(ruta)}")
        print(f"Tiempo estimado: {tiempo} minutos.")
    else:
        print(f"No hay una ruta disponible entre {origen} y {destino}.")
    return ruta
