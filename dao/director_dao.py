"""There is a DirectorDao class in the unit to get access to directors
table"""
from dao.model.director import Director
from setup_db import db
# ----------------------------------------------------------------------


class DirectorDao:
    """The DirectorDao class provides method to get info from
    certain table"""
    def __init__(self):
        """Initialization of the class"""
        self.db = db
        self.model = Director

    def get_all(self) -> list:
        """This method returns a list of objects found in the certain table

        :returns:
            all_records - a list of models
        """
        all_records = self.model.query.all()

        return all_records

    def get_by_id(self, record_id: int) -> dict:
        """This method returns an object containing information about
        a certain record found by id

        :param record_id: an id of searching record

        :returns:
            found_record - a model containing information about searching
            record
        """
        found_record = self.model.query.get(record_id)

        return found_record
