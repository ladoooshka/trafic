import os
import gzip
import io
from sqlalchemy import insert, MetaData, Table, create_engine, make_session
from table_1_volume_data import open_file
from make_table import http_table, raw_table

uri = 'clickhouse://default:tenderftp/home/v.maksimova'

engine = create_engine(uri)
session = make_session(engine)
metadata = MetaData(bind=engine)

start_file = []
list_file_title = os.listdir('/home/v.maksimova')

def gunzip(file): 
		file_mode = 'rb' 
		with gzip.open(file, file_mode) as input_file: 
			with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
				return dec

def make_sqltable(file):
	table = open_file(file)
	for i in range(len(table)):
		if 'http' in file:
			http_table.insert().values(
			ipdrDate = table[i][0],
			url = table[i][1],
			totalbytes = table[i][2],
			requeststarttime = table[i][3],
			srcport = table[i][4],
			dstport = table[i][5],
			srcip = table[i][6],
			dstip = table[i][7],
			)
		elif 'raw' in file:
			raw_table.insert().values(
			ipdrDate = table[i][0],
			sni = table[i][1],
			totalbytes = table[i][2],
			requeststarttime = table[i][3],
			srcport = table[i][4],
			dstport = table[i][5],
			srcip = table[i][6],
			dstip = table[i][7],
			)

if start_file != list_file_title:        
	need_file = list(set(list_file_title) - set(start_file))
	http_f = [name for name in need_file if 'http' in need_file]
	raw_f = [name for name in need_file if 'raw' in need_file]

	http_file = gunzip(http_f)
	raw_file = gunzip(raw_f)
				
	make_sqltable(http_file)
	make_sqltable(raw_file)		
	

	os.remove(f'/home/v.maksimova/{http_file}')
	os.remove(f'/home/v.maksimova/{raw_file}')
	os.remove(f'/home/v.maksimova/{http_f}')
	os.remove(f'/home/v.maksimova/{raw_f}')

