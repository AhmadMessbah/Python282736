import mysql.connector


# active --> status=1
# deactivate --> status=0
class UserDa:
    def connect(self):
        self.connection = mysql.connector.connect(host='localhost', user='root', password='root123', port=3306,
                                                  database='user')
        self.cursor = self.connection.cursor()
    def  disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def execute(self, sql_command, data, commit=False):
        self.connect()
        if data:
            self.cursor.execute(sql_command, data)
        else:
            self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        self.disconnect(commit=commit)
        return result


    def save_user(self,user):
        return self.execute(
        "insert into user_tbl (name,family,gender,age,username,password,email,role,state,city,address,phone,photo,status,score) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        [user.name,user.family,user.gender,user.age,user.username,user.password,user.email,user.role,user.state,user.city,user.address,user.phone,user.photo,user.status,user.score],commit=True)


    def edit_user(self,user):
        return self.execute(
        "update user_tbl set name=%s,family=%s,gender=%s,age=%s,username=%s,password=%s,email=%s,role=%s,state=%s,city=%s,address=%s,phone=%s,photo=%s,status=%s ",
        [user.name,user.family,user.gender,user.age,user.username,user.password,user.email,user.role,user.state,user.city,user.address,user.phone,user.photo,user.status,user.score],
        commit=True)


    def activate(self,code):
        return self.execute("update user_tbl set status = 1 where code = %s", [code],commit=True)


# inactive
    def deactivate(self,code):
        return self.execute("update user_tbl set status = 0 where code = %s", [code],commit=True)


    def find_all_user(self):
        return self.execute("select * from user_tbl where status = 1",commit=True)



    def find_by_code(self,code):
        return self.execute("select * from user_tbl where status=1 and code=%s order by code", [code],commit=True)



    def find_by_name_family(self,name, family):
        return self.execute("select * from user_tbl where status=1 and name=%s and family=%s order by family", [name, family],commit=True)


    def find_by_username_user(self,username):
        return self.execute("select * from user_tbl where status=1 and username=%s order by username", [username],commit=True)


    def find_by_role_user(self,role):
        return self.execute("select * from user_tbl where status=1 and role=%s order by role", [role],commit=True)



    def find_by_gender(self,gender):
        return self.execute("select * from user_tbl where status=1 and gender=%s order by gender", [gender],commit=True)


    def find_by_score_user(self,score):
        return self.execute("select * from user_tbl where status=1 and score=%s order by score", [score],commit=True)


    def login_user(self,username, password):
        return self.execute("select * from user_tbl where username = %s and password = %s and status = 1", [username, password],commit=True)


    def logout(self,username):
        return self.execute("update user_tbl set status=0 where username=%s", [username],commit=True)
