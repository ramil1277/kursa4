from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

class Table:
    def __init__(self, main_window):
        super().__init__()
        self.mainwindow = main_window
        self.table_1()
        self.table_2()
        
        self.mainwindow.tableView_1.setEditTriggers(QTableView.NoEditTriggers)
        self.mainwindow.tableView_2.setEditTriggers(QTableView.NoEditTriggers)
    
        self.mainwindow.tableView_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainwindow.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.mainwindow.tableView_2.hideColumn(0)
        
    def table_1(self):
        query = QSqlQueryModel()
        query.setQuery("SELECT * FROM flights")
        self.mainwindow.tableView_1.setModel(query)
        query.setHeaderData(0, Qt.Horizontal, "Номер рейса")
        query.setHeaderData(1, Qt.Horizontal, "Кон.аэропорт")
        query.setHeaderData(2, Qt.Horizontal, "Время вылета")
        query.setHeaderData(3, Qt.Horizontal, "Тип самолета")
        query.setHeaderData(4, Qt.Horizontal, "Кол-во мест")
        query.setHeaderData(5, Qt.Horizontal, "Цена билета")
        
    def table_2(self):
        query = QSqlQueryModel()
        query.setQuery("SELECT * FROM tickets_sold")
        self.mainwindow.tableView_2.setModel(query)
        query.setHeaderData(1, Qt.Horizontal, "Номер рейса")
        query.setHeaderData(2, Qt.Horizontal, "Дата")
        query.setHeaderData(3, Qt.Horizontal, "Кол-во проданных билетов")
        
