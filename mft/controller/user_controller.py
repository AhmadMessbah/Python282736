import re
from mft.model.da.user_da import *

def valid_name(text):
    return bool (re.match("^[a-zA-Z\s]{2,30}$",text))

def valid_username(text):
    return bool (re.match("^[a-zA-Z\_\-\d]{,20}$"))

def valid_password(text):
    return bool (re.match("^[a-zA-Z]{,10}[\@]?[\_]?[\-]?[\d]{,6}$"))

def valid_address(text):
    return bool(re.match("^[a-zA-z0-9\s\-],[\sآ-ی]{,100}$", text))

def valid_email(text):
    pass

def valid_phone(text):
    return bool (re.match("^09[\d]{9}$"))



def save(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score):
    try:
        if (valid_name(name) and valid_name(family) and valid_username(username) and valid_password(password) and valid_address(address) and valid_name(state) and valid_name(city)
                and valid_phone(phone) and valid_name(photo)):
            save(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score)
            return True , "User Saved"
        else:
            return False , "Save Error"
    except Exception as e:
        return False , str(e)
def edit(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score):
    try:
        if (status == 1 and valid_name(name) and valid_name(family) and valid_username(username) and valid_password(password) and valid_address(address) and valid_name(state) and valid_name(city)
                and valid_phone(phone) and valid_name(photo)):
            edit(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score)
            return True , "User Edited"
        else:
            return False , "Edit Error"
    except Exception as e:
        return False , str(e)
def activate(code):
    pass

def deactivate(code):
    pass


def find_by_name_family(name,family,status):
    try:
        if status == 1 and valid_name(name) and valid_name(family):
            find_by_name_family(name,family)

def find_by_username(username):
    pass

def find_by_role(role):
    pass

def find_by_gender(gender):
    pass

def find_by_score(code):
    pass

def login(username,password):
    pass

def logout(username):
    pass