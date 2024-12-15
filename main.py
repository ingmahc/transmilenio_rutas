from rutas import crear_grafo_transmilenio, ruta_mas_corta, mostrar_ruta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Cambiar el backend de matplotlib para evitar el uso de Tkinter
import matplotlib
matplotlib.use('Agg')

def generar_dataset_simulado():
    # Generar estaciones simuladas
    num_estaciones = 50
    estaciones = pd.DataFrame({
        'ID_Estación': range(1, num_estaciones + 1),
        'Nombre': [f'Estación_{i}' for i in range(1, num_estaciones + 1)],
        'Latitud': np.random.uniform(4.5, 4.8, num_estaciones),
        'Longitud': np.random.uniform(-74.1, -73.95, num_estaciones),
        'Líneas': np.random.choice(['Línea A', 'Línea B', 'Línea C', 'Línea D'], num_estaciones),
        'Capacidad': np.random.randint(2000, 6000, num_estaciones),
        'Rendimiento': np.random.randint(1500, 5000, num_estaciones)
    })

    # Generar conexiones simuladas
    num_conexiones = 100
    conexiones = pd.DataFrame({
        'ID_Conexión': range(1, num_conexiones + 1),
        'Estación_Origen': np.random.choice(estaciones['ID_Estación'], num_conexiones),
        'Estación_Destino': np.random.choice(estaciones['ID_Estación'], num_conexiones),
        'Tiempo_Viaje': np.random.randint(3, 15, num_conexiones),
        'Distancia': np.round(np.random.uniform(1.0, 5.0, num_conexiones), 2)
    })

    # Eliminar conexiones donde origen y destino sean iguales
    conexiones = conexiones[conexiones['Estación_Origen'] != conexiones['Estación_Destino']]

    return estaciones, conexiones

def clustering_estaciones(estaciones):
    # Selección de características para clustering
    features = estaciones[['Latitud', 'Longitud', 'Rendimiento']]

    # Escalamiento de las características
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Aplicación de K-Means
    k_optimo = 4
    kmeans = KMeans(n_clusters=k_optimo, random_state=42)
    estaciones['Cluster'] = kmeans.fit_predict(features_scaled)

    # Guardar visualización de clusters en un archivo
    plt.figure(figsize=(8, 6))
    for cluster in range(k_optimo):
        cluster_data = estaciones[estaciones['Cluster'] == cluster]
        plt.scatter(cluster_data['Longitud'], cluster_data['Latitud'], label=f'Cluster {cluster}')
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.title('Clusters de Estaciones de TransMilenio')
    plt.legend()
    plt.savefig('clusters.png')  # Guardar el gráfico como archivo

    return estaciones

def main():
    print("Bienvenido al sistema de rutas y análisis de TransMilenio.\n")

    # Crear el dataset simulado
    estaciones, conexiones = generar_dataset_simulado()

    print("Dataset de Estaciones:")
    print(estaciones.head())

    print("\nDataset de Conexiones:")
    print(conexiones.head())

    # Aplicar clustering a las estaciones
    estaciones = clustering_estaciones(estaciones)

    # Crear el grafo completo (según funcionalidad previa)
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
