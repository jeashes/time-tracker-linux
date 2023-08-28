
class DataManager:
    def __init__(self, tmanagers: list):
        self.tmanagers = tmanagers
        self.data_app_time = dict()
        self.sessions = dict()

    def create_data(self) -> None:
        for tmngr in self.tmanagers:
            self.data_app_time[tmngr.app_monitor] = {'start': tmngr.get_create_time()}

    def write_data(self) -> None:
        for tmngr in self.tmanagers:
            self.data_app_time[tmngr.app_monitor]['end'] = tmngr.get_end_time()

    def write_sessions(self) -> None:
        for tmngr in self.tmanagers:
            self.sessions[tmngr.app_monitor] = tmngr.get_session(
                                                self.data_app_time[tmngr.app_monitor]['start'],
                                                self.data_app_time[tmngr.app_monitor]['end']
                                                )
