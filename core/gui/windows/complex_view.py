from tkinter import BOTH, Button, Frame, ttk, END, CENTER
from ..utils import get_role


class ComplexViewWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self) -> None:
        """ Постоение окна просмотра """

        w = 1300
        h = 700

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра - просмотр готовых представлений")

        self.place_table_frames()
        self.place_back_button()
        self.place_tables()

        self.pack(fill=BOTH, expand=1)

    def place_back_button(self) -> None:
        """ Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=550, y=600)

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

        self.fill_subjects(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_students(self) -> None:
        """ Создание и расположение представления студентов """

        tree = ttk.Treeview(
            self.f_student, column=("c1", "c2", "c3", "c4"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ФИО")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="ДАТА РОЖДЕНИЯ")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3", text="АДРЕСС")
        tree.column("#4", anchor=CENTER)
        tree.heading("#4", text="НОМЕР")

        self.fill_students(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_teachers(self) -> None:
        """ Создание и расположение представления преподавателей """

        tree = ttk.Treeview(
            self.f_teacher, column=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ФИО")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="ДАТА РОЖДЕНИЯ")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3", text="НОМЕР")
        tree.column("#4", anchor=CENTER)
        tree.heading("#4", text="ОПЫТ ОБУЧЕНИЯ")
        tree.column("#5", anchor=CENTER)
        tree.heading("#5", text="ЗВАНИЕ")
        tree.column("#6", anchor=CENTER)
        tree.heading("#6", text="ОСНОВНОЙ ПРЕДМЕТ")

        self.fill_teachers(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_equipment(self) -> None:
        """ Создание и расположение представления оборудования """

        tree = ttk.Treeview(self.f_equipment, column=("c1", "c2"), show="headings")
        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ОБОРУДОВАНИЕ")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="ПРЕДМЕТ")

        self.fill_equipment(tree)

        tree.pack(fill=BOTH, expand=1)

    def fill_equipment(self, tree: ttk.Treeview) -> None:
        """ Заполнение таблицы представления оборудования """

        import sys

        sys.path.append("..")

        from db.complex_get import get_equipment

        records = get_equipment()

        for record in records:
            tree.insert("", END, values=record)

    def fill_teachers(self, tree: ttk.Treeview) -> None:
        """ Заполнение таблицы представления преподавателей """

        import sys

        sys.path.append("..")

        from db.complex_get import get_teachers

        records = get_teachers()

        for record in records:
            tree.insert("", END, values=record)

    def fill_students(self, tree: ttk.Treeview) -> None:
        """ Заполнение таблицы представления студентов """

        import sys

        sys.path.append("..")

        from db.complex_get import get_students

        records = get_students()

        for record in records:
            tree.insert("", END, values=record)

    def fill_subjects(self, tree: ttk.Treeview) -> None:
        """ Заполнение таблицы представления предметов """

        import sys

        sys.path.append("..")

        from db.complex_get import get_subjects

        records = get_subjects()

        for record in records:
            tree.insert("", END, values=record)

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
