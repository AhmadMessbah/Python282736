import re
from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from mft.model.entity.base import Base


class Rent(Base):
    __tablename__ = "rent_tbl"

    code = Column(Integer, primary_key=True)
    sender_code = Column(Integer, ForeignKey="sender.code")
    renter_code = Column(Integer, ForeignKey="renter.code")
    stuff_code = Column(Integer,ForeignKey="Stuff.code")
    rent_date = Column(DateTime)
    return_date = Column(DateTime)
    stuff_status = Column(String(255))
    rent_price = Column(Integer)
    information = Column(String(255))
    sender = relationship("User")
    renter = relationship("User")
    stuff = relationship("Stuff")


    def __init__(self, code, sender, renter, stuff, rent_date, return_date, stuff_status, rent_price, information):
        self.code = code
        self.sender = sender
        self.renter = renter
        self.stuff = stuff
        self.rent_date = rent_date
        self.return_date = return_date
        self.stuff_status = stuff_status
        self.rent_price = rent_price
        self.information = information

    def __repr__(self):
        return str(self.__dict__)

    @property
    def sender(self, sender):
        self._sender != None

    @property
    def renter(self, renter):
        self._renter != None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str) and re.match("^[a-z]{2,255}$", status):
            self._status = status
        else:
            raise ValueError("Invalid Status")


