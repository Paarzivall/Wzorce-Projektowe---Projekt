from tkinter import *
from src.CreateWindow import CreateWindow


class CreateResultWindow(CreateWindow):
    def __init__(self):
        super().__init__()

    def add_buttons(self):
        pass

    def add_labels(self):
        warn = Label(self.window, text="Klienci którzy dzisiaj mają zwrócić auta")
        warn.place(x=590, y=100)
        warn.config(fg="red", font="bold")

    def add_other_components(self):
        pass
