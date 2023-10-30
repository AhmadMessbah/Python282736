import re


class User:
    def __init__(self,code, name, family, gender, age, username, password, email, role, state, city, address, phone, photo,
              status):
        self.code = code
        self.name = name
        self.family = family
        self.gender = gender
        self.age = age
        self.username = username
        self.password = password
        self.email = email
        self.role =role
        self.state = state
        self.city = city
        self.address = address
        self.phone = phone
        self.photo =photo
        self.status =status

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
        if isinstance(family,str) and re.match("[a-zA-Z\s]{2,30}", family):
            self._family = family
        else:
            raise ValueError("Invalid family")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str):
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
        if isinstance(password,str) and re.match("(^[A-Z]{1,}[a-z]{1,}[\d]{1,}[@$!%?&*]{1,}$){8,}", password):
            self._password = password
        else:
            raise ValueError("Invalid password")


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
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        if isinstance(role,str):
            self._role = role
        else:
            raise ValueError("Invalid role")


    @property
    def state(self):
        return self._state


    @state.setter
    def state(self,state ):
        if isinstance(state, str):
            self._state = state
        else:
            raise ValueError("Invalid state")
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city,str):
            self._city = city
        else:
            raise ValueError("Invalid city")


    @property
    def address(self):
        return self._address


    @address.setter
    def address(self, address):
        if isinstance(address, str)and re.match("^[a-zA-Z0-9\s\-],[\sآ-ی]{,100}$",address):
            self._address = address
        else:
            raise ValueError("Invalid address")


    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if isinstance(phone,str) and re.match(re.match("^09[\d]{9}$"),phone):
            self._phone = phone
        else:
              raise ValueError("Invalid phone")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status,str):
            self._status = status
        else:
            raise ValueError("Invalid status")

    @property
    def photo(self):
       return self._photo

    @photo.setter
    def phone(self, photo):
        if isinstance(photo,str):
           self._phone = photo
        else:
            raise ValueError("Invalid photo")

