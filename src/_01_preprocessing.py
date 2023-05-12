import json

# convert the relevant data for each movie into a single string
def json_to_string(row):
    genres = json.loads(row['genres'])
    genres = ' '.join(''.join(a['name'].split()) for a in genres )
    
    keywords = json.loads(row['keywords'])
    keywords = ' '.join(''.join(a['name'].split()) for a in keywords )

    return "%s %s" %(genres, keywords)
