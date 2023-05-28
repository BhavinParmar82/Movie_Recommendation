from flask import Flask, render_template, request
from _02_code import recommend, unique_movie_list
#from _02a_code import get_poster
from _02b_code import get_moviedetails

app = Flask(__name__)

'''
@app.route('/', methods = ['POST'])
def submit():
    movies = unique_movie_list()
    movie_list = []
    poster_list = []
    final_list = []
    info = [[]]
    plot = []
    if request.method == 'POST':
        name = request.form['name']
        movie_list = recommend(name)
        movie_list = [name] + movie_list
        poster_list, info, plot = get_moviedetails(movie_list)
        final_list = list(zip(movie_list, poster_list, info, plot))
    return render_template('index.html', final_list = final_list, movies=movies)
'''

movies=unique_movie_list()
final_list = []

@app.route('/', methods=['GET', 'POST'])
def submit():
    global final_list

    if request.method == 'POST':
        if 'reset' in request.form:
            # Reset the final_list when the reset button is clicked
            final_list = []
            return render_template('index.html', final_list=final_list, movies=movies)

        else:
            name = request.form['name']
            movie_list = recommend(name)
            movie_list = [name] + movie_list
            poster_list, info, plot = get_moviedetails(movie_list)
            final_list = list(zip(movie_list, poster_list, info, plot))
            return render_template('index.html', final_list=final_list, movies=movies)

    return render_template('index.html', final_list=final_list, movies=movies)

    
if __name__ == '__main__':
    app.run(debug=True)