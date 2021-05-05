from tkinter import BOTH, Button, Frame, Listbox, SINGLE, END, Label, Entry, StringVar


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

        self.place_listbox()
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



    def place_listbox(self) -> None:
        """ Создание листбокса добавления"""
        variants = ["Предметы", "Преподаватели", "Студенты", "Оборудование"]
        lis = Listbox(self, selectmode=SINGLE, height=4, font=("Arial Bold", 15))
        for i in variants:
            lis.insert(END, i)
        lis.bind("<<ListboxSelect>>", self.onSelect)
        lis.place(x=30, y=40)

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        if value == "Предметы":
            self.place_add_subjects_forms()
        elif value == "Преподаватели":
            self.place_add_teachers_forms()
        elif value == "Студенты":
            self.place_add_students_forms()
        elif value == "Оборудование":
            self.place_add_equipment_forms()


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
