# import re
from mft.model.da.user_da import *
from mft.model.entity.user import *


class UserController:
    def save(self, name, family, gender, age, username, password, email, role, state, city, address, phone,
             photo, status):
        try:
            user = User(None, name, family, gender, age, username, password, email, role, state, city, address,
                        phone, photo, status)
            da = UserDa()
            da.save_user(user)
            return True, user
        except Exception as e:
            return False, str(e)

    def edit(self, code, name, family, gender, age, username, password, email, role, state, city, address, phone,
             photo, status):
        try:
            user = User(code, name, family, gender, age, username, password, email, role, state, city, address,
                        phone, photo, status)
            da = UserDa()
            da.edit_user(user)
            return True, user
        except Exception as e:
            return False, str(e)

    def remove(self, code):
        try:
            da = UserDa()
            da.remove_user(code)
            return True, code
        except Exception as e:
            return False, str(e)

    def find_all(self):
        try:
            da = UserDa()
            return True, da.find_all()
        except Exception as e:
            return False, str(e)

    def find_by_code(self, code):
        try:
            da = UserDa()
            result = da.find_by_code(code)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)


    def find_by_name(self, name):
        try:
            da = UserDa()
            result = da.find_by_name(name)
            if result:
                return True,result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)


    def find_by_family(self, family):
        try:
            da = UserDa()
            result = da.find_by_family(family)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)


    def find_by_gender(self, gender):
        try:
            da = UserDa()
            result = da.find_by_gender(gender)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)


    def find_by_role(self, role):
        try:
            da = UserDa()
            result = da.find_by_role(role)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)


    def find_by_username(self, username):
        try:
            da = UserDa()
            result = da.find_by_username(username)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)


    def find_by_score(self, score):
        try:
            da = UserDa()
            result = da.find_by_score(score)
            if result:
                return True, result
            else:
                raise ValueError("No Content")
        except Exception as e:
            return False, str(e)


def login(self, username, password):
    pass


def logout(self, username):
    pass

# def valid_name(text):
# return bool(re.match("^[a-zA-Z\s]{2,30}$", text))


# def valid_age(number):
# return bool(re.match("^[\d]+$", number))

# def valid_score(number):
# return bool(re.match("^[\d]{,2}"))

# def valid_username(text):
# return bool(re.match("^[\w\s\-\*]{1,20}$", text))


# def valid_password(text):
# return bool(re.match("(^[A-Z]{1,}[a-z]{1,}[\d]{1,}[@$!%?&*]{1,}$){8,}", text))


# def valid_email(text):
# return bool(re.match("[\w\.]{1,50}@(outlook|gmail|yahoo).com", text, re.I))


# def valid_address(text):
# return bool(re.match("^[a-zA-Z0-9\s\-],[\sآ-ی]{,100}$", text))


# def valid_phone(text):
# return bool(re.match("^09[\d]{9}$", text))


# def save(name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status, score):
# try:
# if (valid_name(name) and valid_name(family) and valid_username(username) and valid_password(
# password) and valid_address(address) and valid_name(state) and valid_name(city)
# and valid_phone(phone) and valid_name(photo)):
# save_user(name, family, gender, age, username, password, email, role, state, city, address, phone, photo,
# status, score)
# return True, "User Saved"
# else:
# return False, "Save Error"
# except Exception as e:
# return False, str(e)


# def edit(name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status, score):
# try:
# if (status == 1 and valid_name(name) and valid_name(family) and valid_username(username) and valid_password(
# password) and valid_address(address) and valid_name(state) and valid_name(city)
# and valid_phone(phone) and valid_name(photo)):
# edit_user(name, family, gender, age, username, password, email, role, state, city, address, phone, photo,
# status, score)
# return True, "User Edited"
# else:
# return False, "Edit Error"
# except Exception as e:
# return False, str(e)


# def activate(code):
# pass


# def deactivate(code):
# pass


# def find_all():
# try:
# return find_all_user()
# except Exception as e:
# return str(e)


# def find_by_name_family(name, family, status):
# try:
# if valid_name(name) and valid_name(family) and status == 1:
#    return find_by_name_family(name,family)
# else:
#      return False, "Invalid Data"
# except Exception as e:
# return False, str(e)


# def find_by_username(username,status):
# try:
# if valid_username(username) and status == 1:
# return find_by_username_user(username)
# else:
# return False, "Invalid Username"
# except Exception as e:
# return False, str(e)


# def find_by_role(role,status):
# pass

# def find_by_gender(gender):
# pass


# def find_by_score(score,status):
# try:
# if valid_score(score) and status==1 :
# return find_by_score_user(score)
# else:
# return False, "Invalid Score"
# except Exception as e:
# return False, str(e)


# def login(username, password):
# try:
#     if valid_username(username) and valid_password(password):
#         user = login_user(username, password)
#         if user:
#             return True, user
#         else:
#             return False, "Access Denied"
#     else:
#         return False, "Invalid Login Info"
# except Exception as e:
#     return False, str(e)


# def logout(username):
#   pass
