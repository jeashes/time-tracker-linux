from psutil import process_iter
from subprocess import check_output

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
