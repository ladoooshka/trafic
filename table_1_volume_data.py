import pandas as pd
import math
import csv
import seaborn as sbn
import matplotlib.pyplot as plt
import matplotlib as mpl


file = open('http_14-10-2021', 'r', encoding = 'utf-8').readlines()

table = []
for row in file:
    row = row.replace('",', '+').replace(',"', '+')
    table.append(row.rstrip().split('+'))

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

def replace_trafic_volume(column):
    
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
    all_dict = [date_dict, date_time_dict, port_dict]

    return all_dict

def count_trafics(count, time):

    all_trafic = []
    summ_insecond = [count[0]]
    
    for num in range(1, len(time)):
        if time[num-1] == time[num]:
            summ_insecond.append(count[num])
        else:
            part = [time[num-1], sum(summ_insecond)]
            all_trafic.append[part]
            summ_insecond = []
            
    number = []
    datetime = []
    for row in all_trafic:
        number.append(row[0])
        datetime.append(row[-1])
        
    dict_trafic = {'number': number, 'datetime': datetime}
            
    return dict_trafic
            
    
time = list(column[3])
count = list(column[2])

for_viz = count_trafic(count, time)
viz = pd.DataFrame(for_viz,
    columns = ['Время', 'Количество трафика'])

viz.loc[number, datetime].plot()
plt.title('Распределение трафика за указанный период')
plt.ylabel('Количество трафика')
plt.xlabel('Время')
plt.savefig('doc_for_send/data_14-10-2021.png')

#def clear_link(data):

