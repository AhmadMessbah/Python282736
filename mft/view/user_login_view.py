# from tkinter import *
# from mft.controller.user_controller import *
# import tkinter.messagebox as msg
#
# # Login Click def
# def login_click():
#     detail , data =login(username.get(),password.get())
#     if detail:
#         msg.showinfo("Login","Welcome")
#     else:
#         msg.showerror("Login Error",data)
#
# # SignUp Click def
# def signup_click():
#     username.get()
#     password.get()
#
#     # User and Password Check
#     if username.get() !="" and password.get() !="":
#         msg.showinfo("Sign Up","Congratulation! You Are In")
#         login_win.destroy()
#
#     else:
#         msg.showerror("Error","Please Re-Check your information")
#
# # Login window
# login_win = Tk()
# login_win.title("User Login")
# login_win.geometry("300x150")
#
# # Username Entry
# Label(login_win,text="Username").place(x=10,y=20)
# username = StringVar()
# Entry(login_win,textvariable=username,bg="lightgreen").place(x=80,y=20)
#
# # Password Entry
# Label(login_win,text="Password").place(x=10,y=60)
# password = StringVar()
# Entry(login_win,textvariable=password,bg="lightblue").place(x=80,y=60)
#
# # Login and SignUp Button
# Button(login_win,text="Login",command=login_click,width=5).place(x=80,y=120)
# Button(login_win,text="SignUp",command=signup_click,width=5).place(x=150,y=120)
#
# login_win.mainloop()
#
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
class sign_in(QMainWindow):

    def __init__(self):
        super(sign_in, self).__init__()
        uic.loadUi("sign in_view.ui", self)
        self.show()


def main():
    app=QApplication([])
    Window=sign_in()
    app.exec_()


if __name__ == '__main__':
    main()