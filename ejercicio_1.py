#importar librerias
import pandas as pd
import json

# ruta del archivo JSON
json_file_path = 'taylor_swift_spotify.json'

# leo el contenido del archivo
# se abre el archivo JSON en modo de lectura ('r') y leemos su contenido.
# esto nos da una cadena que contiene la representación del archivo JSON.

with open(json_file_path, 'r') as file:
    json_data = file.read()

# Cargo el JSON en un diccionario
data = json.loads(json_data)

# normalizar el diccionario a un DataFrame de pandas
canciones_taylor = pd.json_normalize(data, record_path=['albums', 'tracks'], 
                       meta=['artist_id', 'artist_name', 'artist_popularity', 
                             ['albums', 'album_id'], ['albums', 'album_name'], ['albums', 'album_release_date'], ['albums', 'album_total_tracks']])

# cambio nombre de las columnas
canciones_taylor = canciones_taylor.rename(columns={
    'albums.album_id': 'album_id',
    'albums.album_name': 'album_name',
    'albums.album_release_date': 'album_release_date',
    'albums.album_total_tracks': 'album_total_tracks'
})

# Guardo el DataFrame como un archivo CSV
canciones_taylor.to_csv('canciones_taylor.csv', index=False)