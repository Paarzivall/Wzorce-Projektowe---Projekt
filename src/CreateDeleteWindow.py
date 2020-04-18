from tkinter import *
from tkinter import messagebox
from datetime import date, datetime, timedelta
import tkinter.ttk as ttk
from src.CreateWindow import CreateWindow
from src.ConnectToSQLdb import ConnectToSQLdb
from src.SelectQuery import SelectQuery
from src.InsertQuery import InsertQuery
from src.UpdateQuery import UpdateQuery
from src.CreateResultWindow import CreateResultWindow
from src.Iterator import Iterator


class CreateDeleteWindow(CreateWindow):
    def __init__(self):
        super().__init__()
        self.connection = None

    def add_buttons(self):
        delete_button = Button(self.window, text="Usuń rezerwacje", command=self.delete_reservation, width=40, height=3)
        delete_button.place(x=145, y=150)

    def add_labels(self):
        pass

    def delete_reservation(self):
        if self.next_step():
            if self.check_reservation():
                self.create_free_car()
                sql = "UPDATE rezerwacje SET koniec_rezerwacji = '" + str(date.today()) + \
                      "' WHERE id_rezerwacji = '" + str(self.res_id) + "'"
                query = UpdateQuery()
                self.connection = ConnectToSQLdb(query)
                self.connection.execute_query(self.connection.get_cursor(), sql)
                self.close_all()
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo('Done', 'Usunięto rezerwacje, do zapłaty: ' + str(self.calculate_cost()))
            else:
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo('Error', 'Brak rezerwacji dla tego klienta')
        else:
            Tk().wm_withdraw()  # to hide the main window
            messagebox.showinfo('Error', 'Uzupełnij Brakujące pola')

    def calculate_cost(self):
        sql = "select rezerwacje.start_rezerwacji, samochody.cena_wypozyczenia FROM rezerwacje INNER JOIN " \
              "samochody ON rezerwacje.id_samochodu = samochody.id_samochodu WHERE rezerwacje.id_rezerwacji = '" + \
              str(self.res_id) + "'"
        query_type = SelectQuery()
        self.connection = ConnectToSQLdb(query_type)
        table_of_result = self.connection.execute_query(self.connection.get_cursor(), sql)
        self.close_all()
        day_cost = table_of_result[0][1]
        (rok, mies, day) = str(table_of_result[0][0]).split('-')
        (a_rok, a_mies, a_day) = str(date.today()).split('-')
        diff = abs(date(int(a_rok), int(a_mies), int(a_day)) - date(int(rok), int(mies), int(day))).days
        if diff == 0:
            return day_cost
        else:
            return int(day_cost) * int(diff)

    def create_free_car(self):
        sql = "UPDATE samochody SET zarezerwowany = '0' WHERE id_samochodu = " + str(self.get_car_id())
        query = UpdateQuery()
        self.connection = ConnectToSQLdb(query)
        self.connection.execute_query(self.connection.get_cursor(), sql)
        self.close_all()

    def next_step(self):
        if self.mail.get() == '' or self.car.get() == '':
            return False
        else:
            return True

    def check_reservation(self):
        email = str(self.mail.get())
        car_id = self.get_car_id()
        sql = "SELECT rezerwacje.id_rezerwacji, klienci.email, samochody.id_samochodu FROM samochody INNER JOIN " \
              "(klienci INNER JOIN rezerwacje on klienci.id_klienta = rezerwacje.id_klienta) on " \
              "samochody.id_samochodu = rezerwacje.id_samochodu where klienci.email = '" + email + \
              "' and samochody.id_samochodu = '" + car_id + "'"
        query_type = SelectQuery()
        self.connection = ConnectToSQLdb(query_type)
        table_of_result = self.connection.execute_query(self.connection.get_cursor(), sql)
        self.close_all()
        if len(table_of_result) > 0:
            self.res_id = table_of_result[0][0]
            return True
        else:
            return False

    def get_car_id(self):
        car = str(self.car.get())
        return car[:car.index(" ")]

    def add_values_to_combobox(self):
        sql = "SELECT samochody.id_samochodu, samochody.marka, samochody.model from rezerwacje INNER JOIN samochody " \
              "on rezerwacje.id_samochodu = samochody.id_samochodu WHERE samochody.zarezerwowany = '1' " \
              "and rezerwacje.koniec_rezerwacji IS NULL"
        tmp_table = []
        query_type = SelectQuery()
        self.connection = ConnectToSQLdb(query_type)
        table_of_result = self.connection.execute_query(self.connection.get_cursor(), sql)
        self.close_all()
        for res in table_of_result:
            tmp = ''
            it = Iterator(res)
            it.set_first()
            while it.is_done():
                tmp += str(it.get_current_item()) + ' '
                it.next()
            tmp_table.append(tmp)
        print(tmp_table)
        return tmp_table

    def close_all(self):
        self.connection.close_cursor()
        self.connection.close_connection()

    def add_other_components(self):
        value = StringVar()
        mail_label = Label(self.window, text="E-mail: ")
        mail_label.place(x=75, y=21)
        self.mail = Entry(self.window, width=50)
        self.mail.place(x=165, y=20)
        car_label = Label(self.window, text="Jaki Samochód: ")
        car_label.place(x=75, y=45)
        self.car = ttk.Combobox(self.window, textvariable=value, width=50)
        self.car.place(x=165, y=45)
        self.car['values'] = self.add_values_to_combobox()


