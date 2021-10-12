#import pandas as pd
import math
import csv

file = open('http_12-10-2021', 'r', encoding = 'utf-8').readlines()

table = []
for row in file:
    table.append(row.split(','))

def column_data(table):
    date = []
    link = []
    trafic = []
    date_time = []
    port = []

    column = { 0: date,
        1: link,
        2: trafic,
        3: date_time, 
        4: port}

    for row in table:
        for i in range(len(row)):
            column.setdefault([i]).append(row[i]) #need to know, why do not [] and value

    return column

column = column_data(table)

date_dict_key = set(column[0])
date_time_dict_key = set(column[3])
port_dict_key = set(column[4])

def date_dict(dict_key, table):
    keys = list(dict_key)
    for i in range(len(keys)):
        row = []
        for part in table:
            if int(keys[i]) == int(table[i][-1]):
                row.append(table[i])
        date_dictionary = {keys[i]: row}

print(column[4])
    

#def clear_link(data):
