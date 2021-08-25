class Player:
    def __init__(self, name):
        self.name = name
        self.pbs = [float("inf")]*25

    def pb(self, map_idx, time):
        if time < self.pbs[map_idx]:
            self.pbs[map_idx] = time
            return True, time
        return False, self.pbs[map_idx]

