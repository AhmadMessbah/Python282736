# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign up_viewynSdlv.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# sign up
def sign_in():
    class Ui_Form(object):
        def setupUi(self, Form):
            if Form.objectName():
                Form.setObjectName(u"Form")
            Form.resize(1032, 652)
            self.widget = QWidget(Form)
            self.widget.setObjectName(u"widget")
            self.widget.setEnabled(True)
            self.widget.setGeometry(QRect(20, 10, 991, 621))
            font = QFont()
            font.setPointSize(10)
            self.widget.setFont(font)
            self.widget.setStyleSheet(u"background-color: rgba(16, 30, 41, 240);\n"
                                      "border-radius:10px;\n"
                                      "")
            self.lineEdit = QLineEdit(self.widget)
            self.lineEdit.setObjectName(u"lineEdit")
            self.lineEdit.setGeometry(QRect(60, 200, 250, 40))
            font1 = QFont()
            font1.setPointSize(10)
            font1.setBold(False)
            font1.setWeight(50)
            self.lineEdit.setFont(font1)
            self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                        "border:1px solid rgba(0,0,0,0);\n"
                                        "border-bottom-color:rgba(46,82,101,255);\n"
                                        "color:rgb(255,255,255);\n"
                                        "padding-bottom:7px")
            self.lineEdit_2 = QLineEdit(self.widget)
            self.lineEdit_2.setObjectName(u"lineEdit_2")
            self.lineEdit_2.setGeometry(QRect(60, 270, 250, 40))
            self.lineEdit_2.setFont(font1)
            self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                          "border:1px solid rgba(0,0,0,0);\n"
                                          "border-bottom-color:rgba(46,82,101,255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "padding-bottom:7px")
            self.lineEdit_2.setEchoMode(QLineEdit.Normal)
            self.pushButton = QPushButton(self.widget)
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.setEnabled(True)
            self.pushButton.setGeometry(QRect(390, 480, 150, 50))
            font2 = QFont()
            font2.setPointSize(10)
            font2.setBold(True)
            font2.setWeight(75)
            self.pushButton.setFont(font2)
            self.pushButton.setMouseTracking(False)
            self.pushButton.setAcceptDrops(True)
            self.pushButton.setAutoFillBackground(False)
            self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
                                          "background-color: rgb(2, 65, 118);\n"
                                          "color: rgba(255, 255, 255, 200);\n"
                                          "border-radius:5px;\n"
                                          "}\n"
                                          "QPushButton#pushButton:pressed{\n"
                                          "padding-left:5px;\n"
                                          "padding-top:5px;\n"
                                          "background-color: rgb(2, 65, 100);\n"
                                          "backgroung-position:calc(100%-10px)center;\n"
                                          "}\n"
                                          "QPushButton#pushButton:hover{\n"
                                          "background-color: rgba(2, 65, 118, 200);\n"
                                          "}")
            self.pushButton.setCheckable(False)
            self.pushButton.setAutoRepeat(False)
            self.label_3 = QLabel(self.widget)
            self.label_3.setObjectName(u"label_3")
            self.label_3.setGeometry(QRect(20, 10, 131, 31))
            font3 = QFont()
            font3.setPointSize(13)
            self.label_3.setFont(font3)
            self.label_3.setStyleSheet(u"color: rgb(0, 125, 236);")
            self.label_3.setAlignment(Qt.AlignCenter)
            self.label_3.setOpenExternalLinks(False)
            self.lineEdit_3 = QLineEdit(self.widget)
            self.lineEdit_3.setObjectName(u"lineEdit_3")
            self.lineEdit_3.setGeometry(QRect(60, 130, 250, 40))
            self.lineEdit_3.setFont(font1)
            self.lineEdit_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                          "border:1px solid rgba(0,0,0,0);\n"
                                          "border-bottom-color:rgba(46,82,101,255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "padding-bottom:7px")
            self.lineEdit_4 = QLineEdit(self.widget)
            self.lineEdit_4.setObjectName(u"lineEdit_4")
            self.lineEdit_4.setGeometry(QRect(60, 60, 250, 40))
            self.lineEdit_4.setFont(font1)
            self.lineEdit_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                          "border:1px solid rgba(0,0,0,0);\n"
                                          "border-bottom-color:rgba(46,82,101,255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "padding-bottom:7px")
            self.lineEdit_4.setEchoMode(QLineEdit.Normal)
            self.lineEdit_5 = QLineEdit(self.widget)
            self.lineEdit_5.setObjectName(u"lineEdit_5")
            self.lineEdit_5.setGeometry(QRect(60, 340, 250, 40))
            self.lineEdit_5.setFont(font1)
            self.lineEdit_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                          "border:1px solid rgba(0,0,0,0);\n"
                                          "border-bottom-color:rgba(46,82,101,255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "padding-bottom:7px")
            self.lineEdit_5.setEchoMode(QLineEdit.Normal)
            self.lineEdit_6 = QLineEdit(self.widget)
            self.lineEdit_6.setObjectName(u"lineEdit_6")
            self.lineEdit_6.setGeometry(QRect(60, 410, 250, 40))
            self.lineEdit_6.setFont(font1)
            self.lineEdit_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                          "border:1px solid rgba(0,0,0,0);\n"
                                          "border-bottom-color:rgba(46,82,101,255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "padding-bottom:7px")
            self.lineEdit_6.setEchoMode(QLineEdit.Password)
            self.lineEdit_7 = QLineEdit(self.widget)
            self.lineEdit_7.setObjectName(u"lineEdit_7")
            self.lineEdit_7.setGeometry(QRect(60, 480, 250, 40))
            self.lineEdit_7.setFont(font1)
            self.lineEdit_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                          "border:1px solid rgba(0,0,0,0);\n"
                                          "border-bottom-color:rgba(46,82,101,255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "padding-bottom:7px")
            self.lineEdit_7.setEchoMode(QLineEdit.Password)
            self.lineEdit_8 = QLineEdit(self.widget)
            self.lineEdit_8.setObjectName(u"lineEdit_8")
            self.lineEdit_8.setGeometry(QRect(370, 60, 250, 40))
            self.lineEdit_8.setFont(font1)
            self.lineEdit_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                          "border:1px solid rgba(0,0,0,0);\n"
                                          "border-bottom-color:rgba(46,82,101,255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "padding-bottom:7px")
            self.lineEdit_8.setEchoMode(QLineEdit.Normal)
            self.lineEdit_9 = QLineEdit(self.widget)
            self.lineEdit_9.setObjectName(u"lineEdit_9")
            self.lineEdit_9.setGeometry(QRect(370, 130, 250, 40))
            self.lineEdit_9.setFont(font1)
            self.lineEdit_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                          "border:1px solid rgba(0,0,0,0);\n"
                                          "border-bottom-color:rgba(46,82,101,255);\n"
                                          "color:rgb(255,255,255);\n"
                                          "padding-bottom:7px")
            self.lineEdit_9.setEchoMode(QLineEdit.Normal)
            self.lineEdit_10 = QLineEdit(self.widget)
            self.lineEdit_10.setObjectName(u"lineEdit_10")
            self.lineEdit_10.setGeometry(QRect(370, 200, 250, 40))
            self.lineEdit_10.setFont(font1)
            self.lineEdit_10.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                           "border:1px solid rgba(0,0,0,0);\n"
                                           "border-bottom-color:rgba(46,82,101,255);\n"
                                           "color:rgb(255,255,255);\n"
                                           "padding-bottom:7px")
            self.lineEdit_10.setEchoMode(QLineEdit.Normal)
            self.lineEdit_11 = QLineEdit(self.widget)
            self.lineEdit_11.setObjectName(u"lineEdit_11")
            self.lineEdit_11.setGeometry(QRect(370, 270, 250, 40))
            self.lineEdit_11.setFont(font1)
            self.lineEdit_11.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                           "border:1px solid rgba(0,0,0,0);\n"
                                           "border-bottom-color:rgba(46,82,101,255);\n"
                                           "color:rgb(255,255,255);\n"
                                           "padding-bottom:7px")
            self.lineEdit_11.setEchoMode(QLineEdit.Normal)
            self.lineEdit_12 = QLineEdit(self.widget)
            self.lineEdit_12.setObjectName(u"lineEdit_12")
            self.lineEdit_12.setGeometry(QRect(370, 340, 250, 40))
            self.lineEdit_12.setFont(font1)
            self.lineEdit_12.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                           "border:1px solid rgba(0,0,0,0);\n"
                                           "border-bottom-color:rgba(46,82,101,255);\n"
                                           "color:rgb(255,255,255);\n"
                                           "padding-bottom:7px")
            self.lineEdit_12.setEchoMode(QLineEdit.Normal)
            self.lineEdit_13 = QLineEdit(self.widget)
            self.lineEdit_13.setObjectName(u"lineEdit_13")
            self.lineEdit_13.setGeometry(QRect(370, 410, 250, 40))
            self.lineEdit_13.setFont(font1)
            self.lineEdit_13.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                           "border:1px solid rgba(0,0,0,0);\n"
                                           "border-bottom-color:rgba(46,82,101,255);\n"
                                           "color:rgb(255,255,255);\n"
                                           "padding-bottom:7px")
            self.lineEdit_13.setEchoMode(QLineEdit.Normal)
            self.label = QLabel(self.widget)
            self.label.setObjectName(u"label")
            self.label.setGeometry(QRect(370, 560, 200, 20))
            self.label.setFont(font)
            self.label.setStyleSheet(u"QLabel#label{\n"
                                     "color: rgba(255, 255, 255, 200);\n"
                                     "border-radius:5px;\n"
                                     "}\n"
                                     "QLabel#label:hover{\n"
                                     "color: rgb(255, 255, 255)\n"
                                     "}")
            self.label.setAlignment(Qt.AlignCenter)

            self.retranslateUi(Form)

            QMetaObject.connectSlotsByName(Form)

        # setupUi

        def retranslateUi(self, Form):
            Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
            self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"  Gender ( Male / Female )", None))
            self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"  Age", None))
            self.pushButton.setText(QCoreApplication.translate("Form", u"S i n g   U p", None))
            self.label_3.setText(QCoreApplication.translate("Form", u"Register", None))
            self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"  Family", None))
            self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"  Name", None))
            self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"  User Name", None))
            self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
            self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Form", u"  Repeat Password", None))
            self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Form", u"  Email Address", None))
            self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Form", u"  Role", None))
            self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("Form", u"  State", None))
            self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("Form", u"  City", None))
            self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("Form", u"  Address", None))
            self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("Form", u"  Phone Number", None))
            self.label.setText(QCoreApplication.translate("Form", u"Already have account?", None))
        # retranslateUi

