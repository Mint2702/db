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

    def place_main_frame(self) -> None:
        """" Создание фреймов для размещения таблиц"""

        self.role = get_role()

        self.main_frame = Frame(self, height=300)
        self.main_frame.place(x=20, y=50)

        self.tree = ttk.Treeview(
            self.main_frame, column=("c1", "c2", "c3", "c4"), show="headings"
        )

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

        self.tree.destroy()

        self.tree = ttk.Treeview(
            self.main_frame, column=("c1", "c2", "c3", "c4"), show="headings"
        )
        self.tree.pack(side="left", fill="y")
        self.tree.column("#1", anchor=CENTER)
        self.tree.heading("#1", text="ПРЕДМЕТ")
        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="ГОД ОБУЧЕНИЯ")
        self.tree.column("#3", anchor=CENTER)
        self.tree.heading("#3", text="СЕМЕСТР ОБУЧЕНИЯ")
        self.tree.column("#4", anchor=CENTER)
        self.tree.heading("#4", text="РОД ВОЙСК")

        self.tree.pack(fill=BOTH, expand=1)

        self.fill_table_subject()

    def place_students(self) -> None:
        """ Создание и расположение представления студентов """

        self.main_label.destroy()
        self.place_search_label("студент")

        self.tree.destroy()

        self.tree = ttk.Treeview(
            self.main_frame,
            column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"),
            show="headings",
        )
        self.tree.pack(side="left", fill="y")
        self.tree.column("#1", anchor=CENTER)
        self.tree.heading("#1", text="ИМЯ")
        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="ФАМИЛИЯ")
        self.tree.column("#3", anchor=CENTER)
        self.tree.heading("#3", text="ДАТА РОЖДЕНИЯ")
        self.tree.column("#4", anchor=CENTER)
        self.tree.heading("#4", text="НОМЕР ПАССПОРТА")
        self.tree.column("#5", anchor=CENTER)
        self.tree.heading("#5", text="ДАТА ВЫДАЧИ")
        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="КЕМ ВЫДАН")
        self.tree.column("#7", anchor=CENTER)
        self.tree.heading("#7", text="ИНН")
        self.tree.column("#8", anchor=CENTER)
        self.tree.heading("#8", text="ВЗВОД")

        self.tree.pack(fill=BOTH, expand=1)

        self.fill_table_student()

    def place_teachers(self) -> None:
        """ Создание и расположение представления преподавателей """

        self.main_label.destroy()
        self.place_search_label("преподаватель")

        self.tree.destroy()

        self.tree = ttk.Treeview(
            self.main_frame,
            column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"),
            show="headings",
        )
        self.tree.pack(side="left", fill="y")
        self.tree.column("#1", anchor=CENTER)
        self.tree.heading("#1", text="ИМЯ")
        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="ФАМИЛИЯ")
        self.tree.column("#3", anchor=CENTER)
        self.tree.heading("#3", text="ДАТА РОЖДЕНИЯ")
        self.tree.column("#4", anchor=CENTER)
        self.tree.heading("#4", text="НАЧАЛО ОБУЧЕНИЯ")
        self.tree.column("#5", anchor=CENTER)
        self.tree.heading("#5", text="НОМЕР ПАССПОРТА")
        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="ДАТА ВЫДАЧИ")
        self.tree.column("#7", anchor=CENTER)
        self.tree.heading("#7", text="КЕМ ВЫДАН")
        self.tree.column("#8", anchor=CENTER)
        self.tree.heading("#8", text="ИНН")
        self.tree.column("#9", anchor=CENTER)
        self.tree.heading("#9", text="ЗВАНИЕ")
        self.tree.column("#10", anchor=CENTER)
        self.tree.heading("#10", text="ОСНОВНОЙ ПРЕДМЕТ")

        self.tree.pack(fill=BOTH, expand=1)

        self.fill_table_teacher()

    def place_equipment(self) -> None:
        """ Создание и расположение представления оборудования """

        self.main_label.destroy()
        self.place_search_label("оборудование")

        self.tree.destroy()

        self.tree = ttk.Treeview(self.main_frame, column=("c1", "c2"), show="headings")
        self.tree.pack(side="left", fill="y")
        self.tree.column("#1", anchor=CENTER)
        self.tree.heading("#1", text="ОБОРУДОВАНИЕ")
        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="ПРЕДМЕТ")

        self.tree.pack(fill=BOTH, expand=1)

        self.fill_table_equipment()

    def place_search_entry(self) -> None:

        self.main_entry = Entry(self, width=30, font=("Arial Bold", 10))
        self.main_entry.place(x=800, y=300)

    def place_search_label(self, table: str) -> None:

        if table == "студент" or table == "преподаватель":
            textt = "Фамилия"
        else:
            textt = "Название предмета"

        self.main_label = Label(self, text=textt, font=("Arial Bold", 10))
        self.main_label.place(x=550, y=300)

    def fill_table_student(self) -> None:
        """ Заполнение таблицы "student" """

        import sys

        sys.path.append("..")

        from db.search import search_student

        text = self.main_entry.get()
        if text == "":
            text = "none"

        records = search_student(text)

        for record in records:
            self.tree.insert("", END, values=record)

    def fill_table_subject(self) -> None:
        """ Заполнение таблицы "subject" """

        import sys

        sys.path.append("..")

        from db.search import search_subject

        text = self.main_entry.get()
        if text == "":
            text = "none"

        records = search_subject(text)

        for record in records:
            self.tree.insert("", END, values=record)

    def fill_table_equipment(self) -> None:
        """ Заполнение таблицы "equipment" """

        import sys

        sys.path.append("..")

        from db.search import search_equipment

        text = self.main_entry.get()
        if text == "":
            text = "none"

        records = search_equipment(text)

        for record in records:
            self.tree.insert("", END, values=record)

    def fill_table_teacher(self) -> None:
        """ Заполнение таблицы "teacher" """

        import sys

        sys.path.append("..")

        from db.search import search_teacher

        text = self.main_entry.get()
        if text == "":
            text = "none"

        records = search_teacher(text)

        for record in records:
            self.tree.insert("", END, values=record)

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