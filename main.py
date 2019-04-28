import tkinter as tk
from tkinter import messagebox

from Magazyny.wg_dok import SecondFrame
from Pomoc.about_prog import AbProgFrame
from Pomoc.instruction import InstructProg
from Slowniki.indeks_material import IndexMat
from Slowniki.kard_agent import KardAg
from Slowniki.company_devision import CompDev
from Slowniki.unit_devision import UnitDev
from Slowniki.storage import Storage
from Slowniki.docsstore import DocsStore
from Magazyny.warehouse_records import Warehouse_Rec
from Magazyny.opening_balance import Balance_open
from Magazyny.inventory import Inventory_store
from Dokumenty.income_documents import Income_docs
from Dokumenty.expence_documents import Expence_docs
from Dokumenty.inwentory_documents import Inventory_Docs
from Dokumenty.period_close import Period_close



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
        files_menu_opts = {'Dokumenty przychodowe':{'command':self.income_docs},'Dokumenty rozchodowe':{'command':self.expence_docs},
                           'Dokumenty inwentaryzacyjne':{'command':self.inwent_docs},'Zamkniecie miesiaca':{'command':self.close_period}}
        self.add_menu_elements(file_menu, files_menu_list, files_menu_opts)

        menu_bar.add_cascade(label="Magazyny", underline=0, menu=magMenu)

        mags_menu_list = ['Kartoteki magazynowe', 'Bilans otwarcia', 'Inwentaryzacja', 'Dokumenty magazynowe']
        mags_menu_opts = {'Kartoteki magazynowe':{'command':self.warerec},'Bilans otwarcia':{'command':self.openbal},
                          'Inwentaryzacja':{'command':self.inventory},'Dokumenty magazynowe': {'menu': magmenu2}}
        self.add_menu_elements(magMenu, mags_menu_list, mags_menu_opts)

        magmenu2.add_command(label='wg dokumentow', command=self.on_mag)
        magmenu2.add_command(label='wg indeksow')
        magmenu2.add_command(label='wg grup materialowych i indeksow')

        menu_bar.add_cascade(label="Slowniki", underline=0, menu=slowMenu)
        slow_menu = ['Indeksy materialowe', 'Kartoteka kontrahentow', 'Jednostki firmy', 'Jednostki miary', 'Magazyny',
                     'Dokumenty magazynowe']
        slow_menu_opts = {'Indeksy materialowe':{'command':self.ind_mat},'Kartoteka kontrahentow':{'command':self.kardfile},
                          'Jednostki firmy':{'command':self.compdevision},'Jednostki miary':{'command':self.unitdevision},
                          'Magazyny':{'command':self.storage},'Dokumenty magazynowe':{'command':self.storagedocs}}
        self.add_menu_elements(slowMenu, slow_menu,slow_menu_opts)

        menu_bar.add_cascade(label="Pomoc", underline=0, menu=helpMenu)
        help_menu = ['O programie', 'Instrukcja obslugi']
        help_menu_opts = {'O programie':{'command': self.ab_program},'Instrukcja obslugi':{'command': self.instr}}
        self.add_menu_elements(helpMenu, help_menu, help_menu_opts)



        file_menu.add_separator()
        file_menu.add_command(label="Wyjscie", underline=0, command=self.on_exit)

    def on_exit(self):
        self.quit() #выход из программы

    def on_mag(self):
        self.master.change(SecondFrame) #выпадающее меню

    def ab_program(self):
        self.master.change(AbProgFrame) #помощь

    def instr(self):
        self.master.change(InstructProg) #помощь

    def ind_mat(self):
        self.master.change(IndexMat) #slowniki

    def kardfile(self):
        self.master.change(KardAg) #slowniki

    def compdevision(self):
        self.master.change(CompDev) #slowniki

    def unitdevision(self):
        self.master.change(UnitDev) #slowniki

    def storage(self):
        self.master.change(Storage) #slowniki

    def storagedocs(self):
        self.master.change(DocsStore) #slowniki

    def warerec(self):
        self.master.change(Warehouse_Rec) #magazyny

    def openbal(self):
        self.master.change(Balance_open) #magazyny

    def inventory(self):
        self.master.change(Inventory_store) #magazyny

    def income_docs(self):
        self.master.change(Income_docs)
    def expence_docs(self):
        self.master.change(Expence_docs)
    def inwent_docs(self):
        self.master.change(Inventory_Docs)
    def close_period(self):
        self.master.change(Period_close)





    @classmethod
    def add_menu_elements(cls, menu, elements, opts=None):
        opts = opts or {}
        for el in elements:
            menu.add_cascade(label=el, **opts.get(el, {}))


if __name__ == "__main__":
    app = AppFrame()
    app.mainloop()
