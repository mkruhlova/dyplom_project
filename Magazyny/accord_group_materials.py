import tkinter as tk
from base_frame import BaseFrame

class AccordMaterials(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Kartoteka kontrahentow")
        master.geometry("850x650+300+200")