import pandas as pd
import math
import numpy as np
import csv

list_with_test_data = [["2021-09-01","ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/pinrulesstl.cab?b10ce11509a3e09c",429], 
["2021-09-01","x1.c.lencr.org/",441],
["2021-09-01","crl.identrust.com/DSTROOTCAX3CRL.crl",446], 
["2021-09-01","web.redhelper.ru/rc/status/661320?timeShift=-180&callback=jQuery112405109243876311269_1630069004680&_=1630069010923",1346],
["2021-09-14","v10.events.data.microsoft.com",5349],
["2021-09-14","config.edge.skype.com",8011],
["2021-09-14","www.bing.com",9634],
["2021-09-14","array509.prod.do.dsp.mp.microsoft.com",3699]]

def create_table(n_list):
  column = []
  len_row = len(n_list[0])
  len_column = len(n_list)
  for row in range(len_row):
    every_column = []
    for colmn in range(len_column):
      every_column.append(n_list[colmn][row])
    column.append(every_column)
  return column

table = create_table(list_with_test_data)

def take_domen_name_second_level(table):
  domen_name = []
  for row in table[1]:
    string = row.replace('/', '.')
    new_row = string.split('.')
    for i in range(len(new_row)):
      name_domen = ''
      if new_row[i] == 'com' or new_row[i] == 'ru':
        name_domen = new_row[i-1] + '.' + new_row[i]
        domen_name.append(name_domen)
        break
  return domen_name

domen = take_domen_name_second_level(table)

def count_of_trafic_for_domen(data, domen):
  list_for_count = []
  for name_domen in domen:
    count_trafic = 0
    part_of_trafic = []
    for link in data:
      if name_domen in link[1]:
        count_trafic += link[2]
    count_trafic /= (1024*3)
    part_of_trafic.append(name_domen)
    part_of_trafic.append(count_trafic)
    list_for_count.append(part_of_trafic)
  return list_for_count

count_of_trafic = count_of_trafic_for_domen(list_with_test_data, domen)

def procent_trafic(data, list_for_count_trafic):
  summ_trafic = 0
  for i in range(len(data)):
    summ_trafic += data[i][2]
  summ_trafic /= (1024*3)
  procent = []
  for i in range(len(list_for_count_trafic)):
    domen_procent = str((list_for_count_trafic[i][1] / summ_trafic) * 100) + '%'
    procent.append(domen_procent)
  return procent

procent = procent_trafic(list_with_test_data, count_of_trafic)

#all of this columns need union each other to row and then will make csv for dbeaver

def make_table(count_of_trafic, procent, data):
  table = []
  len_table = len(data)
  number = 1 
  for i in range(len_table):
    row = []
    row.append(str(number) + '.')
    row.append(count_of_trafic[i][0])
    row.append(count_of_trafic[i][1])
    row.append(procent[i])
    row.append(data[i][0]) #here wrong calculation date 
    number += 1
    table.append(row)
  return table

table_for_csv = make_table(count_of_trafic, procent, data)

witn open('Распределение_трафика_по_доменным_именам_второго_уровня.csv', mode = 'w', endcoding = 'utf-8') as w_file:
  file_writer = csv.writer(w_file, delimer = ',', letrminator = '\r\n')
  file_writer.writerow('№', 'Наименование домена второго уровня', 'Объем данных (трафика), Гбайт', 'Использование от общего объема данных на канале (по убыванию), %', 'Период измерения показателя: месяц/год')
  for i in range(len(table_for_csv)):
    file_writer.writerow(table_for_csv[i])

file_writer.close()
#here can doesnt work convertion file. Need testing 
