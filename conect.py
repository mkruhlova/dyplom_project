import pymysql

conn = pymysql.connect(
    host="localhost", port=3306, user="root", passwd="root", db="system_magazynowy"
)


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
def insert_data(cur, id, nazwa_jednostki, symbol):
    s = (
        "INSERT INTO `slownik jednostki firmy`(`ID`,`Nazwa_jednostki`,`Symbol`) "
        "VALUES ('{}','{}','{}')".format(id, nazwa_jednostki, symbol)
    )

    cur.execute(s)


@create_cursor
def delete_data(cur, index):
    s = (
        "DELETE FROM `system_magazynowy`.`slownik jednostki firmy` WHERE (`ID` = '%s')"
        % index
    )
    cur.execute(s)


@create_cursor
def insert_data_unit(cur, id, nazwa_jednostki, symbol):
    s = (
        "INSERT INTO `slownik jednostek miar`(`ID`,`Nazwa_jednostki`,`Symbol`) "
        "VALUES ('{}','{}','{}')".format(id, nazwa_jednostki, symbol)
    )

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
def insert_data_index(
    cur, id, nazwa_materialu, jednostka_miary, grupa_materialowa, symbol
):
    s = "INSERT INTO `kartoteka indeksow materialowych`(`ID`,`Nazwa_materialu`,`Jednostka_miary`,`Grupa_materialowa`, `Symbol`) VALUES ('{}','{}','{}','{}','{}')".format(
        id, nazwa_materialu, jednostka_miary, grupa_materialowa, symbol
    )
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


@create_cursor
def select_materials(cur):
    s = "SELECT `Nazwa_grupy` FROM system_magazynowy.`słownik grup materialowych`"
    cur.execute(s)
    return cur


@create_cursor
def get_kartoteka_agent(cur):
    s = "SELECT * FROM system_magazynowy.`kartoteka kontrahentow`"
    cur.execute(s)
    return cur


@create_cursor
def select_agent(cur):
    s = "SELECT `Nazwa_kontrahenta` FROM system_magazynowy.`kartoteka kontrahentow`"
    cur.execute(s)
    return cur


@create_cursor
def insert_data_agent(
    cur, id, nazwa_kontrahenta, adres_kontrahenta, symbol_kontrahenta
):
    s = (
        "INSERT INTO `kartoteka kontrahentow`(`ID`,`Nazwa_kontrahenta`,`Adres_kontrahenta`,`Symbol_kontrahenta`) "
        "VALUES ('{}','{}','{}','{}')".format(
            id, nazwa_kontrahenta, adres_kontrahenta, symbol_kontrahenta
        )
    )
    cur.execute(s)


@create_cursor
def delete_data_agent(cur, index: str):
    s = "DELETE FROM `kartoteka kontrahentow` WHERE id=%s" % index
    cur.execute(s)


@create_cursor
def get_kartoteka_storage(cur):
    s = "SELECT * FROM system_magazynowy.`slownik magazynow`"
    cur.execute(s)
    return cur


@create_cursor
def get_storage_names(cur):
    s = "SELECT `Nazwa_magazynu` FROM system_magazynowy.`slownik magazynow`"
    cur.execute(s)
    return cur


@create_cursor
def get_storage(cur):
    s = "SELECT * FROM `slownik magazynow`"
    cur.execute(s)

    return cur


@create_cursor
def insert_data_storage(
    cur,
    id,
    symbol_magazynu,
    nazwa_magazynu,
    data_otwarcia,
    status_inwentaryzacji,
    data_inwentaryzacji,
    symbol_placowki,
    id_dokumentu,
):
    s = (
        "INSERT INTO `slownik magazynow`(`ID`,`Symbol_magazynu`, `Nazwa_magazynu`, `Data_otwarcia`,"
        "`Status_inwentarizacji`, `Data_inwentarizacji`,"
        "`Symbol_placowki`,`ID_Dokumentu`)"
        "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
            id,
            symbol_magazynu,
            nazwa_magazynu,
            data_otwarcia,
            status_inwentaryzacji,
            data_inwentaryzacji,
            symbol_placowki,
            id_dokumentu,
        )
    )
    cur.execute(s)


@create_cursor
def delete_data_storage(cur, index: str):
    s = "DELETE FROM `slownik magazynow` WHERE id=%s" % index
    cur.execute(s)


@create_cursor
def select_symbols_for_storage(cur):
    s = "SELECT `Symbol` FROM system_magazynowy.`slownik jednostki firmy`"
    cur.execute(s)
    return cur


@create_cursor
def get_docs_pz(cur):
    s = "SELECT * FROM `slownik_dokumentow_magazynowych`"
    cur.execute(s)

    return cur


@create_cursor
def delete_doc(cur, index):
    s = (
        "DELETE FROM `system_magazynowy`.`slownik_dokumentow_magazynowych` WHERE (`Nr_Dok` = '%s')"
        % index
    )
    cur.execute(s)


