import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='system_magazynowy')


def create_cursor(func):
    def wrapper(*args, **kwargs):
        cur = conn.cursor()
        result = func(cur, *args, **kwargs)
        conn.commit()
        cur.close()
        return result

    return wrapper


@create_cursor
def get_kartoteka(cur):
    s = "SELECT * FROM `slownik jednostki firmy`"
    cur.execute(s)

    return cur


@create_cursor
def insert_data(cur, ID, Nazwa_jednostki, Symbol):
    s = "INSERT INTO `slownik jednostki firmy`(`ID`,`Nazwa_jednostki`,`Symbol`) " \
        "VALUES ('{}','{}','{}')".format(ID, Nazwa_jednostki, Symbol)

    cur.execute(s)


@create_cursor
def delete_data(cur, index):
    s = "DELETE FROM `system_magazynowy`.`slownik jednostki firmy` WHERE (`ID` = '%s')" % index
    cur.execute(s)


@create_cursor
def insert_data_unit(cur, ID, Nazwa_jednostki, Symbol):
    s = "INSERT INTO `slownik jednostek miar`(`ID`,`Nazwa_jednostki`,`Symbol`) " \
        "VALUES ('{}','{}','{}')".format(ID, Nazwa_jednostki, Symbol)

    cur.execute(s)


@create_cursor
def get_kartoteka_unit(cur):
    s = "SELECT * FROM `slownik jednostek miar`"
    cur.execute(s)
    return cur


@create_cursor
def delete_data_unit(cur, index):
    s = "DELETE FROM `slownik jednostek miar` WHERE id=%s" % index
    cur.execute(s)


@create_cursor
def get_kartoteka_index(cur):
    s = "SELECT * FROM `kartoteka indeksow materialowych`"
    cur.execute(s)

    return cur


@create_cursor
def insert_data_index(cur, id, Nazwa_materialu, Jednostka_miary, Grupa_materialowa, Symbol):
    s = "INSERT INTO `kartoteka indeksow materialowych`(`ID`,`Nazwa_materialu`,`Jednostka_miary`,`Grupa_materialowa`, `Symbol`) VALUES ('{}','{}','{}','{}','{}')".format(
        id, Nazwa_materialu, Jednostka_miary, Grupa_materialowa, Symbol)
    cur.execute(s)


@create_cursor
def delete_data_index(cur, index: str):
    s = "DELETE FROM `kartoteka indeksow materialowych` WHERE id=%s" % index
    cur.execute(s)


@create_cursor
def select_units(cur):
    s = "SELECT `Nazwa_jednostki` FROM system_magazynowy.`slownik jednostek miar`"
    cur.execute(s)
    return cur
