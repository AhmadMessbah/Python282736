import mysql.connector
from mft.model.da.database import DatabaseManager
from mft.model.entity.user import User
class UserDa(DatabaseManager):
    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(User.name == name)
        self.session.close()
        return result

    def find_by_family(self, family):
        self.make_engine()
        result = self.session.query(User.family == family)
        self.session.close()
        return result

    def find_by_gender(self, gender):
        self.make_engine()
        result = self.session.query(User.gender == gender)
        self.session.close()
        return result

    def find_by_age(self, age):
        self.make_engine()
        result = self.session.query(User.age == age)
        self.session.close()
        return result



    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(User.username == username)
        self.session.close()
        return result

    def find_by_password(self, password):
        self.make_engine()
        result = self.session.query(User.password == password)
        self.session.close()
        return result


    def find_by_email(self, email):
        self.make_engine()
        result = self.session.query(User.email == email)
        self.session.close()
        return result


    def find_by_role(self, role):
        self.make_engine()
        result = self.session.query(User.role == role)
        self.session.close()
        return result

    def find_by_state(self, state):
        self.make_engine()
        result = self.session.query(User.state == state)
        self.session.close()
        return result


    def find_by_city(self, city):
        self.make_engine()
        result = self.session.query(User.city == city)
        self.session.close()
        return result


    def find_by_address(self, address):
        self.make_engine()
        result = self.session.query(User.address == address)
        self.session.close()
        return result


    def find_by_phone(self, phone):
        self.make_engine()
        result = self.session.query(User.phone == phone)
        self.session.close()
        return result


    def find_by_photo(self, photo):
        self.make_engine()
        result = self.session.query(User.photo == photo)
        self.session.close()
        return result


    def find_by_status(self, status):
        self.make_engine()
        result = self.session.query(User.status == status)
        self.session.close()
        return result


    def find_by_score(self, score):
        self.make_engine()
        result = self.session.query(User.score == score)
        self.session.close()
        return result