# import mysql.connector
# from mft.model.entity.user import User
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import relationship
# from sqlalchemy import text, and_, or_
#
# from mft.model.entity.base import Base
#
# from sqlalchemy.orm import sessionmaker
#
#
# import sqlalchemy_utils
# from sqlalchemy_utils import database_exists, create_database
#
#
#
#
# # active --> status=1
# # inactive --> status=0
#
# class UserDa:
#     def make_engine(self):
#         if not database_exists('mysql+pymysql://root:root123@localhost:3306/mft'):
#             create_database('mysql+pymysql://root:root123@localhost:3306/mft')
#         self.engine = create_engine('mysql+pymysql://root:root123@localhost:3306/mft')
#
#         Base.metadata.create_all(self.engine)
#
#         Session = sessionmaker(bind=self.engine)
#         self.session = Session()
#
#     def connect(self):
#         self.connection = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306,
#                                                   database='rent_db')
#         self.cursor = self.connection.cursor()
#
#     def disconnect(self, commit=False):
#         if commit:
#             self.connection.commit()
#         self.cursor.close()
#         self.connection.close()
#
#     def execute(self, sql_command, data=None, commit=False):
#         self.connect()
#         if data:
#             self.cursor.execute(sql_command, data)
#         else:
#             self.cursor.execute(sql_command)
#         result = self.cursor.fetchall()
#         self.disconnect(commit=commit)
#         return result
#
#     def save(self, user):
#         self.execute(
#             """
#             insert into user_tbl
#             (
#                 name,
#                 family,
#                 gender,
#                 age,
#                 username,
#                 password,
#                 email,
#                 role,
#                 state,
#                 city,
#                 address,
#                 phone,
#                 photo,
#                 status,
#                 score
#             )
#             values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#             """,
#             [
#                 user.name,
#                 user.family,
#                 user.gender,
#                 user.age,
#                 user.username,
#                 user.password,
#                 user.email,
#                 user.role,
#                 user.state,
#                 user.city,
#                 user.address,
#                 user.phone,
#                 user.photo,
#                 user.status,
#                 user.score
#             ],
#
#             commit=True)
#         return user
#
#     def edit(self, user):
#         self.execute(
#             "update user_tbl set name=%s,family=%s,gender=%s,age=%s,username=%s,password=%s,email=%s,role=%s,state=%s,city=%s,address=%s,phone=%s,photo=%s,status=%s where code=%s",
#             [
#                 user.name,
#              user.family,
#              user.gender,
#              user.age,
#              user.username,
#              user.password,
#              user.email,
#              user.role,
#              user.state,
#              user.city,
#              user.address,
#              user.phone,
#              user.photo,
#              user.status,
#              user.code],
#             commit = True)
#         return user
#
#     def remove(self, code):
#         self.execute("update user_tbl set deleted=1 where code=%s",
#                      [code],
#                      commit=True)
#         return code
#
#     def activate(self, code):
#         self.execute("update user_tbl set status = 1 where code = %s", [code],
#                      commit=True)
#         return code
#
#     # inactive
#     def deactivate(self, code):
#         self.execute("update user_tbl set status = 0 where code = %s", [code],
#                      commit=True)
#         return code
#
#     def find_all(self):
#         return self.execute("select * from user_tbl")
#
#     def find_by_code(self, code):
#         return self.execute("select * from user_tbl where code=%s and deleted =0",
#                             [code]
#                             )
#
#     def find_by_name(self, name):
#         return self.execute("select * from user_tbl where status=1 and name=%s  order by name",
#                             [name])
#
#     def find_by_family(self, family):
#         return self.execute("select * from user_tbl where status=1 and family=%s  order by family",
#                             [family])
#
#     def find_by_name_family(self, name, family):
#         return self.execute("select * from user_tbl where status=1 and name like %s and family like %s order by family",
#                             [name + "%", family + "%"])
#
#     def find_by_username(self, username):
#         return self.execute("select * from user_tbl where status=1 and username=%s order by username",
#                             [username])
#
#     def find_by_role(self, role):
#         return self.execute("select * from user_tbl where status=1 and role=%s order by role",
#                             [role])
#
#     def find_by_gender(self, gender):
#         return self.execute("select * from user_tbl where status=1 and gender=%s order by gender",
#                             [gender])
#
#     def find_by_score(self, score):
#         return self.execute("select * from user_tbl where status=1 and score=%s order by score",
#                             [score])
#
#     def login(self, username, password):
#         return self.execute("update user_tbl set status=1 where username=%s and password = %s ",
#                             [username, password],
#                             commit=True)
#
#     def logout(self, username):
#         return self.execute("update user_tbl set status=0 where username=%s",
#                             [username],
#                             commit=True)





from mft.model.da.database import DatabaseManager
from mft.model.entity.user import User


class CustomerDa(DatabaseManager):
    def find_by_name(self, name, search_type=None):
        match search_type:
            case "contain":
                name = "%" + name + "%"
            case "start":
                name = name + "%"
            case "end":
                name = "%" + name

        self.make_engine()
        return self.session.query(User).filter(User.name.like(name))
    def find_by_family(self, family,search_type = None ):
        match search_type:
            case "contain":
                family ="%" + family + "%"
            case "start":
                family = family + "%"
            case "end":
                family = "%" + family




