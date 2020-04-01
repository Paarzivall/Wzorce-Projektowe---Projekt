from tkinter import *
from src.CreateWindow import CreateWindow
from src.SelectQuery import SelectQuery
from src.ConnectToSQLdb import ConnectToSQLdb

class CreateResultWindow(CreateWindow):
    _instance = None
    @staticmethod
    def get_instance():
        if CreateResultWindow._instance == None:
            return CreateResultWindow()
        return CreateResultWindow._instance

    def __init__(self):
        if CreateResultWindow._instance == None:
            super().__init__()
        self.list_of_car = []
        self.create_list_of_car()
        CreateResultWindow._instance = self

    def create_list_of_car(self):
        sql = 'SELECT * FROM Samochody WHERE zarezerwowany = 0'
        query_type = SelectQuery()
        connection = ConnectToSQLdb(query_type)
        self.list_of_car = connection.execute_query(connection.get_cursor(), sql)
        print(self.list_of_car)


    def add_buttons(self):
        pass

    def add_labels(self):
        warn = Label(self.window, text="Dostępne Auta")
        warn.place(x=400, y=30)
        warn.config(font="bold", fg="red")

    def add_other_components(self):
        t = Text(self.window)
        x = 435
        y = 60
        for element in self.list_of_car:
            print(str(element[1]) + '\n' + str(element[2]) + '\n' + str(element[3]) + '\n' + str(element[4]) + '\n')
            tmp = Label(self.window, text=str(element[1]) + '\n' + str(element[2]) + '\n' + str(element[3]) + '\n' + str(element[4]) + '\n')
            tmp.place(x=x, y=y)
            tmp.config(font="bold")
            y += 100
