from tkinter import *
from src.CreateWindow import CreateWindow


class CreateMainWindow(CreateWindow):
    def __init__(self):
        super().__init__()

    def add_buttons(self):
        add_button = Button(self.window, text="Dodaj nową rezerwację", command=self.print, width=40, height=3)
        add_button.place(x=55, y=500)
        search_button = Button(self.window, text="Sprawdź dostępne auta", command=self.print, width=40, height=3)
        search_button.place(x=615, y=30)

    def add_labels(self):
        warn = Label(self.window, text="Klienci którzy dzisiaj mają zwrócić auta")
        warn.place(x=590, y=100)
        warn.config(fg="red", font="bold")

    def print(self):
        print("aaa")

    def add_other_components(self):
        pass