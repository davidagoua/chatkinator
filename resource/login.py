from PyQt5.QtWidgets import QWidget, QApplication
from login_view import Ui_Form


class Login(QWidget, Ui_Form):


    def __init__(self, parent=None):
        super(Login, self).__init__(parent=parent)
        self.setWindowTitle("Formulaire de connection")
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.setupClient)

    def setupClient(self):
        username = self.ldtUsername.text()
        password = self.ltdHost.text()
        print(f"Nom d'utilisateur: {username} \n Host: {password}")



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())
