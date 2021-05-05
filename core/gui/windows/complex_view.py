from tkinter import BOTH, Button, Frame, ttk, END, CENTER
from ..utils import get_role


class ComplexViewWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self) -> None:
        """ Постоение окна просмотра """

        w = 1300
        h = 700

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.parent.title("Военная кафедра - просмотр готовых представлений")

        # self.place_table_frames()
        # self.place_back_button()
        # self.place_tables()

        self.pack(fill=BOTH, expand=1)
