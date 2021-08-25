class Player:
    def __init__(self, name):
        self.name = name
        self.pbs = [None]*25

    def pb(self, map_idx, time):
        current_pb = self.pbs[map_idx]
        if current_pb is None or int(time) < int(current_pb):
            self.pbs[map_idx] = time
            return True, time
        return False, self.pbs[map_idx]
