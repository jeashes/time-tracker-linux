
def add_new_year(data: dict, curr_year: int) -> None:

    data[f'{curr_year}'] = {f'{curr_year}_total': 0.0}
    
    print('new YEAR was added')

def add_new_month(data: dict, curr_year: int, 
                    curr_month: int) -> None:
    # dk - data key
    dk_year = data[f'{curr_year}']
    dk_year[f'{curr_month}'] = {f'{curr_month}_total': 0.0, f'{curr_month}_avg': 0.0}

    print('new MONTH was added')

def add_new_week(data: dict, curr_year: int, 
                   curr_month: int, curr_week: int) -> None:

    dk_month = data[f'{curr_year}'][f'{curr_month}']

    dk_month[f'{curr_week}'] = {f'{curr_week}_avg': 0.0}
    
    print('new WEEK was added ')

def add_new_day(data: dict, curr_year: int, curr_month: int, 
                  curr_week: int, curr_day: int) -> None:

    dk_week = data[f'{curr_year}'][f'{curr_month}'][f'{curr_week}']

    dk_week[f'{curr_day}'] = {f'{curr_day}_total': 0.0}
    
    print('new DAY was added')
