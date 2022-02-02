import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('halsatu.ui', self)

class Extended(QDialog):
    def __init__(self):
        super(Extended, self).__init__()
        loadUi('extended.ui', self)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.addWidget(Login())  # Index jadi 0   
widget.addWidget(Extended())  # Index jadi 1
widget.setCurrentIndex(0)
widget.setFixedWidth(500)
widget.setFixedHeight(500)
widget.show()
app.exec_()

print("1 vigenere, 2 full, 3 autokey, 4 running key, 5 playfair, 6 enigma")
type = input("Type 1/2/3/4/5/6: ")


