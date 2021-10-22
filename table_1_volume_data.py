import pandas as pd
import matplotlib.pyplot as plt


def open_file(file_title):
    f = open(f'{file_title}', 'r', encoding = 'utf-8')
    file = f.readlines()

    table = []
    for row in file:
        row = row.replace('",', '+').replace(',"', '+')
        table.append(row.rstrip().split('+'))
    
    f.close()
    return table
 

def column_data(table):
    date = []
    link = []
    trafic = []
    date_time = []
    port = []

    column = [date, link, trafic, date_time, port]

    for row in table:
        for i in range(len(row)):
            if i >= len(column):
                break
            column[i].append(row[i]) 

    return column
    

def count_trafics(column):
    
    count = column[2]
    time = column[3]

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
        
    list_trafic = [number, datetime]
            
    return list_trafic


def mk_viz(column, count_trafic):    
    time = list(column[3])
    count = list(column[2])

    for_viz = count_trafic(count, time)
    viz = pd.DataFrame(for_viz,
        columns = ['Время', 'Количество трафика'])

    number = count_trafic[0]
    datime = count_trafic[1]

    viz.loc[number, datime].plot()
    plt.title('Распределение трафика за указанный период')
    plt.ylabel('Количество трафика')
    plt.xlabel('Время')
    plt.savefig('doc_for_send/data_14-10-2021.png')

