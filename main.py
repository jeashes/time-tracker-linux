import time
from subprocess import run
from worktimer.time_manager import TimeManager
from worktimer.app_manager import (get_installed_software_linux,
                                   is_app_running,
                                   get_name)

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

