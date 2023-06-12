from flask import Flask, render_template, request
from _02_code import recommend, unique_movie_list
from _02b_code import get_moviedetails
from _00_lockfile import acquire_lock, release_lock

app = Flask(__name__)

movies = unique_movie_list()
final_list = []
instance_in_use = False  # Flag to indicate if the instance is already in use

@app.route('/', methods=['GET', 'POST'])
def submit():
    global final_list
    global instance_in_use

    if request.method == 'POST':
        if 'reset' in request.form:
            # Reset the final_list and instance_in_use flag when the reset button is clicked
            final_list = []
            instance_in_use = False
            return render_template('index.html', final_list=final_list, movies=movies, instance_in_use=instance_in_use)

        else:
            if instance_in_use:
                # Display the message on the index.html template if the instance is already in use
                return render_template('index.html', final_list=final_list, movies=movies, instance_in_use=instance_in_use)

            else:
                # Acquire the lock before executing critical code
                acquire_lock()

                try:
                    name = request.form['name']
                    movie_list = recommend(name)
                    movie_list = [name] + movie_list
                    poster_list, info, plot = get_moviedetails(movie_list)
                    final_list = list(zip(movie_list, poster_list, info, plot))
                    return render_template('index.html', final_list=final_list, movies=movies, instance_in_use=instance_in_use)

                finally:
                    # Release the lock after executing critical code
                    release_lock()

    return render_template('index.html', final_list=final_list, movies=movies, instance_in_use=instance_in_use)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
