from tkinter import *
from tkinter import messagebox
from datetime import date, datetime
import tkinter.ttk as ttk
from src.CreateWindow import CreateWindow
from src.ConnectToSQLdb import ConnectToSQLdb
from src.SelectQuery import SelectQuery
from src.InsertQuery import InsertQuery
from src.UpdateQuery import UpdateQuery
from src.CreateResultWindow import CreateResultWindow
from src.CreateDeleteWindow import CreateDeleteWindow
from src.Iterator import Iterator


class CreateMainWindow(CreateWindow):
    def __init__(self):
        super().__init__()
        self.connection = None

    def add_buttons(self):
        add_button = Button(self.window, text="Dodaj nową rezerwację", command=self.add_reservation, width=40, height=3)
        add_button.place(x=145, y=250)
        search_button = Button(self.window, text="Sprawdź zarezerwowane auta", command=self.show_free_cars, width=40, height=3)
        search_button.place(x=615, y=30)

        delete_button = Button(self.window, text="Usuń rezerwacje", command=self.delete_window, width=40, height=3)
        delete_button.place(x=145, y=350)

    def delete_window(self):
        window = CreateDeleteWindow()
        window.start_app()

    def show_free_cars(self):
        window = CreateResultWindow.get_instance()
        window.start_app()

    def add_reservation(self):
        if self.next_step():
            if self.check_client():
                self.add_new_client()
            sql = "INSERT INTO rezerwacje(id_klienta, id_samochodu, start_rezerwacji) " \
                  "VALUES('" + str(self.get_client_id()) + "', '" + str(self.get_car_id()) + "', '" \
                  + str(date.today()) + "')"
            query = InsertQuery()
            self.connection = ConnectToSQLdb(query)
            self.connection.execute_query(self.connection.get_cursor(), sql)
            self.close_all()
            self.update_car_status()
        else:
            Tk().wm_withdraw()  # to hide the main window
            messagebox.showinfo('Error', 'Uzupełnij Brakujące pola')

    def get_client_id(self):
        sql = "SELECT id_klienta FROM klienci WHERE email = '" + str(self.mail.get()) + "'"
        query = SelectQuery()
        self.connection = ConnectToSQLdb(query)
        client_id = self.connection.execute_query(self.connection.get_cursor(), sql)
        self.close_all()
        return client_id[0][0]

    def check_client(self):
        sql = "SELECT * FROM klienci WHERE email = '" + str(self.mail.get()) + "'"
        query = SelectQuery()
        self.connection = ConnectToSQLdb(query)
        client = self.connection.execute_query(self.connection.get_cursor(), sql)
        self.close_all()
        if len(client) < 1:
            return True
        else:
            return False

    def add_new_client(self):
        sql = "INSERT INTO klienci(imie, nazwisko, ulica, nr_domu, miasto, kod_pocztowy, nr_telefonu, email) " \
              "VALUES('" + str(self.name.get()) + "', '" + str(self.surname.get()) + "', '" + \
              str(self.ulica.get()) + "','" + str(self.home.get()) + "', '" + str(self.city.get()) + "', '" + \
              str(self.pc.get()) + "', '" + str(self.phone.get()) + "', '" + str(self.mail.get()) + "')"
        query = InsertQuery()
        self.connection = ConnectToSQLdb(query)
        self.connection.execute_query(self.connection.get_cursor(), sql)
        self.close_all()

    def get_car_id(self):
        car = str(self.car.get())
        return car[:car.index(" ")]

    def update_car_status(self):
        sql = "UPDATE samochody SET zarezerwowany = '1' WHERE id_samochodu=" + str(self.get_car_id())
        query = UpdateQuery()
        self.connection = ConnectToSQLdb(query)
        self.connection.execute_query(self.connection.get_cursor(), sql)
        self.close_all()

    def next_step(self):
        if self.name.get() == '' or self.surname.get() == '' or self.ulica.get() == '' or \
                self.home.get() == '' or self.city.get() == '' or self.pc.get() == '' or self.phone.get() == '' or \
                self.mail.get() == '' or self.car.get() == '':
            return False
        else:
            return True

    def add_labels(self):
        warn = Label(self.window, text="Przykładowe wolne auta")
        warn.place(x=650, y=100)
        warn.config(fg="red", font="bold")
        self.example_cars()

    def example_cars(self):
        sql = 'SELECT marka, model, rok_produkcji, cena_wypozyczenia FROM Samochody WHERE zarezerwowany = 0 LIMIT 2'
        query_type = SelectQuery()
        connection = ConnectToSQLdb(query_type)
        cars = connection.execute_query(connection.get_cursor(), sql)
        result = ''
        for car in cars:
            it = Iterator(car)
            it.set_first()
            while it.is_done():
                result += str(it.get_current_item()) + '\n'
                it.next()
            result += '\n\n'
        result_label = Label(self.window, text=result)
        result_label.place(x=730, y=150)

    def close_all(self):
        self.connection.close_cursor()
        self.connection.close_connection()

    def add_values_to_combobox(self):
        sql = 'SELECT id_samochodu, marka, model, rok_produkcji, cena_wypozyczenia FROM Samochody WHERE zarezerwowany = 0'
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
        return tmp_table

    def add_other_components(self):
        value = StringVar()
        name_label = Label(self.window, text="Imie: ")
        name_label.place(x=75, y=21)
        self.name = Entry(self.window, width=50)
        self.name.place(x=165, y=20)
        surname_label = Label(self.window, text="Nazwisko: ")
        surname_label.place(x=75, y=45)
        self.surname = Entry(self.window, width=50)
        self.surname.place(x=165, y=45)
        ulica_label = Label(self.window, text="Ulica: ")
        ulica_label.place(x=75, y=70)
        self.ulica = Entry(self.window, width=50)
        self.ulica.place(x=165, y=70)
        home_label = Label(self.window, text="Nr. Domu: ")
        home_label.place(x=75, y=95)
        self.home = Entry(self.window, width=50)
        self.home.place(x=165, y=95)
        city_label = Label(self.window, text="Miasto: ")
        city_label.place(x=75, y=120)
        self.city = Entry(self.window, width=50)
        self.city.place(x=165, y=120)
        pc_label = Label(self.window, text="Kod pocztowy: ")
        pc_label.place(x=75, y=145)
        self.pc = Entry(self.window, width=50)
        self.pc.place(x=165, y=145)
        phone_label = Label(self.window, text="Nr. Telefonu: ")
        phone_label.place(x=75, y=170)
        self.phone = Entry(self.window, width=50)
        self.phone.place(x=165, y=170)
        mail_label = Label(self.window, text="E-mail: ")
        mail_label.place(x=75, y=195)
        self.mail = Entry(self.window, width=50)
        self.mail.place(x=165, y=195)
        car_label = Label(self.window, text="Jaki Samochód: ")
        car_label.place(x=75, y=220)
        self.car = ttk.Combobox(self.window, textvariable=value, width=50)
        self.car.place(x=165, y=220)
        self.car['values'] = self.add_values_to_combobox()
