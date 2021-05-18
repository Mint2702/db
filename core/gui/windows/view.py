from tkinter import BOTH, Button, Frame, ttk, END, CENTER
from ..utils import get_role


class ViewWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self) -> None:
        """Постоение окна просмотра"""

        w = 1500
        h = 600

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2 + 100
        y = (sh - h) / 2 - 50

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра - просмотр таблиц")

        self.place_table_frames()
        self.place_back_button()
        self.place_tables()

        self.pack(fill=BOTH, expand=1)

    def place_table_frames(self) -> None:
        """ " Создание фреймов для размещения таблиц"""

        note_tree = ttk.Notebook(self, style="style.TNotebook")
        note_tree.place(x=20, y=50)

        self.role = get_role()

        if self.role == "Студент":
            self.f_subject = Frame(note_tree, height=300)
            self.f_subject_of_platoon = Frame(note_tree, height=300)
            self.f_teacher = Frame(note_tree, height=300)
            self.f_teacher_subject_area = Frame(note_tree, height=300)

            note_tree.add(self.f_subject, text="Предметы")
            note_tree.add(self.f_subject_of_platoon, text="Предметы у войск")
            note_tree.add(self.f_teacher, text="Преподаватели")
            note_tree.add(
                self.f_teacher_subject_area, text="Предметная область преподавателей"
            )
        elif self.role == "Преподаватель":
            self.f_equipment = Frame(note_tree, height=300)
            self.f_equipment_for_subject = Frame(note_tree, height=300)
            self.f_platoon = Frame(note_tree, height=300)
            self.f_student = Frame(note_tree, height=300)
            self.f_student_contacts = Frame(note_tree, height=300)
            self.f_subject = Frame(note_tree, height=300)
            self.f_subject_of_platoon = Frame(note_tree, height=300)
            self.f_teacher = Frame(note_tree, height=300)
            self.f_teacher_contacts = Frame(note_tree, height=300)
            self.f_teacher_subject_area = Frame(note_tree, height=300)

            note_tree.add(self.f_equipment, text="Оборудование")
            note_tree.add(self.f_equipment_for_subject, text="Оборудование для пар")
            note_tree.add(self.f_platoon, text="Войска")
            note_tree.add(self.f_student, text="Студенты")
            note_tree.add(self.f_student_contacts, text="Контакты студентов")
            note_tree.add(self.f_subject, text="Предметы")
            note_tree.add(self.f_subject_of_platoon, text="Предметы у войск")
            note_tree.add(self.f_teacher, text="Преподаватели")
            note_tree.add(self.f_teacher_contacts, text="Контакты преподавателей")
            note_tree.add(
                self.f_teacher_subject_area, text="Предметная область преподавателей"
            )
        elif self.role == "Начальник цикла":
            self.f_platoon = Frame(note_tree, height=300)
            self.f_student = Frame(note_tree, height=300)
            self.f_student_contacts = Frame(note_tree, height=300)
            self.f_subject = Frame(note_tree, height=300)
            self.f_subject_of_platoon = Frame(note_tree, height=300)
            self.f_teacher = Frame(note_tree, height=300)
            self.f_teacher_contacts = Frame(note_tree, height=300)
            self.f_teacher_subject_area = Frame(note_tree, height=300)

            note_tree.add(self.f_platoon, text="Войска")
            note_tree.add(self.f_student, text="Студенты")
            note_tree.add(self.f_student_contacts, text="Контакты студентов")
            note_tree.add(self.f_subject, text="Предметы")
            note_tree.add(self.f_subject_of_platoon, text="Предметы у войск")
            note_tree.add(self.f_teacher, text="Преподаватели")
            note_tree.add(self.f_teacher_contacts, text="Контакты преподавателей")
            note_tree.add(
                self.f_teacher_subject_area, text="Предметная область преподавателей"
            )

        else:
            self.f_platoon = Frame(note_tree, height=300)
            self.f_rank = Frame(note_tree, height=300)
            self.f_student = Frame(note_tree, height=300)
            self.f_student_contacts = Frame(note_tree, height=300)
            self.f_subject = Frame(note_tree, height=300)
            self.f_subject_of_platoon = Frame(note_tree, height=300)
            self.f_teacher = Frame(note_tree, height=300)
            self.f_teacher_contacts = Frame(note_tree, height=300)
            self.f_teacher_subject_area = Frame(note_tree, height=300)

            note_tree.add(self.f_platoon, text="Войска")
            note_tree.add(self.f_rank, text="Звания")
            note_tree.add(self.f_student, text="Студенты")
            note_tree.add(self.f_student_contacts, text="Контакты студентов")
            note_tree.add(self.f_subject, text="Предметы")
            note_tree.add(self.f_subject_of_platoon, text="Предметы у войск")
            note_tree.add(self.f_teacher, text="Преподаватели")
            note_tree.add(self.f_teacher_contacts, text="Контакты преподавателей")
            note_tree.add(
                self.f_teacher_subject_area, text="Предметная область преподавателей"
            )

    def place_back_button(self) -> None:
        """Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=550, y=500)

    def place_tables(self) -> None:
        """Создание и расположение таблиц"""

        if self.role == "Студент":
            self.place_table_subject()
            self.place_table_subject_of_platoon()
            self.place_table_teacher()
            self.place_table_teacher_subject_area()

        elif self.role == "Преподаватель":
            self.place_table_equipment()
            self.place_table_equipment_for_subject()
            self.place_table_platoon()
            self.place_table_student()
            self.place_table_student_contacts()
            self.place_table_subject()
            self.place_table_subject_of_platoon()
            self.place_table_teacher()
            self.place_table_teacher_contacts()
            self.place_table_teacher_subject_area()

        elif self.role == "Начальник цикла":
            self.place_table_platoon()
            self.place_table_student()
            self.place_table_student_contacts()
            self.place_table_subject()
            self.place_table_subject_of_platoon()
            self.place_table_teacher()
            self.place_table_teacher_contacts()
            self.place_table_teacher_subject_area()

        else:
            self.place_table_platoon()
            self.place_table_rank()
            self.place_table_student()
            self.place_table_student_contacts()
            self.place_table_subject()
            self.place_table_subject_of_platoon()
            self.place_table_teacher()
            self.place_table_teacher_contacts()
            self.place_table_teacher_subject_area()

    def place_table_equipment(self) -> None:
        """Создание и расположение таблицы "equipment" """

        tree = ttk.Treeview(self.f_equipment, column=("c1", "c2"), show="headings")
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="DENOMINATION")

        self.fill_table_equipment(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_equipment_for_subject(self) -> None:
        """Создание и расположение таблицы "equipment_for_subject" """

        tree = ttk.Treeview(
            self.f_equipment_for_subject, column=("c1", "c2"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID_EQUIPMENT")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="ID_SUBJECT")

        self.fill_table_equipment_for_subject(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_platoon(self) -> None:
        """Создание и расположение таблицы "platoon" """

        tree = ttk.Treeview(self.f_platoon, column=("c1", "c2"), show="headings")
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="DIRECTION")

        self.fill_table_platoon(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_rank(self) -> None:
        """Создание и расположение таблицы "rank" """

        tree = ttk.Treeview(self.f_rank, column=("c1", "c2"), show="headings")
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="TITLE")

        self.fill_table_rank(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_student(self) -> None:
        """Создание и расположение таблицы "student" """

        tree = ttk.Treeview(
            self.f_student,
            column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"),
            show="headings",
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="FIRST_NAME")
        tree.column("#3", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#3", text="LAST_NAME")
        tree.column("#4", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#4", text="DATE_OF_BIRTH")
        tree.column("#5", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#5", text="PASSPORT_NUM")
        tree.column("#6", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#6", text="PASSPORT_DATE")
        tree.column("#7", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#7", text="PASSPORT_GIVEN")
        tree.column("#8", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#8", text="INN")
        tree.column("#9", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#9", text="PLATOON_ID")

        self.fill_table_student(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_student_contacts(self) -> None:
        """Создание и расположение таблицы "student_contacts" """

        tree = ttk.Treeview(
            self.f_student_contacts, column=("c1", "c2", "c3"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID_STUDENT")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="ADDRESS")
        tree.column("#3", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#3", text="PHONE_NUMBER")

        self.fill_table_student_contacts(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_subject(self) -> None:
        """Создание и расположение таблицы "subject" """

        tree = ttk.Treeview(
            self.f_subject, column=("c1", "c2", "c3", "c4"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="NAME")
        tree.column("#3", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#3", text="YEAR_OF_STUDY")
        tree.column("#4", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#4", text="SEMESTER_OF_STUDY")

        self.fill_table_subject(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_subject_of_platoon(self) -> None:
        """Создание и расположение таблицы "subject_of_platoon" """

        tree = ttk.Treeview(
            self.f_subject_of_platoon, column=("c1", "c2"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID_PLATOON")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="ID_SUBJECT")

        self.fill_table_subject_of_platoon(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_teacher(self) -> None:
        """Создание и расположение таблицы "teacher" """

        tree = ttk.Treeview(
            self.f_teacher,
            column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"),
            show="headings",
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="FIRST_NAME")
        tree.column("#3", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#3", text="LAST_NAME")
        tree.column("#4", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#4", text="DATE_OF_BIRTH")
        tree.column("#5", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#5", text="TEACHING_BEGIN")
        tree.column("#6", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#6", text="PASSPORT_NUM")
        tree.column("#7", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#7", text="PASSPORT_DATE")
        tree.column("#8", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#8", text="PASSPORT_GIVEN")
        tree.column("#9", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#9", text="INN")
        tree.column("#10", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#10", text="RANK")

        self.fill_table_teacher(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_teacher_contacts(self) -> None:
        """Создание и расположение таблицы "teacher_contacts" """

        tree = ttk.Treeview(
            self.f_teacher_contacts, column=("c1", "c2", "c3"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID_TEACHER")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="ADDRESS")
        tree.column("#3", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#3", text="PHONE_NUMBER")

        self.fill_table_teacher_contacts(tree)

        tree.pack(fill=BOTH, expand=1)

    def place_table_teacher_subject_area(self) -> None:
        """Создание и расположение таблицы "teacher_subject_area" """

        tree = ttk.Treeview(
            self.f_teacher_subject_area, column=("c1", "c2"), show="headings"
        )
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ID_SUBJECT")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="ID_TEACHER")

        self.fill_table_teacher_subject_area(tree)

        tree.pack(fill=BOTH, expand=1)

    def fill_table_equipment(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "equipment" """

        import sys

        sys.path.append("..")

        from db.get import get_table_equipment

        records = get_table_equipment()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_equipment_for_subject(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "equipment_for_subject" """

        import sys

        sys.path.append("..")

        from db.get import get_table_equipment_for_subject

        records = get_table_equipment_for_subject()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_platoon(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "platoon" """

        import sys

        sys.path.append("..")

        from db.get import get_table_platoon

        records = get_table_platoon()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_rank(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "rank" """

        import sys

        sys.path.append("..")

        from db.get import get_table_rank

        records = get_table_rank()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_student(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "student" """

        import sys

        sys.path.append("..")

        from db.get import get_table_student

        records = get_table_student()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_student_contacts(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "student_contacts" """

        import sys

        sys.path.append("..")

        from db.get import get_table_student_contacts

        records = get_table_student_contacts()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_subject(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "subject" """

        import sys

        sys.path.append("..")

        from db.get import get_table_subject

        records = get_table_subject()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_subject_of_platoon(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "subject_of_platoon" """

        import sys

        sys.path.append("..")

        from db.get import get_table_subject_of_platoon

        records = get_table_subject_of_platoon()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_teacher(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "teacher" """

        import sys

        sys.path.append("..")

        from db.get import get_table_teacher

        records = get_table_teacher()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_teacher_contacts(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "teacher_contacts" """

        import sys

        sys.path.append("..")

        from db.get import get_table_teacher_contacts

        records = get_table_teacher_contacts()

        for record in records:
            tree.insert("", END, values=record)

    def fill_table_teacher_subject_area(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы "teacher_subject_area" """

        import sys

        sys.path.append("..")

        from db.get import get_table_teacher_subject_area

        records = get_table_teacher_subject_area()

        for record in records:
            tree.insert("", END, values=record)

    def back(self) -> None:
        """Возвращает в меню выбора действия"""

        from .main_window import MainWindow

        self.remove_window()
        MainWindow(self.parent)

    def remove_window(self) -> None:
        """Удаляет все обьекты родительского окна"""

        self.destroy()
