import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Selección de características para el clustering
features = estaciones[['Latitud', 'Longitud', 'Rendimiento']]

# Escalamiento de las características
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Determinación del número óptimo de clusters usando el método del codo
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

# Visualización del método del codo
plt.figure(figsize=(8, 4))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Número de clusters')
plt.ylabel('Inercia')
plt.title('Método del Codo para Determinar K Óptimo')
plt.show()

# Aplicación de K-Means con K=4 (ejemplo)
k_optimo = 4
kmeans = KMeans(n_clusters=k_optimo, random_state=42)
estaciones['Cluster'] = kmeans.fit_predict(features_scaled)

# Visualización de los clusters en el espacio geográfico
plt.figure(figsize=(8, 6))
for cluster in range(k_optimo):
    cluster_data = estaciones[estaciones['Cluster'] == cluster]
    plt.scatter(cluster_data['Longitud'], cluster_data['Latitud'], label=f'Cluster {cluster}')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Clusters de Estaciones de TransMilenio')
plt.legend()
plt.show()

# Análisis de los clusters
print("\nDescripción de los Clusters:")
print(estaciones.groupby('Cluster').agg({
    'Latitud': 'mean',
    'Longitud': 'mean',
    'Rendimiento': ['mean', 'median', 'max']
}))
