import os
import json
import pkg.models.records as records

backup_dir = "backup"

season = "summer"
year = 2021


def get_path():
    path = os.path.join(backup_dir, f"{season}{year}.json")
    return path


def dump(r):
    with open(get_path(), 'w') as f:
        json.dump(r.marshal_json(), f, indent=4)


def read(path):
    if not os.path.isfile(path):
        return records.Records()
    with open(path, 'r') as f:
        return records.Records.unmarshal_json(json.load(f))

