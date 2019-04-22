import openpyxl
import sys
import os
# import requests
# import json
from flask import Flask, render_template, redirect, request as re
import sqlite3
import asyncio

app = Flask(__name__)


# ---------------------------------- Читаем excel и записываем в исходный массив -----------------------------------

# @staticmethod функция может использоваться в не класса


def parse_array():
    path_db = os.path.join(sys.path[0], 'static/base/base.db')
    connect_db = sqlite3.connect(path_db)
    cursor = connect_db.cursor()
    cursor.execute('select Name from Speller')
    return cursor.fetchall()


class ReadExcel(object):
    def __init__(self):
        super(ReadExcel, self).__init__()

    @staticmethod
    def OpenFile():
        path_file = os.path.join(sys.path[0], "excel\асумтр.xlsx")
        read_file = openpyxl.load_workbook(path_file)
        sheetnames = read_file.sheetnames[0]
        read_file = read_file[sheetnames]
        max_row = read_file.max_row
        max_column = read_file.max_column
        array = []
        for i in range(max_row):
            array_temp = []
            for j in range(max_column):
                array_temp.append(str(read_file.cell(i + 1, j + 1).value))
            array.append(array_temp)
            del array_temp

        return array[1:]


class ParseJson(ReadExcel):
    def __init__(self):
        super(ParseJson, self).__init__()
        self.array = super().OpenFile()

    def make_array(self):
        slovar = {}

        for i, item in enumerate(self.array):
            slovar[item[0]] = []

        for key, Item in slovar.items():
            values = []
            for parse in self.array:
                if key == parse[0]:
                    values.append(parse[1:])
            slovar[key] = values
            del values

        return slovar

        #
        # request = requests.get(
        #     'https://speller.yandex.net/services/spellservice.json/checkText?text=={}'.format(values))
        # try:
        #     response_json = request.json()
        # except Exception.args:
        #     print(sys.path)
        # else:
        #     if response_json:
        #         parse_json = json.loads(response_json)
        #          print(parse_json)


# ----------------------------------------------------------------------------------------


# сверка с массиовом


class qeryStatsFileParse(object):

    def __init__(self, obshii_massiv = None):
        super(qeryStatsFileParse, self).__init__()
        self.obshii_massiv = str(array_items)
        for _item in slovarParse.values():
            _item = _item[0]
            string_find = str(_item[4] + " " + _item[6] + " " + _item[7] + " " + _item[8]).replace("-", " ").replace(",", "").split(" ")
            for val in string_find:
                if val == 'None' or val.find('id') > -1:
                    break
                index = self.obshii_massiv.find(str(val).lower())
                if index > -1:
                   # print("Найден", val)
                   pass
                else:
                    print("Не найден" , val)


    #
    # for key, _items in self.array.items():
    #     elements = _items[0]
    #     string_q = str(str(elements[4]) + " "
    #                    + str(elements[6]) + " "
    #                    + str(elements[7]) + " " +
    #                    str(elements[8])).split(" ")
    #     for values in string_q:
    #         try:
    #             cursor.execute("select a.Name  from Speller a  where a.Name = '{}'".format(values))
    #         except sqlite3.DatabaseError:
    #             print(sys.exc_info()[1])
    #         else:
    #             if cursor.fetchall():
    #                 print(cursor.fetchall())
    #

# ____________________________
# --- Обработчик Flask ----------------------------------------------
class Mass(object):
    def __init__(self):
        super(Mass, self).__init__()

    @staticmethod
    def Array_Parse():
        return ParseJson().make_array()


@app.route("/")
def index():
    if re.method == "GET":
        if re.args.get("start") == '1':
            massive = array_items
            qeryStatsFileParse(massive)
            return redirect('/')
        return render_template("index.html", slovar=slovarParse)


@app.route("/attribyte/<id>")
def attribyte(id=None):
    slovar = slovarParse[id][0]
    return render_template('attribyte.html', slovar=slovar)


# ----------------------------------------------------------------------

if __name__ == '__main__':
    slovarParse = Mass.Array_Parse()
    print("SLOVAR GOOD")
    array_items = parse_array()
    app.run(host="127.0.0.1", port=5000, debug=True)
