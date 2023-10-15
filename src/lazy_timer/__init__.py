""""""

__all__ = [
    "LazyTimer"
]

from datetime import datetime, timedelta


class LazyTimer(object):
    def __init__(self, *args, **kwargs):
        self.__delta = timedelta(*args, **kwargs)
        self._start_time = None
        self._end_time = None

    def start(self):
        self._start_time = datetime.utcnow()
        self._end_time = self._start_time + self.__delta

    def stop(self):
        return self.reset()

    @property
    def duration(self):
        return self.__delta

    @property
    def seconds(self):
        return self.__delta.total_seconds()

    @property
    def end_time(self):
        return self._end_time

    @property
    def finished(self):
        return datetime.utcnow() > self._end_time

    @property
    def left_time(self):
        if self.finished:
            return timedelta()
        return self._end_time - datetime.utcnow()

    @property
    def active(self):
        return self._start_time and self._end_time and not self.finished

    def reset(self):
        self._end_time = None
        self._start_time = None

    def restart(self):
        return self.start()

    def set_delta(self, *args, **kwargs):
        self.__delta = timedelta(*args, **kwargs)

    def __str__(self):
        return f"{self.active} | {self.duration}"
