from tkinter import BOTH, Button, Frame, Label, Entry, IntVar, Radiobutton

import sys

from ..utils import show_error, show_info


class Connection_tk(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self) -> None:
        """ Постоение окна соединения с бд """

        w = 1300
        h = 700

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.parent.title("Военная кафедра")
        self.default_user()
        self.place_connection_labels()
        self.place_radiobuttons()

        self.pack(fill=BOTH, expand=1)


    def default_user(self) -> None:
       with open("user_status.txt", "w") as file:
           file.write(str(1))


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
        btn_env.place(x=650, y=600)

        btn_input = Button(
            self,
            text="Использовать введенные данные",
            font=("Arial Bold", 10),
            width=30,
            command=lambda: self.env_connect(env=False),
        )
        btn_input.place(x=650, y=550)

        self.host = Entry(self, width=30, font=("Arial Bold", 10))
        self.host.place(x=800, y=100)
        host_label = Label(
            self,
            text="Host",
            font=("Arial Bold", 15),
        )
        host_label.place(x=580, y=100)

        self.port = Entry(self, width=30, font=("Arial Bold", 10))
        self.port.place(x=800, y=200)
        port_label = Label(
            self,
            text="Port",
            font=("Arial Bold", 15),
        )
        port_label.place(x=580, y=200)

        self.user = Entry(self, width=30, font=("Arial Bold", 10))
        self.user.place(x=800, y=300)
        user_label = Label(
            self,
            text="User",
            font=("Arial Bold", 15),
        )
        user_label.place(x=580, y=300)

        self.password = Entry(self, width=30, font=("Arial Bold", 10))
        self.password.place(x=800, y=400)
        password_label = Label(
            self,
            text="Password",
            font=("Arial Bold", 15),
        )
        password_label.place(x=550, y=400)

        self.db_name = Entry(self, width=30, font=("Arial Bold", 10))
        self.db_name.place(x=800, y=500)
        db_name_label = Label(
            self,
            text="Database name",
            font=("Arial Bold", 15),
        )
        db_name_label.place(x=500, y=500)

    """Функции для изменения статуса, тк variable не робит с self
    Разбил на несколько функций из-за того что если делать одну с разными параметрами,
    они она просто запускается 4 раза. ХЗ почему"""
    def status_1(self) -> None:
        self.status = 1

    def status_2(self) -> None:
        self.status = 2

    def status_3(self) -> None:
        self.status = 3

    def status_4(self) -> None:
        self.status = 4



    def place_radiobuttons(self) -> None:
        """ Создание и размещение кнопочек выбора роли"""
        self.var = IntVar()
        self.status = 1
        rad0 = Radiobutton(self, text="Cтудент", variable=self.var, value=1, font=("Arial Bold", 15), command=self.status_1)
        rad1 = Radiobutton(self, text="Преподаватель", variable=self.var, value=2, font=("Arial Bold", 15), command=self.status_2)
        rad2 = Radiobutton(self, text="Начальник цикла", variable=self.var, value=3, font=("Arial Bold", 15), command=self.status_3)
        rad3 = Radiobutton(self, text="Начальник ВУЦ", variable=self.var, value=4, font=("Arial Bold", 15), command=self.status_4)
        rad0.place(x=20, y=210)
        rad1.place(x=20, y=240)
        rad2.place(x=20, y=270)
        rad3.place(x=20, y=300)
        #labelValue = Label(self, textvariable=self.var)
        #labelValue.place(x=10, y=10)



    def env_connect(self, env: bool) -> None:
        """ Вызывает функцию подключения к бд c """

        sys.path.append("..")

        from db import utils as db
        from db import settings as st

        # Три строчки сверху нужны для того, чтобы импортнуть модули из папки db

        """ Запись в файл """
        with open("user_status.txt", "w") as file:
            file.write(str(self.status))

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
            self.main_window()

        else:
            show_error(
                "Ошибка подключения",
                "Не получилось подключиться к базе данных. Пожалуйста, попробуйте снова",
            )

    def main_window(self) -> None:
        """ Переходит в меню выбора действия """

        self.remove_window()

        from tkinter import Tk

        from .main_window import MainWindow
        from ..utils import create_new_window

        @create_new_window
        def to_main(root: Tk) -> None:
            MainWindow(root)

        to_main()

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """
        self.parent.destroy()
