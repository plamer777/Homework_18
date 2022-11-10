"""The main file serves to run the Flask application"""
from config import Config
from utils import create_app
from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns
# --------------------------------------------------------------------------
# creation of the Flask app and registration of namespaces
app = create_app(Config(), [movie_ns, genre_ns, director_ns])
# --------------------------------------------------------------------------

if __name__ == '__main__':
    app.run()
