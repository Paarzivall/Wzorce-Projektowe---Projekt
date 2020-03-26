from abc import ABC, abstractmethod
from tkinter import *


class CreateWindow(ABC):
    def __init__(self):
        self.window = Tk

    def start_app(self):
        self.window = Tk()
        self.add_options()
        self.add_buttons()
        self.add_labels()
        self.add_other_components()
        mainloop()

    def add_options(self):
        self.window.title("Wypożyczalnia Samochodów")
        self.window.geometry("960x600")
        self.window.wm_resizable(width=False, height=False)

    @abstractmethod
    def add_buttons(self):
        pass

    @abstractmethod
    def add_labels(self):
        pass

    @abstractmethod
    def add_other_components(self):
        pass
