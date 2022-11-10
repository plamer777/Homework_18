"""This unit contains a DirectorService class to process requests like
/directors/"""
from dao.director_dao import DirectorDao
from dao.model.director import DirectorSchema
# -------------------------------------------------------------------------


class DirectorService:
    """The DirectorService class provides a business logic to work with
    routes like /directors/
    """
    def __init__(self, dao: DirectorDao, schema: DirectorSchema) -> None:
        """The initialization of the class

        :param dao: the DirectorDao instance
        :param schema: the DirectorSchema instance
        """
        self.dao = dao
        self.schema = schema

    def get_all(self) -> tuple:
        """This method returns a list of all found records in the certain
        table

        :returns:
            a tuple with the result of the operation
        """
        all_directors = self.dao.get_all()

        if not all_directors:
            return 'Not found', 404

        records_list = self.schema.dump(all_directors, many=True)

        return records_list, 200

    def get_one(self, record_id: int):
        """This method returns a single record found in the specified table

        :param record_id: the id of the record

        :returns:
            a tuple with the result of the operation
        """
        found = self.dao.get_by_id(record_id)

        if not found:
            return 'Not found', 404

        record_dict = self.schema.dump(found)

        return record_dict, 200
