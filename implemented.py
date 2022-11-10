"""This unit provides different objects like DAOs, Services, etc."""
from dao.movie_dao import MovieDao
from dao.director_dao import DirectorDao
from dao.model.director import DirectorSchema
from dao.genre_dao import GenreDao, GenreSchema
from service.genre_service import GenreService
from service.movie_service import MovieService, MovieSchema
from service.director_service import DirectorService
# ----------------------------------------------------------------------

# movies' DAO, service and schema creation
movies_dao = MovieDao()
movie_schema = MovieSchema()
movies_service = MovieService(movies_dao, movie_schema)

# creation of GenreDao, GenreService and GenreSchema instances
genres_dao = GenreDao()
genre_schema = GenreSchema()
genre_service = GenreService(genres_dao, genre_schema)

# creation of DirectorDao, DirectorService and DirectorSchema instances
directors_dao = DirectorDao()
director_schema = DirectorSchema()
director_service = DirectorService(directors_dao, director_schema)
