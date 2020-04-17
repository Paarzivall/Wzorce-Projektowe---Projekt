from tkinter import *
from src.CreateWindow import CreateWindow
from src.SelectQuery import SelectQuery
from src.ConnectToSQLdb import ConnectToSQLdb
from src.Iterator import Iterator


class CreateResultWindow(CreateWindow):
    _instance = None
    @staticmethod
    def get_instance():
        if CreateResultWindow._instance is None:
            return CreateResultWindow()
        return CreateResultWindow._instance

    def __init__(self):
        if CreateResultWindow._instance is None:
            super().__init__()
        self.list_of_car = []
        self.create_list_of_car()
        CreateResultWindow._instance = self

    def create_list_of_car(self):
        sql = 'SELECT id_samochodu, marka, model, rok_produkcji FROM Samochody WHERE zarezerwowany = 1'
        query_type = SelectQuery()
        connection = ConnectToSQLdb(query_type)
        self.list_of_car = connection.execute_query(connection.get_cursor(), sql)


    def add_buttons(self):
        pass

    def add_labels(self):
        warn = Label(self.window, text="Zarezerwowane Samochody")
        warn.place(x=370, y=30)
        warn.config(font="bold", fg="red")

    def add_other_components(self):
        t = Text(self.window)
        x = 435
        y = 60
        for element in self.list_of_car:
            result = ''
            it = Iterator(element)
            it.set_first()
            while it.is_done():
                result += str(it.get_current_item()) + '\n'
                it.next()
            result += '\n\n'
            tmp = Label(self.window, text=result)
            tmp.place(x=x, y=y)
            tmp.config(font="bold")
            y += 100
