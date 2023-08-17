from re import findall
from datetime import datetime

def month_total_calc(curr_month: dict) -> None:
    number_month, total = datetime.now().month, 0.0
    weeks = list(curr_month.keys())[2:]

    for week in weeks:
        # adays - all days
        curr_week = curr_month[week]
        total += curr_week[f'{week}_avg'] * len(list(curr_week.keys())[1:])
    
    curr_month[f'{number_month}_total'] = total

def year_total_calc(curr_year: dict) -> None:
    number_year, akeys_year = datetime.now().year, list(curr_year.keys())[1:]
    total_months = list(map(lambda x: curr_year[x][f'{x}_total'], akeys_year))

    total_year = sum(total_months)
    curr_year[f'{number_year}_total'] = total_year

def data_total_calc(data: dict) -> None:
    akeys_data = list(data.keys())
    akeys_data.remove('total')
    total_year = list(map(lambda x: data[x][f'{x}_total'], akeys_data))
        
    total = sum(total_year)
    data['total'] = total

