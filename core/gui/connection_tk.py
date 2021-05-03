from tkinter import BOTH, Button, Frame, Label, Entry
import sys

from .utils import show_error, show_info


class Connection_tk(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self) -> None:
        """ Постоение окна соединения с бд """

        w = 2000
        h = 1200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.parent.title("Военная кафедра")

        self.place_connection_labels()

        self.pack(fill=BOTH, expand=1)

    def place_connection_labels(self) -> None:
        """ Создание и расположение виджетов окна подключения к бд"""

        choose_label = Label(
            self,
            text="Введите данные для подключения к базе данных военной кафедры, или выберете иной способ подключения",
            font=("Arial Bold", 15),
        )
        choose_label.place(x=200, y=20)

        btn_env = Button(
            self,
            text="Использовать .env файл",
            font=("Arial Bold", 10),
            width=30,
            command=lambda: self.env_connect(env=True),
        )
        btn_env.place(x=650, y=1000)

        btn_input = Button(
            self,
            text="Использовать введенные данные",
            font=("Arial Bold", 10),
            width=30,
            command=lambda: self.env_connect(env=False),
        )
        btn_input.place(x=650, y=900)

        self.host = Entry(self, width=30, font=("Arial Bold", 10))
        self.host.place(x=800, y=250)
        host_label = Label(
            self,
            text="Host",
            font=("Arial Bold", 15),
        )
        host_label.place(x=580, y=250)

        self.port = Entry(self, width=30, font=("Arial Bold", 10))
        self.port.place(x=800, y=350)
        port_label = Label(
            self,
            text="Port",
            font=("Arial Bold", 15),
        )
        port_label.place(x=580, y=350)

        self.user = Entry(self, width=30, font=("Arial Bold", 10))
        self.user.place(x=800, y=450)
        user_label = Label(
            self,
            text="User",
            font=("Arial Bold", 15),
        )
        user_label.place(x=580, y=450)

        self.password = Entry(self, width=30, font=("Arial Bold", 10))
        self.password.place(x=800, y=550)
        password_label = Label(
            self,
            text="Password",
            font=("Arial Bold", 15),
        )
        password_label.place(x=550, y=550)

        self.db_name = Entry(self, width=30, font=("Arial Bold", 10))
        self.db_name.place(x=800, y=650)
        db_name_label = Label(
            self,
            text="Database name",
            font=("Arial Bold", 15),
        )
        db_name_label.place(x=500, y=650)

    def env_connect(self, env: bool) -> None:
        """ Вызывает функцию подключения к бд c """

        sys.path.append("..")

        from db import utils as db
        from db import settings as st

        # Три строчки сверху нужны для того, чтобы импортнуть модули из папки db

        if env:
            flag = db.db_connect(
                host=st.settings.host,
                port=st.settings.port,
                user=st.settings.user,
                password=st.settings.password,
                database=st.settings.db_name,
            )
        else:
            flag = db.db_connect(
                host=self.host.get(),
                port=self.port.get(),
                user=self.user.get(),
                password=self.password.get(),
                database=self.db_name.get(),
            )

        if flag:
            show_info(
                "Соединение успешно",
                "Подключение к базе данных прошло успешно. Нажмите ОК чтобы продолжить.",
            )
            self.remove_window()
        else:
            show_error(
                "Ошибка подключения",
                "Не получилось подключиться к базе данных. Пожалуйста, попробуйте снова",
            )

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """

        self.parent.destroy()