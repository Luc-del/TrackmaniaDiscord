import re

second_regex = "[0-5][0-9].[0-9]{3}"
minute_regex = "[0-9]{1,2}'[0-5][0-9].[0-9]{3}"


def parse(time):
    if re.match(second_regex, time):
        s, ms = time.split(".")

        return to_int(0, int(s), int(ms))

    if re.match(minute_regex, time):
        s, ms = time.split(".")
        m, s = s.split("'")

        return to_int(int(m), int(s), int(ms))

    return None


def to_int(m, s, ms):
    return ms + 1000 * (s + 60 * m)


def from_int(time):
    ms = time % 1000
    time //= 1000

    s = time % 60
    time //= 60

    return time, s, ms


def to_string(time):
    if time is None:
        return None

    m, s, ms = from_int(time)

    time = f"{str(s).zfill(2)}.{str(ms).zfill(3)}"
    if m > 0:
        time = f"{str(m)}'" + time

    return time
