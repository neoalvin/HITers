# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from Ui_main_window import Ui_MainWindow

from grade import GradeDialog
from classes import ClassDialog
from news import NewsDialog
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.gradewindow=GradeDialog()
        self.classWindow=ClassDialog()
        self.newsWindow=NewsDialog()
        self.buttonGrade.clicked.connect(self.gradewindow.show)
        self.buttonClass.clicked.connect(self.classWindow.show)
        self.buttonNews.clicked.connect(self.newsWindow.show)
if __name__ == '__main__':
 
    from PyQt5.QtWidgets import  QApplication
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
