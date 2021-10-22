import datetime
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, Date, create_engine, make_session
from table_1_volume_data import open_file

#from sqlalchemy import create_engine, Column, MetaData, literal
from clickhouse_sqlalchemy import Table, make_session, get_declarative_base, types, engines

uri = 'clickhouse://default:tenderftp/home/v.maksimova'

engine = create_engine(uri)
session = make_session(engine)
metadata = MetaData(bind=engine)

http_table = Table('http_table', metadata,
	Column('ipdrDate', Date, default = datetime.today()),  
	Column('url', String(), nullable = False),
	Column('totalbytes', Integer(), nullable = False),  
	Column('requeststarttime', DateTime, nullable = False),  
	Column('srcport', Integer(), nullable = False),  
	Column('dstport', Integer(), nullable = False), 
	Column('srcip', String(), ForeignKey('ip_client.client_ip')),  
	Column('dstip', String(), nullable = False), 
	)

ip_contact = Table('ip_clients', metadata,
	Column('client_id', Integer(), primary_key = True),
	Column('client_ip', String(), nullable = False),
	Column('client_title', String(), nullable = False),
	)

raw_table = Table('raw_table', metadata,
	Column('ipdrDate', Date, default = datetime.today()),  
	Column('sni', String(), nullable = False),
	Column('totalbytes', Integer(), nullable = False),  
	Column('requeststarttime', DateTime, nullable = False),  
	Column('srcport', Integer(), nullable = False),  
	Column('dstport', Integer(), nullable = False), 
	Column('srcip', String(), ForeignKey('ip_client.client_ip')),  
	Column('dstip', String(), nullable = False), 
	)