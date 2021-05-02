from tkinter import messagebox


def show_info(header: str, text: str) -> None:
    """ Всплывающее окно с инфой """

    messagebox.showinfo(header, text)


def show_error(header: str, text: str) -> None:
    """ Всплывающее окно с ошибкой """

    messagebox.showerror(header, text)
