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

    # @property
    # def family(self):
    #     return self._family
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family, str) and re.match("[a-zA-Z\s]{2,30}", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid family")
    # @property
    # def family(self):
    #     return self._family
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family,str) and re.match("[a-zA-Z\s]{2,30}", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid family")
    #
    #
    # @property
    # def family(self):
    #     return self._family
    #
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family, str) and re.match("[a-zA-Z\s]{2,30}", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid family")
    #
    # @property
    # def family(self):
    #     return self._family
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family,str) and re.match("[a-zA-Z\s]{2,30}", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid family")
    #
    #
    # @property
    # def family(self):
    #     return self._family
    #
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family, str) and re.match("[a-zA-Z\s]{2,30}", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid family")
    # @property
    # def family(self):
    #     return self._family
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family,str) and re.match("[a-zA-Z\s]{2,30}", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid family")
    #
    #
    # @property
    # def family(self):
    #     return self._family
    #
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family, str) and re.match("[a-zA-Z\s]{2,30}", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid family")
    #
    #
    # @property
    # def family(self):
    #     return self._family
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family,str) and re.match("[a-zA-Z\s]{2,30}", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid family")


