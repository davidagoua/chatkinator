# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(801, 578)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(189, 79, 591, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtReadSection = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.txtReadSection.sizePolicy().hasHeightForWidth())
        self.txtReadSection.setSizePolicy(sizePolicy)
        self.txtReadSection.setReadOnly(True)
        self.txtReadSection.setObjectName("txtReadSection")
        self.verticalLayout.addWidget(self.txtReadSection)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 10, 591, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLogout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnLogout.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"color: rgb(255, 255, 255);\n"
"padding: 10px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/24/sign-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogout.setIcon(icon)
        self.btnLogout.setObjectName("btnLogout")
        self.horizontalLayout.addWidget(self.btnLogout)
        self.btnExit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnExit.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"color: rgb(255, 255, 255);\n"
"padding: 10px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resource/24/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon1)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout.addWidget(self.btnExit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(189, 490, 591, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtWriteSection = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.txtWriteSection.setObjectName("txtWriteSection")
        self.horizontalLayout_2.addWidget(self.txtWriteSection)
        self.btnSend = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btnSend.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"color: rgb(255, 255, 255);\n"
"padding: 10px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resource/24/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSend.setIcon(icon2)
        self.btnSend.setObjectName("btnSend")
        self.horizontalLayout_2.addWidget(self.btnSend)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 69, 181, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.listView.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(51, 51, 51);")
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 181, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"padding-left: 10px;\n"
"padding-right: 5px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resource/24/user-circle.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.labUsername = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.labUsername.sizePolicy().hasHeightForWidth())
        self.labUsername.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labUsername.setFont(font)
        self.labUsername.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(51, 51, 51);\n"
"padding-left:5px;\n"
"")
        self.labUsername.setObjectName("labUsername")
        self.horizontalLayout_3.addWidget(self.labUsername)
        self.horizontalLayout_3.setStretch(1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnLogout.setText(_translate("Form", "Se déconnecter"))
        self.btnExit.setText(_translate("Form", "Quitter"))
        self.btnSend.setText(_translate("Form", "Send"))
        self.labUsername.setText(_translate("Form", "Username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

