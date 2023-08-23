import time
from subprocess import run
from worktimer.time_manager import TimeManager
from worktimer.data_manager import DataManager
from worktimer.app_manager import (AppManager,
                                   get_name,
                                   get_installed_software_linux)

if __name__ == "__main__":
    apps_monitor = get_name()
    app_manager = AppManager(apps_monitor)
    # tmanager - time_manager
    tmanagers = [TimeManager(app) for app in apps_monitor]
    data_manager = DataManager(tmanagers)

    if app_manager.is_startup():
        data_manager.create_data()
        
        while app_manager.is_app_running():
            message = app_manager.get_status_message()
            print(message)
            data_manager.write_data()
            time.sleep(2) 
    
    try:
        data_manager.write_sessions()
        [print(f'{k}: {v}min.') for k, v in data_manager.sessions.items()]
        #run(['python', 'time-control/main.py', f'{sessions}'])

    except NameError:
        [print('App is closed'), print('Apps are closed')][len(apps_monitor) > 1]
    

