import pandas as pd
import matplotlib as mtpl
import seaborn as sb
import math

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
	for row in range(len(n_list)-1):
		every_column = []
		for colmn in range(len(n_list[row])-1):
			every_column.append(n_list[column][row])
		column.append(every_column)
	return column


