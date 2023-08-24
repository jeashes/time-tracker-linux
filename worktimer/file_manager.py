class FileManager:
    def __init__(self):
        self.__filename = 'tracking apps.txt'
    
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, new_name: str) -> None:
        self.__filename = new_name 

    def create_file(self, app_names) -> None:
        with open(self.__filename, 'w', encoding='utf-8') as file:
            for name in app_names:
                file.write(name + '\n')

    def read_file(self) -> list:
        with open(self.__filename, 'r', encoding='utf-8') as file:
            content = file.read().splitlines()
            return content
