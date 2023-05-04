import pandas as pd

# Cargar el archivo csv en un DataFrame
datos = pd.read_csv('imdb_top_1000.csv')

# Dividir la columna "Generos" en diferentes columnas
generos_sep = datos['Genre'].str.split(',', expand=True)

# Renombrar las nuevas columnas
generos_sep = generos_sep.add_prefix('Genre_')

# Combinar las nuevas columnas con el DataFrame original
datos = pd.concat([datos, generos_sep], axis=1)

# Eliminar la columna original "Generos" si se desea
datos.drop('Genre', axis=1, inplace=True)