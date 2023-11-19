import mysql.connector

from mft.model.da.database import DatabaseManager
from mft.model.entity.user_contact import UserContact


class UserContactDa(DatabaseManager):
    def find_by_email(self, class_name, email):
        pass

    def find_by_state(self, class_name, state):
        pass

    def find_by_city(self, class_name, city):
        pass

    def find_by_address(self, class_name, address):
        pass

    def find_by_phone(self, class_name, phone):
        pass

    def find_by_photo(self, class_name, photo):
        pass
