import mysql.connector
def save(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score):
    db=mysql.connector.connect(host = "localhost",user= "root",database="mft",port=3307)
    cursor = db.cursor()
    cursor.execute("insert into user_tbl(name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   [name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score])
    db.commit()
    cursor.close()
    db.close()


def edit(code,name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute(
        "update user_tbl set name=%s,family=%s,gender=%s,age=%s,username=%s,password=%s,email=%s,role,state,city,address,phone,photo,status ",
        [name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status,code])
    db.commit()
    cursor.close()
    db.close()

def activate(code):
    pass

def deactivate(code):
    pass

def find_all():
    pass

def find_by_code(code):
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