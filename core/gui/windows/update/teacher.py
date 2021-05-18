from tkinter import BOTH, Button, Frame, ttk, END, CENTER, BOTTOM, TOP, Label, Entry


class UpdateWindow(Frame):
    def __init__(self, parent, tree: ttk.Treeview) -> None:
        Frame.__init__(self, parent)
        self.parent = parent

        self.values = tree.item(tree.selection())["values"]
        self.old = tree.item(tree.selection())["values"]

        self.initUI()

    def initUI(self) -> None:
        """Постоение окна редактирования"""

        w = 800
        h = 800

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Редактирование информации о преподавателе")

        self.place_update_button()
        self.place_labels()
        self.place_entries()

        self.pack(fill=BOTH, expand=1)

    def place_update_button(self) -> None:
        """Создание и расположение кнопки "Редактировать" """

        btn_update = Button(
            self,
            text="Редактировать",
            font=("Arial Bold", 10),
            width=10,
            command=self.update,
        )
        btn_update.place(x=300, y=750)

    def place_labels(self) -> None:
        name_label = Label(
            self,
            text="Имя",
            font=("Arial Bold", 11),
        )
        name_label.place(x=25, y=20)

        last_label = Label(
            self,
            text="Фамилия",
            font=("Arial Bold", 11),
        )
        last_label.place(x=25, y=80)

        born_label = Label(
            self,
            text="Дата рождения",
            font=("Arial Bold", 11),
        )
        born_label.place(x=25, y=140)

        teaching_label = Label(
            self,
            text="Начало преподавания",
            font=("Arial Bold", 11),
        )
        teaching_label.place(x=25, y=200)

        pas_num_label = Label(
            self,
            text="Номер пасспорта",
            font=("Arial Bold", 11),
        )
        pas_num_label.place(x=25, y=260)

        pas_date_label = Label(
            self,
            text="Дата выдачи пасспорта",
            font=("Arial Bold", 11),
        )
        pas_date_label.place(x=25, y=320)

        pas_given_label = Label(
            self,
            text="Кем выдан",
            font=("Arial Bold", 11),
        )
        pas_given_label.place(x=25, y=380)

        inn_label = Label(
            self,
            text="ИНН",
            font=("Arial Bold", 11),
        )
        inn_label.place(x=25, y=440)

        rank_label = Label(
            self,
            text="Звание",
            font=("Arial Bold", 11),
        )
        rank_label.place(x=25, y=500)

        subject_label = Label(
            self,
            text="Основной предмет",
            font=("Arial Bold", 11),
        )
        subject_label.place(x=25, y=560)

        adres_label = Label(
            self,
            text="Адрес",
            font=("Arial Bold", 11),
        )
        adres_label.place(x=25, y=620)

        number_label = Label(
            self,
            text="Номер телефона",
            font=("Arial Bold", 11),
        )
        number_label.place(x=25, y=680)

    def place_entries(self) -> None:
        self.name_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.name_entry.insert(0, self.values[0])
        self.name_entry.place(x=350, y=20)

        self.last_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.last_entry.insert(0, self.values[1])
        self.last_entry.place(x=350, y=80)

        self.born_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.born_entry.insert(0, self.values[2])
        self.born_entry.place(x=350, y=140)

        self.teaching_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.teaching_entry.insert(0, self.values[3])
        self.teaching_entry.place(x=350, y=200)

        self.pas_num_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.pas_num_entry.insert(0, self.values[4])
        self.pas_num_entry.place(x=350, y=260)

        self.pas_date_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.pas_date_entry.insert(0, self.values[5])
        self.pas_date_entry.place(x=350, y=320)

        self.pas_given_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.pas_given_entry.insert(0, self.values[6])
        self.pas_given_entry.place(x=350, y=380)

        self.inn_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.inn_entry.insert(0, self.values[7])
        self.inn_entry.place(x=350, y=440)

        self.rank_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.rank_entry.insert(0, self.values[8])
        self.rank_entry.place(x=350, y=500)

        self.subject_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.subject_entry.insert(0, self.values[9])
        self.subject_entry.place(x=350, y=560)

        self.adres_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.adres_entry.insert(0, self.values[10])
        self.adres_entry.place(x=350, y=620)

        self.number_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.number_entry.insert(0, self.values[11])
        self.number_entry.place(x=350, y=680)

    def update(self) -> None:
        from db.update import update_teacher

        values = {
            "name": self.name_entry.get(),
            "last_name": self.last_entry.get(),
            "born": self.born_entry.get(),
            "teaching": self.teaching_entry.get(),
            "pas_num": self.pas_num_entry.get(),
            "pas_date": self.pas_date_entry.get(),
            "pas_given": self.pas_given_entry.get(),
            "inn": self.inn_entry.get(),
            "rank": self.rank_entry.get(),
            "subject": self.subject_entry.get(),
            "address": self.adres_entry.get(),
            "number": self.number_entry.get(),
        }
        update_teacher(values, self.old)
