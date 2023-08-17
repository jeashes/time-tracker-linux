from psutil import process_iter
import time
from datetime import datetime
from subprocess import check_output, run

class TimeManager:
    def __init__(self, app_monitor: str):
        self.app_monitor = app_monitor
        self.pattern = "%d/%m/%Y %H:%M:%S"

    def get_create_time(self) -> str:

        started_times = []
        process = process_iter(attrs=['name', 'create_time'])

        for proc in process:

            if proc.info['name'] == self.app_monitor:

                create_time = proc.info['create_time']
                formatted_time = datetime.fromtimestamp(create_time)

                started_times.append(formatted_time)

        started = started_times[0].strftime(self.pattern)

        return started

    def get_end_time(self) -> str:

        curr_time = datetime.now()
        formatted_time = curr_time.strftime(self.pattern)

        return formatted_time

    def get_session(self, start: str, end: str) -> float:
        formatted_start = datetime.strptime(start, self.pattern)
        formatted_end = datetime.strptime(end, self.pattern)

        difference = formatted_end - formatted_start
        difference = (difference.total_seconds() / 3600) * 60

        return difference

def get_installed_software_linux() -> list:

    result = check_output(['pacman', '-Qe'], universal_newlines=True)
    result = result.strip().split('\n')

    installed_soft = [line.split()[0] for line in result]

    return installed_soft

def is_app_running(soft_name: str) -> bool:

    process = process_iter(attrs=['name'])

    for proc in process:

        if proc.info['name'] == soft_name:
            return True

    return False


def get_name() -> str:

    installed = get_installed_software_linux()
    name = input('Input name app: ')

    while (name in installed) != True:
        name = input('Please, input correct name app: ')

    return name



if __name__ == "__main__":
    app_monitor = get_name()
    # tmanager - time_manager
    tmanager = TimeManager(app_monitor)

    if is_app_running(app_monitor):
        data_app_time = {
                app_monitor: {'start': tmanager.get_create_time()}}

        while is_app_running(app_monitor):
            data_app_time[app_monitor]['end'] = tmanager.get_end_time()
            print(f'{app_monitor} is working')
            time.sleep(3) 
            
    try:
        session = tmanager.get_session(
                data_app_time[app_monitor]['start'],
                data_app_time[app_monitor]['end']
                )

        print(data_app_time[app_monitor]['start'])
        print(data_app_time[app_monitor]['end'])

        run(['python', 'time-control/main.py', f'{app_monitor}', f'{session}'])

    except NameError:
        print('App is closed')

