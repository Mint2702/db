from tkinter import Tk

from .windows.connection_tk import Connection_tk
from .windows.main_window import MainWindow


def start_graphics() -> None:
    """Стартовая точка в графике"""

    root = Tk()
    Connection_tk(root)
    root.mainloop()
