import os
import json
import pkg.models.records as records

backup_dir = "backup"
backup_file = "summer2021.json"


def __get_path():
    return os.path.join(backup_dir, backup_file)


def dump(r):
    with open(__get_path(), 'w') as f:
        json.dump(r.marshal_json(), f, indent=4)


def read():
    with open(__get_path(), 'r') as f:
        return records.Records.unmarshal_json(json.load(f))

