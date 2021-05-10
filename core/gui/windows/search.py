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
        self.place_search_button()
        self.place_table_frames()
        self.place_tables()
        self.place_search_entry()

        self.pack(fill=BOTH, expand=1)

    def place_back_button(self) -> None:
        """ Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=550, y=600)

    def place_search_button(self) -> None:
        """ Создание и расположение кнопки "поиск" """

        btn_filter = Button(
            self, text="Найти", font=("Arial Bold", 10), width=10, command=self.search
        )
        btn_filter.place(x=850, y=400)

    def place_table_frames(self) -> None:
        """" Создание фреймов для размещения таблиц"""

        note_tree = ttk.Notebook(self, style="style.TNotebook")
        note_tree.place(x=20, y=50)

        self.role = get_role()

        if self.role == "Студент":
            self.f_subject = Frame(note_tree, height=300)
            self.f_teacher = Frame(note_tree, height=300)

            note_tree.add(self.f_subject, text="Предметы")
            note_tree.add(self.f_teacher, text="Преподаватели")

        elif self.role == "Преподаватель":
            self.f_subject = Frame(note_tree, height=300)
            self.f_teacher = Frame(note_tree, height=300)
            self.f_student = Frame(note_tree, height=300)
            self.f_equipment = Frame(note_tree, height=300)

            note_tree.add(self.f_subject, text="Предметы")
            note_tree.add(self.f_teacher, text="Преподаватели")
            note_tree.add(self.f_student, text="Студенты")
            note_tree.add(self.f_equipment, text="Оборудование")

        else:
            self.f_subject = Frame(note_tree, height=300)
            self.f_teacher = Frame(note_tree, height=300)
            self.f_student = Frame(note_tree, height=300)

            note_tree.add(self.f_subject, text="Предметы")
            note_tree.add(self.f_teacher, text="Преподаватели")
            note_tree.add(self.f_student, text="Студенты")

    def place_tables(self) -> None:
        """Создание и расположение таблиц"""

        if self.role == "Студент":
            self.place_subjects()
            self.place_teachers()

        elif self.role == "Преподаватель":
            self.place_equipment()
            self.place_subjects()
            self.place_teachers()
            self.place_students()

        else:
            self.place_subjects()
            self.place_teachers()
            self.place_students()

    def place_subjects(self) -> None:
        """ Создание и расположение представления предметов """

        tree = ttk.Treeview(
            self.f_subject, column=("c1", "c2", "c3", "c4"), show="headings"
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

        tree = ttk.Treeview(
            self.f_student,
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

        tree = ttk.Treeview(
            self.f_teacher,
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

        tree = ttk.Treeview(self.f_equipment, column=("c1", "c2"), show="headings")
        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ОБОРУДОВАНИЕ")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="ПРЕДМЕТ")

        tree.pack(fill=BOTH, expand=1)

    def place_search_entry(self) -> None:

        main_entry = Entry(self, width=30, font=("Arial Bold", 10))
        main_entry.place(x=800, y=300)

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
