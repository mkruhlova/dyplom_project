import tkinter as tk
from tkinter import messagebox

import config


class LoginFrame(tk.Frame):
    def __init__(self, master=None, MainFrame=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title(config.LOGIN_TITLE)
        master.geometry("300x200")

        self.MainFrame = MainFrame

        lbl = tk.Label(self, text="Zaloguj sie")
        lbl.pack()
        self.login = tk.Entry(self, show="*")
        self.login.pack()
        self.login.focus()
        self.login.bind("<Return>", self.check)

        lbl = tk.Label(self, text="Wpisz haslo")
        lbl.pack()
        self.pwd = tk.Entry(self, show="*")
        self.pwd.pack()
        self.pwd.bind("<Return>", self.check)
        btn = tk.Button(self, text="Gotowe", command=self.check)
        btn.pack(padx=5, pady=5)
        btn = tk.Button(self, text="Odrzuc", command=self.quit)
        btn.pack(padx=5, pady=5)

    def check(self, event=None):
        if (
            self.pwd.get() == config.DEFAULT_PASSWORD
            and self.login.get() == config.DEFAULT_LOGIN
        ):
            messagebox.showinfo("Pomyslne zalogowanie", "Witam")
            self.master.change(self.MainFrame)
        else:
            messagebox.showwarning("Blad logowania", "Sproboj ponownie")
