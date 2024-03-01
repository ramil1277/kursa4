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
        
    def table_add(self):
        if self.mainwindow.fly_line.text() and self.mainwindow.finalfly_line.text() and self.mainwindow.timefly_line.text() and self.mainwindow.tipfly_line.text() and self.mainwindow.quantityplace_line.text() and self.mainwindow.priceticket_line.text():
            query = QSqlQuery()
            query.exec(f"""INSERT INTO flights(number_flights, final_airport, flyit, tip_airplane, quantity_place, price_tick) 
                    VALUES ('{self.mainwindow.fly_line.text()}', '{self.mainwindow.finalfly_line.text()}', '{self.mainwindow.timefly_line.text()}', '{self.mainwindow.tipfly_line.text()}', '{self.mainwindow.quantityplace_line.text()}', '{self.mainwindow.priceticket_line.text()}');""")
            if query.isActive() == False:
                pass
        self.table_1()
        self.mainwindow.groupBox_fly_1.hide()
        
    def table_add_2(self):
        if self.mainwindow.date_add_line.text() and self.mainwindow.quantitetick_line.text():
            query = QSqlQuery()
            query.exec(f"""INSERT INTO tickets_sold(date, quntity_tickets_sold) 
                    VALUES ('{self.mainwindow.date_add_line.text()}', '{self.mainwindow.quantitetick_line.text()}');""")
            if query.isActive() == False:
                pass
        self.table_2()
        self.mainwindow.groupBox_ticked_1.hide()
