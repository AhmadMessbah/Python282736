import re
from mft.model.da.stuff_da import *
from mft.model.entity.stuff import Stuff


class StuffController:
    def save(self, name, brand, description, price, image, rent_condition, rent_price):
        try:
            stuff = Stuff(None, name, brand, description, price, image, rent_condition, rent_price)
            da = StuffDa()
            da.save(stuff)
            return True, stuff
        except Exception as e:
            return False, str(e)

    def edit(self,code, name, brand, description, price, image, rent_condition, rent_price):
        try:
            stuff = Stuff(code, name, brand, description, price, image, rent_condition, rent_price)
            da = StuffDa()
            da.edit(stuff)
            return True, stuff
        except Exception as e:
            return False, str(e)

    def remove(self, code):
        try:
            da = StuffDa()
            da.remove(code)
            return True, code
        except Exception as e:
            return False, str(e)

#
    def find_all(self):
        try:
            da = StuffDa()
            return True, da.find_all()
        except Exception as e:
            return False, str(e)

# def valid_code(number):
#     return re.match("^\d{1}$", number)
#
#
# def valid_name(text):
#     return re.match("^[a-zA-z\s]{500}$", text)
#
#
# def valid_price(number):
#     return re.match("^[1000-10000]{1}", number)
#
#
# def save_c(name, brand, description, price, rent_condiotion, rent_price):
#     try:
#         # if valid_name(name) and valid_name(brand) and valid_name(description) and valid_price(price) and valid_name(rent_condiotion)  and valid_price(rent_price) >= 1000:
#         stuff = Stuff(None, name, brand, description)
#         da = StuffDa()
#         return True, da.save(stuff)
#     else:
#     False, "invalid data"
#
# except Exception as e:
# False, str(e)
#
#
# def edit_c(code, name, brand, description, price, rent_condiotion, rent_price):
#     try:
#         if valid_code(code) >= 1 and valid_name(name) and valid_name(brand) and valid_name(description) and valid_price(
#                 price) and valid_name(rent_condiotion) and valid_price(rent_price) > 1000:
#             True, edit()
#         else:
#             False, "invalid data"
#     except Exception as e:
#         False, str(e)
#
#
# def remove_c(code):
#     try:
#         if valid_code(code) >= 1:
#             True, remove()
#         else:
#             False, "invalid data"
#     except Exception as e:
#         False, str(e)
#
#
# def find_all_c():
#     try:
#         True, find_all()
#     except Exception as e:
#         False, str(e)
#
#
# def find_by_code_C(code):
#     try:
#         if valid_code(code) >= 0:
#             True, find_by_code()
#         else:
#             False, "invalid Data"
#     except Exception as e:
#         False, str(e)
#
#
# def find_by_name_c(name):
#     try:
#         if valid_name(name):
#             True, find_by_name()
#         else:
#             False, "invalid Data"
#     except Exception as e:
#         False, str(e)
#
#
# def find_by_brand_C(brand):
#     try:
#         if valid_name(brand):
#             True, find_by_brand()
#         else:
#             False, "invalid brand"
#     except Exception as e:
#         False, str(e)
#
#
# def find_by_description_c(description):
#     try:
#         if valid_name(description):
#             True, find_by_description()
#         else:
#             False, "invalid description"
#     except Exception as e:
#         False, str(e)
#
#
# def find_by_price_range_c(start_price, end_price):
#     try:
#         if valid_price(start_price) >= 1000 and valid_name(end_price) <= 10000:
#             True, find_by_price_range()
#         else:
#             False, "invalid Range"
#     except Exception as e:
#         False, str(e)
#
#
# def find_by_rent_price_range_c(start_price, end_price):
#     try:
#         if valid_price(start_price) >= 1000 and valid_name(end_price) <= 10000:
#             True, find_by_rent_price_range()
#         else:
#             False, "invalid Range"
#     except Exception as e:
#         False, str(e)
#
#
# def find_by_condition_c(condition):
#     try:
#         if valid_name(condition):
#             True, find_by_condition()
#         else:
#             False, "invalid Condition"
#     except Exception as e:
#         False, str(e)
