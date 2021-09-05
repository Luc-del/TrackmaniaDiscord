import pkg.models.time as time
from utils.json import marshal_json_dict


class Player:
    def __init__(self):
        self.pbs = {}

    def register_time(self, map_idx, t):
        current_pb = self.get_pb(map_idx)
        if current_pb is None or t < current_pb:
            self.pbs[map_idx] = t
            return True
        return False

    def get_pb(self, map_idx):
        return self.pbs.get(map_idx, None)

    def delete_pb(self, map_idx):
        return self.pbs.pop(map_idx)

    def marshal_json(self):
        return self.pbs

    @staticmethod
    def unmarshal_json(data):
        p = Player()
        p.pbs = time.Time.unmarshal_json(data["pbs"])
        return p
