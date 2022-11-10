"""The unit serves to provide SQLAlchemy class instance to get access to
database from any file of the application"""
from flask_sqlalchemy import SQLAlchemy
# ------------------------------------------------------------------------

db = SQLAlchemy()
