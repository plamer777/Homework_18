"""This unit contains the Genre model and GenreSchema class to work with
the genres table"""
from marshmallow import Schema, fields
from setup_db import db
# -----------------------------------------------------------------------


class Genre(db.Model):
    """This is a model to get access to a genres' table of the database"""
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))


class GenreSchema(Schema):
    """The GenreSchema is a class for serializing and deserializing Genre
    models"""
    id = fields.Int()
    name = fields.Str()
