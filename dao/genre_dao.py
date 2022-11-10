"""This unit contains the GenreDao class to work with the genres table"""
from dao.model.genre import Genre, GenreSchema
from dao.director_dao import DirectorDao
# --------------------------------------------------------------------------


class GenreDao(DirectorDao):
    """The GenreDao class was inherited from DirectorDao because both classes
    have the same logic"""
    def __init__(self):
        """Initialization of the GenreDao class"""
        super().__init__()
        self.model = Genre
