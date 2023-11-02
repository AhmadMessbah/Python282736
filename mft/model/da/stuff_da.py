import mysql.connector

from mft.model.entity.stuff import Stuff


class StuffDa:
    def connect(self):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306,
                                                  database='rent_db')
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def execute(self, sql_command, data=None, commit=False):
        self.connect()
        if data:
            self.cursor.execute(sql_command, data)
        else:
            self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        self.disconnect(commit=commit)
        return result

    def save(self, stuff):
        self.execute(
            'insert into stuff_tbl(name,brand,description,price,rent_condition,rent_price)values(%s,%s,%s,%s,%s,%s)',
            [stuff.name, stuff.brand, stuff.description, stuff.price, stuff.rent_condition, stuff.rent_price],
            commit=True)
        return stuff

    def edit(self, stuff):
        self.execute(
            'update stuff_tbl set name=%s, brand=%s ,description=%s, price=%s, rent_condition=%s ,rent_price=%s where code=%s',
            [stuff.name, stuff.brand, stuff.description, stuff.price, stuff.rent_condition,
             stuff.rent_price, stuff.code],
            commit=True)
        return stuff

    def remove(self, code):
        self.execute('update stuff_tbl set deleted=1 where code=%s',
                     [code],
                     commit=True)
        return code


    def find_all(self):
        return self.execute("select * from stuff_tbl")

    def find_by_code(self, code):
        return self.execute("select * from stuff_tbl where code=%s deleted =0", [code])

    def find_by_name(self, name):
        connection = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306,
                                             database='stuff')
        cursor = connection.cursor()
        cursor.execute('select * from stuff_tbl where name like %s', [name])
        stuff_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return stuff_list

    def find_by_brand(self, brand):
        connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', password="root123",
                                             user='root')
        cursor = connection.cursor()
        cursor.execute('select * from stuff_tbl where brand like %s and deleted = 0', [brand])
        stuff_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return stuff_list

    def find_by_description(self, description):
        connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root',
                                             password="root123")
        cursor = connection.cursor()
        cursor.execute("select * from stuff_tbl where description like %s and deleted = 0", [description])
        stuff_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return stuff_list

    def find_by_price_range(self, start_price, end_price):
        connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root',
                                             password="root123")
        cursor = connection.cursor()
        cursor.execute("select * from stuff_tbl where start_price >= %s and end_price<=%s and deleted =0",
                       [start_price, end_price])
        stuff_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return stuff_list

    def find_by_rent_price_range(self, start_price, end_price):
        connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root',
                                             password="root123")
        cursor = connection.cursor()
        cursor.execute("select * from stuff_tbl where start_price >= %s and end_price<=%s and deleted =0",
                       [start_price, end_price])
        stuff_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return stuff_list

    def find_by_condition(self, condition):
        connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root',
                                             password="root123")
        cursor = connection.cursor()
        cursor.execute("select * from stuff_tbl where condition like %s and deleted = 0", [condition])
        stuff_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return stuff_list


stuff= Stuff(1,"Mobile","Samsung","de", 1000, "adada","adasdasda",200)
print(stuff)

da = StuffDa()
# da.save(stuff)
print(da.find_all())