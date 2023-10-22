import re
from mft.model.da.user_da import *


def valid_name(text):
    return bool(re.match("^[a-zA-Z\s]{2,30}$", text))


def valid_age(number):
    return bool(re.match("^[\d]+$", number))

def valid_score(number):
    return bool(re.match("^[\d]{,2}"))

def valid_username(text):
    return bool(re.match("^[\w\s\-\*]{1,20}$", text))


def valid_password(text):
    return bool(re.match("(^[A-Z]{1,}[a-z]{1,}[\d]{1,}[@$!%?&*]{1,}$){8,}", text))


def valid_email(text):
    return bool(re.match("[\w\.]{1,50}@(outlook|gmail|yahoo).com", text, re.I))


def valid_address(text):
    return bool(re.match("^[a-zA-Z0-9\s\-],[\sآ-ی]{,100}$", text))


def valid_phone(text):
    return bool(re.match("^09[\d]{9}$", text))



def save(name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status, score):
    try:
        if (valid_name(name) and valid_name(family) and valid_username(username) and valid_password(
                password) and valid_address(address) and valid_name(state) and valid_name(city)
                and valid_phone(phone) and valid_name(photo)):
            save_user(name, family, gender, age, username, password, email, role, state, city, address, phone, photo,
                      status, score)
            return True, "User Saved"
        else:
            return False, "Save Error"
    except Exception as e:
        return False, str(e)


def edit(name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status, score):
    try:
        if (status == 1 and valid_name(name) and valid_name(family) and valid_username(username) and valid_password(
                password) and valid_address(address) and valid_name(state) and valid_name(city)
                and valid_phone(phone) and valid_name(photo)):
            edit_user(name, family, gender, age, username, password, email, role, state, city, address, phone, photo,
                      status, score)
            return True, "User Edited"
        else:
            return False, "Edit Error"
    except Exception as e:
        return False, str(e)

#todo:active and deactive
def activate(code):
    pass

def deactivate(code):
    pass


def find_all():
    try:
        return find_all_user()
    except Exception as e:
        return str(e)


def find_by_name_family(name, family, status):
    try:
        if valid_name(name) and valid_name(family) and status == 1:
            return find_by_name_family(name,family)
        else:
            return False, "Invalid Data"
    except Exception as e:
        return False, str(e)


def find_by_username(username,status):
    try:
        if valid_username(username) and status == 1:
            return find_by_username_user(username)
        else:
            return False, "Invalid Username"
    except Exception as e:
        return False, str(e)



def find_by_role(role,status):
    try:
        if role  and status==1:
            return find_by_role_user(role)
        else:
            return False , "Invalid role"

    except Exception as e:
        return False , str(e)

def find_by_gender(gender):
    try:
        if gender :
            return find_by_gender(gender)
        else:
            return False, "Invalid gender"

    except Exception as e:
        return False, str(e)


def find_by_score(score,status):
    try:
        if valid_score(score) and status==1 :
            return find_by_score_user(score)
        else:
            return False, "Invalid Score"
    except Exception as e:
        return False, str(e)


def login(username, password):
    try:
        if valid_username(username) and valid_password(password):
            user = login_user(username, password)
            if user:
                return True, user
            else:
                return False, "Access Denied"
        else:
            return False, "Invalid Login Info"
    except Exception as e:
        return False, str(e)


def logout(username):
    try:
        if valid_username(username):
            return logout(username)
        else:
            return False, "Invalid User Name"

    except Exception as e:
        return False, str(e)
