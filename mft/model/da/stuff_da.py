import mysql.connector


def save(name, brand, description, price, rent_condiotion, rent_price):
    db = mysql.connector.connect(host='localhost', user='root', password='@kasra0622', port=3306, database='stuff')
    cursor = db.cursor()
    cursor.execute(
        'insert into stuff_tbl(name,brand,description,price,rent_condition,rent_price)values(%s,%s,%s,%s,%s,%s)',
        [name, brand, description, price, rent_condiotion, rent_price])
    db.commit()
    cursor.close()
    db.close()


def edit(code, name, brand, description, price, rent_condiotion, rent_price):
    db = mysql.connector.connect(host='localhost', user='root', password='@kasra0622', port=3306, database='stuff')
    cursor = db.cursor()
    cursor.execute(
        'update stuff_tbl set name = %s, brand =%s ,description = %s, price =%s,rent_condition=%s ,rent_price=%s where code =%s',
        [code, name, brand, description, price, rent_condiotion, rent_price])
    db.commit()
    cursor.close()
    db.close()

def remove(code):
    db = mysql.connector.connect(host='localhost', user='root', password='@kasra0622', port=3306, database='stuff')
    cursor = db.cursor()
    cursor.execute('update stuff_tbl set deleted =1 where code =%s', [code])
    db.commit()
    cursor.close()
    db.close()

def find_all():
    db = mysql.connector.connect(host='localhost', user='root', password='@kasra0622', port=3306, database='stuff')
    cursor = db.cursor()
    cursor.execute('select * from stuff_tbl where deleted =0')
    stuff_list = cursor.fetchall()
    cursor.close()
    db.close()
    return stuff_list


def find_by_code(code):
    db = mysql.connector.connect(host='localhost', user='root', port=3306, password='@kasra0622', database='stuff')
    cursor = db.cursor()
    cursor.execute("select * from stuff_tbl where code = %s and deleted = 0", [code])
    stuff_list = cursor.fetchall()
    cursor.close()
    db.close()
    return stuff_list


def find_by_name(name):
    db = mysql.connector.connect(host='localhost', user='root', password='@kasra0622', port=3306, database='stuff')
    cursor = db.cursor()
    cursor.execute('select * from stuff_tbl where name like %s and deleted =0', [name])
    stuff_list = cursor.fetchall()
    cursor.close()
    db.close()
    return stuff_list


def find_by_brand(brand):
    db = mysql.connector.connect(host='localhost', port=3306, database='stuff', password="@kasra0622", user='root')
    cursor = db.cursor()
    cursor.execute('select * from stuff_tbl where brand like %s and deleted = 0', [brand])
    stuff_list = cursor.fetchall()
    cursor.close()
    db.close()
    return stuff_list


def find_by_description(description):
    db = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root', password="@kasra0622")
    cursor = db.cursor()
    cursor.execute("select * from stuff_tbl where description like %s and deleted = 0", [description])
    stuff_list = cursor.fetchall()
    cursor.close()
    db.close()
    return stuff_list


def find_by_price_range(start_price, end_price):
    db = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root', password="@kasra0622")
    cursor = db.cursor()
    cursor.execute("select * from stuff_tbl where start_price >= %s and end_price<=%s and deleted =0",
                   [start_price, end_price])
    stuff_list = cursor.fetchall()
    cursor.close()
    db.close()
    return stuff_list


def find_by_rent_price_range(start_price, end_price):
    db = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root', password="@kasra0622")
    cursor = db.cursor()
    cursor.execute("select * from stuff_tbl where start_price >= %s and end_price<=%s and deleted =0",
                   [start_price, end_price])
    stuff_list = cursor.fetchall()
    cursor.close()
    db.close()
    return stuff_list


def find_by_condition(condition):
    db = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root', password="@kasra0622")
    cursor = db.cursor()
    cursor.execute("select * from stuff_tbl where condition like %s and deleted = 0", [condition])
    stuff_list = cursor.fetchall()
    cursor.close()
    db.close()
    return stuff_list
