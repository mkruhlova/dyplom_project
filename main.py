import tkinter as tk
from tkinter.ttk import Style
from tkinter import ttk
import config
from base_frame import BaseFrame
from login import LoginFrame
from tkcalendar import DateEntry


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
        if hasattr(self.frame, "table"):
            self.frame.table.pack_forget()
        self.frame = frame(self)
        self.frame.pack()


class MainFrame(BaseFrame, ttk.Frame):
    def __init__(self, master=None, **kwargs):
        ttk.Frame.__init__(self, master, **kwargs)
        master.title(config.APP_TITLE)
        master.geometry("850x650+300+200")
        cal = DateEntry(
            self,
            width=12,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            year=2019,
        )
        cal.pack(padx=10, pady=10)
        text = tk.Label(
            self,
            text="Application for Manager your Storage!",
            fg="darkblue",
            font="Helvetica 16 bold italic",
        )
        text.pack()
        self.init_ui()


if __name__ == "__main__":
    app = AppFrame()
    app.mainloop()
