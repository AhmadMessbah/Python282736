import mysql.connector

from mft.model.da.database import DatabaseManager
from mft.model.entity.user_contact import UserContact


class UserContactDa(DatabaseManager):
    def find_by_email(self, email, search_type=None):
        match search_type:
            case "contain":
                email = "%" + email + "%"
            case "start":
                email = email + "%"
            case "end":
                email = "%" + email
                self.make_engine()
        return self.session.query(UserContact).filter(UserContact.email.like(email))

    def find_by_state(self,state, search_type=None):
        match search_type:
            case "contain":
                state = "%" + state + "%"
            case "start":
                state = state + "%"
            case "end":
                state = "%" + state
                self.make_engine()
        return self.session.query(UserContact).filter(UserContact.state.like(state))

    def find_by_city(self,  city, search_type=None):
        match search_type:
            case "contain":
                city = "%" + city + "%"
            case "start":
                city = city + "%"
            case "end":
                city = "%" + city
                self.make_engine()
        return self.session.query(UserContact).filter(UserContact.city.like(city))

    def find_by_address(self, address, search_type=None):
        match search_type:
            case "contain":
                address = "%" + address + "%"
            case "start":
                address = address + "%"
            case "end":
                address = "%" + address
                self.make_engine()
        return self.session.query(UserContact).filter(UserContact.address.like(address))

    def find_by_phone(self, phone, search_type=None):
        match search_type:
            case "contain":
                phone = "%" + phone + "%"
            case "start":
                phone = phone + "%"
            case "end":
                phone = "%" + phone
                self.make_engine()
        return self.session.query(UserContact).filter(UserContact.phone.like(phone))

    def find_by_photo(self, photo, search_type=None):
        pass
