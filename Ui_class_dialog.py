# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Program\Eric6\HITers\class_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setWindowModality(QtCore.Qt.NonModal)
        dialog.setEnabled(True)
        dialog.resize(827, 539)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        dialog.setFont(font)
        dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/HITers.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        dialog.setStyleSheet("alternate-background-color: rgb(85, 0, 255);")
        dialog.setSizeGripEnabled(True)
        self.tableWidget = QtWidgets.QTableWidget(dialog)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 791, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QHeaderView::section{background:rgb(85, 170, 255)};")
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(False)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.buttonQuery = QtWidgets.QPushButton(dialog)
        self.buttonQuery.setGeometry(QtCore.QRect(630, 450, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.buttonQuery.setFont(font)
        self.buttonQuery.setObjectName("buttonQuery")
        self.lineStuid = QtWidgets.QLineEdit(dialog)
        self.lineStuid.setGeometry(QtCore.QRect(380, 420, 151, 31))
        self.lineStuid.setObjectName("lineStuid")
        self.linePwd = QtWidgets.QLineEdit(dialog)
        self.linePwd.setGeometry(QtCore.QRect(380, 470, 151, 31))
        self.linePwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePwd.setObjectName("linePwd")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(330, 430, 31, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 480, 31, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(dialog)
        self.comboBox.setGeometry(QtCore.QRect(100, 420, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 420, 51, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "课表查询"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("dialog", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("dialog", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("dialog", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("dialog", "6"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dialog", "周一"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dialog", "周二"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dialog", "周三"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("dialog", "周四"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("dialog", "周五"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("dialog", "周六"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("dialog", "周日"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.buttonQuery.setText(_translate("dialog", "查询"))
        self.label.setText(_translate("dialog", "学号"))
        self.label_2.setText(_translate("dialog", "密码"))
        self.comboBox.setItemText(0, _translate("dialog", "1"))
        self.comboBox.setItemText(1, _translate("dialog", "2"))
        self.comboBox.setItemText(2, _translate("dialog", "3"))
        self.comboBox.setItemText(3, _translate("dialog", "4"))
        self.comboBox.setItemText(4, _translate("dialog", "5"))
        self.comboBox.setItemText(5, _translate("dialog", "6"))
        self.comboBox.setItemText(6, _translate("dialog", "7"))
        self.comboBox.setItemText(7, _translate("dialog", "8"))
        self.comboBox.setItemText(8, _translate("dialog", "9"))
        self.comboBox.setItemText(9, _translate("dialog", "10"))
        self.comboBox.setItemText(10, _translate("dialog", "11"))
        self.comboBox.setItemText(11, _translate("dialog", "12"))
        self.comboBox.setItemText(12, _translate("dialog", "13"))
        self.comboBox.setItemText(13, _translate("dialog", "14"))
        self.comboBox.setItemText(14, _translate("dialog", "15"))
        self.comboBox.setItemText(15, _translate("dialog", "16"))
        self.comboBox.setItemText(16, _translate("dialog", "17"))
        self.comboBox.setItemText(17, _translate("dialog", "18"))
        self.comboBox.setItemText(18, _translate("dialog", "19"))
        self.comboBox.setItemText(19, _translate("dialog", "20"))
        self.comboBox.setItemText(20, _translate("dialog", "21"))
        self.comboBox.setItemText(21, _translate("dialog", "22"))
        self.label_3.setText(_translate("dialog", "当前周数"))

from res import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

