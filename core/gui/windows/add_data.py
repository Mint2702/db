from tkinter import (
    BOTH,
    Button,
    Frame,
    Label,
    Entry,
    StringVar,
    Radiobutton,
    IntVar,
    ttk,
)
from ..utils import get_role


class AddDataWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self) -> None:
        """Постоение окна добавления информации"""

        w = 1500
        h = 600

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2 + 100
        y = (sh - h) / 2 - 50

        self.add_status = "0"
        self.user = get_role()
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра - добавление информации")
        self.place_add_frame()

        self.place_radiobuttons()

        self.place_add_button()
        self.place_back_button()

        self.pack(fill=BOTH, expand=1)

    def place_add_frame(self) -> None:
        """Создание фрейма для добавления"""
        self.add_frame = Frame(self, width=800, height=400)
        self.add_frame.place(x=500, y=50)

    def place_add_subjects_forms(self) -> None:
        """Создание форм для добавления предметов"""
        from db.get import get_roda

        self.add_frame.destroy()
        self.place_add_frame()
        self.add_status = "Добавление предмета"
        add_label = Label(
            self.add_frame,
            text="Добавление предмета",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=20)

        subject_label_1 = Label(
            self.add_frame,
            text="Название: ",
            font=("Arial Bold", 14),
        )
        subject_label_1.place(x=5, y=100)

        subject_label_2 = Label(
            self.add_frame,
            text="Год обучения: ",
            font=("Arial Bold", 14),
        )
        subject_label_2.place(x=5, y=130)

        subject_label_3 = Label(
            self.add_frame,
            text="Семестр обучения: ",
            font=("Arial Bold", 14),
        )
        subject_label_3.place(x=5, y=160)

        subject_label_4 = Label(
            self.add_frame,
            text="Род войск: ",
            font=("Arial Bold", 14),
        )
        subject_label_4.place(x=5, y=190)

        self.subject_name = StringVar()
        subject_name_entry = Entry(self.add_frame, textvariable=self.subject_name)
        subject_name_entry.place(x=220, y=100)

        self.subject_year = StringVar()
        subject_year_entry = Entry(self.add_frame, textvariable=self.subject_year)
        subject_year_entry.place(x=220, y=130)

        self.subject_semestr = ttk.Combobox(self.add_frame, values=[1, 2], width=2)
        self.subject_semestr.place(x=220, y=160)

        roda = get_roda()
        self.subject_rod = ttk.Combobox(self.add_frame, values=roda, width=30)
        self.subject_rod.place(x=220, y=190)

    def place_add_teachers_forms(self) -> None:
        """Создание форм для добавления преподавателя"""
        from db.get import get_rank, get_subjects

        self.add_frame.destroy()
        self.place_add_frame()
        self.add_status = "Добавление преподавателя"
        add_label = Label(
            self.add_frame,
            text="Добавление преподавателя",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=20)

        teacher_label_1 = Label(
            self.add_frame,
            text="Имя: ",
            font=("Arial Bold", 14),
        )
        teacher_label_1.place(x=5, y=100)

        teacher_label_2 = Label(
            self.add_frame,
            text="Фамилия: ",
            font=("Arial Bold", 14),
        )
        teacher_label_2.place(x=5, y=130)

        teacher_label_3 = Label(
            self.add_frame,
            text="Дата рождения: ",
            font=("Arial Bold", 14),
        )
        teacher_label_3.place(x=5, y=160)

        teacher_label_4 = Label(
            self.add_frame,
            text="Начало преподавания: ",
            font=("Arial Bold", 14),
        )
        teacher_label_4.place(x=5, y=190)

        teacher_label_5 = Label(
            self.add_frame,
            text="Номер паспорта: ",
            font=("Arial Bold", 14),
        )
        teacher_label_5.place(x=5, y=220)

        teacher_label_6 = Label(
            self.add_frame,
            text="Дата выдачи паспорта: ",
            font=("Arial Bold", 14),
        )
        teacher_label_6.place(x=5, y=250)

        teacher_label_7 = Label(
            self.add_frame,
            text="Паспорт выдан: ",
            font=("Arial Bold", 14),
        )
        teacher_label_7.place(x=5, y=280)

        teacher_label_8 = Label(
            self.add_frame,
            text="ИНН: ",
            font=("Arial Bold", 14),
        )
        teacher_label_8.place(x=5, y=310)

        teacher_label_9 = Label(
            self.add_frame,
            text="Звание: ",
            font=("Arial Bold", 14),
        )
        teacher_label_9.place(x=5, y=340)

        teacher_label_10 = Label(
            self.add_frame,
            text="Специализация: ",
            font=("Arial Bold", 14),
        )
        teacher_label_10.place(x=400, y=100)

        teacher_label_11 = Label(
            self.add_frame,
            text="Адрес: ",
            font=("Arial Bold", 14),
        )
        teacher_label_11.place(x=400, y=130)

        teacher_label_12 = Label(
            self.add_frame,
            text="Телефон: ",
            font=("Arial Bold", 14),
        )
        teacher_label_12.place(x=400, y=160)

        self.teacher_name = StringVar()
        self.teacher_surname = StringVar()
        self.teacher_date_of_birth = StringVar()
        self.teacher_begin = StringVar()
        self.teacher_passport_num = StringVar()
        self.teacher_passport_date = StringVar()
        self.teacher_passport_given = StringVar()
        self.teacher_passport_inn = StringVar()
        self.teacher_address = StringVar()
        self.teacher_phone = StringVar()

        teacher_name_entry = Entry(self.add_frame, textvariable=self.teacher_name)
        teacher_name_entry.place(x=230, y=100)

        teacher_surname_entry = Entry(self.add_frame, textvariable=self.teacher_surname)
        teacher_surname_entry.place(x=230, y=130)

        teacher_date_entry = Entry(
            self.add_frame, textvariable=self.teacher_date_of_birth
        )
        teacher_date_entry.place(x=230, y=160)

        teacher_begin_entry = Entry(self.add_frame, textvariable=self.teacher_begin)
        teacher_begin_entry.place(x=230, y=190)

        teacher_passport_num_entry = Entry(
            self.add_frame, textvariable=self.teacher_passport_num
        )
        teacher_passport_num_entry.place(x=230, y=220)

        teacher_passport_date_entry = Entry(
            self.add_frame, textvariable=self.teacher_passport_date
        )
        teacher_passport_date_entry.place(x=230, y=250)

        teacher_passport_given_entry = Entry(
            self.add_frame, textvariable=self.teacher_passport_given
        )
        teacher_passport_given_entry.place(x=230, y=280)

        teacher_passport_inn_entry = Entry(
            self.add_frame, textvariable=self.teacher_passport_inn
        )
        teacher_passport_inn_entry.place(x=230, y=310)

        ranks = get_rank()
        self.teacher_rank = ttk.Combobox(self.add_frame, values=ranks, width=15)
        self.teacher_rank.place(x=230, y=340)

        subjects = get_subjects()
        self.teacher_specialisation = ttk.Combobox(
            self.add_frame, values=subjects, width=20
        )
        self.teacher_specialisation.place(x=580, y=100)

        teacher_address_entry = Entry(self.add_frame, textvariable=self.teacher_address)
        teacher_address_entry.place(x=580, y=130)

        teacher_phone_entry = Entry(self.add_frame, textvariable=self.teacher_phone)
        teacher_phone_entry.place(x=580, y=160)

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

        student_label_1 = Label(
            self.add_frame,
            text="Имя: ",
            font=("Arial Bold", 14),
        )
        student_label_1.place(x=5, y=100)

        student_label_2 = Label(
            self.add_frame,
            text="Фамилия: ",
            font=("Arial Bold", 14),
        )
        student_label_2.place(x=5, y=130)

        student_label_3 = Label(
            self.add_frame,
            text="Дата рождения: ",
            font=("Arial Bold", 14),
        )
        student_label_3.place(x=5, y=160)

        student_label_4 = Label(
            self.add_frame,
            text="Номер паспорта: ",
            font=("Arial Bold", 14),
        )
        student_label_4.place(x=5, y=190)

        student_label_5 = Label(
            self.add_frame,
            text="Дата выдачи паспорта: ",
            font=("Arial Bold", 14),
        )
        student_label_5.place(x=5, y=220)

        student_label_6 = Label(
            self.add_frame,
            text="Паспорт выдан: ",
            font=("Arial Bold", 14),
        )
        student_label_6.place(x=5, y=250)

        student_label_7 = Label(
            self.add_frame,
            text="ИНН: ",
            font=("Arial Bold", 14),
        )
        student_label_7.place(x=5, y=280)

        student_label_8 = Label(
            self.add_frame,
            text="Номер взвода: ",
            font=("Arial Bold", 14),
        )
        student_label_8.place(x=5, y=310)

        student_label_9 = Label(
            self.add_frame,
            text="Адрес: ",
            font=("Arial Bold", 14),
        )
        student_label_9.place(x=400, y=100)

        student_label_10 = Label(
            self.add_frame,
            text="Номер телефона: ",
            font=("Arial Bold", 14),
        )
        student_label_10.place(x=400, y=130)

        self.student_name = StringVar()
        self.student_surname = StringVar()
        self.student_date_of_birth = StringVar()
        self.student_passport_num = StringVar()
        self.student_passport_date = StringVar()
        self.student_passport_given = StringVar()
        self.student_passport_inn = StringVar()
        self.student_address = StringVar()
        self.student_phone = StringVar()

        student_name_entry = Entry(self.add_frame, textvariable=self.student_name)
        student_name_entry.place(x=230, y=100)
        student_surname_entry = Entry(self.add_frame, textvariable=self.student_surname)
        student_surname_entry.place(x=230, y=130)
        student_date_entry = Entry(
            self.add_frame, textvariable=self.student_date_of_birth
        )
        student_date_entry.place(x=230, y=160)
        student_passport_num_entry = Entry(
            self.add_frame, textvariable=self.student_passport_num
        )
        student_passport_num_entry.place(x=230, y=190)
        student_passport_date_entry = Entry(
            self.add_frame, textvariable=self.student_passport_date
        )
        student_passport_date_entry.place(x=230, y=220)
        student_passport_given_entry = Entry(
            self.add_frame, textvariable=self.student_passport_given
        )
        student_passport_given_entry.place(x=230, y=250)
        student_passport_inn_entry = Entry(
            self.add_frame, textvariable=self.student_passport_inn
        )
        student_passport_inn_entry.place(x=230, y=280)

        self.student_platoon = ttk.Combobox(self.add_frame, values=[1, 2, 3], width=2)
        self.student_platoon.place(x=230, y=310)

        student_address_entry = Entry(self.add_frame, textvariable=self.student_address)
        student_address_entry.place(x=580, y=100)

        student_phone_entry = Entry(self.add_frame, textvariable=self.student_phone)
        student_phone_entry.place(x=580, y=130)

    def place_add_equipment_forms(self) -> None:
        """Создание форм для добавления оборудования"""
        from db.get import get_subjects

        self.add_frame.destroy()
        self.place_add_frame()
        self.add_status = "Добавление оборудования"
        add_label = Label(
            self.add_frame,
            text="Добавление оборудования",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=20)

        equipment_label_1 = Label(
            self.add_frame,
            text="Название: ",
            font=("Arial Bold", 14),
        )
        equipment_label_1.place(x=5, y=100)

        equipment_label_2 = Label(
            self.add_frame,
            text="Предмет: ",
            font=("Arial Bold", 14),
        )
        equipment_label_2.place(x=5, y=130)

        self.equipment_name = StringVar()
        equipment_name_entry = Entry(self.add_frame, textvariable=self.equipment_name)
        equipment_name_entry.place(x=190, y=100)

        subjects = get_subjects()
        self.equipment_subject = ttk.Combobox(self.add_frame, values=subjects, width=30)
        self.equipment_subject.place(x=190, y=130)

    def place_radiobuttons(self) -> None:
        """Создание и размещение кнопочек выбора роли"""
        self.var = IntVar()

        if self.user == "Преподаватель":
            self.status = "Преподаватели"
            rad3 = Radiobutton(
                self,
                text="Оборудование",
                variable=self.var,
                value=4,
                font=("Arial Bold", 15),
                command=self.place_add_equipment_forms,
            )
            rad3.place(x=30, y=70)

        elif self.user == "Начальник цикла":
            self.status = "Студент"
            rad0 = Radiobutton(
                self,
                text="Предметы",
                variable=self.var,
                value=1,
                font=("Arial Bold", 15),
                command=self.place_add_subjects_forms,
            )
            rad0.place(x=30, y=40)
            rad2 = Radiobutton(
                self,
                text="Студенты",
                variable=self.var,
                value=3,
                font=("Arial Bold", 15),
                command=self.place_add_students_forms,
            )
            rad2.place(x=30, y=70)
        elif self.user == "Начальник ВУЦ":
            self.status = "Студент"
            rad1 = Radiobutton(
                self,
                text="Преподаватели",
                variable=self.var,
                value=2,
                font=("Arial Bold", 15),
                command=self.place_add_teachers_forms,
            )
            rad1.place(x=30, y=40)
            """
            rad2 = Radiobutton(
                self,
                text="Студенты",
                variable=self.var,
                value=3,
                font=("Arial Bold", 15),
                command=self.place_add_students_forms,
            )
            rad2.place(x=30, y=70)
            """

        """

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
            
        """

    def place_back_button(self) -> None:
        """Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=100, y=500)

    def back(self) -> None:
        """Возвращает в меню выбора действия"""
        from .main_window import MainWindow

        self.remove_window()
        MainWindow(self.parent)

    def remove_window(self) -> None:
        """Удаляет все обьекты родительского окна"""
        self.destroy()

    def place_add_button(self) -> None:
        add_student_button = Button(
            self, text="Добавить", font=("Arial Bold", 12), width=12, command=self.add
        )
        add_student_button.place(x=750, y=500)

    def add(self) -> None:
        """Добавление студента в бд при нажатии кнопки"""
        from db.post import post_student, post_subject, post_equipment, post_teacher

        if self.add_status == "Добавление предмета":
            post_subject(
                self.subject_name.get(),
                self.subject_year.get(),
                self.subject_semestr.get(),
                self.subject_rod.get(),
            )

        elif self.add_status == "Добавление преподавателя":
            post_teacher(
                self.teacher_name.get(),
                self.teacher_surname.get(),
                self.teacher_date_of_birth.get(),
                self.teacher_begin.get(),
                self.teacher_passport_num.get(),
                self.teacher_passport_date.get(),
                self.teacher_passport_given.get(),
                self.teacher_passport_inn.get(),
                self.teacher_rank.get(),
                self.teacher_specialisation.get(),
                self.teacher_address.get(),
                self.teacher_phone.get(),
            )

        elif self.add_status == "Добавление студента":
            post_student(
                self.student_name.get(),
                self.student_surname.get(),
                self.student_date_of_birth.get(),
                self.student_passport_num.get(),
                self.student_passport_date.get(),
                self.student_passport_given.get(),
                self.student_passport_inn.get(),
                self.student_platoon.get(),
                self.student_address.get(),
                self.student_phone.get(),
            )

        elif self.add_status == "Добавление оборудования":
            post_equipment(self.equipment_name.get(), self.equipment_subject.get())
