import mysql.connector
from mft.model.da.database import DatabaseManager
from mft.model.entity.user import User


class UserDa(DatabaseManager):
    def find_by_name(self, name, search_type=None):
        match search_type:
            case "contain":
                name = "%" + name + "%"
            case "start":
                name = name + "%"
            case "end":
                name = "%" + name
        self.make_engine()
        return self.session.query(User).filter(User.name.like(name))

    def find_by_family(self, family):
        pass

    def find_by_gender(self, gender):
        pass

    def find_by_age(self, age):
        pass

    def find_by_username(self, username):
        pass

    def find_by_password(self, password):
        pass
    def find_by_email(self, email):
        pass

    def find_by_role(self, role):
        pass

    def find_by_state(self, state):
        pass

    def find_by_city(self, city):
        pass

    def find_by_address(self, address):
        pass

    def find_by_phone(self, phone):
        pass

    def find_by_photo(self, photo):
        pass

    def find_by_status(self, status):
        pass

    def find_by_score(self, score):
        pass
