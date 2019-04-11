import tkinter as tk
from tkinter import messagebox

import config


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
        master.geometry("300x200")

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


class MainFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title(config.APP_TITLE)
        master.geometry("850x650+300+200")
        self.init_ui()

    def init_ui(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)
        magMenu = tk.Menu(menu_bar)
        magmenu2 = tk.Menu(magMenu, tearoff=0)
        slowMenu = tk.Menu(menu_bar)
        helpMenu = tk.Menu(menu_bar)

        menu_bar.add_cascade(label="Dokumenty", underline=0, menu=file_menu)
        files_menu_list = ['Dokumenty przychodowe', 'Dokumenty rozchodowe', 'Dokumenty inwentaryzacyjne',
                           'Zamkniecie miesiaca']
        self.add_menu_elements(file_menu, files_menu_list)

        menu_bar.add_cascade(label="Magazyny", underline=0, menu=magMenu)

        mags_menu_list = ['Kartoteki magazynowe', 'Bilans otwarcia', 'Inwentaryzacja', 'Dokumenty magazynowe']
        mags_menu_opts = {'Dokumenty magazynowe': {'menu': magmenu2}}
        self.add_menu_elements(magMenu, mags_menu_list, mags_menu_opts)

        magmenu2.add_command(label='wg dokumentow')
        magmenu2.add_command(label='wg indeksow')
        magmenu2.add_command(label='wg grup materialowych i indeksow')

        menu_bar.add_cascade(label="Slowniki", underline=0, menu=slowMenu)
        slow_menu = ['Indeksy materialowe', 'Kartoteka kontrahentow', 'Jednostki firmy', 'Jednostki miary', 'Magazyny',
                     'Dokumenty magazynowe']
        self.add_menu_elements(slowMenu, slow_menu)

        menu_bar.add_cascade(label="Pomoc", underline=0, menu=helpMenu)
        help_menu = ['O programie', 'Instrukcja obsugi']
        self.add_menu_elements(helpMenu, help_menu)

        file_menu.add_separator()
        file_menu.add_command(label="Wyjscie", underline=0, command=self.on_exit)

    def on_exit(self):
        self.quit()

    @classmethod
    def add_menu_elements(cls, menu, elements, opts=None):
        opts = opts or {}
        for el in elements:
            menu.add_cascade(label=el, **opts.get(el, {}))


if __name__ == "__main__":
    app = AppFrame()
    app.mainloop()
