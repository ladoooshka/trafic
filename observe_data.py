import send_data as sd
import table_1_volume_data as tvd
import table_with_trafic_every_domen as ted
import os
import gzip
import datetime
import io

start_file = ['http_20-10-2021.gz', '.bash_logout', 'http_19-10-2021.gz', 'raw_19-10-2021.gz', 'raw_20-10-2021.gz', '.config', 'raw_2021-10-09', 'http_17-10-2021.gz', 'raw_17-10-2021.gz', '.python_history', '.gitconfig', 'raw_10-10-2021.gz', 'anaconda3', 'http_10-10-2021.gz', 'raw_2021-10-08.gz', 'http_18-10-2021.gz', '.profile', '.cache', 'raw_16-10-2021.gz', 'http_16-10-2021.gz', 'http_2021-10-08.gz', '.local', 'raw_15-10-2021.gz', '.sudo_as_admin_successful', 'http_11-10-2021', 'http_15-10-2021.gz', '.bash_history', 'http_2021-10-09.gz', 'trafic', '.bashrc', 'raw_18-10-2021.gz', '.git']

while 'dead' not in start_file:
    list_file_title = os.listdir()
    
    if start_file != list_file_title:
        
        need_file = list(set(list_file_title) - set(start_file))

        http_f = [name for name in need_file if 'http' in need_file]
        raw_f = [name for name in need_file if 'raw' in need_file]
       
        def gunzip(file): 
            file_mode = 'rb' 
            with gzip.open(http_f, file_mode) as input_file: 
                with io.TextIOWrapper(input_file, encoding='utf-8') as dec
            return dec
        
        http_file = gunzip(http_f)
        raw_file = gunzip(raw_f)

        start_file = list_file_title

        table = tvd.open_file(raw_file)
        column = tvd.column_data(table)
        count_trafic = tvd.count_trafics(column)
        mk_viz = tvd.mk_viz(column, count_trafic)

        table = tvd.open_file(http_file)
        domen = ted.take_domen_name_second_level(table)
        count_of_trafic = ted.count_of_trafic_for_domen(table, domen)
        procent_trafic = ted.procent_trafic(table, count_of_trafic)
        date = ted.date(table)
        mk_dict = ted.make_dict(domen, count_of_trafic, procent_trafic, date)
        mk_table = ted.mk_table(domen, count_of_trafic, procent_trafic, date)

        today = datetime.datetime.now()
        sd.send_email(today)


os.removedirs('dead')
