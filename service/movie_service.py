"""This unit provides a business logic to process users requests to /movies/
route"""
from dao.model.movie import MovieSchema
from dao.movie_dao import MovieDao
# -------------------------------------------------------------------------


class MovieService:
    """The MovieService class provides a business logic to work with movies
    table"""
    def __init__(self, dao: MovieDao, schema: MovieSchema) -> None:
        """Initialization of the class

        :param dao: a MovieDao instance
        :param schema: a MovieSchema instance to serialize and deserialize
        models
        """
        self.dao = dao
        self.schema = schema

    def get_all(self, args: dict) -> tuple:
        """This method processes all GET requests to /movies/ route taking into
        account additional parameters

        :param args: parameters parsed from the GET request

        :returns:
            a list of serialized objects
        """
        # checking if any additional parameters present in the GET request
        if 'director_id' in args:
            all_movies = self.dao.get_by_director_id(args.get('director_id'))

        elif 'genre_id' in args:
            all_movies = self.dao.get_by_genre_id(args.get('genre_id'))

        elif 'year' in args:
            all_movies = self.dao.get_by_year(args.get('year'))

        else:
            all_movies = self.dao.get_all()

        if not all_movies:
            return 'Not found', 404

        # serialization of the objects
        movies_list = self.schema.dump(all_movies, many=True)

        return movies_list, 200

    def get_by_id(self, movie_id: int) -> tuple:
        """This method processes GET requests to the routes like /movies/1

        :param movie_id: the id of the searching record

        :returns:
            a dictionary with movie data or 404 error if the movie is not found
        """
        single_movie = self.dao.get_by_id(movie_id)

        if not single_movie:
            return 'Not found', 404

        movie_dict = self.schema.dump(single_movie)

        return movie_dict, 200

    def add_new(self, json_data: dict) -> tuple:
        """This method processes POST requests and adds a new movie to
        the movie table

        :param json_data: a dictionary containing a new movie's data

        :returns:
            a tuple with the result of the operation
        """
        try:
            self.dao.add_new(json_data)

        except Exception as e:

            print(f'При создании модели возникла ошибка {e}')

            return 'Bad request', 400

        # creating a location to add it into headers
        location = f"/movies/{json_data.get('id')}"
        return 'Created', 201, {'Location': location}

    def update(self, movie_id: int, json_data: dict):
        """The method updates a movie's data in the table

        :param movie_id: an id of the updated movie
        :param json_data: a dictionary containing an updated movie's data

        :returns:
            a tuple with the result of the operation
        """
        updated = self.dao.get_by_id(movie_id)

        if not updated:
            return 'Not found', 404

        try:
            for key in json_data:

                # updating all fields presented in json_data
                exec(f'updated.{key} = json_data["{key}"]')

            self.dao.update(updated)

        except Exception as e:

            print(f'При обновлении данных возникла ошибка {e}')
            return 'Bad request', 400

        return '', 204

    def delete(self, movie_id: int):
        """This method deletes a movie from the movie table

        :param movie_id: an id of the deleted movie

        :returns:
            a tuple with the result of the operation
        """
        deleted_movie = self.dao.get_by_id(movie_id)

        if not deleted_movie:
            return 'Not found', 404

        self.dao.delete(deleted_movie)

        return '', 204
