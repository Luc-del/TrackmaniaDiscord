min_idx = 1
max_idx = 25


def validate(idx):
    idx = int(idx)
    if min_idx <= idx <= max_idx:
        return idx, True

    return -1, False


def get_list():
    return range(min_idx, max_idx + 1)


def validate_list(map_idx):
    validated = []
    for x in map_idx:
        idx, ok = validate(x)
        if ok:
            validated.append(idx)
    return sorted(set(validated))
