from tkinter import BOTH, Button, Frame, Label, Entry

from .utils import show_error


class MainWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self) -> None:
        """ Построение главного окна """

        w = 2000
        h = 1200

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

        choose_label = Label(
            self,
            text="Выберите желаемое действие",
            font=("Arial Bold", 15),
        )
        choose_label.place(x=700, y=20)

        btn_view = Button(
            self,
            text="Просмотр",
            font=("Arial Bold", 10),
            width=30,
            command=self.change_to_view,
        )
        btn_view.place(x=750, y=500)

        btn_add = Button(
            self,
            text="Добавление данных",
            font=("Arial Bold", 10),
            width=30,
            command=self.remove_window,
        )
        btn_add.place(x=750, y=700)

        btn_filter = Button(
            self,
            text="Фильтрация",
            font=("Arial Bold", 10),
            width=30,
            command=self.remove_window,
        )
        btn_filter.place(x=750, y=900)

    def change_to_view(self) -> None:
        """ Переключает окно на окно просмотра таблиц """

        self.remove_window()

        from tkinter import Tk

        from .view import ViewWindow
        from .utils import create_new_window

        @create_new_window
        def change_to_view_inner(root: Tk) -> None:
            ViewWindow(root)

        change_to_view_inner()

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """

        self.parent.destroy()
