from flask import Flask, render_template, request
from _02_code import recommend, unique_movie_list
#from _02a_code import get_poster
from _02b_code import get_moviedetails

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def submit():
    movies = unique_movie_list()
    movie_list = []
    poster_list = []
    final_list = [[]]
    info = []
    if request.method == 'POST':
        name = request.form['name']
        movie_list = recommend(name)
        movie_list = [name] + movie_list
        poster_list, info = get_moviedetails(movie_list)
        final_list = list(zip(poster_list, movie_list))
        print(final_list[0][0])
    return render_template('index.html', final_list = final_list, movies=movies, info=info)
                 
if __name__ == '__main__':
    app.run(debug=True)