from tkinter import BOTH, Button, Frame, Listbox, SINGLE, END, StringVar


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

        self.place_listbox()
        self.place_back_button()

        self.pack(fill=BOTH, expand=1)

    def place_listbox(self) -> None:
        """ Создание листбокса добавления"""
        variants = ["Оборудование", "Предметы"]
        lis = Listbox(self, selectmode=SINGLE, height=4)
        for i in variants:
            lis.insert(END, i)
        lis.bind("<<ListboxSelect>>", self.onSelect)
        lis.place(x=30, y=40)

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        if value == "Предметы":
            print("Предметы")
        elif value == "Оборудование":
            print("Оборудование")

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
