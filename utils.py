"""The unit contains utility functions to load data from the JSON, create a
Flask app, create a database and to fill it up"""
import json
from flask import Flask
from flask_restx import Api
from setup_db import db
from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre
from constants import JSON_DATA_PATH, DB_PATH
# ------------------------------------------------------------------------


def load_from_json(filename: str) -> dict:
    """This function loads a data from JSON file

    :param filename: a path to the json file

    :returns:
        a dict or list with data
    """
    try:
        with open(filename, encoding='utf-8') as fin:

            json_data = json.load(fin)

    except FileNotFoundError:
        print('Запрашиваемый файл не найден')
        return {}

    except json.JSONDecodeError as e:
        print(f'Ошибка декодирования JSON {e}')
        return {}

    return json_data


def create_app(config_object, namespaces: list) -> Flask:
    """This function creates a Flask application

    :param config_object: a class to configure Flask application
    :param namespaces: a list of namespaces

    :returns:
        app - a configured Flask instance
    """
    app = Flask(__name__, instance_path=DB_PATH)
    app.config.from_object(config_object)
    app.app_context().push()
    register_extensions(app, namespaces)

    return app


def register_extensions(app: Flask, namespaces: list) -> None:
    """The function creates Api instance, configure SQLAlchemy object,
    and adds namespaces

    :param app: a Flask instance
    :param namespaces: a list of namespaces
    """
    db.init_app(app)
    api = Api(app)
    add_namespaces(api, namespaces)


def add_namespaces(api: Api, namespaces: list) -> None:
    """This is an additional function to work with a list of namespaces

    :param api: an Api instance
    :param namespaces: a list of namespaces
    """
    for namespace in namespaces:

        api.add_namespace(namespace)


def create_data(db_obj: db) -> None:
    """This function serves to create a database

    :param db_obj: a database object
    """
    # receiving data from JSON file
    all_data = load_from_json(JSON_DATA_PATH)

    # creating all tables
    db_obj.create_all()

    # filling up tables with data
    fill_table(db_obj, Movie, all_data['movies'])
    fill_table(db_obj, Director, all_data['directors'])
    fill_table(db_obj, Genre, all_data['genres'])

    db_obj.session.commit()
    db_obj.session.close()


def fill_table(db_obj: db, model: db.Model, data_list: list) -> None:
    """This function fills the database table

    :param db_obj: a database object
    :param model: one of model's classes
    :param data_list: a list of dictionaries
    """
    for data in data_list:

        movie_model = model(**data)
        db_obj.session.add(movie_model)
