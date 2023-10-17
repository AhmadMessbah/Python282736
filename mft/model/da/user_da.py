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
        "update user_tbl set name=%s,family=%s,gender=%s,age=%s,username=%s,password=%s,email=%s,role=%s,state=%s,city=%s,address=%s,phone=%s,photo=%s,status=%s ",
        [name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status,code])
    db.commit()
    cursor.close()
    db.close()

def activate(code):
    pass

def deactivate(code):
    pass

def find_all():
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where status = 1",)
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list

def find_by_code(code):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where code = %s", [code])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list

def find_by_name_family(name,family):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where name = %s and family = %s",[name,family])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list



def find_by_username(username):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where username = %s", [username])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list


def find_by_role(role):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where role = %s", [role])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list

def find_by_gender(gender):
    pass

def find_by_score(score):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where score = %s", [score])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list

def login(username,password):
    pass

def logout(username):
    pass