"""The unit contains the Director class model and Director schema to
serialize and deserialize models"""
from marshmallow import Schema, fields
from setup_db import db
# -----------------------------------------------------------------------


class Director(db.Model):
    """The Director class is a model to work with a directors table"""
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


class DirectorSchema(Schema):
    """This class is a schema for serializing and deserializing a Director
    class' instances"""
    id = fields.Int()
    name = fields.Str()
