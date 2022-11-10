"""This unit contains a CBV to work with /movies/ routes"""
from flask_restx import Resource, Namespace
from flask import request
from implemented import movies_service
# ------------------------------------------------------------------------
# creation the movie namespace to work with /movies/ routes
movie_ns = Namespace('movies')
# ------------------------------------------------------------------------


@movie_ns.route('/')
class MoviesView(Resource):
    """This class works as a CBV to process requests to routes like
    '/movies/'"""

    def get(self):
        """The method returns a JSON with all movies data

        :returns:
            a tuple containing the JSON and the operation's status code
        """
        search_args = request.args

        all_movies = movies_service.get_all(search_args)

        return all_movies

    def post(self):
        """This method serves to add new movie to database

        :returns:
            a tuple with a result of the operation
        """
        json_data = request.json

        result = movies_service.add_new(json_data)

        return result


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    """The MovieView class is a CBV to work with routes like '/movies/1'"""

    def get(self, movie_id: int):
        """This method works with GET requests

        :param movie_id: an id of searching movie

        :returns:
            a tuple containing the JSON and the operation's status code
        """
        single_movie = movies_service.get_by_id(movie_id)

        return single_movie

    def put(self, movie_id: int):
        """This method serves to update movie's data

        :param movie_id: an id of the updated movie

        :returns:
            a tuple containing status code of the operation and string
        """
        json_data = request.json

        result = movies_service.update(movie_id, json_data)

        return result

    def delete(self, movie_id: int):
        """This method serves to delete movie from database

        :param movie_id: an id of the deleted movie

        :returns:
            a tuple containing status code of the operation and string
        """
        result = movies_service.delete(movie_id)

        return result
