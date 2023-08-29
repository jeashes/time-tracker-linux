import time
from subprocess import run
from worktimer.file_manager import FileManager
from worktimer.time_manager import TimeManager
from worktimer.data_manager import DataManager
from worktimer.app_manager import (AppManager,
                                   get_name,
                                   get_installed_software_linux)

if __name__ == "__main__":
    file_manager = FileManager()
    try:
        apps_monitor = file_manager.read_file()
    except FileNotFoundError:
        app_names = get_name()
        file_manager.create_file(app_names)
        apps_monitor = file_manager.read_file()

    # second main part
    app_manager = AppManager(apps_monitor)
    # tmanager - time_manager
    apps_monitor = app_manager.soft_names
    tmanagers = [TimeManager(app) for app in apps_monitor]
    data_manager = DataManager(tmanagers)
    
    match len(app_manager.soft_names):
        case 0:
            print('Not a single program works')

        case _:
            data_manager.create_data()
            while app_manager.is_app_running():
                message = app_manager.get_status_message()
                print(message)
                data_manager.write_data()
                time.sleep(2)

            try:
                data_manager.write_sessions()
                [print(f'{k}: {v}min.') for k, v in data_manager.sessions.items()]
                apps_name = ' '.join(list(data_manager.sessions.keys()))
                apps_session = ' '.join(list(map(str, data_manager.sessions.values())))
                run(['python', 'time-control/main.py', apps_name, apps_session])
            except NameError:
                [print('App is closed'), print('Apps are closed')][len(apps_monitor) > 1]


