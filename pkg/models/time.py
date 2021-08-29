import re

second_regex = "[0-5][0-9].[0-9]{3}"
minute_regex = "[0-9]{1,2}'[0-5][0-9].[0-9]{3}"


def parse(time):
    if re.match(second_regex, time):
        s, ms = time.split(".")

        return Time(0, int(s), int(ms)), True

    if re.match(minute_regex, time):
        s, ms = time.split(".")
        m, s = s.split("'")

        return Time(int(m), int(s), int(ms)), True

    return Time(), False


class Time:
    def __init__(self, m=0, s=0, ms=0):
        self.m = m
        self.s = s
        self.ms = ms

    def __str__(self):
        time = f"{str(self.s).zfill(2)}.{str(self.ms).zfill(3)}"
        if self.m > 0:
            time = f"{str(self.m)}'" + time

        return time

    def __int__(self):
        return self.ms + 1000*(self.s + 60*self.m)

    def marshall_json(self):
        return {"time": str(self)}




