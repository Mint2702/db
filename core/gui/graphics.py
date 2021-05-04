from tkinter import Tk

from .windows.connection_tk import Connection_tk
from .windows.main_window import MainWindow
from .utils import create_new_window


@create_new_window
def start_graphics(root: Tk) -> None:
    """ Стартовая точка в графике """

    Connection_tk(root)
