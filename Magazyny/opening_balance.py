import tkinter as tk
from base_frame import BaseFrame


class Balance_open(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Bilans Otwarcia")
        master.geometry("850x650+300+200")
