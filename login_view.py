# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\devspace\python\reseaux\chatkinator\login_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Formulaire de connection")
        Form.resize(351, 328)
        Form.setStyleSheet("background-color: #333;")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 331, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resource/24/user-circle-o.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignVCenter)
        self.ldtUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ldtUsername.setFont(font)
        self.ldtUsername.setStyleSheet("color: white;")
        self.ldtUsername.setObjectName("ldtUsername")
        self.verticalLayout.addWidget(self.ldtUsername, 0, QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(329, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ltdHost = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ltdHost.setFont(font)
        self.ltdHost.setStyleSheet("color: white;")
        self.ltdHost.setObjectName("ltdHost")
        self.verticalLayout.addWidget(self.ltdHost)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.btnLogin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("color: white;\n"
"padding: 7px;\n"
"border: 1px solid white;\n"
"")
        self.btnLogin.setObjectName("btnLogin")
        self.verticalLayout.addWidget(self.btnLogin)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Nom d\'utilisateur:"))
        self.label_3.setText(_translate("Form", "Adresse de l\'hôte:"))
        self.btnLogin.setText(_translate("Form", "Se connecter"))

