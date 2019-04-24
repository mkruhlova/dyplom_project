import tkinter as tk

import config
from magazyny.wg_dok import SecondFrame
from pomoc.about_prog import AbProgFrame
from pomoc.instruction import InstructProg
from slowniki.indeks_material import IndexMat
from slowniki.kard_agent import KardAg
from login import LoginFrame

files_menu_list = ['Dokumenty przychodowe', 'Dokumenty rozchodowe', 'Dokumenty inwentaryzacyjne', 'Zamkniecie miesiaca']
mags_menu_list = ['Kartoteki magazynowe', 'Bilans otwarcia', 'Inwentaryzacja', 'Dokumenty magazynowe']
slow_menu = [
    'Indeksy materialowe', 'Kartoteka kontrahentow', 'Jednostki firmy', 'Jednostki miary', 'Magazyny',
    'Dokumenty magazynowe'
]
help_menu = ['O programie', 'Instrukcja obslugi']


class AppFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        if config.DEV:
            self.frame = MainFrame(self)
        else:
            self.frame = LoginFrame(self, MainFrame)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()


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
        self.add_menu_elements(file_menu, files_menu_list)

        menu_bar.add_cascade(label="Magazyny", underline=0, menu=magMenu)

        mags_menu_opts = {'Dokumenty magazynowe': {'menu': magmenu2}}
        self.add_menu_elements(magMenu, mags_menu_list, mags_menu_opts)

        magmenu2.add_command(label='wg dokumentow', command=self.on_mag)
        magmenu2.add_command(label='wg indeksow')
        magmenu2.add_command(label='wg grup materialowych i indeksow')

        menu_bar.add_cascade(label="Slowniki", underline=0, menu=slowMenu)

        slow_menu_opts = {'Indeksy materialowe': {'command': self.ind_mat},
                          'Kartoteka kontrahentow': {'command': self.kardfile}}
        self.add_menu_elements(slowMenu, slow_menu, slow_menu_opts)

        menu_bar.add_cascade(label="Pomoc", underline=0, menu=helpMenu)
        help_menu_opts = {'O programie': {'command': self.ab_program}, 'Instrukcja obslugi': {'command': self.instr}}
        help_menu_re = {'Instrukcja Obslugi': {'command': self.instr}}
        self.add_menu_elements(helpMenu, help_menu, help_menu_opts)

        file_menu.add_separator()
        file_menu.add_command(label="Wyjscie", underline=0, command=self.on_exit)

    def on_exit(self):
        self.quit()

    def on_mag(self):
        self.master.change(SecondFrame)

    def ab_program(self):
        self.master.change(AbProgFrame)

    def instr(self):
        self.master.change(InstructProg)

    def ind_mat(self):
        self.master.change(IndexMat)

    def kardfile(self):
        self.master.change(KardAg)

    @classmethod
    def add_menu_elements(cls, menu, elements, opts=None):
        opts = opts or {}
        for el in elements:
            menu.add_cascade(label=el, **opts.get(el, {}))


if __name__ == "__main__":
    app = AppFrame()
    app.mainloop()
