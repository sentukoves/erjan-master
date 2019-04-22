from os import path as pa
import sys
import sqlite3






# def sql(text):
#     con = sqlite3.connect(pa.join(sys.path[0], 'static/Base/base.db'))
#     cur = con.cursor()
#     try:
#         for _items in text:
#             cur.execute(_items)
#         # cur.execute("""
#         # CREATE TABLE  Speller(
#     # ID int,
#     # Name varchar(255));
#      #    """)
#     except sqlite3.DatabaseError:
#         print(sys.exc_info())
#     else:
#         con.commit()
#         cur.close()
#         con.close()
#
#
# def eeee():
#     BaseTextFile_Path = pa.join(sys.path[0], 'Speller/russian.txt')
#     with open(BaseTextFile_Path, encoding='windows-1251') as russianas_text:
#
#         a  =[]
#         for i, items in enumerate(russianas_text.readlines()):
#             ite = str(items).replace("\n", "")
#             if ite.find("Генри") > -1:
#                 print(ite)
#             a.append("INSERT INTO Speller (ID, Name) VALUES ({},'{}')".format(i , ite.replace('"',"").replace("'", "")))
#         sql(a)
#
# eeee()