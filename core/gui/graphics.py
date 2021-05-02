from tkinter import Tk

from .connection_tk import Connection_tk


def connect_to_db() -> None:
    """ Окно подключения к бд """

    root = Tk()
    app = Connection_tk(root)
    root.mainloop()
