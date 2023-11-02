import mysql.connector
from mft.model.entity.user import User


# active --> status=1
# inactive --> status=0




def save_user(name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status,
              score):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute(
        "insert into user_tbl (name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        [name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status, score])
    db.commit()
    cursor.close()
    db.close()


def edit_user(code, name, family, gender, age, username, password, email, role, state, city, address, phone, photo,
              status):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute(
        "update user_tbl set name=%s,family=%s,gender=%s,age=%s,username=%s,password=%s,email=%s,role=%s,state=%s,city=%s,address=%s,phone=%s,photo=%s,status=%s ",
        [name, family, gender, age, username, password, email, role, state, city, address, phone, photo, status, code])
    db.commit()
    cursor.close()
    db.close()


def activate(code):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("update user_tbl set status = 1 where code = %s", [code])
    db.commit()
    cursor.close()
    db.close()


# inactive
def deactivate(code):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("update user_tbl set status = 0 where code = %s", [code])
    db.commit()
    cursor.close()
    db.close()


def find_all_user():
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where status = 1")
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list


def find_by_code(code):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where status=1 and code=%s order by code",[code])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list


def find_by_name_family(name,family):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where status=1 and name=%s and family=%s order by family",[name,family])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list


def find_by_username_user(username):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where status=1 and username=%s order by username",[username])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list


def find_by_role_user(role):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where status=1 and role=%s order by role",[role])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list


def find_by_gender(gender):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where status=1 and gender=%s order by gender",[gender])


def find_by_score_user(score):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where status=1 and score=%s order by score",[score])
    user_list = cursor.fetchall()
    cursor.close()
    db.close()
    return user_list


def login_user(username, password):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("select * from user_tbl where username = %s and password = %s and status = 1", [username, password])
    user = cursor.fetchall()
    cursor.close()
    db.close()
    return user


def logout(username):
    db = mysql.connector.connect(host="localhost", user="root", database="mft", port=3307)
    cursor = db.cursor()
    cursor.execute("update user_tbl set status=0 where username=%s",[username])
    user = cursor.fetchall()
    cursor.close()
    db.close()
    return user
