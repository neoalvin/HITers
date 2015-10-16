# -*- coding: utf-8 -*-

"""
Module implementing GradeDialog.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QCheckBox, QWidget

from Ui_grade_dialog import Ui_Dialog
from login import GetItems

class GradeDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(GradeDialog, self).__init__(parent)
        self.setupUi(self)
        self.radioPast.checked=True
        self.buttonQuery.clicked.connect(self.getgrade)
        self.buttonCalcu.clicked.connect(self.calcgrade)
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 150)
    def getgrade(self):
        """initialize TableView"""
        getitems=GetItems()
        stuid=self.lineStuid.text()
        pwd=self.linePwd.text()
        if stuid=="" or pwd=="":
            QMessageBox.information(self, 'Warning', self.tr("用户名或密码错误！"))
        else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.clearContents()
            getitems.setpost(stuid, pwd)
            getitems.getauthstatus()
            if getitems.isAuth==False:
                QMessageBox.information(self, "Warning", self.tr("用户名或密码错误！"))
            else:
                self.myItems=getitems.getgrade()
                row=0
                col=0
#        self.newItem = QTableWidgetItem('Item')
#        self.tableWidget.insertRow(0)
#        self.tableWidget.setItem(0,0,self.newItem)
                for row in range(len(self.myItems)):
                    self.tableWidget.insertRow(row)
                    self.checkbox=QCheckBox(self)
                    self.tableWidget.setCellWidget(row, 0, self.checkbox)
                    for col in range(len(self.myItems[0])):
                        self.newItem = QTableWidgetItem(self.myItems[row][col])
                        self.tableWidget.setItem(row,col+1,self.newItem)
                        col=col+1
                    row=row+1
    def turngpabu(self, score):
        """return score to gpa in Beijing University"""
        grade=0
        grade=4-3*(pow((100-score), 2))/1600
        return grade
        
    def turngpastrict(self, score):
        """turn score to gpa strictly"""
        grade=0
        if 90<=score<=100:
            grade=4
        elif 80<=score<=89:
            grade=3
        elif 70<=score<=79:
            grade=2
        elif 60<=score<=69:
            grade=1
        else:
            grade=0
        return grade
    def calcgrade(self):
        """calculate averrage grade and GPA"""
        row=0
        grade=0     #学分
        gradebu=0   #北大算法科目绩点
        gradestr=0  #严格算法科目绩点
        gradesum=0  #总学分
        scoresum=0  #总成绩
        gradebusum=0    #北大算法总绩点
        gradestrsum=0   #严格算法总绩点
        scoreaver=0     #平均成绩 
        gradebuaver=0   #北大算法gpa
        gradestraver=0  #严格算法gpa
        count=0     #总课程数
        errorstr=""
        for row in range(self.tableWidget.rowCount()):
            #获取成绩
            if self.tableWidget.item(row,6).text()!="":
                score=float(self.tableWidget.item(row,6).text())
            else:
                score=0
            #获取学分
            if self.tableWidget.item(row, 2).text()!="":
                grade=float(self.tableWidget.item(row, 2).text())
            else:
                errorstr="课程<"+self.tableWidget.item(row, 1).text()+">学分有误！"
            scoresum+=score
            gradesum+=grade
            #北大算法
            gradebu=self.turngpabu(score)
            gradebusum=gradebusum+gradebu*grade
            #严格算法
            gradestr=self.turngpastrict(score)
            gradestrsum=gradestrsum+gradestr*grade
            #课程数+1
            count+=1
        scoreaver=scoresum/count    #平均成绩
        gradebuaver=gradebusum/gradesum     #北大算法GPA结果
        gradestraver=gradestrsum/gradesum   #严格算法GPA结果
        result="平均成绩:   "+str("%4.4f"%scoreaver)+"\n\n北大算法GPA:   "+str("%4.4f"%gradebuaver)+"\n\n严格算法GPA:   "+str("%4.4f"%gradestraver)+"\n"+errorstr
        #可选计算
        """for row in range(self.tableWidget.rowCount()):
            ckb=QCheckBox()
            ckb=QCheckBox(self.tableWidget.cellWidget(row, 0))
            if ckb.isChecked()==True:
                str+=self.tableWidget.item(row,1).text()"""
        msgBox=QMessageBox(self)  
        msgBox.setWindowTitle("绩点计算")  
        msgBox.addButton(self.tr("确定"), QMessageBox.ActionRole)  
        msgBox.addButton("退出",QMessageBox.ActionRole)  
  
        msgBox.setText(self.tr(result))
        msgBox.exec_()
        #QMessageBox.information(self,"information",self.tr("This is your GPA"))
if __name__ == '__main__':
 
    import sys  
    from PyQt5.QtWidgets import  QApplication
    app = QApplication(sys.argv)
    window = GradeDialog()
    window.show()
    sys.exit(app.exec_())
