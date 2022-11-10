"""This unit contains a GenreService to work with /genres/ routes"""
from dao.genre_dao import GenreDao
from dao.model.genre import GenreSchema
from service.director_service import DirectorService
# ------------------------------------------------------------------------


class GenreService(DirectorService):
    """The GenreService class provides a business logic to work with /genres/
    routes"""
    def __init__(self, dao: GenreDao, schema: GenreSchema):
        """The initialization of the GenreService class

        :param dao: the GenreDao instance
        :param schema: the GenreSchema instance
        """
        self.dao = dao
        self.schema = schema
