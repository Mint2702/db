from tkinter import BOTH, Button, Frame, ttk, END, CENTER, Entry, Label
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

        self.place_search_label("оборудование")

        self.place_back_button()
        self.place_search_button()
        self.place_main_frame()
        self.place_choose_buttons()
        self.place_search_entry()

        self.pack(fill=BOTH, expand=1)

    def place_back_button(self) -> None:
        """ Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=850, y=600)

    def place_search_button(self) -> None:
        """ Создание и расположение кнопки "поиск" """

        btn_filter = Button(
            self, text="Найти", font=("Arial Bold", 10), width=10, command=self.search
        )
        btn_filter.place(x=850, y=400)

    def place_main_frame(self) -> None:
        """" Создание фреймов для размещения таблиц"""

        self.role = get_role()

        self.main_frame = Frame(self, height=300)
        self.main_frame.place(x=20, y=50)

    def place_choose_buttons(self) -> None:

        if self.role == "Студент":
            btn_teacher = Button(
                self,
                text="Преподаватели",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_teachers,
            )
            btn_teacher.place(x=100, y=300)

            btn_subjects = Button(
                self,
                text="Предметы",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_subjects,
            )
            btn_subjects.place(x=100, y=400)

        elif self.role == "Преподаватель":
            btn_student = Button(
                self,
                text="Студенты",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_students,
            )
            btn_student.place(x=100, y=300)

            btn_teacher = Button(
                self,
                text="Преподаватели",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_teachers,
            )
            btn_teacher.place(x=100, y=400)

            btn_subjects = Button(
                self,
                text="Предметы",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_subjects,
            )
            btn_subjects.place(x=100, y=500)

            btn_equipment = Button(
                self,
                text="Оборудование",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_equipment,
            )
            btn_equipment.place(x=100, y=600)

        else:
            btn_student = Button(
                self,
                text="Студенты",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_students,
            )
            btn_student.place(x=100, y=300)

            btn_teacher = Button(
                self,
                text="Преподаватели",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_teachers,
            )
            btn_teacher.place(x=100, y=400)

            btn_subjects = Button(
                self,
                text="Предметы",
                font=("Arial Bold", 10),
                width=10,
                command=self.place_subjects,
            )
            btn_subjects.place(x=100, y=500)

    def place_subjects(self) -> None:
        """ Создание и расположение представления предметов """

        self.main_label.destroy()
        self.place_search_label("предметы")

        tree = ttk.Treeview(
            self.main_frame, column=("c1", "c2", "c3", "c4"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ПРЕДМЕТ")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="ГОД ОБУЧЕНИЯ")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3", text="СЕМЕСТР ОБУЧЕНИЯ")
        tree.column("#4", anchor=CENTER)
        tree.heading("#4", text="РОД ВОЙСК")

        tree.pack(fill=BOTH, expand=1)

    def place_students(self) -> None:
        """ Создание и расположение представления студентов """

        self.main_label.destroy()
        self.place_search_label("студент")

        tree = ttk.Treeview(
            self.main_frame,
            column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"),
            show="headings",
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ИМЯ")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="ФАМИЛИЯ")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3", text="ДАТА РОЖДЕНИЯ")
        tree.column("#4", anchor=CENTER)
        tree.heading("#4", text="НОМЕР ПАССПОРТА")
        tree.column("#5", anchor=CENTER)
        tree.heading("#5", text="ДАТА ВЫДАЧИ")
        tree.column("#6", anchor=CENTER)
        tree.heading("#6", text="КЕМ ВЫДАН")
        tree.column("#7", anchor=CENTER)
        tree.heading("#7", text="ИНН")
        tree.column("#8", anchor=CENTER)
        tree.heading("#8", text="ВЗВОД")

        tree.pack(fill=BOTH, expand=1)

    def place_teachers(self) -> None:
        """ Создание и расположение представления преподавателей """

        self.main_label.destroy()
        self.place_search_label("преподаватель")

        tree = ttk.Treeview(
            self.main_frame,
            column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"),
            show="headings",
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ИМЯ")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="ФАМИЛИЯ")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3", text="ДАТА РОЖДЕНИЯ")
        tree.column("#4", anchor=CENTER)
        tree.heading("#4", text="НАЧАЛО ОБУЧЕНИЯ")
        tree.column("#5", anchor=CENTER)
        tree.heading("#5", text="НОМЕР ПАССПОРТА")
        tree.column("#6", anchor=CENTER)
        tree.heading("#6", text="ДАТА ВЫДАЧИ")
        tree.column("#7", anchor=CENTER)
        tree.heading("#7", text="КЕМ ВЫДАН")
        tree.column("#8", anchor=CENTER)
        tree.heading("#8", text="ИНН")
        tree.column("#9", anchor=CENTER)
        tree.heading("#9", text="ЗВАНИЕ")
        tree.column("#10", anchor=CENTER)
        tree.heading("#10", text="ОСНОВНОЙ ПРЕДМЕТ")

        tree.pack(fill=BOTH, expand=1)

    def place_equipment(self) -> None:
        """ Создание и расположение представления оборудования """

        self.main_label.destroy()
        self.place_search_label("оборудование")

        tree = ttk.Treeview(self.main_frame, column=("c1", "c2"), show="headings")
        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ОБОРУДОВАНИЕ")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="ПРЕДМЕТ")

        tree.pack(fill=BOTH, expand=1)

    def place_search_entry(self) -> None:

        main_entry = Entry(self, width=30, font=("Arial Bold", 10))
        main_entry.place(x=800, y=300)

    def place_search_label(self, table: str) -> None:

        if table == "студент" or table == "преподаватель":
            textt = "Фамилия"
        else:
            textt = "Название предмета"

        self.main_label = Label(self, text=textt, font=("Arial Bold", 10))
        self.main_label.place(x=600, y=300)

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

    def search(self) -> None:
        """ Искать """

        import sys

        sys.path.append("..")

        from db.search import search_student
