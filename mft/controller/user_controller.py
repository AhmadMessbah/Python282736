import re
from mft.model.da.user_da import *

def valid_name(text):
    return bool (re.match("^[a-zA-Z\s]{2,30}$",text))

def valid_username(text):
    pass

def valid_password(text):
    pass

def valid_address(text):
    pass

def valid_email(text):
    pass

def valid_phone(text):
    pass



def save(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score):
    try:
        if valid_name(name) and valid_name(family) and valid_name(state) and valid_name(city) and valid_name(photo):
            save(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score)
            return True , "User Saved"
        else:
            return False , "Save Error"
    except Exception as e:
        return False , str(e)
def edit(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score):
    try:
        if status == 1 and valid_name(name) and valid_name(family) and valid_name(state) and valid_name(city) and valid_name(photo):
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


def find_by_name_family(name,family):
    pass

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