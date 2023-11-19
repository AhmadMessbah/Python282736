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

    def find_by_family(self, family, search_type=None):
        match search_type:
            case "contain":
                family = "%" + family + "%"
            case "start":
                family = family + "%"
            case "end":
                family = "%" + family
                self.make_engine()
        return self.session.query(User).filter(User.family.like(family))

    def find_by_gender(self, gender, search_type=None):
        pass

    def find_by_age(self, age, search_type=None):
        pass

    def find_by_username(self, username, search_type=None):
        pass

    def find_by_password(self, password, search_type=None):
        pass

    def find_by_email(self, email, search_type=None):
        pass

    def find_by_role(self, role, search_type=None):
        pass

    def find_by_state(self, state, search_type=None):
        pass

    def find_by_city(self, city, search_type=None):
        pass

    def find_by_address(self, address, search_type=None):
        pass

    def find_by_phone(self, phone, search_type=None):
        pass

    def find_by_photo(self, photo, search_type=None):
        pass

    def find_by_status(self, status, search_type=None):
        pass

    def find_by_score(self, score, search_type=None):
        pass
