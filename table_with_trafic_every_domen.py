import pandas as pd
import math
import numpy as np

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
	len_row = len(n_list[0])-1
	len_column = len(n_list)-1
	for row in range(len_row):
		every_column = []
		for colmn in range(len_column):
			every_column.append(n_list[colmn][row])
		column.append(every_column)
	return column

table = create_table(list_with_test_data)
pd_table = pd.DataFrame((table), column=['data', 'link', 'size'])

def take_domen_name_second_level(table):
	domen_name = []
	links = []
	for row in table:
		links.append(row[1])
	for row in links:
		part_of_link = row.split('.').split('/')
		len_part_of_link = len(part_of_link) - 1
		for num_blok in range(len_of_part_link):
			if part_of_link[num_blok] = 'com' or part_of_link[num_blok] = 'ru':
				name_domen = part_of_link[num_blok -1] +'.'+part_of_link[num_blok]
				break
		domen_name.append(name_domen)
	domen_clear = set(domen_name)
	domen = list(domen_clear)
	return domen

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
		part_of trafic.append(name_domen)
		part_of_trafic.append(round(count_trafic, 0))
		list_for_count.append(part_of_trafic)
	return list_for_count

count_of_trafic = count_of_trafic_for_domen(list_with_test_data, domen)

def procent_trafic(data, list_for_count_trafic):
	summ_trafic = 0
	for i in range(len(data)-1):
		summ_trafic += data[i][2]
	summ_trafic /= (1024*3)
	procent = []
	for i in range(len(list_for_count_trafic)-1):
		domen_procent = (list_for_count_trafic[i][1] / round(summ_trafic, 0) * 100
		procent.append(str(domen_procent) + '%')
	return procent

procent = procent_trafic(list_with_test_data, count_of_trafic)
pd.table_trafic_domen['№', 'domen_name', 'volume_of_data', 'data_procent'] = [i for i in range(1, len(procent)+1)], count_of_trafic[0], count_of_trafic[1], procent


