import mysql.connector

from mft.model.da.database import DatabaseManager
from mft.model.entity.stuff import Stuff


class StuffDa(DatabaseManager):
    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.name == name)
        self.session.close()
        return result
#
#     def find_by_brand(self, brand):
#         connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', password="root123",
#                                              user='root')
#         cursor = connection.cursor()
#         cursor.execute('select * from stuff_tbl where brand like %s and deleted = 0', [brand])
#         stuff_list = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return stuff_list
#
#     def find_by_description(self, description):
#         connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root',
#                                              password="root123")
#         cursor = connection.cursor()
#         cursor.execute("select * from stuff_tbl where description like %s and deleted = 0", [description])
#         stuff_list = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return stuff_list
#
#     def find_by_price_range(self, start_price, end_price):
#         connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root',
#                                              password="root123")
#         cursor = connection.cursor()
#         cursor.execute("select * from stuff_tbl where start_price >= %s and end_price<=%s and deleted =0",
#                        [start_price, end_price])
#         stuff_list = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return stuff_list
#
#     def find_by_rent_price_range(self, start_price, end_price):
#         connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root',
#                                              password="root123")
#         cursor = connection.cursor()
#         cursor.execute("select * from stuff_tbl where start_price >= %s and end_price<=%s and deleted =0",
#                        [start_price, end_price])
#         stuff_list = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return stuff_list
#
#     def find_by_condition(self, condition):
#         connection = mysql.connector.connect(host='localhost', port=3306, database='stuff', user='root',
#                                              password="root123")
#         cursor = connection.cursor()
#         cursor.execute("select * from stuff_tbl where condition like %s and deleted = 0", [condition])
#         stuff_list = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return stuff_list
#
#
# stuff= Stuff(1,"Mobile","Samsung","de", 1000, "adada","adasdasda",200)
# print(stuff)
#
# da = StuffDa()
# # da.save(stuff)
# print(da.find_all())