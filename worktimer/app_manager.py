from psutil import process_iter
from subprocess import check_output

class AppManager:
    def __init__(self, soft_names: list):
        self.soft_names = soft_names

    def get_curr_process(self) -> list:
        process = process_iter(attrs=['name'])
        process_names = [proc.info['name'] for proc in process]
        
        return process_names
    
    def get_status_message(self) -> str:
        if len(self.soft_names) > 0:
            return f'{" ".join(self.soft_names)} are working'

        return f'All app(s) has been closed\n'

    def is_app_running(self) -> bool:
        curr_process = self.get_curr_process()

        for name in self.soft_names:
            if name not in curr_process:
                print(f'{name} has been closed')
                self.soft_names.remove(name)
            return True
        return False

    def is_startup(self) -> bool:
        process_names = self.get_curr_process()
        return all(list(map(lambda x: x in process_names, self.soft_names)))

def get_installed_software_linux() -> list:
    #result = check_output(['pacman', '-Qe'], universal_newlines=True)
    command = ["bash", "-c", "ls /usr/share/applications | awk -F '.desktop' '{print $1}'"]
    result = check_output(command, universal_newlines=True).strip().split('\n')
    installed_soft = ' '.join(result).lower()
    return installed_soft

def get_name() -> list:
    count_of_apps = int(input('Quantity of apps for track: '))
    installed, names = get_installed_software_linux(), []

    for _ in range(count_of_apps):
        name = input('Input name app: ')
        while (name in installed) != True:
            name = input('Please, input correct name app: ')

        names.append(name)
    return names
