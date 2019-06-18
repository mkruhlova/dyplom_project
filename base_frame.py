import tkinter as tk


class BaseFrame(tk.Frame):
    def init_ui(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        documents_menu = tk.Menu(menu_bar)
        warehouse_menu = tk.Menu(menu_bar)
        dict_menu = tk.Menu(menu_bar)
        help_menu = tk.Menu(menu_bar)

        menu_bar.add_cascade(label="Dokumenty", menu=documents_menu)
        files_menu_list = [
            "Dokumenty Przychodowe",
            "Dokumenty Rozchodowe",
            "Zamkniecie miesiaca",
        ]
        files_menu_opts = {
            "Dokumenty Przychodowe": {"command": self.income_docs},
            "Dokumenty Rozchodowe": {"command": self.expense_docs},
            "Zamkniecie miesiaca": {"command": self.close_period},
        }
        self.add_menu_elements(documents_menu, files_menu_list, files_menu_opts)

        menu_bar.add_cascade(label="Magazyny", underline=0, menu=warehouse_menu)

        mags_menu_list = ["Kartoteki magazynowe", "Bilans otwarcia"]
        mags_menu_opts = {
            "Kartoteki magazynowe": {"command": self.warerec},
            "Bilans otwarcia": {"command": self.openbal},
        }
        self.add_menu_elements(warehouse_menu, mags_menu_list, mags_menu_opts)

        menu_bar.add_cascade(label="Slowniki", underline=0, menu=dict_menu)
        slow_menu = [
            "Indeksy materialowe",
            "Kartoteka kontrahentow",
            "Grupy materialowe",
            "Jednostki firmy",
            "Jednostki miary",
            "Magazyny",
        ]
        slow_menu_opts = {
            "Indeksy materialowe": {"command": self.ind_mat},
            "Kartoteka kontrahentow": {"command": self.kardfile},
            "Placowki": {"command": self.compdevision},
            "Grupy materialowe": {"command": self.groupmaterials},
            "Jednostki miary": {"command": self.unitdevision},
            "Jednostki firmy": {"command": self.compdevision},
            "Magazyny": {"command": self.storage},
        }
        self.add_menu_elements(dict_menu, slow_menu, slow_menu_opts)

        menu_bar.add_cascade(label="Pomoc", underline=0, menu=help_menu)
        help_menu_lst = ["O programie", "Instrukcja obslugi"]
        help_menu_opts = {
            "O programie": {"command": self.ab_program},
            "Instrukcja obslugi": {"command": self.instr},
        }
        self.add_menu_elements(help_menu, help_menu_lst, help_menu_opts)

        documents_menu.add_separator()
        documents_menu.add_command(label="Wyjscie", underline=0, command=self.on_exit)

    def on_exit(self):
        self.quit()

    def ab_program(self):
        self.master.change(AboutProg)

    def instr(self):

        self.master.change(InstructProg)

    def ind_mat(self):

        self.master.change(IndexMat)

    def kardfile(self):

        self.master.change(KardAg)

    def compdevision(self):

        self.master.change(CompDev)

    def unitdevision(self):

        self.master.change(UnitDev)

    def groupmaterials(self):

        self.master.change(GroupMaterials)

    def storage(self):

        self.master.change(Storage)

    def storagedocs(self):

        self.master.change(DocsStore)

    def warerec(self):

        self.master.change(WarehouseRec)

    def openbal(self):
        self.master.change(BalanceOpen)

    def expense_docs(self):

        self.master.change(ExpenseDocs)

    def income_docs(self):

        self.master.change(IncomeDocs)

    def close_period(self):

        self.master.change(PeriodClose)

    @classmethod
    def add_menu_elements(cls, menu, elements, opts=None):
        opts = opts or {}
        for el in elements:
            menu.add_cascade(label=el, **opts.get(el, {}))


from Pomoc.about_prog import AboutProg
from Pomoc.instruction import InstructProg
from Slowniki.indeks_material import IndexMat
from Slowniki.kard_agent import KardAg
from Slowniki.company_devision import CompDev
from Slowniki.unit_devision import UnitDev
from Slowniki.material_grup import GroupMaterials
from Slowniki.storage import Storage
from Slowniki.docsstore import DocsStore
from Magazyny.warehouse_records import WarehouseRec
from Magazyny.opening_balance import BalanceOpen
from Dokumenty.expense_documents import ExpenseDocs
from Dokumenty.income_documents import IncomeDocs
from Dokumenty.period_close import PeriodClose
