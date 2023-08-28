import math
import sys
from datetime import datetime
from json_work import JSONHandler
from errorhandler import hke_datetime
from avgtotalcalc.total_calc import ( 
                        month_total_calc, 
                        year_total_calc,
                        data_total_calc
                        )
from avgtotalcalc.avg_calc import week_avg_calc, month_avg_calc


apps_name = sys.argv[1].split()
apps_session = list(map(float, sys.argv[2].split()))

apps_info = dict(zip(apps_name, apps_session))
json_handlers = [JSONHandler(name) for name in apps_info.keys()]

curr_year = datetime.now().year
curr_month = datetime.now().month
curr_day = datetime.now().day
curr_week = math.ceil(curr_day / 7)

for json_handler in json_handlers:
    try:
        data = json_handler.get_data_json()
    except FileNotFoundError:
        json_handler.create_json(curr_year, curr_month, curr_week, curr_day)
        data = json_handler.get_data_json()

    data = hke_datetime(data, curr_year, curr_month, curr_week, curr_day)
    app_name = json_handler.app_name
    session = apps_info[app_name]

    day_data = data[f'{curr_year}'][f'{curr_month}'][f'{curr_week}'][f'{curr_day}']
    week_data = data[f'{curr_year}'][f'{curr_month}'][f'{curr_week}']
    month_data = data[f'{curr_year}'][f'{curr_month}']
    year_data = data[f'{curr_year}']

    day_data[f'{curr_day}_total'] += abs(float(session))

    week_avg_calc(week_data)
    month_total_calc(month_data)
    month_avg_calc(month_data)
    year_total_calc(year_data)
    data_total_calc(data)

    json_handler.write_data_json(data)