@create_cursor
def insert_doc_unit(
    cur, nr_dok, kontrahent, data_dok, data_ksiegowania, wartosc, ilosc
):
    s = (
        "INSERT INTO `slownik_dokumentow_magazynowych`(`Nr_Dok`, `Data_Dok`, `Data_Ksiegowania`, `Wartosc`, "
        "`Ilosc`,`Kontrahent`) "
        "VALUES ('{}','{}','{}','{}','{}','{}')".format(
            nr_dok, kontrahent, data_dok, data_ksiegowania, wartosc, ilosc
        )
    )
    cur.execute(s)


@create_cursor
def select_comp_devision_in_income_doc(cur):
    s = "SELECT `Nazwa_jednostki` FROM system_magazynowy.`slownik jednostki firmy`"
    cur.execute(s)
    return cur


@create_cursor
def get_income_docs_rw(cur):
    s = "SELECT * FROM `slownik_dokumentow_magazynowych`"
    cur.execute(s)

    return cur


@create_cursor
def insert_income_doc(
    cur, nr_dok, kontrahent, data_dok, data_ksiegowania, wartosc, ilosc
):
    s = (
        "INSERT INTO `slownik_dokumentow_magazynowych`(`Nr_Dok`,`Kontrahent`,  `Data_Dok`, `Data_Ksiegowania`,"
        " `Wartosc`, `Ilosc`)"
        "VALUES ('{}','{}','{}','{}','{}','{}')".format(
            nr_dok, kontrahent, data_dok, data_ksiegowania, wartosc, ilosc
        )
    )

    cur.execute(s)


@create_cursor
def delete_income_doc(cur, index):
    s = (
        "DELETE FROM `system_magazynowy`.`slownik_dokumentow_magazynowych` WHERE (`Nr_Dok` = '%s')"
        % index
    )
    cur.execute(s)


@create_cursor
def get_storage_records(cur):
    s = "SELECT * FROM `kartoteka magazynu`"
    cur.execute(s)

    return cur


@create_cursor
def get_kartoteka_unit_for_storage(cur):
    s = "SELECT `Nazwa_jednostki` FROM system_magazynowy.`slownik jednostek miar`"
    cur.execute(s)
    return cur


@create_cursor
def select_warehouse_records(cur):
    s = "SELECT * FROM system_magazynowy.`kartoteka magazynu`"
    cur.execute(s)
    return cur


@create_cursor
def insert_warehouse_records(
    cur, index, nazwa, jednostka_miary, ilosc, cena, wartosc, grupa_materialowa
):
    s = (
        "INSERT INTO `slownik_dokumentow_magazynowych`(`Index`, `Nazwa`, `Jednostka miary`, "
        "`Ilosc`, `Cena`, `Wartosc`, `Grupa materialowa`)"
        "VALUES ('{}','{}','{}','{}','{}','{}')".format(
            index, nazwa, jednostka_miary, ilosc, cena, wartosc, grupa_materialowa
        )
    )

    cur.execute(s)


@create_cursor
def delete_warechouse_records(cur, index):
    s = (
        "DELETE FROM `system_magazynowy`.`kartoteka magazynu` WHERE (`Index` = '%s')"
        % index
    )
    cur.execute(s)


@create_cursor
def get_kartoteka_unit_for_bilance(cur):
    s = "SELECT `Nazwa_jednostki` FROM system_magazynowy.`slownik jednostek miar`"
    cur.execute(s)
    return cur


@create_cursor
def select_opening_balance(cur):
    s = "SELECT * FROM system_magazynowy.`bilans_otwarcia`"
    cur.execute(s)
    return cur


@create_cursor
def delete_data_bilans(cur, index):
    s = (
        "DELETE FROM `system_magazynowy`.`kartoteka magazynu` WHERE (`Index` = '%s')"
        % index
    )
    cur.execute(s)


@create_cursor
def insert_data_bilans(cur, index, lp, nazwa, jednostka_miary, ilosc, cena, wartosc):
    s = (
        "INSERT INTO `bilans_otwarcia`(`Index`, `Lp`, `Nazwa`, `Jednostka_miary`, `Ilosc`,`Cena`,`Wartosc`) "
        "VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(
            index, lp, nazwa, jednostka_miary, ilosc, cena, wartosc
        )
    )
    cur.execute(s)


@create_cursor
def get_bilance_otwarcia(cur):
    s = "SELECT * FROM `bilans_otwarcia`"
    cur.execute(s)
    return cur


@create_cursor
def get_group_material(cur):
    s = "SELECT * FROM `słownik grup materialowych`"
    cur.execute(s)

    return cur


@create_cursor
def get_group_materials(cur):
    s = "SELECT `Nazwa_GRUPY` FROM system_magazynowy.`slownik jednostki firmy`"
    cur.execute(s)
    return cur


@create_cursor
def insert_group_materials(cur, id, nazwa_grupy, symbol):
    s = (
        "INSERT INTO `słownik grup materialowych`(`ID`,`Nazwa_grupy`,`Symbol`) "
        "VALUES ('{}','{}','{}')".format(id, nazwa_grupy, symbol)
    )

    cur.execute(s)


@create_cursor
def delete_group_materials(cur, index):
    s = (
        "DELETE FROM `system_magazynowy`.`słownik grup materialowych` WHERE (`ID` = '%s')"
        % index
    )
    cur.execute(s)
