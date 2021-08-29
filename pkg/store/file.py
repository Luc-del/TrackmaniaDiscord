import json

import pkg.models.records as records

backup_dir = "backup"
backup_file = "backup.json"


def dump(r):
    with open(backup_file, 'w') as f:
        j = json.dumps(r.marshall_json(), indent=4)
        print(j)
        # json.dump(j, f, indent=4)


def read():
    with open(backup_file, 'r') as f:
        return json.load(f, object_hook=records.Records.unmarshall_json)

