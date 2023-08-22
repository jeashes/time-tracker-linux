from psutil import process_iter
from subprocess import check_output

class AppManager:
    def __init__(self, soft_names: list):
        self.soft_names = soft_names

    def get_curr_process(self) -> list:
        process = process_iter(attrs=['name'])
        process_names = [proc.info['name'] for proc in process]
        
        return process_names

    def is_app_running(self) -> bool:
        curr_process = self.get_curr_process()

        for name in self.soft_names:
            if name not in curr_process:
                self.soft_names.remove(name)
                print(f'{name} has been closed')

            return True
        
        print('All apps has been closed')
        return False

    def is_startup(self) -> bool:
        process_names = self.get_curr_process()

        return all(list(map(lambda x: x in process_names, self.soft_names)))

def get_installed_software_linux() -> list:

    result = check_output(['pacman', '-Qe'], universal_newlines=True)
    result = result.strip().split('\n')

    installed_soft = [line.split()[0] for line in result]

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
