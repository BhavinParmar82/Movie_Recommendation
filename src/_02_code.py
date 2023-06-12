import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from _01_preprocessing import json_to_string

data = pd.read_csv('./data/tmdb_5000_movies.csv')
data.head()

# create a new string representation of each movie
data['string'] = data.apply(json_to_string, axis=1)

# create a tf-idf vectorizer object
tfidf = TfidfVectorizer(max_features=2000)

# create a data matrix from the overviews
X = tfidf.fit_transform(data['string'])

# Generate a mapping from movie title to index
movie2idx = pd.Series(data.index, index=data['title'])

# Generating unique list of movies
def unique_movie_list():
    movie_list = sorted(data['title'].unique().tolist())
    return movie_list

# create a function that generates recommendations
def recommend(title):
    # get the row in the dataframe for this movie
    idx = movie2idx[title]
    if type(idx) == pd.Series:
        idx = idx.iloc[0]
        
    # calculate the pairwise similarities for this movie
    query = X[idx]
    scores = cosine_similarity(query, X)
    
    # currently the array is 1xN, make it just a 1-D array
    scores = scores.flatten()
    
    plt.plot(scores)
    plt.plot(scores[(-scores).argsort()])
    
    recommended_idx = (-scores).argsort()[1:4]
    
    return data['title'].iloc[recommended_idx].tolist()