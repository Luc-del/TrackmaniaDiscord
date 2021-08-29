import pkg.models.map as vmap
from utils.json import marshall_json_dict


class Player:
    def __init__(self, name):
        self.name = name
        self.pbs = {k: None for k in vmap.get_list()}

    def pb(self, map_idx, time):
        current_pb = self.get_pb(map_idx)
        if current_pb is None or int(time) < int(current_pb):
            self.pbs[map_idx] = time
            return True
        return False

    def get_pb(self, map_idx):
        return self.pbs[map_idx]

    def marshall_json(self):
        return {
            "name": self.name,
            "pbs": marshall_json_dict(self.pbs)
        }
