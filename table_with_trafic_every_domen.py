import pandas as pd
import math
import numpy as np
import csv

list_data = open('/home/v.maksimova/raw_2021-10-09','r',  encoding = 'utf-8').readlines()

list_with_test_data = []
for row in list_data:
  m_row = row.split(',')
  list_with_test_data.append(m_row)
  print(m_row, row)

print(*list_data, 'all data without changes')
print(*list_with_test_data, 'clear data')

def take_domen_name_second_level(table):
  domen_name = []
  for row in table:
    link = row[1] 
    string = link.replace('/', '.')
    new_row = string.split('.')
    for i in range(len(new_row)):
      name_domen = ''
      if new_row[i] == 'com' or new_row[i] == 'ru':
        name_domen = new_row[i-1] + '.' + new_row[i]
        domen_name.append(name_domen)
        break
  domen = set(domen_name)
  domen_name = list(domen) 
  return domen_name

#domen = take_domen_name_second_level(list_with_test_data)
#print(domen)

def count_of_trafic_for_domen(data, domen):
  list_for_count = []
  for name_domen in domen:
    count_trafic = 0
    part_of_trafic = []
    for link in data:
      if name_domen in link[1]:
        count_trafic += link[-1]
    count_trafic /= (1024*3)
    part_of_trafic.append(name_domen)
    part_of_trafic.append(count_trafic)
    list_for_count.append(part_of_trafic)
  return list_for_count

#count_of_trafic = count_of_trafic_for_domen(list_with_test_data, domen)

def procent_trafic(data, list_for_count_trafic):
  summ_trafic = 0
  for i in range(len(data)):
   # print(data[i][-1], end = '')
    #summ_trafic += int(data[i][-1].strip())
 # summ_trafic /= (1024*3)
#  procent = []
  for i in range(len(list_for_count_trafic)):
   # domen_procent = str((list_for_count_trafic[i][1] / summ_trafic) * 100) + '%'
    #procent.append(domen_procent)
  return procent

#procent = procent_trafic(list_with_test_data, count_of_trafic)

def date(data):
  mounth = {'01': 'Январь',
	 '02': 'Февраль',
	 '03': 'Март',
	 '04': 'Апрель',
	 '05': 'Май',
	 '06': 'Июнь',
	 '07': 'Июль',
	 '08': 'Август',
	 '09': 'Сентябрь',
	 '10': 'Октябрь',
	 '11': 'Ноябрь',
	 '12': 'Декабрь'}
  key_mount = data[0][0].split('-')
  mount_data = mounth.value(str(key_mount[1])) + ' ' + str(key_mount[0])
  return mount_data

#mounth = date(list_with_test_data)

def make_dict(count_of_trafic, procent, mounth):
  len_table = len(count_of_trafic)
  number = [num for num in range(1, len_table+1)] 
  data_dict = {'Number': number,
      'Domen_name': [name[0] for name in count_of_trafic],
      'Trafic volume': [name[1] for name in count_of_trafic],
      'Procent': [prot for prot in procent],
      'Date': [mounth for i in range(len_table)]}  
  return data_dict

#table_for_csv = make_dict(count_of_trafic, procent, mounth)

#end_table = pd.DataFrame(table_for_csv,
      columns = ['', '', '', '', ''])

list_with_test_data.close()
