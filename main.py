from tkinter import *
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox

def try_login():
    if name_entry.get()==default_name and password_entry.get() == default_password:
       messagebox.showinfo("LOGIN SUCCESSFULLY","WELCOME")
    else:
       messagebox.showwarning("login failed","Please try again" )


def cancel_login():
    log.destroy()



default_name=("admin")
default_password=("test")

log=Tk()
log.title("MagazynProLogin")
log.geometry("600x400+400+200")
log.resizable (width=FALSE,height=FALSE)


LABEL_1 = Label(log,text="USER NAME")
LABEL_1.place(x=50,y=100)
LABEL_2 = Label(log,text="PASSWORD")
LABEL_2.place(x=50,y=150)

BUTTON_1=ttk. Button(text="Login",command=open())
BUTTON_1.place(x=50,y=200)
BUTTON_1=ttk. Button(text="Cancel",command=quit)
BUTTON_1.place(x=200,y=200)

name_entry=Entry(log,width=30)
name_entry.place(x=150,y=100)
password_entry=ttk. Entry(log,width=30,show="*")
password_entry.place(x=150,y=150)

log. mainloop()

def main():
    root = Tk()
    root.geometry("850x650+300+200")
    app = Main(root)
    root.mainloop()

class Main (Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("MagazynPro")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        magMenu = Menu(menubar)
        magmenu2 = Menu(magMenu, tearoff=0)
        slowMenu = Menu(menubar)
        helpMenu = Menu (menubar)

        #submenu = Menu(fileMenu)

        menubar.add_cascade(label="Dokumenty", underline=0, menu=fileMenu)

        files_menu = ['Dokumenty przychodowe', 'Dokumenty rozchodowe', 'Dokumenty inwentaryzacyjne',
                      'Zamkniecie miesiaca']
        add_menu_elements(fileMenu, files_menu)


        menubar.add_cascade(label="Magazyny", underline=0, menu=magMenu)

        mags_menu = ['Kartoteki magazynowe', 'Bilans otwarcia', 'Inwentaryzacja', 'Dokumenty magazynowe']
        mags_menu_opts = {'Dokumenty magazynowe': {'menu': magmenu2}}
        add_menu_elements(magMenu, mags_menu, mags_menu_opts)

        magmenu2.add_command(label='wg dokumentow')
        magmenu2.add_command(label='wg indeksow')
        magmenu2.add_command(label='wg grup materialowych i indeksow')



        menubar.add_cascade(label="Slowniki", underline=0, menu=slowMenu)
        slow_menu = ['Indeksy materialowe','Kartoteka kontrahentow', 'Jednostki firmy','Jednostki miary','Magazyny','Dokumenty magazynowe']
        add_menu_elements(slowMenu, slow_menu)



        menubar.add_cascade(label="Pomoc", underline=0, menu=helpMenu)
        help_menu = ['O programie', 'Instrukcja obsugi']
        add_menu_elements(helpMenu, help_menu)


        fileMenu.add_separator()
        fileMenu.add_command(label="Wyjscie", underline=0, command=self.onExit)

    def onExit(self):
        self.quit()




def add_menu_elements(menu, elements, opts=None):
    opts = opts or {}
    for el in elements:
        menu.add_cascade(label=el, **opts.get(el, {}))







if __name__ == '__main__':
    main()