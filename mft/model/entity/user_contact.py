import re
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey

from mft.model.entity.base import Base


class UserContact(Base):
    __tablename__ = "user_contact_tbl"
    code = Column(Integer, primary_key=True)
    email = Column(String(30))
    state = Column(String(30))
    city = Column(String(30))
    address = Column(String(30))
    phone = Column(String(30))
    photo = Column(String(30))

    def __init__(self, code, email, state, city, address, phone, photo):
        self.code = code
        self.email = email
        self.state = state
        self.city = city
        self.address = address
        self.phone = phone
        self.photo = photo

    def __repr__(self):
        return str(self.__dict__)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and re.match("[\w\.]{1,50}@(outlook|gmail|yahoo).com", email):
            self._email = email
        else:
            raise ValueError("Invalid email")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if isinstance(state, str):
            self._state = state
        else:
            raise ValueError("Invalid state")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str):
            self._city = city
        else:
            raise ValueError("Invalid city")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, str) and re.match("^[a-zA-Z0-9\s\-],[\sآ-ی]{,100}$", address):
            self._address = address
        else:
            raise ValueError("Invalid address")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if isinstance(phone, str) and re.match(re.match("^09\d{9}$"), phone):
            self._phone = phone
        else:
            raise ValueError("Invalid phone")

    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, photo):
        if isinstance(photo, int):
            self._photo = photo
        else:
            raise ValueError("Invalid photo")

