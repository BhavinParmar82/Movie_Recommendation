from flask import Flask, render_template, request
import os
from _02_code import recommend

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def submit():
    movie_list = None
    if request.method == 'POST':
        name = request.form['name']
        movie_list = recommend(name)
        movie_list = movie_list.tolist()
    return render_template('index.html', movie_list = movie_list)
                 
if __name__ == '__main__':
    app.run(debug=True)