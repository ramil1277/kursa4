from PyQt5.QtSql import *

class Database:
    def __init__(self, main_window):
        self.mainwindow = main_window
        self.db = QSqlDatabase.addDatabase('QPSQL')
        self.db.setHostName('localhost')
        self.db.setPort(5432)
        self.db.setDatabaseName('kursach')
        self.db.setUserName('postgres')
        self.db.setPassword('student')
        self.db.open()