import pymysql
from tkinter import *
from tkinter import messagebox
from src.CreateMainWindow import CreateMainWindow


if __name__ == '__main__':
    try:
        window = CreateMainWindow()
        window.start_app()
    except pymysql.err.OperationalError:
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo('Error', 'Brak połączenia z bazą danych')


