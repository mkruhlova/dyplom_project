import tkinter as tk
from base_frame import BaseFrame


class CompDev(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Jednostki firmy")
        master.geometry("850x650+300+200")
