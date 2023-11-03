import re


class Stuff:
    def __init__(self, code, name, brand, description, price, image, rent_condition, rent_price,deleted=0):
        self.code = code
        self.name = name
        self.brand = brand
        self.description = description
        self.price = price
        self.image = image
        self.rent_condition = rent_condition
        self.rent_price = rent_price
        self.deleted = deleted

    def __repr__(self):
        return str(self.__dict__)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # props
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand,str) and re.match("^[a-zA-Z\s]{2,30}$", brand):
            self._brand = brand
        else:
            raise ValueError("Invalid Brand")

