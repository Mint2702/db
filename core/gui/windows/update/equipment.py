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
        self.parent.title("Редактирование оборудования")

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
        name_label = Label(
            self,
            text="Оборудование",
            font=("Arial Bold", 11),
        )
        name_label.place(x=25, y=50)

        subject_label = Label(
            self,
            text="Предмет",
            font=("Arial Bold", 11),
        )
        subject_label.place(x=25, y=250)

    def place_entries(self) -> None:
        self.name_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.name_entry.insert(0, self.values[0])
        self.name_entry.place(x=350, y=50)

        self.subject_entry = Entry(
            self,
            font=("Arial Bold", 11),
            width=30,
        )
        self.subject_entry.insert(0, self.values[1])
        self.subject_entry.place(x=350, y=250)

    def update(self) -> None:
        values = {
            "subject": self.subject_entry.get(),
            "name": self.name_entry.get(),
        }
        print(values)
