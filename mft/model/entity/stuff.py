import re

from mft.model.entity.base import Base
from sqlalchemy import Column, Integer,String,Boolean


class Stuff(Base):
    __tablename__ = "stuff_tbl"

    code = Column(Integer, primary_key=True)
    name = Column(String(30))
    brand = Column(String(30))
    description = Column(String(200))
    price = Column(Integer)
    image = Column(String(50))
    rent_condition = Column(String(200))
    rent_price = Column(Integer)
    deleted = Column(Boolean)

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

