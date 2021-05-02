from tkinter import messagebox, Tk
from functools import wraps


def show_info(header: str, text: str) -> None:
    """ Всплывающее окно с инфой """

    messagebox.showinfo(header, text)


def show_error(header: str, text: str) -> None:
    """ Всплывающее окно с ошибкой """

    messagebox.showerror(header, text)


def create_new_window(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        root = Tk()
        func(root, *args, **kwargs)
        root.mainloop()

    return wrapper
