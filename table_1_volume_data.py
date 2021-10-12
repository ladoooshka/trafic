#import pandas as pd
import math
import csv

file = open('http_12-10-2021', 'r', encoding = 'utf-8').readlines()

table = []
for row in file:
    table.append(row.rstrip().split('",'))

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
            column[i].append(row[i]) #need to know, why do not [] and value

    return column
    
column = column_data(table)

date_dict_key = set(column[0])
date_time_dict_key = set(column[3])
port_dict_key = set(column[4])

def make_dict(dict_key, table, num):
    keys = list(dict_key)
    date_dictionary = {}
    for i in range(len(keys)):
        row = []
        for part in table:
            if keys[i] == part[num]:
                row.append(part)
        date_dictionary.update([keys[i], row])
    return date_dictionary
    
date_dict = make_dict(date_dict_key, table, 0)
date_time_dict = make_dict(date_time_dict_key, table, 3)
port_dict = make_dict(port_dict_key, table, 4)

print(port_dict)
#def clear_link(data):
