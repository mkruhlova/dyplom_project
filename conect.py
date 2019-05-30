import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='system_magazynowy')


def create_cursor(func):
    def wrapper(**kwargs):
        cur = conn.cursor()
        result = func(cur, **kwargs)
        cur.close()
        return result

    return wrapper


@create_cursor
def insert_data(cur, ID, Nazwa_jednostki, Symbol):
    s = "INSERT INTO `slownik jednostki firmy`(`ID`,`Nazwa_jednostki`,`Symbol`) " \
        "VALUES ({},{},{})".format(ID, Nazwa_jednostki, Symbol)

    cur.execute(s)
    conn.commit()


@create_cursor
def insert_data_unit(cur, ID, Nazwa_jednostki, Symbol):
    s = "INSERT INTO `slownik jednostek miar`(`ID`,`Nazwa_jednostki`,`Symbol`) " \
        "VALUES ({},{},{})".format(ID, Nazwa_jednostki, Symbol)

    cur.execute(s)
    conn.commit()


@create_cursor
def get_kartoteka(cur):
    s = "SELECT * FROM `slownik jednostek miar`"
    cur.execute(s)

    return cur


@create_cursor
def get_kartoteka(cur):
    s = "SELECT * FROM `slownik jednostki firmy`"
    cur.execute(s)

    return cur

# cur.execute("SELECT * FROM system_magazynowy.`kartoteka indeksow materialowych`")
#
# print(cur.description)
# print()
#
# for row in cur:
#     print(row)
#
# cur.close()
# conn.close()
