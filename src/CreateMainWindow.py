from tkinter import *
from tkinter import messagebox
from datetime import date, datetime
import tkinter.ttk as ttk
from tkcalendar import DateEntry
from src.CreateWindow import CreateWindow
from src.ConnectToSQLdb import ConnectToSQLdb
from src.SelectQuery import SelectQuery
from src.CreateResultWindow import CreateResultWindow


class CreateMainWindow(CreateWindow):
    def __init__(self):
        super().__init__()
        self.connection = None

    def add_buttons(self):
        add_button = Button(self.window, text="Dodaj nową rezerwację", command=self.add_reservation, width=40, height=3)
        add_button.place(x=145, y=190)
        search_button = Button(self.window, text="Sprawdź dostępne auta", command=self.print, width=40, height=3)
        search_button.place(x=615, y=30)

    def add_reservation(self):
        if self.next_step():
            self.date_end = self.formate_date()
            self.date_end = datetime.strptime(self.date_end, '%Y-%m-%d')
            cost = self.calculate(str(self.car.get())[':':])
            print(cost)
            imie_i_nazwisko = self.name.get() + " " + self.surname.get()
            sql = "INSERT INTO rezerwacje(imie_i_nazwisko, adres, nr_telefonu, start_rezerwacji, koniec_rezerwacji, cena) " \
                  "VALUES(" + imie_i_nazwisko + ", " + str(self.adress.get()) + ", " + str(self.phone.get()) + "," + \
                  str(date.today()) + ", " + str(self.date_end)[:10] + ", " + str(cost) + ")"
            print(sql)
        else:
            Tk().wm_withdraw()  # to hide the main window
            messagebox.showinfo('Error', 'Uzupełnij Brakujące pola')

    def next_step(self):
        if self.name.get() == '' or self.surname.get() == '' or self.adress.get() == '' or self.phone.get() == '' or self.car.get() == '' or self.date_end.get() == '':
            return False
        else:
            return True

    def calculate(self, car):
        print(car)
        if self.date_end != datetime.strptime(str(date.today()), '%Y-%m-%d'):
            diff = str(self.date_end - datetime.strptime(str(date.today()), '%Y-%m-%d'))[:str(self.calculate()).index(" ")]
        else:
            diff = 1
        return int(diff * int(car[car.index(':') + 1:]))

    def formate_date(self):
        print(date.today(), type(date.today()))
        data = str(self.date_end.get())
        tmp = data.index('/')
        year = data[len(data) - 2:]
        month = data[:tmp]
        day = data[tmp + 1:len(data) - 3]
        return '20' + str(year) + '-' + self.add_zeros(str(month)) + '-' + self.add_zeros(str(day))

    def add_zeros(self, number):
        if len(number) < 2:
            number = '0' + str(number)
        return number

    def add_labels(self):
        warn = Label(self.window, text="Klienci którzy dzisiaj mają zwrócić auta")
        warn.place(x=590, y=100)
        warn.config(fg="red", font="bold")

    def print(self):
        print("aaa")

    def add_values_to_combobox(self):
        sql = 'SELECT marka, model, cena_wypozyczenia, rok_produkcji FROM Samochody'
        result = []
        query_type = SelectQuery()
        self.connection = ConnectToSQLdb.get_instance(query_type)
        table_of_result = self.connection.execute_query(self.connection.get_cursor(), sql)
        self.connection.close_connection()
        for res in table_of_result:
            tmp = str(res[0]) + " " + str(res[1]) + " - Rok prod.(" + str(res[3]) + ") - Cena za dzień: " + str(res[2])
            result.append(tmp)
        return result

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
        adress_label = Label(self.window, text="Adres: ")
        adress_label.place(x=75, y=70)
        self.adress = Entry(self.window, width=50)
        self.adress.place(x=165, y=70)
        phone_label = Label(self.window, text="Nr. Telefonu: ")
        phone_label.place(x=75, y=95)
        self.phone = Entry(self.window, width=50)
        self.phone.place(x=165, y=95)
        car_label = Label(self.window, text="Jaki Samochód: ")
        car_label.place(x=75, y=120)
        self.car = ttk.Combobox(self.window, textvariable=value, width=50)
        self.car.place(x=165, y=120)
        self.car['values'] = self.add_values_to_combobox()
        date_label = Label(self.window, text="Do kiedy: ")
        date_label.place(x=75, y=145)
        self.date_end = DateEntry(self.window)
        self.date_end.place(x=165, y=145)
