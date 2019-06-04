import tkinter as tk
from tkinter.ttk import Style

from tkinter import ttk
import config
from base_frame import BaseFrame
from login import LoginFrame


class AppFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.style = Style()  # TODO
        self.style.theme_use("vista")
        if config.DEV:
            self.frame = MainFrame(self)
        else:
            self.frame = LoginFrame(self, MainFrame)
        self.frame.pack()

    def change(self, frame):
        if self.frame.__class__.__name__ == frame.__name__:
            return
        self.frame.pack_forget()
        if hasattr(self.frame, 'table'):
            self.frame.table.pack_forget()
        self.frame = frame(self)
        self.frame.pack()


class MainFrame(BaseFrame, ttk.Frame):
    def __init__(self, master=None, **kwargs):
        ttk.Frame.__init__(self, master, **kwargs)
        master.title(config.APP_TITLE)
        master.geometry("850x650+300+200")
        # master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        self.init_ui()


if __name__ == "__main__":
    app = AppFrame()
    app.mainloop()
