import os
import sys
import sqlite3
path = os.path.join(sys.path[0], 'Speller/russian.txt')
path_base = os.path.join(sys.path[0], 'static/Base/Base.db')

connect = sqlite3.connect(path_base)
cursor = connect.cursor()


def qyery(sql):
    for sql_item in sql:
        cursor.execute(sql_item)


    # cursor.execute("DELETE from SPELLER")
    connect.commit()
    print('good')


with open(path, encoding='windows-1251') as file:
    array = []
    for i , items in enumerate(file.readlines()):
        _items = items.replace("\n", "")
        sql_text = "INSERT INTO Speller (Name) VALUES ('{}')".format(_items.replace("'", "").replace('"', "").title())
        array.append(sql_text)


qyery(array)






