from tkinter import messagebox, Tk
from functools import wraps


def show_info(header: str, text: str) -> None:
    """Всплывающее окно с инфой"""

    messagebox.showinfo(header, text)


def show_error(header: str, text: str) -> None:
    """Всплывающее окно с ошибкой"""

    messagebox.showerror(header, text)


def get_role() -> str:
    with open("user_status.txt", "r") as file:
        return file.readline()
