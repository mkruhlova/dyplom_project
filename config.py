DEV = True

DEFAULT_LOGIN = "admin"
DEFAULT_PASSWORD = "123"

APP_TITLE = "MagazynPro"
LOGIN_TITLE = "MagazynProLogin"

db_cnf = dict(
    host="localhost", port=3306, user="root", passwd="root", db="system_magazynowy"
)

date_entry_cnf = dict(
    width=12,
    background="darkblue",
    locale="pl",
    foreground="white",
    borderwidth=2,
    year=2019,
)

tables_cnf = dict(cell_font="Helvetica 12", header_font="Helvetica 12 italic")

datetime_format = "%Y-%m-%d"
