# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Program\Eric6\HITers\news_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(783, 554)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/HITers.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(140, 40, 631, 461))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section{background:rgb(85, 170, 255)};")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.buttonNews = QtWidgets.QPushButton(Dialog)
        self.buttonNews.setGeometry(QtCore.QRect(20, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.buttonNews.setFont(font)
        self.buttonNews.setObjectName("buttonNews")
        self.buttonNotice = QtWidgets.QPushButton(Dialog)
        self.buttonNotice.setGeometry(QtCore.QRect(20, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.buttonNotice.setFont(font)
        self.buttonNotice.setObjectName("buttonNotice")
        self.buttonScience = QtWidgets.QPushButton(Dialog)
        self.buttonScience.setGeometry(QtCore.QRect(20, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.buttonScience.setFont(font)
        self.buttonScience.setObjectName("buttonScience")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "工大动态"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "标题"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "浏览量"))
        self.buttonNews.setText(_translate("Dialog", "工大新闻"))
        self.buttonNotice.setText(_translate("Dialog", "通知公告"))
        self.buttonScience.setText(_translate("Dialog", "学术科研"))

from res import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

