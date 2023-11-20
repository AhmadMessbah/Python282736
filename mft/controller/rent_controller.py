import re
from mft.model.da.rent_da import *
from mft.model.entity.rent import Rent


class RentController:
    def save(self, sender, renter, stuff, rent_date, return_date, stuff_status, rent_price, information):
        try:
            rent = Rent(sender, renter, stuff, rent_date, return_date, stuff_status, rent_price, information)
            da = RentDa()
            da.save(rent)
            return True, rent
        except Exception as e:
            return False, str(e)

    def edit(self, code, sender_code, renter_code, stuff_code, rent_date, return_date, stuff_status, rent_price,
             information):
        try:
            rent = Rent(sender_code, renter_code, stuff_code, rent_date, return_date, stuff_status, rent_price,
                        information)
            rent.code = code
            da = RentDa()
            da.edit(rent)
            return True, rent
        except Exception as e:
            return False, str(e)

    def find_by_code(self, code):
        try:
            da = RentDa()
            rent = da.find_by_code(Rent, code)
            return True, da.remove(rent)
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            da = Rent()
            return True, da.find_all(Rent)
        except Exception as e:
            return False, str(e)

    def find_by_code(self,code):
        try:
            da = RentDa()
            return True, da.find_by_code()
        except Exception as e:
            return False, int(e)

    def valid_code(code):
        return re.match("^\ {1}$", code)

    def find_by_sender_code(code):
        try:
            if code.valid_code(code) >= 0:
                True, find_by_code()
            else:
                return False, "invalid Data"
        except Exception as e:
            False, int(e)

    def valid_renter(renter_code):
        return re.match("^\ {1}$")

    def find_by_renter_code(renter_code):
        try:
            if renter_code.valid_renter(renter_code) >= 0:
                True, find_by_code()
            else:
                return False, "invalid Data"
        except Exception as e:
            False, int(e)

    def valid_stuff(stuff_code):
        return re.match("^\ {1}$")

    def find_by_stuff_code(stuff_code):
        try:
            if stuff_code.valid_renter(stuff_code) >= 0:
                return True, find_by_code()
            else:
                return False, "invalid Data"
        except Exception as e:
            False, int(e)

    # def date_validator(start_date, end_date):
    #    re.match("^[2023/13/11,%s]" [start_date, end_date])
    def find_by_rent_date_range(start_date, end_date):
        try:
            if start_date and end_date > 0:
                return True, start_date(), end_date()
            else:
                return False, "invalid Date"
        except Exception as e:
            False, int(e)

    def find_by_return_date_range(start_date, end_date):
        try:
            if start_date and end_date > 0:
                return True, start_date(), end_date()
            else:
                return False, "invalid Date"
        except Exception as e:
            False, int(e)

    def rent_price_validator(price):
        return re.match("^[1000-10000]{1}", price)

    def find_by_rent_price_range(start_price, end_price):
        try:
            if start_price and end_price > 0:
                return True, start_price(), end_price()
            else:
                return False, "Invalid Price"
        except Exception as e:
            False, int(e)

    def valid_name(text):
        return re.match('^[a-zA-Z\s]{500}$', text)

    def find_by_information(information):
        try:
            if valid_name(information):
                return True, find_by_information()
            else:
                return False, 'invalid information'
        except Exception as e:
            False, str(e)

    def valid_status(text):
        return re.match('^[a-zA-Z\s]{500}$', text)

    def find_by_rent_status(rent_status):
        try:
            if valid_status(rent_status):
                return True, find_by_rent_status()
            else:
                return False, "Invalid Status"
        except Exception as e:
            False, str(e)
