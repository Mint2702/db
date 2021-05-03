from tkinter import BOTH, Button, Frame, ttk, END, CENTER


class ViewWindow(Frame):
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
        self.parent.title("Военная кафедра - просмотр таблиц")

        self.place_table_frames()
        self.place_back_button()
        self.place_tables()

        self.pack(fill=BOTH, expand=1)


    def place_table_frames(self) -> None:
        """" Создание фреймов для размещения таблиц"""

        note_tree = ttk.Notebook(self, style='style.TNotebook', height=200, width=400)
        note_tree.place(x=300, y=200)
        self.f_equipment = Frame(note_tree, width=300, height=300)
        self.f_test = Frame(note_tree, width=300, height=300)
        note_tree.add(self.f_equipment, text='Оборудование')
        note_tree.add(self.f_test, text='Тест')


    def place_back_button(self) -> None:
        """ Создание и расположение кнопки "назад" """

        btn_filter = Button(
            self, text="Назад", font=("Arial Bold", 10), width=10, command=self.back
        )
        btn_filter.place(x=400, y=500)


    def place_tables(self) -> None:
        """Создание и расположение таблиц"""

        self.place_table_equipment()
        self.place_table_test()


    def place_table_equipment(self) -> None:
        """ Создание и расположение таблицы "equipment" """

        tree = ttk.Treeview(self.f_equipment, column=("c1", "c2"), show="headings")
        tree.pack(side='left', fill='y')
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="DENOMINATION")

        self.fill_table_equipment(tree)

        tree.place(x=1, y=1)

    def place_table_test(self) -> None:
        """ Создание и расположение таблицы "test" """

        tree = ttk.Treeview(self.f_test, column=("c1", "c2"), show="headings")
        tree.pack(side='left', fill='y')
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="ID")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="DENOMINATION")

        self.fill_table_equipment(tree)

        tree.place(x=1, y=1)

    def fill_table_equipment(self, tree: ttk.Treeview) -> None:
        """ Заполнение таблицы "equipment" """

        import sys

        sys.path.append("..")

        from db.database import get_table_equipment

        records = get_table_equipment()

        for record in records:
            tree.insert("", END, values=record)

    def back(self) -> None:
        """ Возвращает в меню выбора действия """

        self.remove_window()

        from tkinter import Tk

        from .main_window import MainWindow
        from .utils import create_new_window

        @create_new_window
        def back_to_main(root: Tk) -> None:
            MainWindow(root)

        back_to_main()

    def remove_window(self) -> None:
        """ Удаляет все обьекты родительского окна """

        self.parent.destroy()
