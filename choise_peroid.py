from datetime import date
import datetime
import json

new_line = '\n'
period = int(input(f'За какой период нужны данные? {new_line} 1 - один день, {new_line} 2 - последняя неделя, {new_line} 3 - месяц, {new_line} 4 - полгода, {new_line} другое число - все время работы системы мониторинга трафика {new_line}'))

today = date.today()
#now = today.split('-')
yesterday = today - datetime.timedelta(days=30)
print(yesterday)

#with open('month.json') as json_file:
    #month_dict = json.load(json_file)

'''month_30day = ['09', '04', '06', '11']
month_31day = ['01', '03', '05', '07', '08', '10', '12']
february = '02'
 
def make_table(data, table):
    for row in data:
        table.append(row.rstrip().split(',')) #here i dont remembert why i had pasted this 

def make_period(now, num):

    def make_title_1(day_dict):
        week = (f'http_{day_dict['year']}-{day_dict['month']}-{day_dict['day']}_-_{day_dict['year']}-{day_dict['month']}-{int(day_dict['day'])-7}')
        return week 

    def make_title_2(day_dict, need_day, need_month):
        week = (f'http_{day_dict['year']}-{need_month}-{need_day}_-_{day_dict['year']}-{day_dict['month']}-{day_dict['day']}')
        return week 

    def preMonth(day_dict):
        pre_month = int(day_dict['month'])-1           
        if pre_month < 11 and pre_month > 1:
            pre_month += '0'     
        elif pre_month >= 11:
            pre_month = str(pre_month)
        return pre_month
        

    def calculation_day(count_day, int_day, day_dict):
        part_of_premonth = int_day - 7
        need_day = count_day + part_of_premonth
        pre_month = preMonth(day_dict)
        week = make_title_2(day_dict, need_day, pre_month)
        return week

    day_dict = {'year': now[0], 
        'month': now[1], 
        'day': now[-1]}
    if num == 1:
        title_file_http = str(f'http_{day_dict['year']}-{day_dict['month']}-{day_dict['day']}')
    
    elif num == 2 and int(day_dict['month']) != 1:
            

        if int(day_dict['day'].strip()) >= 7:
            titleFile = make_title_1(day_dict)

        if int(day_dict['day'].strip()) < 7 :
            int_day = int(day_dict['day'])

            if str(day_dict['month']) in month_30day and preMonth(day_dict) in month_31day :
                titleFile = calculation_day(31, int_day, day_dict)

            elif str(day_dict['month']) in month_30day and preMonth(day_dict) in month_30day :
                titleFile = calculation_day(30, int_day, day_dict)

            elif str(day_dict['month']) in month_30day and preMonth(day_dict) == february:
                titleFile = calculation_day(28, int_day, day_dict)

    elif num == 2 and int(day_dict['month']) == 1:'''

            





