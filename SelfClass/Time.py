# -- coding: UTF-8 --
from __future__ import print_function, division


class Time:
    """
    Represents the time of day.

    attributed:hour, minute, second
    """

    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0


def print_time(t):
    """prints a string representation of the time.

    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def is_after(t1, t2):
    """Return True if t1 is after t2; False otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def add_time(t1, t2):
    """add two time objects

    :param t1, t2:Time
    :return:Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a time object satisfies the invariants

    :param time:
    :return: bollean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0 :
        return False
    if time.minute > 59 or time.second > 59:
        return False
    return True


def time_to_int(time):
    """Computes the number of seconds since midnight.

    :param time: Time object
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    """Makes a new time object

    :param seconds:int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# 修改器
def increment(time, seconds):
    """Adds seconds to a time object

    :param time:time
    :param seconds:int seconds
    """
    assert valid_time(time)
    seconds += time_to_int(time)
    return int_to_time(seconds)


def main():
    time = Time()
    time.hour = 11
    time.minute = 59
    time.second = 30
    print_time(time)
    time2 = Time()
    print(is_after(time, time2))
    print_time(add_time(time, time2))

if __name__ == '__main__':
    main()
