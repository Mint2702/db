from tkinter import Tk

from .connection_tk import Connection_tk
from .main_window import MainWindow


def connect_to_db() -> None:
    """ Окно подключения к бд """
    root = Tk()
    Connection_tk(root)
    root.mainloop()


def main_window() -> None:
    """ Главное окно """
    root = Tk()
    MainWindow(root)
    root.mainloop()
