# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Program\Eric6\HITers\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 439)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/HITers.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.buttonNews = QtWidgets.QPushButton(self.centralWidget)
        self.buttonNews.setGeometry(QtCore.QRect(30, 60, 101, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.buttonNews.setFont(font)
        self.buttonNews.setObjectName("buttonNews")
        self.buttonGrade = QtWidgets.QPushButton(self.centralWidget)
        self.buttonGrade.setGeometry(QtCore.QRect(30, 170, 101, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.buttonGrade.setFont(font)
        self.buttonGrade.setObjectName("buttonGrade")
        self.buttonClass = QtWidgets.QPushButton(self.centralWidget)
        self.buttonClass.setGeometry(QtCore.QRect(30, 280, 101, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonClass.setFont(font)
        self.buttonClass.setObjectName("buttonClass")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(160, -10, 571, 431))
        self.label.setStyleSheet("image: url(:/HIT.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HITers"))
        self.buttonNews.setText(_translate("MainWindow", "工大动态"))
        self.buttonGrade.setText(_translate("MainWindow", "成绩查询"))
        self.buttonClass.setText(_translate("MainWindow", "课表查询"))

from res import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

