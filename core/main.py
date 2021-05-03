from tkinter import mainloop

from gui import graphics
from db import database

if __name__ == "__main__":
    graphics.connect_to_db()
    database.get_table("equipment")
    graphics.main_window()
