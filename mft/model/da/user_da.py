import mysql.connector
from mft.model.da.database import DatabaseManager
from mft.model.entity.user import User
class UserDa(DatabaseManager):
    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(User.name == name)
        self.session.close()
        return result

    def find_by_family(self, family) :
        self.make_engine()
        result = self.session.query(User.family == family)
        self.session.close()
        return result