from tkinter import *
from PIL import ImageTk, Image


def connect_to_db() -> None:
    """ Окно подключения к бд """

    root = build_connection_window()

    place_connection_labels(root)

    root.mainloop()


def build_connection_window() -> Tk:
    """ Создание окна для подключения к бд"""

    root = Tk()
    root.title("Военная кафедра")
    root.geometry("2000x1200")

    return root


def place_connection_labels(root: Tk) -> None:
    """ Создание и расположение виджетов окна подключения к бд"""

    choose_label = Label(
        root,
        text="Введите данные для подключения к базе данных военной кафедры, или выберете иной способ подключения",
        font=("Arial Bold", 15),
    )
    choose_label.place(x=200, y=20)

    btn_env = Button(
        root, text="Использовать .env файл", font=("Arial Bold", 10), width=30
    )

    btn_env.place(x=650, y=1000)

    host = Entry(root, width=30, font=("Arial Bold", 10))
    host.place(x=800, y=250)
    host_label = Label(
        root,
        text="Host",
        font=("Arial Bold", 15),
    )
    host_label.place(x=580, y=250)

    port = Entry(root, width=30, font=("Arial Bold", 10))
    port.place(x=800, y=350)
    port_label = Label(
        root,
        text="Port",
        font=("Arial Bold", 15),
    )
    port_label.place(x=580, y=350)

    user = Entry(root, width=30, font=("Arial Bold", 10))
    user.place(x=800, y=450)
    user_label = Label(
        root,
        text="User",
        font=("Arial Bold", 15),
    )
    user_label.place(x=580, y=450)

    password = Entry(root, width=30, font=("Arial Bold", 10))
    password.place(x=800, y=550)
    password_label = Label(
        root,
        text="Password",
        font=("Arial Bold", 15),
    )
    password_label.place(x=550, y=550)

    db_name = Entry(root, width=30, font=("Arial Bold", 10))
    db_name.place(x=800, y=650)
    db_name_label = Label(
        root,
        text="Database name",
        font=("Arial Bold", 15),
    )
    db_name_label.place(x=500, y=650)
