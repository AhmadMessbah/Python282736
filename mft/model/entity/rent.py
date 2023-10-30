import re


class Rent:
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


rent = Rent()
