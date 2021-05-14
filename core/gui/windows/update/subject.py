from tkinter import BOTH, Button, Frame, ttk, END, CENTER, BOTTOM, TOP, Label, Entry


class UpdateWindow(Frame):
    def __init__(self, parent, tree: ttk.Treeview) -> None:
        Frame.__init__(self, parent)
        self.parent = parent

        self.values = tree.item(tree.selection())["values"]

        self.initUI()

    def initUI(self) -> None:
        """ Постоение окна редактирования """

        w = 800
        h = 800

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Редактирование предмета")

        self.place_update_button()
        self.place_labels()
        self.place_entries()

        self.pack(fill=BOTH, expand=1)

    def place_update_button(self) -> None:
        """ Создание и расположение кнопки "Редактировать" """

        btn_update = Button(
            self,
            text="Редактировать",
            font=("Arial Bold", 10),
            width=10,
            command=self.update,
        )
        btn_update.place(x=300, y=700)

    def place_labels(self) -> None:
        subject_label = Label(
            self,
            text="Предмет",
            font=("Arial Bold", 11),
        )
        subject_label.place(x=25, y=20)

        year_label = Label(
            self,
            text="Год",
            font=("Arial Bold", 11),
        )
        year_label.place(x=25, y=120)

        sem_label = Label(
            self,
            text="Семестр",
            font=("Arial Bold", 11),
        )
        sem_label.place(x=25, y=220)

        platoon_label = Label(
            self,
            text="Взвод",
            font=("Arial Bold", 11),
        )
        platoon_label.place(x=25, y=320)

    def place_entries(self) -> None:
        self.subject_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=40,
        )
        self.subject_entry.insert(0, self.values[0])
        self.subject_entry.place(x=140, y=20)

        self.year_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=40,
        )
        self.year_entry.insert(0, self.values[1])
        self.year_entry.place(x=140, y=120)

        self.sem_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=40,
        )
        self.sem_entry.insert(0, self.values[2])
        self.sem_entry.place(x=140, y=220)

        self.platoon_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=40,
        )
        self.platoon_entry.insert(0, self.values[3])
        self.platoon_entry.place(x=140, y=320)

    def update(self) -> None:
        values = {
            "subject": self.subject_entry.get(),
            "year": self.year_entry.get(),
            "semestr": self.sem_entry.get(),
            "platoon": self.platoon_entry.get(),
        }
        print(values)
