from json import dump, load


class JSONHandler:
    def __init__(self, app_name: str):
        self.app_name = app_name

# for first start program
    def create_json(self, curr_year: int, curr_month: int, 
                    curr_week: int, curr_day: int) -> None:
    
        start_dict = {'total': 0.0, 
                      curr_year: {f'{curr_year}_total': 0.0,
                      curr_month: {f'{curr_month}_total': 0.0,
                                      f'{curr_month}_avg': 0.0, 
                      curr_week: {f"{curr_week}_avg": 0.0, 
                      curr_day: {f'{curr_day}_total': 0.0,}}}}}

        self.write_data_json(start_dict)
        print('json file is generated')


    def get_data_json(self) -> dict:
        with open(f'time-control/{self.app_name}.json', 'r') as read_file:
            data = load(read_file)
            return data


    def write_data_json(self, data: dict) -> None:
        with open(f'time-control/{self.app_name}.json', 'w') as write_file:
            dump(data, write_file)

