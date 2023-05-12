# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 08:34:14 2023

@author: Bhavin
"""

import pandas as pd
import json

import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

data = pd.read_csv('C:/Users/bhavi/Projects_Part2/TMDB 5000 Movies/tmdb_5000_movies.csv')
data.head()

# convert the relevant data for each movie into a single string
def json_to_string(row):
    genres = json.loads(row['genres'])
    genres = ' '.join(''.join(a['name'].split()) for a in genres )
    
    keywords = json.loads(row['keywords'])
    keywords = ' '.join(''.join(a['name'].split()) for a in keywords )

    return "%s %s" %(genres, keywords)

# create a new string representation of each movie
data['string'] = data.apply(json_to_string, axis=1)

# create a tf-idf vectorizer object
tfidf = TfidfVectorizer(max_features=2000)

# create a data matrix from the overviews
X = tfidf.fit_transform(data['string'])
X

# Generate a mapping from movie title to index
movie2idx = pd.Series(data.index, index=data['title'])
movie2idx

idx = movie2idx['Stuart Little']
idx

query = X[idx]
query

query.toarray()

# compute similarity between query and every vector in X
scores = cosine_similarity(query, X)
scores

# currently the array is 1xN, make it just a 1-D array
scores = scores.flatten()

plt.plot(scores)

(-scores).argsort()

plt.plot(scores[(-scores).argsort()])

# get top 5 matches excluding the query one
recommended_idx = (-scores).argsort()[1:6]

data['title'].iloc[recommended_idx]

# convert indices back to titles
data['title'].iloc[recommended_idx]

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
    
    recommended_idx = (-scores).argsort()[1:6]
    
    return data['title'].iloc[recommended_idx]

recommend('Bubble Boy')
    
    
    
    
    
    