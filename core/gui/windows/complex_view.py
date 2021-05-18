from tkinter import BOTH, Button, Frame, ttk, END, CENTER, BOTTOM, TOP, X
from ..utils import get_role, show_error


class ComplexViewWindow(Frame):
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
        self.parent.title("Военная кафедра - работа с готовыми представлениями")

        self.place_table_frames()
        self.place_back_button()

        self.place_tables()

        self.pack(fill=BOTH, expand=1)

    def place_back_button(self) -> None:
        """Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=550, y=500)

    def place_table_frames(self) -> None:
        """ " Создание фреймов для размещения таблиц"""

        note_tree = ttk.Notebook(self, style="style.TNotebook", width=1250)
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
        """Создание и расположение представления предметов"""

        tree = ttk.Treeview(
            self.f_subject, column=("c1", "c2", "c3", "c4"), show="headings"
        )

        tree.pack(side="left", fill="y")
        tree.column("#1", anchor=CENTER, minwidth=0, width=110)
        tree.heading("#1", text="ПРЕДМЕТ")
        tree.column("#2", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#2", text="ГОД ОБУЧЕНИЯ")
        tree.column("#3", anchor=CENTER, minwidth=0, width=130)
        tree.heading("#3", text="СЕМЕСТР ОБУЧЕНИЯ")
        tree.column("#4", anchor=CENTER, minwidth=0, width=110)
        tree.heading("#4", text="РОД ВОЙСК")

        self.fill_subjects(tree)

        tree.pack(fill=BOTH, expand=True, side=TOP)

        if (
            self.role != "Студент"
            and self.role != "Преподаватель"
            and self.role != "Начальник ВУЦ"
        ):
            btn_del = Button(
                self.f_subject,
                text="Удалить",
                font=("Arial Bold", 10),
                width=10,
                command=lambda: self.delete_subject(tree),
            )
            btn_del.pack(fill=BOTH, expand=True, side=BOTTOM)

    def place_students(self) -> None:
        """Создание и расположение представления студентов"""

        tree = ttk.Treeview(
            self.f_student,
            column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"),
            show="headings",
        )

        scroll = ttk.Scrollbar(self.f_student, orient="horizontal", command=tree.xview)

        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ИМЯ")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="ФАМИЛИЯ")
        tree.column("#3", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#3", text="ДАТА РОЖДЕНИЯ")
        tree.column("#4", minwidth=0, width=100, anchor=CENTER)
        tree.heading("#4", text="НОМЕР ПАССПОРТА")
        tree.column("#5", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#5", text="ДАТА ВЫДАЧИ")
        tree.column("#6", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#6", text="КЕМ ВЫДАН")
        tree.column("#7", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#7", text="ИНН")
        tree.column("#8", minwidth=0, width=210, anchor=CENTER)
        tree.heading("#8", text="РОД ВОЙСК")
        tree.column("#9", minwidth=0, width=250, anchor=CENTER)
        tree.heading("#9", text="АДРЕС")
        tree.column("#10", minwidth=0, width=120, anchor=CENTER)
        tree.heading("#10", text="НОМЕР ТЕЛЕФОНА")

        self.fill_students(tree)

        tree.pack(fill=BOTH, expand=True, side=TOP)

        scroll.pack(side=BOTTOM, fill=X)
        tree.configure(xscrollcommand=scroll.set)

        if (
            self.role != "Студент"
            and self.role != "Преподаватель"
            and self.role != "Начальник ВУЦ"
        ):
            btn_del = Button(
                self.f_student,
                text="Удалить",
                font=("Arial Bold", 10),
                width=10,
                command=lambda: self.delete_student(tree),
            )
            btn_del.pack(fill=BOTH, expand=True, side=BOTTOM)

    def place_teachers(self) -> None:
        """Создание и расположение представления преподавателей"""

        tree = ttk.Treeview(
            self.f_teacher,
            column=(
                "c1",
                "c2",
                "c3",
                "c4",
                "c5",
                "c6",
                "c7",
                "c8",
                "c9",
                "c10",
                "c11",
                "c12",
            ),
            show="headings",
        )

        scroll = ttk.Scrollbar(self.f_teacher, orient="horizontal", command=tree.xview)

        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=140, anchor=CENTER)
        tree.heading("#1", text="ОСНОВНОЙ ПРЕДМЕТ")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="ИМЯ")
        tree.column("#3", minwidth=0, width=120, anchor=CENTER)
        tree.heading("#3", text="ФАМИЛИЯ")
        tree.column("#4", minwidth=0, width=110, anchor=CENTER)
        tree.heading("#4", text="ДАТА РОЖДЕНИЯ")
        tree.column("#5", minwidth=0, width=130, anchor=CENTER)
        tree.heading("#5", text="НАЧАЛО ОБУЧЕНИЯ")
        tree.column("#6", minwidth=0, width=120, anchor=CENTER)
        tree.heading("#6", text="НОМЕР ПАССПОРТА")
        tree.column("#7", minwidth=0, width=120, anchor=CENTER)
        tree.heading("#7", text="ДАТА ВЫДАЧИ")
        tree.column("#8", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#8", text="КЕМ ВЫДАН")
        tree.column("#9", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#9", text="ИНН")
        tree.column("#10", minwidth=0, width=80, anchor=CENTER)
        tree.heading("#10", text="ЗВАНИЕ")
        tree.column("#11", minwidth=0, width=250, anchor=CENTER)
        tree.heading("#11", text="АДРЕС")
        tree.column("#12", minwidth=0, width=120, anchor=CENTER)
        tree.heading("#12", text="НОМЕР ТЕЛЕФОНА")

        self.fill_teachers(tree)

        tree.pack(fill=BOTH, expand=True, side=TOP)

        scroll.pack(side=BOTTOM, fill=X)
        tree.configure(xscrollcommand=scroll.set)

        if (
            self.role != "Студент"
            and self.role != "Преподаватель"
            and self.role != "Начальник цикла"
        ):
            btn_del = Button(
                self.f_teacher,
                text="Удалить",
                font=("Arial Bold", 10),
                width=10,
                command=lambda: self.delete_teacher(tree),
            )
            btn_del.pack(fill=BOTH, expand=True, side=BOTTOM)

    def place_equipment(self) -> None:
        """Создание и расположение представления оборудования"""

        tree = ttk.Treeview(self.f_equipment, column=("c1", "c2"), show="headings")
        tree.pack(side="left", fill="y")
        tree.column("#1", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#1", text="ОБОРУДОВАНИЕ")
        tree.column("#2", minwidth=0, width=90, anchor=CENTER)
        tree.heading("#2", text="ПРЕДМЕТ")

        self.fill_equipment(tree)

        tree.pack(fill=BOTH, expand=True, side=TOP)

        btn_del = Button(
            self.f_equipment,
            text="Удалить",
            font=("Arial Bold", 10),
            width=10,
            command=lambda: self.delete_equipment(tree),
        )
        btn_del.pack(fill=BOTH, expand=True, side=BOTTOM)

    def fill_equipment(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы представления оборудования"""

        import sys

        sys.path.append("..")

        from db.complex_get import get_equipment

        records = get_equipment()

        for record in records:
            tree.insert("", END, values=record)

    def fill_teachers(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы представления преподавателей"""

        import sys

        sys.path.append("..")

        from db.complex_get import get_teachers

        records = get_teachers()

        for record in records:
            tree.insert("", END, values=record)

    def fill_students(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы представления студентов"""

        import sys

        sys.path.append("..")

        from db.complex_get import get_students

        records = get_students()

        for record in records:
            tree.insert("", END, values=record)

    def fill_subjects(self, tree: ttk.Treeview) -> None:
        """Заполнение таблицы представления предметов"""

        import sys

        sys.path.append("..")

        from db.complex_get import get_subjects

        records = get_subjects()

        for record in records:
            tree.insert("", END, values=record)

    def delete_equipment(self, tree) -> None:
        for selection in tree.selection():
            item = tree.item(selection)
            values = item["values"]

            params = {"name": values[0]}
            import sys

            sys.path.append("..")

            from db.delete import delete_equipment

            delete_equipment(params)

    def delete_student(self, tree) -> None:
        for selection in tree.selection():
            item = tree.item(selection)
            values = item["values"]

            params = {
                "first_name": values[0],
                "last_name": values[1],
                "passport": values[3],
            }
            import sys

            sys.path.append("..")

            from db.delete import delete_student

            delete_student(params)

    def delete_subject(self, tree) -> None:
        for selection in tree.selection():
            item = tree.item(selection)
            values = item["values"]
            print(values)

            params = {"name": values[0]}
            import sys

            sys.path.append("..")

            from db.delete import delete_subject

            delete_subject(params)

    def delete_teacher(self, tree) -> None:
        for selection in tree.selection():
            item = tree.item(selection)
            values = item["values"]

            params = {
                "first_name": values[1],
                "last_name": values[2],
                "passport": values[5],
            }
            import sys

            sys.path.append("..")

            from db.delete import delete_teacher

            flag = delete_teacher(params)
            if not flag:
                show_error(
                    "Ошибка удаления",
                    "У данного преподавателя ессть привязанный взвод. Пожалуйста, удалите или перезапишите взвод на другого преподавателя.",
                )

    def back(self) -> None:
        """Возвращает в меню выбора действия"""

        from .main_window import MainWindow

        self.remove_window()
        MainWindow(self.parent)

    def remove_window(self) -> None:
        """Удаляет все обьекты родительского окна"""

        self.destroy()
