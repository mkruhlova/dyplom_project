# import mysql
# # import mysql.connector
# # from mysql.connector import Error
# #
# #
# # def connect():
# #     global conn
# #     try:
# #         conn = mysql.connector.connect(host='localhost',
# #                                        database='system_magazynowy',
# #                                        user='root',
# #                                        password='root')
# #         if conn.is_connected():
# #             print('Connected to MySQL database')
# #
# #     except Error as e:
# #         print(e)
# #
# #     finally:
# #         conn.close()
# #
# #
# # if __name__ == '__main__':
# #     connect()

import pymysql

# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='system_magazynowy')

cur = None #conn.cursor()
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