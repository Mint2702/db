from tkinter import BOTH, Button, Frame, Label, Entry

from .utils import show_error


class MainWindow(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self) -> None:
        """ Постоение главного окна """

        w = 2000
        h = 1200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.parent.title("Военная кафедра")

        quitButton = Button(self, text="Закрыть окно")
        quitButton.place(x=50, y=50)

        self.pack(fill=BOTH, expand=1)
