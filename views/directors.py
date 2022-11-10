"""There're two CBVs in the unit to work with routes like /directors/ and
/directors/1"""
from flask_restx import Resource, Namespace
from implemented import director_service
# ------------------------------------------------------------------------
# creation of the directors namespace
director_ns = Namespace('directors')
# ------------------------------------------------------------------------


@director_ns.route('/')
class DirectorsView(Resource):
    """This class processes requests for '/' route"""
    def get(self):

        all_directors = director_service.get_all()

        return all_directors


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    """This class serves to work with routes having ids and can process
    GET, PUT, DELETE requests"""
    def get(self, director_id: int):

        single_director = director_service.get_one(director_id)

        return single_director
