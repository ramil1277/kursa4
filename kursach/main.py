import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from design.mainwindow import MainWindow
from bin.db import Database
from bin.table import Table

class Main(MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.database = Database(self)
        self.table = Table(self)
        
        self.groupBox_fly_1.hide()
        self.groupBox_fly_2.hide()
        self.groupBox_ticked_1.hide()
        self.groupBox_ticked_2.hide()
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        
        self.add.setCheckable(True)
        self.add_2.setCheckable(True)
        self.change.setCheckable(True)
        self.change_2.setCheckable(True)    
        self.add.clicked.connect(self.createfly)
        self.change.clicked.connect(self.changefly)
        self.add_2.clicked.connect(self.createtick)
        self.change_2.clicked.connect(self.changetick)
        self.ok_1.clicked.connect(self.table.table_add)
        self.ok_2.clicked.connect(self.table.table_add_2)
        
    def createfly(self):
        if self.add.isChecked() == True:
            self.groupBox_fly_1.show()
        elif self.add.isChecked() == False:
            self.groupBox_fly_1.hide()
            
    def changefly(self):
        if self.change.isChecked() == True:
            self.groupBox_fly_2.show()
        else:
            self.groupBox_fly_2.hide()
        
    def createtick(self):
        if self.add_2.isChecked() == True:
            self.groupBox_ticked_1.show()
        else:
            self.groupBox_ticked_1.hide()
            
    def changetick(self):
        if self.change_2.isChecked() == True:
            self.groupBox_ticked_2.show()
        else:
            self.groupBox_ticked_2.hide()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()