from tkinter import (
    BOTH,
    Button,
    Frame,
    Listbox,
    SINGLE,
    END,
    Label,
    Entry,
    StringVar,
    Radiobutton,
    IntVar,
)


class AddDataWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self) -> None:
        """ Постоение окна добавления информации """

        w = 1300
        h = 700

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.add_status = "0"
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра - добавление информации")
        self.place_add_frame()
        self.place_radiobuttons()
        self.place_add_button()
        self.place_back_button()

        self.pack(fill=BOTH, expand=1)

    def place_add_frame(self) -> None:
        """Создание фрейма для добавления"""
        self.add_frame = Frame(self, width=600, height=500, bg="red")
        self.add_frame.place(x=500, y=50)

    def place_add_subjects_forms(self) -> None:
        """Создание форм для добавления предметов"""
        self.add_frame.destroy()
        self.place_add_frame()
        self.add_status = "Добавление предмета"
        add_label = Label(
            self.add_frame,
            text="Добавление предмета",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=20)

    def place_add_teachers_forms(self) -> None:
        """Создание форм для добавления преподавателя"""
        self.add_frame.destroy()
        self.place_add_frame()
        self.add_status = "Добавление преподавателя"
        add_label = Label(
            self.add_frame,
            text="Добавление преподавателя",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=20)

    def place_add_students_forms(self) -> None:
        """Создание форм для добавления студента"""
        self.add_frame.destroy()
        self.place_add_frame()
        self.add_status = "Добавление студента"
        add_label = Label(
            self.add_frame,
            text="Добавление студента",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=30)

        self.student_full_name = StringVar()
        self.student_date_of_birth = StringVar()
        self.student_adres = StringVar()
        self.student_phone = StringVar()
        student_name_entry = Entry(self.add_frame, textvariable=self.student_full_name)
        student_name_entry.place(x=20, y=100)
        student_date_entry = Entry(
            self.add_frame, textvariable=self.student_date_of_birth
        )
        student_date_entry.place(x=20, y=130)

        student_adres_entry = Entry(self.add_frame, textvariable=self.student_adres)
        student_adres_entry.place(x=20, y=160)
        student_phone_entry = Entry(self.add_frame, textvariable=self.student_phone)
        student_phone_entry.place(x=20, y=190)

    def place_add_equipment_forms(self) -> None:
        """Создание форм для добавления оборудования"""
        self.add_frame.destroy()
        self.place_add_frame()
        self.add_status = "Добавление оборудования"
        add_label = Label(
            self.add_frame,
            text="Добавление оборудования",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=20)

    def place_radiobuttons(self) -> None:
        """ Создание и размещение кнопочек выбора роли"""
        self.var = IntVar()
        self.status = "Студент"
        rad0 = Radiobutton(
            self,
            text="Предметы",
            variable=self.var,
            value=1,
            font=("Arial Bold", 15),
            command=self.place_add_subjects_forms,
        )
        rad1 = Radiobutton(
            self,
            text="Преподаватели",
            variable=self.var,
            value=2,
            font=("Arial Bold", 15),
            command=self.place_add_teachers_forms,
        )
        rad2 = Radiobutton(
            self,
            text="Студенты",
            variable=self.var,
            value=3,
            font=("Arial Bold", 15),
            command=self.place_add_students_forms,
        )
        rad3 = Radiobutton(
            self,
            text="Оборудование",
            variable=self.var,
            value=4,
            font=("Arial Bold", 15),
            command=self.place_add_equipment_forms,
        )
        rad0.place(x=30, y=40)
        rad1.place(x=30, y=70)
        rad2.place(x=30, y=100)
        rad3.place(x=30, y=130)

    def place_back_button(self) -> None:
        """ Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=100, y=600)

    def back(self) -> None:
        """ Возвращает в меню выбора действия """
        from .main_window import MainWindow

        self.remove_window()
        MainWindow(self.parent)

    def place_add_button(self) -> None:
        add_student_button = Button(
            self,
            text="Добавить",
            font=("Arial Bold", 12),
            width=12,
            command=self.test_add,
        )
        add_student_button.place(x=750, y=570)

    def test_add(self) -> None:
        """Добавление студента в бд при нажатии кнопки"""
        if self.add_status == "Добавление предмета":
            print("Предмет добавлен")
        elif self.add_status == "Добавление преподавателя":
            print("Преподаватель добавлен")
        elif self.add_status == "Добавление студента":
            print(self.student_full_name.get())
            print(self.student_date_of_birth.get())
            print(self.student_adres.get())
            print(self.student_phone.get())
        elif self.add_status == "Добавление оборудования":
            print("Оборудование добавлено")

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """
        self.destroy()
