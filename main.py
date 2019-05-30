import tkinter as tk

# from conect import cur

import config
from base_frame import BaseFrame
from login import LoginFrame






class AppFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
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


class MainFrame(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title(config.APP_TITLE)
        master.geometry("850x650+300+200")
        self.init_ui()



if __name__ == "__main__":
    app = AppFrame()
    app.mainloop()
