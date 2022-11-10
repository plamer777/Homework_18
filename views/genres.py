"""This unit contains CBVs to process requests at /genres/ routes"""
from flask_restx import Resource, Namespace
from implemented import genre_service
# -----------------------------------------------------------------------
# creation a genre namespace
genre_ns = Namespace('genres')
# -----------------------------------------------------------------------


@genre_ns.route('/')
class GenresView(Resource):
    """This class is a CBV to work with /genres/ route"""
    def get(self):

        all_genres = genre_service.get_all()

        return all_genres


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    """This class is a CBV to work with routes like /genres/1"""
    def get(self, genre_id: int):

        single_genre = genre_service.get_one(genre_id)

        return single_genre
