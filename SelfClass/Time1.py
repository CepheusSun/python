# -- coding: UTF-8 --
from __future__ import print_function, division


class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        :param hour: int
        :param minute: int
        :param second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    # 类似OC的 description 和 debugDescription 方法
    def __str__(self):
        """Returns a string representation of the time"""
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        """prints a string representation of the time.
        t: Time object
        """
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        secconds = self.minute * 60 + self.second
        return secconds

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 00
    start.print_time()

if __name__ == '__main__':
    main()
