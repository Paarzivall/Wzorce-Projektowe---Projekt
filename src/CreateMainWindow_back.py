"""from tkinter import *


class CreateMainWindow(object):
    _instance = None

    @staticmethod
    def get_instance():
        if CreateMainWindow._instance is None:
            CreateMainWindow()
        else:
            return CreateMainWindow._instance

    def __init__(self):
        if CreateMainWindow._instance is None:
            self.window = Tk()
            self.add_options()
        self.start_app()
        CreateMainWindow._instance = self

    def add_options(self):
        self.window.title("Wypożyczalnia Samochodów")
        self.window.geometry("960x600")
        self.window.wm_resizable(width=False, height=False)

    def start_app(self):
        add_button = Button(self.window, text="Dodaj nową rezerwację", command=self.print, width=40, height=3)
        add_button.place(x=55, y=500)
        search_button = Button(self.window, text="Sprawdź dostępne auta", command=self.print, width=40, height=3)
        search_button.place(x=615, y=30)
        warn = Label(self.window, text="Klienci którzy dzisiaj mają zwrócić auta")
        warn.place(x=590, y=100)
        warn.config(fg="red", font="bold")
        mainloop()

    def print(self):
        Label(self.window, text = "GUI with Tkinter!").pack()"""
import tkinter as tk

import datetime as dt

window = tk.Tk()  # tworzenie okna głównego programu

window.geometry("430x160")  # ustawienie wymiarów okna

window.title("Przykładowy program")  # ustawienie tytułu okna

labelDescription = tk.StringVar()  # zminna, która będzie ustawiała tekst wypisywany w kontrolkach

label = tk.Label(window,
                 textvariable=labelDescription)  # tworzenie kontrolki Label z ustawieniem wyświetlania tekstu zawartego w zmiennej typu StringVar

labelDescription.set(
    "Przykładowy label:")  # ustawienie tekstu zawartego w zmiennej oraz (jednocześnie) w kontrolce label

label.pack()  # wstawianie kontrolki do okna głównego

label.place(x=10, y=10)  # zmiana położenia kontrolki w oknie

edit = tk.Entry(window, width=50,
                textvariable=labelDescription)  # tworzenie kontrolki Entry z przypisaniem jej zmiennej labelDescription

edit.pack()  # dodawanie jej do okna

edit.place(x=10, y=30)  # zmiana położenia kontrolki w oknie głównym


def buttonClicked():  # zdarzenie związane z kliknięciem przycisku

    labelDescription.set(
        dt.datetime.now())  # tutaj ustawiam zawartość zmiennej labelDescription i jednocześnie zmieniam tekst wyświetlany w kontrolce Label


button = tk.Button(window, text="Wczytaj bierzącą datę",
                   command=buttonClicked)  # tworzę przycisk, który będzie wstawiał datę

button.pack()  # wstawiam przycisk na okno główne

button.place(x=10, y=50)  # ustawiam położenie przycisku

ct_listbox = tk.Listbox(window, width=50, height=4)  # tworzę kontrolkę listbox

ct_listbox.pack()  # wstawiam ją w oknie

ct_listbox.place(x=10, y=80)  # ustawienie położenia kontrolki

ct_listbox.insert(tk.END, "Tydzień dzieci ma siedmioro")  # dodaję pierwszy element do kontrolki


def listboxSelect(
        index):  # to będzie funkcja, którą podepnę pod zdarzenie <<ListboxSelect>> - wywoływane, gdy zmienione zostanie zaznaczenie w kontrolce

    labelDescription.set(ct_listbox.get(
        ct_listbox.curselection()))  # tutaj wyciągam tekst zaznaczenie i wstawiam go do zmiennej labelDescription co powoduje wyświetlenie tego tekstu w kontrolkach Entry i Label


for item in ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota",
             "Niedziela"]:  # iteruję po elementach listy

    ct_listbox.insert(tk.END, item)  # wstawiam je kolejno do listbox-a

ct_listbox.bind('<<ListboxSelect>>', listboxSelect)  # łączę zdarzenie zmiany zaznaczenia z funkcją listboxSelect

window.mainloop()  # wywołanie głównej pętli programu

