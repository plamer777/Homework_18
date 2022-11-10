"""There is a MovieDao class in the unit. The class serves to work with
a movies table"""
from setup_db import db
from dao.model.movie import Movie
# ------------------------------------------------------------------------


class MovieDao:
    """The MovieDao class provides a logic to work with movie table"""

    def __init__(self):
        """The initialization method of the MovieDao class. There're fields
        to store objects in the method"""
        self.db = db
        self.model = Movie

    def get_all(self) -> list:
        """This method returns all movies found in table

        :returns:
            movies_list - a list of objects containing movies data or
            an empty list if there are no movies in the table
        """
        all_movies = self.model.query.all()

        return all_movies

    def get_by_id(self, movie_id: int) -> Movie:
        """This method returns a single movie found by its id

        :param movie_id: the id of searching movie

        :returns:
            single_movie - an object containing movie data
        """
        single_movie = self.model.query.get(movie_id)

        return single_movie

    def get_by_director_id(self, director_id: int) -> list:
        """This method returns movies found by the director_id

        :param director_id: an id of the director to search movies by

        :returns:
            found_movies - a list of objects containing movies data
        """
        found_movies = self.model.query.filter(
            self.model.director_id == director_id).all()

        return found_movies

    def get_by_genre_id(self, genre_id: int) -> list:
        """This method returns movies found by the genre_id

        :param genre_id: an id of the genre to search movies by

        :returns:
            found_movies - a list of objects containing movies data
        """
        found_movies = self.model.query.filter(
            self.model.genre_id == genre_id).all()

        return found_movies

    def get_by_year(self, year: int) -> list:
        """This method returns movies found by the certain year

        :param year: the year to search movies by

        :returns:
            found_movies - a list of objects containing movies data
        """
        found_movies = self.model.query.filter(self.model.year == year).all()

        return found_movies

    def add_new(self, json_data: dict) -> None:
        """This method serves to add a new movie in the table

        :param json_data: a dictionary containing movie's data
        """
        new_movie = self.model(**json_data)

        self.db.session.add(new_movie)
        self.db.session.commit()
        self.db.session.close()

    def update(self, movie_obj: Movie) -> None:
        """This method serves to update a movie in the table

        :param movie_obj: an instance of Movie class
        """
        self.db.session.add(movie_obj)
        self.db.session.commit()
        self.db.session.close()

    def delete(self, movie_obj: Movie) -> None:
        """This method serves to delete a movie from the table

        :param movie_obj: an instance of Movie class
        """
        self.db.session.delete(movie_obj)
        self.db.session.commit()
        self.db.session.close()
