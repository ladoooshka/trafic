import math
import csv

#here will be file with trafic data 

list_with_test_data = [["2021-09-01","ctldl.windowsupdate.com/msdownload/update/v3/static/trustedr/en/pinrulesstl.cab?b10ce11509a3e09c",429], 
["2021-09-01","x1.c.lencr.org/",441],
["2021-09-01","crl.identrust.com/DSTROOTCAX3CRL.crl",446], 
["2021-09-01","web.redhelper.ru/rc/status/661320?timeShift=-180&callback=jQuery112405109243876311269_1630069004680&_=1630069010923",1346],
["2021-09-14","v10.events.data.microsoft.com",5349],
["2021-09-14","config.edge.skype.com",8011],
["2021-09-14","www.bing.com",9634],
["2021-09-14","array509.prod.do.dsp.mp.microsoft.com",3699]]

def part_of_data(list_with_test_data):
  need_data = []
  mounth_year = list_with_test_data[0][0].split('-') 
  for i in range(len(list_with_test_data)):
    date = list_with_test_data[i][0].split('-')
    if date[:2] == mounth_year[:2]:
      need_data.append(list_with_test_data[i])
  return need_data

data = part_of_data(list_with_test_data)

def trafic_volume(data):
  len_data = len(data)
  trafic_count = 0
  for i in range(len_data):
    trafic_count += data[i][-1]
  trafic = trafic_count / (1024*3)
  return trafic

trafic = trafic_volum(data)

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

mount_year = date(data)

#To get enumiration of mounth year. To make table with year data. Mb to expand to general function with create table.
