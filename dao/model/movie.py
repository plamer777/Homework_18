"""There are the Movie model and the MovieSchema classes to work with the
 movies table"""
from marshmallow import Schema, fields
from setup_db import db
# ------------------------------------------------------------------------


class Movie(db.Model):
    """The Movie class serves to work with the movies table"""
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(100))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))


class MovieSchema(Schema):
    """This class created to serialize and deserialize instances of Movie
    class"""
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
