from tkinter import BOTH, Button, Frame, Label


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

        self.place_buttons()

        self.pack(fill=BOTH, expand=1)

    def place_buttons(self) -> None:
        """ Создание и расположение кнопок выбора раздела """
        with open("user_status.txt", "r") as file:
            self.user = file.readline()

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

        btn_view = Button(
            self,
            text="Просмотр",
            font=("Arial Bold", 10),
            width=30,
            command=self.change_to_view,
        )
        btn_view.place(x=750, y=100)

        btn_add = Button(
            self,
            text="Добавление данных",
            font=("Arial Bold", 10),
            width=30,
            command=self.change_to_add_data,
        )
        btn_add.place(x=750, y=300)

        btn_filter = Button(
            self,
            text="Фильтрация",
            font=("Arial Bold", 10),
            width=30,
            command=self.remove_window,
        )
        btn_filter.place(x=750, y=500)

    def change_to_view(self) -> None:
        """ Переключает окно на окно просмотра таблиц """

        self.remove_window()

        from tkinter import Tk

        from .view import ViewWindow
        from ..utils import create_new_window

        @create_new_window
        def change_to_view_inner(root: Tk) -> None:
            ViewWindow(root)

        change_to_view_inner()

    def change_to_add_data(self) -> None:
        """ Переключает окно на окно добавления данных """

        self.remove_window()

        from tkinter import Tk

        from .add_data import AddDataWindow
        from ..utils import create_new_window

        @create_new_window
        def change_to_add_data_inner(root: Tk) -> None:
            AddDataWindow(root)

        change_to_add_data_inner()

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """

        self.parent.destroy()
