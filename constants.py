"""This unit provides constants for the application"""
import os
# --------------------------------------------------------------------------

DB_PATH = os.path.abspath('data')
DATABASE_URI = f'sqlite:///cinema.db'
JSON_DATA_PATH = os.path.join('data', 'data.json')
