from psutil import process_iter
import time
from datetime import datetime

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
