# -*- coding: utf-8 -*-

"""
Module implementing NewsDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from Ui_news_dialog import Ui_Dialog
from condition import GetNews

class NewsDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(NewsDialog, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setColumnWidth(1, 380)
        self.buttonNotice.clicked.connect(self.shownotice)
        self.buttonNews.clicked.connect(self.shownews)
        self.buttonScience.clicked.connect(self.showscience)
        self.tableWidget.clicked.connect(self.jumpweb)
        self.urlList=[]
        self.domainName=''
        
    def shownotice(self):
        """show notices from website"""
        getnews=GetNews()
        self.domainName='http://today.hitwh.edu.cn/'
        self.urlList=[]
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.myItems=getnews.getnotices()
        row=0
        col=0
        for row in range(len(self.myItems)):
            self.tableWidget.insertRow(row)
            for col in range(len(self.myItems[0])):
                if col==0:
                    self.newItem = QTableWidgetItem(self.myItems[row][col])
                    self.tableWidget.setItem(row,2-col,self.newItem)
                elif col==1:
                    self.urlList.append(self.myItems[row][col])
                else:
                    self.newItem = QTableWidgetItem(self.myItems[row][col])
                    self.tableWidget.setItem(row,3-col,self.newItem) 
                col=col+1
            row=row+1
    def jumpweb(self):
        """jump to website to read details"""
        import webbrowser  
        row=self.tableWidget.currentItem().row()
        webbrowser.open(self.domainName+self.urlList[row])
    
    def shownews(self):
        """show news from website"""
        getnews=GetNews()
        self.domainName='http://news.hitwh.edu.cn/'
        self.urlList=[]
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.myItems=getnews.getnews()
        row=0
        col=0
        for row in range(20):
            self.tableWidget.insertRow(row)
            for col in range(len(self.myItems[0])):
                if col==0:
                    self.urlList.append(self.myItems[row][col])
                elif col==1:
                    self.newItem = QTableWidgetItem(self.myItems[row][col])
                    self.tableWidget.setItem(row,col,self.newItem)
                elif col==2:
                    self.newItem = QTableWidgetItem(self.myItems[row][col])
                    self.tableWidget.setItem(row,2-col,self.newItem)
                col=col+1
            row=row+1
    def showscience(self):
        """show notices from website"""
        getnews=GetNews()
        self.domainName='http://today.hitwh.edu.cn/'
        self.urlList=[]
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        self.myItems=getnews.getscience()
        row=0
        col=0
        for row in range(len(self.myItems)):
            self.tableWidget.insertRow(row)
            for col in range(len(self.myItems[0])):
                if col==0:
                    self.newItem = QTableWidgetItem(self.myItems[row][col])
                    self.tableWidget.setItem(row,2-col,self.newItem)
                elif col==1:
                    self.urlList.append(self.myItems[row][col])
                else:
                    self.newItem = QTableWidgetItem(self.myItems[row][col])
                    self.tableWidget.setItem(row,3-col,self.newItem) 
                col=col+1
            row=row+1
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import  QApplication
    app = QApplication(sys.argv)
    window = NewsDialog()
    window.show()
    sys.exit(app.exec_())
