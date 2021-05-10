from tkinter import BOTH, Button, Frame, ttk, END, CENTER, Entry
from ..utils import get_role


class SearchWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self) -> None:
        """ Постоение окна поиска """

        w = 2050
        h = 700

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра - поиск по представлениям")

        self.place_back_button()
        self.place_choose_buttons()
        self.place_search_entry()

        self.pack(fill=BOTH, expand=1)

    def place_back_button(self) -> None:
        """ Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=550, y=600)

    def place_choose_buttons(self) -> None:
        """ Создание и расположение кнопок выбора представления для поиска """

        btn_student = Button(
            self, text="Студенты", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_student.place(x=100, y=200)

        btn_subject = Button(
            self, text="Предметы", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_subject.place(x=100, y=300)

        btn_teacher = Button(
            self, text="Преподаватели", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_teacher.place(x=100, y=400)

        btn_equipment = Button(
            self, text="Оборудование", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_equipment.place(x=100, y=500)

    def place_search_entry(self) -> None:

        main_entry = Entry(self, width=30, font=("Arial Bold", 10))
        main_entry.place(x=500, y=50)

    def back(self) -> None:
        """ Возвращает в меню выбора действия """

        from tkinter import Tk
        from .main_window import MainWindow

        import sys

        sys.path.append("..")

        from db.complex_get import get_teachers

        get_teachers()

        self.remove_window()
        MainWindow(self.parent)

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """

        self.destroy()
