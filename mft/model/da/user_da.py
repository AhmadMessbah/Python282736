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
        match search_type:
            case "man":
                return self.session.query(User).filter(User.gender == "man")
            case  "woman":
                return self.session.query(User).filter(User.gender == "woman")

    def find_by_age(self, age, search_type=None):
        pass

    def find_by_username(self, username, search_type=None):
        match search_type:
            case "contain":
                username = "%" + username + "%"
            case "start":
                username = username + "%"
            case "end":
                username = "%" + username
        self.make_engine()
        return self.session.query(User).filter(User.username.like(username))

    def find_by_role(self, role, search_type=None):
        match search_type:
            case "renter":
                return self.session.query(User).filter(User.role == "renter")
            case "sender":
                return self.session.query(User).filter(User.role == "sender")

    def find_by_status(self, status, search_type=None):
        match search_type:
            case "":
                return self.session.query(User).filter(User.status == 1)
            case "":
                return self.session.query(User).filter(User.status == 0)
