import pandas as pd
import json

# Carregando os dados
credits = pd.read_csv('/mnt/data/tmdb_5000_credits.csv')

# Função para extrair o elenco de cada filme
def extract_cast(cast_json):
    cast_list = json.loads(cast_json)
    return ", ".join([actor['name'] for actor in cast_list])

# Aplicando a função para criar uma nova coluna com os nomes do elenco
credits['cast_names'] = credits['cast'].apply(extract_cast)

# Exibindo as primeiras cinco linhas para os títulos dos filmes e nomes do elenco
print(credits[['title', 'cast_names']].head())

# Função para extrair os dados necessários para o desafio
def challenge_representation(row):
    cast_list = json.loads(row['cast'])
    return [(row['title'], actor['name']) for actor in cast_list[:5]]  # Limitando a 5 atores por filme para simplicidade

# Aplicando a função e explodindo os resultados para criar uma lista
challenge_output = credits.apply(challenge_representation, axis=1).explode().dropna()

# Mostrando as primeiras cinco linhas do desafio
print(challenge_output.head(5))
