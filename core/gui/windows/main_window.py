from tkinter import BOTH, Button, Frame, Label
from ..utils import get_role


class MainWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self) -> None:
        """ Построение главного окна """

        w = 1300
        h = 700

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра")

        self.user = get_role()

        self.place_buttons()

        self.pack(fill=BOTH, expand=1)

    def place_buttons(self) -> None:
        """ Создание и расположение кнопок выбора раздела """

        roll_label = Label(
            self,
            text="Вы зашли как: " + self.user,
            font=("Arial Bold", 15),
        )
        roll_label.place(x=25, y=200)

        choose_label = Label(
            self,
            text="Выберите желаемое действие",
            font=("Arial Bold", 15),
        )
        choose_label.place(x=500, y=20)

        btn_view_raw = Button(
            self,
            text="Просмотр исходных таблиц",
            font=("Arial Bold", 10),
            width=30,
            command=self.change_to_view,
        )
        btn_view_raw.place(x=750, y=100)

        btn_view = Button(
            self,
            text="Просмотр готовых представлений",
            font=("Arial Bold", 10),
            width=30,
            command=self.change_to_complex_view,
        )
        btn_view.place(x=750, y=250)

        btn_filter = Button(
            self,
            text="Поиск",
            font=("Arial Bold", 10),
            width=30,
            command=self.change_to_search,
        )
        btn_filter.place(x=750, y=400)

        if self.user != "Студент":
            btn_add = Button(
                self,
                text="Добавление данных",
                font=("Arial Bold", 10),
                width=30,
                command=self.change_to_add_data,
            )
            btn_add.place(x=750, y=550)

    def change_to_view(self) -> None:
        """ Переключает окно на окно просмотра таблиц """

        from tkinter import Tk
        from .view import ViewWindow

        self.remove_window()
        ViewWindow(self.parent)

    def change_to_complex_view(self) -> None:
        """ Переключает окно на окно просмотра таблиц """

        from tkinter import Tk
        from .complex_view import ComplexViewWindow

        self.remove_window()
        ComplexViewWindow(self.parent)

    def change_to_add_data(self) -> None:
        """ Переключает окно на окно добавления данных """

        from tkinter import Tk
        from .add_data import AddDataWindow

        self.remove_window()
        AddDataWindow(self.parent)

    def change_to_search(self) -> None:
        """ Переключает окно на окно поиска данных """

        from tkinter import Tk
        from .search import SearchWindow

        self.remove_window()
        SearchWindow(self.parent)

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """

        self.destroy()
