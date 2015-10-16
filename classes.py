# -*- coding: utf-8 -*-

"""
Module implementing ClassDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox

from Ui_class_dialog import Ui_dialog

from login import GetItems
class ClassDialog(QDialog, Ui_dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(ClassDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonQuery.clicked.connect(self.queryclass)
        i=0
        j=0
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setColumnWidth(i, 150)
                self.tableWidget.setRowHeight(j, 60)
    def cleartable(self):
        """clear tableWidget"""
        row=0
        col=0
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                self.item=QTableWidgetItem('')
                self.tableWidget.setItem(row, col, self.item)
                
    def queryclass(self):
        """query classes from website"""
        getitems=GetItems()
        stuid=self.lineStuid.text()
        pwd=self.linePwd.text()
        if stuid=="" or pwd=="":
            QMessageBox.information(self, "Warning", self.tr("用户名或密码错误！"))
        else:
            currentWeek=int(self.comboBox.currentText())
            getitems.setpost(stuid, pwd)
            getitems.getauthstatus()
            if getitems.isAuth==False:
                QMessageBox.information(self, "Warning", self.tr("用户名或密码错误！"))
            else:
                self.cleartable()
                self.myItems=getitems.getclass()
                row=0
                col=0
                for row in range(len(self.myItems)):
                    for col in range(len(self.myItems[0])):
                        self.item=QTableWidgetItem(str(self.myItems[row][0])+'\n         '+str(self.myItems[row][1]))
                
                        tRow=int(self.myItems[row][3])
                        tCol=int(self.myItems[row][2])
                        weekL=int(self.myItems[row][4])
                        weekH=int(self.myItems[row][5])
                        if currentWeek<=weekH and currentWeek>=weekL:
                            self.tableWidget.setItem(tRow-1, tCol-1, self.item)
                
                    
if __name__=="__main__":
    import sys
    from PyQt5.QtWidgets import  QApplication
    app = QApplication(sys.argv)
    window = ClassDialog()
    window.show()
    sys.exit(app.exec_())
    
