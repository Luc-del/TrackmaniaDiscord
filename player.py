import validators.map as vmap


class Player:
    def __init__(self, name):
        self.name = name
        self.pbs = [None]*vmap.max_idx

    def pb(self, map_idx, time):
        current_pb = self.pbs[map_idx]
        if current_pb is None or int(time) < int(current_pb):
            self.pbs[map_idx] = time
            return True
        return False

    def get_pb(self, map_idx):
        return self.pbs[map_idx]
