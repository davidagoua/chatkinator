from PyQt5.QtWidgets import QApplication, QWidget
from home_view import Ui_Form
from datetime import datetime


class Message(object):

    def __init__(self, sender=None, contenue=None):
        self.sender = sender
        self.contenue = contenue
        self.time = datetime.now()

    def getHtml(self):
        html = f"""
<div style="width: 70%; background-color: #ddf">
    <div style="justify-content: space-between; padding: 4px; background-color: #eee">
        <h3 style="flex-grow: 1">{self.sender}</h3>
        <small>{str(self.time)}</small>
    </div>
    <div style="padding: 5px">{self.contenue}<div/>
</div>
<hr/>
        """
        return html


class Home(QWidget, Ui_Form):

    sender: str = "James"

    def __init__(self, parent=None):
        super(Home, self).__init__(parent=parent)
        self.setupUi(self)
        self.setupBtn()

    def setupBtn(self):
        self.btnExit.clicked.connect(lambda: sys.exit())
        self.btnSend.clicked.connect(self.sendMessage)

    def buildMessage(self):
        message = None
        text: str = self.txtWriteSection.toPlainText()
        if text is not None and text != "":
            message = Message(sender=self.sender, contenue=text)
        return message

    def sendMessage(self):
        message = self.buildMessage()
        if message is not None:
            self.notify(message)
        self.txtWriteSection.setPlainText("")

    def notify(self, message: Message):
        self.txtReadSection.appendHtml(message.getHtml())



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec())