import tkinter as tk


class BaseFrame(tk.Frame):
    def init_ui(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)
        magMenu = tk.Menu(menu_bar)
        slowMenu = tk.Menu(menu_bar)
        helpMenu = tk.Menu(menu_bar)

        menu_bar.add_cascade(label="Dokumenty", underline=0, menu=file_menu)
        files_menu_list = [
            "Dokumenty Przychodowe",
            "Dokumenty Rozchodowe",
            "Zamkniecie miesiaca",
        ]
        files_menu_opts = {
            "Dokumenty Przychodowe": {"command": self.expence_docs},
            "Dokumenty Rozchodowe": {"command": self.income_docs},
            "Zamkniecie miesiaca": {"command": self.close_period},
        }
        self.add_menu_elements(file_menu, files_menu_list, files_menu_opts)

        menu_bar.add_cascade(label="Magazyny", underline=0, menu=magMenu)

        mags_menu_list = ["Kartoteki magazynowe", "Bilans otwarcia"]
        mags_menu_opts = {
            "Kartoteki magazynowe": {"command": self.warerec},
            "Bilans otwarcia": {"command": self.openbal},
        }
        self.add_menu_elements(magMenu, mags_menu_list, mags_menu_opts)

        menu_bar.add_cascade(label="Slowniki", underline=0, menu=slowMenu)
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
        self.add_menu_elements(slowMenu, slow_menu, slow_menu_opts)

        menu_bar.add_cascade(label="Pomoc", underline=0, menu=helpMenu)
        help_menu = ["O programie", "Instrukcja obslugi"]
        help_menu_opts = {
            "O programie": {"command": self.ab_program},
            "Instrukcja obslugi": {"command": self.instr},
        }
        self.add_menu_elements(helpMenu, help_menu, help_menu_opts)

        file_menu.add_separator()
        file_menu.add_command(label="Wyjscie", underline=0, command=self.on_exit)

    def on_exit(self):
        self.quit()

    def ab_program(self):
        from Pomoc.about_prog import AboutProg

        self.master.change(AboutProg)

    def instr(self):
        from Pomoc.instruction import InstructProg

        self.master.change(InstructProg)

    def ind_mat(self):
        from Slowniki.indeks_material import IndexMat

        self.master.change(IndexMat)

    def kardfile(self):
        from Slowniki.kard_agent import KardAg

        self.master.change(KardAg)

    def compdevision(self):
        from Slowniki.company_devision import CompDev

        self.master.change(CompDev)

    def unitdevision(self):
        from Slowniki.unit_devision import UnitDev

        self.master.change(UnitDev)

    def groupmaterials(self):
        from Slowniki.material_grup import GroupMaterials

        self.master.change(GroupMaterials)

    def storage(self):
        from Slowniki.storage import Storage

        self.master.change(Storage)

    def storagedocs(self):
        from Slowniki.docsstore import DocsStore

        self.master.change(DocsStore)

    def warerec(self):
        from Magazyny.warehouse_records import WarehouseRec

        self.master.change(WarehouseRec)

    def openbal(self):
        from Magazyny.opening_balance import BalanceOpen

        self.master.change(BalanceOpen)

    def income_docs(self):
        from Dokumenty.income_documents import IncomeDocs

        self.master.change(IncomeDocs)

    def expence_docs(self):
        from Dokumenty.expence_documents import ExpenceDocs

        self.master.change(ExpenceDocs)

    def close_period(self):
        from Dokumenty.period_close import PeriodClose

        self.master.change(PeriodClose)

    @classmethod
    def add_menu_elements(cls, menu, elements, opts=None):
        opts = opts or {}
        for el in elements:
            menu.add_cascade(label=el, **opts.get(el, {}))
