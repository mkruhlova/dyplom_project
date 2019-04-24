import tkinter as tk
from tkinter import messagebox

import config


class LoginFrame(tk.Frame):
    def __init__(self, master=None, MainFrame=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title(config.LOGIN_TITLE)
        master.geometry("300x200")

        self.MainFrame = MainFrame

        lbl = tk.Label(self, text='Enter login')
        lbl.pack()
        self.login = tk.Entry(self, show="*")
        self.login.pack()
        self.login.focus()
        self.login.bind('<Return>', self.check)

        lbl = tk.Label(self, text='Enter password')
        lbl.pack()
        self.pwd = tk.Entry(self, show="*")
        self.pwd.pack()
        self.pwd.bind('<Return>', self.check)
        btn = tk.Button(self, text="Done", command=self.check)
        btn.pack()
        btn = tk.Button(self, text="Cancel", command=self.quit)
        btn.pack()

    def check(self, event=None):
        if self.pwd.get() == config.DEFAULT_PASSWORD and self.login.get() == config.DEFAULT_LOGIN:
            messagebox.showinfo("Successfully login", "Welcome")
            self.master.change(self.MainFrame)
        else:
            messagebox.showwarning("Login failed", "Please try again")

