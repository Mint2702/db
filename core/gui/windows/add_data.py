from tkinter import BOTH, Button, Frame, Listbox, SINGLE, END, Label, Entry, StringVar, Radiobutton, IntVar


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

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра - добавление информации")
        self.place_add_frame()
        self.place_radiobuttons()
        #self.place_listbox()
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
        add_label = Label(
            self.add_frame,
            text="Добавление предмета",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=100)


    def place_add_teachers_forms(self) -> None:
        """Создание форм для добавления преподавателя"""
        self.add_frame.destroy()
        self.place_add_frame()
        add_label = Label(
            self.add_frame,
            text="Добавление преподавателя",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=100)





    def place_add_students_forms(self) -> None:
        """Создание форм для добавления студентов"""
        self.add_frame.destroy()
        self.place_add_frame()
        add_label = Label(
            self.add_frame,
            text="Добавление студента",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=100)

        self.student_full_name = StringVar()

        message_entry = Entry(self.add_frame, textvariable=self.student_full_name)
        message_entry.place(x=500, y=100)

        '''
        add_student_button = Button(
            self.add_frame, text="Добавить", font=("Arial Bold", 10), width=10, command=self.test_add()
        )
        add_student_button.place(x=500, y=300)
        '''


    def test_add(self) -> None:
        """Добавление студента в бд при нажатии кнопки"""
        print('fefeff')


    def place_add_equipment_forms(self) -> None:
        """Создание форм для добавления оборудования"""
        self.add_frame.destroy()
        self.place_add_frame()
        add_label = Label(
            self.add_frame,
            text="Добавление оборудования",
            font=("Arial Bold", 15),
        )
        add_label.place(x=25, y=100)



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
        btn_filter.place(x=900, y=600)

    def back(self) -> None:
        """ Возвращает в меню выбора действия """

        from tkinter import Tk
        from .main_window import MainWindow

        self.remove_window()
        MainWindow(self.parent)

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """

        self.destroy()
