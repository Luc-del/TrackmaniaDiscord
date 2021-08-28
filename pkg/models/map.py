min_idx = 1
max_idx = 25


def parse(idx):
    idx = int(idx)
    if min_idx <= idx <= max_idx:
        return idx, True

    return -1, False


def get_list():
    return range(min_idx, max_idx + 1)
