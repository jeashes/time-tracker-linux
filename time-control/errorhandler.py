from addtime.add_ymwd import add_new_year, add_new_month, add_new_week, add_new_day

def hke_datetime(data: dict, curr_year: int, curr_month: int, 
                 curr_week: int, curr_day: int) -> dict:
    
    if data.get(f'{curr_year}') == None:
        add_new_year(data, curr_year)
    
    dk_year = data[f'{curr_year}']
    if dk_year.get(f'{curr_month}') == None:
        add_new_month(data, curr_year, curr_month)

    dk_month = data[f'{curr_year}'][f'{curr_month}']
    if dk_month.get(f'{curr_week}') == None:
        add_new_week(data, curr_year, curr_month, curr_week)

    dk_week = data[f'{curr_year}'][f'{curr_month}'][f'{curr_week}']
    if dk_week.get(f'{curr_day}') == None:
        add_new_day(data, curr_year, curr_month, curr_week, curr_day) 

    return data
