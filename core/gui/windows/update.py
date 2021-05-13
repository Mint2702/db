from tkinter import BOTH, Button, Frame, ttk, END, CENTER, BOTTOM, TOP
from ..utils import get_role


class UpdateWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self) -> None:
        """ Постоение окна редактирования """

        w = 700
        h = 800

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра - редактирование представлений")

        self.place_update_button()
        # self.place_back_button()
        # self.place_tables()

        self.pack(fill=BOTH, expand=1)

    def place_update_button(self) -> None:
        """ Создание и расположение кнопки "Редактировать" """

        btn_update = Button(
            self, text="Редактировать", font=("Arial Bold", 10), width=10
        )
        btn_update.place(x=350, y=700)
