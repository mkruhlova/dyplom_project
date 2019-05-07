import tkinter as tk
from tkinter import messagebox

import config
from base_frame import BaseFrame


class AppFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = LoginFrame(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()


class LoginFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title(config.LOGIN_TITLE)
        master.geometry("300x200+300+200")

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
            self.master.change(MainFrame)
        else:
            messagebox.showwarning("Login failed", "Please try again")


class MainFrame(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title(config.APP_TITLE)
        master.geometry("850x650+300+200")
        self.init_ui()


if __name__ == "__main__":
    app = AppFrame()
    app.mainloop()
