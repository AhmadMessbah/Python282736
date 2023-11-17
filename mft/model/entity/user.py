import re
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship

from mft.model.entity.base import Base


class User(Base):
    __tablename__ = "user_tbl"

    code = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column()
    gender = Column()
    age = Column()
    username = Column()
    password = Column()
    role = Column()
    contact_id = Column(Integer, ForeignKey="contact.id")
    status = Column(Boolean)

    contact = relationship("Contact")

    def __init__(self, code, name, family, gender, age, username, password, role, contact, status):
        self.code = code
        self.name = name
        self.family = family
        self.gender = gender
        self.age = age
        self.username = username
        self.password = password
        self.role = role
        self.contact = contact
        self.status = status

    def __repr__(self):
        return str(self.__dict__)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and re.match("^[a-zA-Z\s]{2,30}$", name):
            self._name = name
        else:
            raise ValueError("Invalid name")

    # props
    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if isinstance(family, str) and re.match("[a-zA-Z\s]{2,30}", family):
            self._family = family
        else:
            raise ValueError("Invalid family")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and gender in ("Male", "Female"):
            self._gender = gender
        else:
            raise ValueError("Invalid gender")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, str) and re.match("^[\d]+$", age):
            self._age = age
        else:
            raise ValueError("Invalid age")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and re.match("^[\w\s\-\*]{1,20}$", username):
            self._username = username
        else:
            raise ValueError("Invalid username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if isinstance(password, str) and re.match("(^[A-Z]{1,}[a-z]{1,}[\d]{1,}[@$!%?&*]{1,}$){8,}", password):
            self._password = password
        else:
            raise ValueError("Invalid password")

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        if isinstance(role, str):
            self._role = role
        else:
            raise ValueError("Invalid role")

    @property
    def state(self):
        return self._state

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise ValueError("Invalid status")

