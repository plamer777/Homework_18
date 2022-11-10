"""The unit contains different settings for the Flask application"""
from constants import DATABASE_URI


class Config:
    """This class serves to provide all necessary settings for a Flask app"""
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
