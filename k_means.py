import pandas as pd
from sklearn.cluster import KMeans

#Obtención del set de datos

dataset = pd.read_csv('./In/PokemonDb.csv') #Ubicación del dataset
df = pd.DataFrame(dataset)   
df = df.drop(['Name', 'Variation', 'Type1', 'Type2'], axis=1 )


#Algoritmo de K-means

kmeans = KMeans(n_clusters=6, random_state=1).fit(df) #Usar n_clusters para el númer de grupos deseados, random_state se define con cualquier número para asegurar los mismos resultados

#Estas líneas son para darle estética de impresión en la terminal

print('='*64) 
print('Total de grupos:', len(kmeans.cluster_centers_))
print('='*64)

#Predicción y obtención de resultados

dataset['grupo'] = kmeans.predict(df) #Nombre de la nueva columna donde pondremos nuestra predicción de algoritmo
dataset.to_csv('./Output/groups.csv', index=False, header=True) #Creación de archivo en carpeta destino

#Imprimir grupos obtenidos

grouped_df = dataset.groupby(['grupo']) 
for key, group in grouped_df:  #Muestra cada grupo
    print(grouped_df.get_group(key), "\n\n", '='*180)  

print('El Archivo "groups.csv" ha sido creado con éxito en la carpeta "out".')




