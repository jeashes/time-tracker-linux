from math import ceil
from datetime import datetime

def week_avg_calc(curr_week: dict) -> None:
    akeys_week = list(curr_week.keys())
    number_week = ceil(datetime.now().day / 7)
    count_days = len(akeys_week) - 1
    # adays - all days
    total_adays = list(map(lambda x: curr_week[x][f'{x}_total'], akeys_week[1:]))
    # int(x * 10) / 10.0 - formula for 0.f
    avg_week = int((sum(total_adays) / count_days) * 10) / 10.0
    curr_week[f'{number_week}_avg'] = avg_week 

def month_avg_calc(curr_month: dict) -> None:
    number_month = datetime.now().month
    total_month = curr_month[f'{number_month}_total']
    weeks_month = list(curr_month.keys())[2:]
    count_days = list(map(lambda x: len(list(curr_month[x].keys())[1:]), weeks_month))
    avg_month = total_month / sum(count_days)
    curr_month[f'{number_month}_avg'] = avg_month

