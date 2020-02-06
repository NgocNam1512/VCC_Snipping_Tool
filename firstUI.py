# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from VCCCutTool import VCCCropBorder, VCCCropSmallBoard

class Ui_MainWindow(object):
    def testClicked(self):
        self.label_warning.setText("you pressed the button")
        name = self.textEdit_name.toPlainText()
        try:
            VCCCropBorder(name)
        except:
            self.label_warning.setText("Check the filename")


    def cutClicked(self):
        self.label_warning.setText("you clicked ""Cut"" ")
        name = self.textEdit_name.toPlainText()
        row = int(self.textEdit_row.toPlainText())
        column = int(self.textEdit_column.toPlainText())
        top = int(self.textEdit_top.toPlainText())
        bottom = int(self.textEdit_bottom.toPlainText())
        left = int(self.textEdit_left.toPlainText())
        right = int(self.textEdit_right.toPlainText())
        try:
            VCCCropSmallBoard(name, row, column, left, right, top, bottom)
        except:
            self.label_warning.setText("Please check the info")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 440)
        MainWindow.setAnimated(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_cut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cut.setGeometry(QtCore.QRect(150, 360, 75, 23))
        self.pushButton_cut.setObjectName("pushButton_cut")
        self.pushButton_cut.clicked.connect(self.cutClicked)

        self.pushButton_test = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_test.setGeometry(QtCore.QRect(250, 360, 75, 23))
        self.pushButton_test.setObjectName("pushButton_test")
        self.pushButton_test.clicked.connect(self.testClicked)

        self.textEdit_row = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_row.setGeometry(QtCore.QRect(100, 120, 141, 31))
        self.textEdit_row.setObjectName("textEdit_row")

        self.label_column = QtWidgets.QLabel(self.centralwidget)
        self.label_column.setGeometry(QtCore.QRect(270, 130, 47, 13))
        self.label_column.setObjectName("label_column")

        self.textEdit_column = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_column.setGeometry(QtCore.QRect(320, 120, 141, 31))
        self.textEdit_column.setObjectName("textEdit_column")

        self.label_row = QtWidgets.QLabel(self.centralwidget)
        self.label_row.setGeometry(QtCore.QRect(40, 130, 47, 13))
        self.label_row.setObjectName("label_row")

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(40, 20, 47, 13))
        self.label_name.setObjectName("label_name")

        self.textEdit_name = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_name.setGeometry(QtCore.QRect(100, 10, 241, 31))
        self.textEdit_name.setObjectName("textEdit_name")

        self.label_top = QtWidgets.QLabel(self.centralwidget)
        self.label_top.setGeometry(QtCore.QRect(220, 180, 47, 13))
        self.label_top.setObjectName("label_top")

        self.label_bottom = QtWidgets.QLabel(self.centralwidget)
        self.label_bottom.setGeometry(QtCore.QRect(210, 270, 47, 13))
        self.label_bottom.setObjectName("label_bottom")

        self.label_left = QtWidgets.QLabel(self.centralwidget)
        self.label_left.setGeometry(QtCore.QRect(80, 220, 47, 13))
        self.label_left.setObjectName("label_left")

        self.label_right = QtWidgets.QLabel(self.centralwidget)
        self.label_right.setGeometry(QtCore.QRect(350, 220, 47, 13))
        self.label_right.setObjectName("label_right")

        self.label_warning = QtWidgets.QLabel(self.centralwidget)
        self.label_warning.setGeometry(QtCore.QRect(210, 330, 100, 13))
        self.label_warning.setObjectName("label_warning")

        self.textEdit_top = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_top.setGeometry(QtCore.QRect(200, 200, 61, 31))
        self.textEdit_top.setObjectName("textEdit_top")

        self.textEdit_bottom = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_bottom.setGeometry(QtCore.QRect(200, 290, 61, 31))
        self.textEdit_bottom.setObjectName("textEdit_bottom")

        self.textEdit_right = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_right.setGeometry(QtCore.QRect(330, 240, 61, 31))
        self.textEdit_right.setObjectName("textEdit_right")

        self.textEdit_left = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_left.setGeometry(QtCore.QRect(60, 240, 61, 31))
        self.textEdit_left.setObjectName("textEdit_left")

        self.label_default = QtWidgets.QLabel(self.centralwidget)
        self.label_default.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_default.setObjectName("label_default")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.setDefaultValue(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_cut.setText(_translate("MainWindow", "Cut"))
        self.pushButton_test.setText(_translate("MainWindow", "Test"))
        self.label_column.setText(_translate("MainWindow", "Column:"))
        self.label_row.setText(_translate("MainWindow", "Row:"))
        self.label_name.setText(_translate("MainWindow", "Filename:"))
        self.label_top.setText(_translate("MainWindow", "Top"))
        self.label_bottom.setText(_translate("MainWindow", "Bottom"))
        self.label_left.setText(_translate("MainWindow", "Left"))
        self.label_right.setText(_translate("MainWindow", "Right"))
        self.label_warning.setText(_translate("MainWindow", "Warning"))
        self.label_default.setText(_translate("MainWindow", "Default:"))

    def setDefaultValue(self, MainWindow):
        self.textEdit_row.setText("3")
        self.textEdit_column.setText("1")
        self.textEdit_left.setText("80")
        self.textEdit_right.setText("30")
        self.textEdit_top.setText("130")
        self.textEdit_bottom.setText("130")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
