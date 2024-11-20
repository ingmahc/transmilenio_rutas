import networkx as nx

def crear_grafo_transmilenio():
    """Crea un grafo representando todas las rutas de TransMilenio."""
    G = nx.DiGraph()

    # Estaciones y conexiones de ejemplo
    estaciones = [
        'Portal Sur', 'General Santander', 'Calle 40 Sur', 'Venecia',
        'Carrera 30', 'Ricaurte', 'Calle 19', 'Calle 72',
        'Calle 100', 'Portal Norte', 'Calle 26'
    ]
    G.add_nodes_from(estaciones)

    # Conexiones con tiempos estimados y rutas
    conexiones = [
        # Ruta C19
        ('Portal Sur', 'General Santander', {'tiempo': 5, 'ruta': 'C19'}),
        ('General Santander', 'Calle 40 Sur', {'tiempo': 4, 'ruta': 'C19'}),
        ('Calle 40 Sur', 'Venecia', {'tiempo': 3, 'ruta': 'C19'}),
        ('Venecia', 'Carrera 30', {'tiempo': 6, 'ruta': 'C19'}),
        ('Carrera 30', 'Ricaurte', {'tiempo': 8, 'ruta': 'C19'}),
        ('Ricaurte', 'Calle 19', {'tiempo': 7, 'ruta': 'C19'}),
        ('Calle 19', 'Calle 72', {'tiempo': 9, 'ruta': 'C19'}),
        ('Calle 72', 'Calle 100', {'tiempo': 5, 'ruta': 'C19'}),
        ('Calle 100', 'Portal Norte', {'tiempo': 6, 'ruta': 'C19'}),
        # Ruta B23
        ('Portal Norte', 'Calle 100', {'tiempo': 6, 'ruta': 'B23'}),
        ('Calle 100', 'Calle 72', {'tiempo': 5, 'ruta': 'B23'}),
        ('Calle 72', 'Calle 26', {'tiempo': 10, 'ruta': 'B23'}),
        ('Calle 26', 'Ricaurte', {'tiempo': 8, 'ruta': 'B23'}),
        ('Ricaurte', 'Calle 40 Sur', {'tiempo': 7, 'ruta': 'B23'}),
        ('Calle 40 Sur', 'Portal Sur', {'tiempo': 5, 'ruta': 'B23'}),
        # Ruta D21
        ('Portal Sur', 'Venecia', {'tiempo': 3, 'ruta': 'D21'}),
        ('Venecia', 'Calle 26', {'tiempo': 9, 'ruta': 'D21'}),
        ('Calle 26', 'Portal Norte', {'tiempo': 12, 'ruta': 'D21'}),
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


def mostrar_ruta(G, ruta):
    """Muestra las estaciones y las rutas utilizadas en el trayecto."""
    detalles = []
    for i in range(len(ruta) - 1):
        estacion_origen = ruta[i]
        estacion_destino = ruta[i + 1]
        datos = G[estacion_origen][estacion_destino]
        detalles.append(f"{estacion_origen} -> {estacion_destino} (Ruta: {datos['ruta']}, Tiempo: {datos['tiempo']} min)")
    return detalles

