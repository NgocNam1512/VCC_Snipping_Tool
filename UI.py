from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from VCCCutTool import VCCCrop
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        self.label.setText("you pressed the button")
        input = self.textEdit.toPlainText()
        VCCCrop(input)
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("VCC Snipping Tool")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50,50)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 250, 30))
        self.textEdit.setObjectName("textEdit")

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setGeometry(QtCore.QRect(100, 100, 50, 50))
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()