from tkinter import mainloop

from gui import graphics
from db import database

if __name__ == "__main__":
    database.db_connect()
    root = graphics.start()
    root.mainloop()
