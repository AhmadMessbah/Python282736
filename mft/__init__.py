# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign in_viewWXqPhY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 551)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 380, 521))
        self.widget.setStyleSheet(u"background-color: rgba(16, 30, 41, 240);\n"
"border-radius:10px;\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 161, 131))
        font = QFont()
        font.setPointSize(70)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 125, 236);")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 210, 250, 40))
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
        self.lineEdit_2.setGeometry(QRect(70, 270, 250, 40))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QRect(70, 330, 160, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.checkBox.setFont(font2)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"QCheckBox#checkBox{\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}")
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 380, 140, 40))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton.setFont(font3)
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
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 460, 250, 20))
        font4 = QFont()
        font4.setPointSize(9)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"QLabel#label_2{\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QLabel#label_2:hover{\n"
"color: rgb(255, 255, 255)\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\ue094", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"  User Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
#if QT_CONFIG(whatsthis)
        self.checkBox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.checkBox.setText(QCoreApplication.translate("Form", u"Remember me", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"S i g n   I n", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Forgot your User Name or Password ?", None))
    # retranslateUi

