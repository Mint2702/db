from tkinter import Tk

from .connection_tk import Connection_tk
from .main_window import MainWindow
from .utils import create_new_window


@create_new_window
def connect_to_db(root: Tk) -> None:
    """ Окно подключения к бд """

    Connection_tk(root)


@create_new_window
def main_window(root: Tk) -> None:
    """ Главное окно """

    MainWindow(root)
