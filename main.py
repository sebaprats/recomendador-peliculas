# Librerias 
from fastapi import FastAPI
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# intanciacion de la API
app = FastAPI()
app.title = "Funciones API"


# Lectura de dataset
# ruta_csv = (r"C:\Users\User\Documents\Henry\DataScience\Primer_Proyecto\dataset\movies_dataset_produccion.csv", low_memory=False)
df = pd.read_csv("dataset/movies_dataset_produccion.csv")



# Primera funcion

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    
    meses_validos = [
        'enero', 'febrero', 'marzo', 'abril', 
        'mayo', 'junio', 'julio', 'agosto', 
        'septiembre', 'octubre', 'noviembre', 'diciembre'
    ]
    
    if mes not in meses_validos:
        return f"El mes '{mes}' no es válido. Por favor, ingresa un mes correcto."
    
    cantidad = df[df['release_month'].str.lower() == mes].shape[0]
    
    return f"{cantidad} películas fueron estrenadas en el mes de {mes}."


# Segunda función
@app.get('/añoestreno_y_popularidad/{pelicula}')
def score_titulo(titulo_pelicula: str):
    
    # Filtro el dataframe para encontrar la película por título
    pelicula = df[df['title'].str.lower() == titulo_pelicula]
    
    # Advierto si no encuentra la película
    if pelicula.empty:
        return f"No se encontró ninguna película con el título '{titulo_pelicula}'."
    
    # Obtengo los datos de la película
    titulo_pelicula = pelicula['title'].values[0]
    año_estreno = pelicula['release_year'].values[0]
    score = pelicula['popularity'].values[0]
    
    return f"La película '{titulo_pelicula}' fue estrenada en el año {año_estreno} con un score/popularidad de {score}."


# Tercera función
@app.get('/promedio_valoraciones/{pelicula}')
def votos_titulo(titulo_pelicula: str):
    
    # Filtro el dataframe para encontrar la película por título
    pelicula = df[df['title'].str.lower() == titulo_pelicula]
    
    # Advierto si no encuentra la película
    if pelicula.empty:
        return f"No se encontró ninguna película con el título '{titulo_pelicula}'."
    
    # Obtengo los datos de la película
    titulo_pelicula = pelicula['title'].values[0]
    cantidad_votos = pelicula['vote_count'].values[0]
    
    # Verifico si la cantidad de votos es menor a 10
    if cantidad_votos < 10:
        return f"La película '{titulo_pelicula}' no cuenta con la siguiente cantidad de valoraciones para ser considerada."
    
    promedio_votos = pelicula['vote_average'].values[0]
    
    return f"La película '{titulo_pelicula}' recibió {cantidad_votos} votos y su promedio de valoración fue de {promedio_votos}."

# Función de Recomendacion
@app.get('/recomendacion/{titulo_pelicula}')
def recomendacion(titulo_pelicula: str):
    
    # Convertir el título de la película a minúsculas
    titulo_pelicula = titulo_pelicula.lower()
    
    # Filtro el dataframe para encontrar la película por título
    pelicula = df[df['title'].str.lower().str.contains(titulo_pelicula)]
    
    if pelicula.empty:
        return {"mensaje": f"No se encontró ninguna película con el título '{titulo_pelicula}'."}
    
    tfidf = TfidfVectorizer(stop_words='english')
    
    tfidf_matrix = tfidf.fit_transform(df['overview'] + ' ' + df['genre'] + ' ' + df['country'] + df['vote_average'].astype(str))
    # tfidf_matrix = tfidf.fit_transform(df['overview'] + ' ' + df['genre'] + ' ' + df['country'])
    
    idx = df.index[df['title'].str.lower() == titulo_pelicula].tolist()[0]
    
    sim_scores = list(enumerate(cosine_similarity(tfidf_matrix[idx], tfidf_matrix)[0]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:6]
    
    movie_indices = [i[0] for i in sim_scores]
    similarity_scores = [round(i[1], 5) for i in sim_scores]
    
    return {"películas_recomendadas": df['title'].iloc[movie_indices].tolist(), "score_de_similitud": similarity_scores}

# Para ejecutar el servidor, usa el siguiente comando en tu terminal:
# uvicorn main:app --reload
