import player
import validators.map as vmap


class Records:
    def __init__(self):
        self.players = {}
        self.by_map = {k: Dual() for k in range(vmap.max_idx)}

    def add_player(self, player_name):
        p = player.Player(player_name)
        self.players[p.name] = p

    def add_pb(self, player_name, map_idx, time):
        if player_name not in self.players.keys():
            self.add_player(player_name)
        is_pb = self.players[player_name].pb(map_idx, time)
        is_server_record = self.pb_by_map(map_idx, player_name, time)
        return is_pb, is_server_record

    def pb_by_map(self, map_idx, player_name, time):
        if self.by_map[map_idx].is_better(time):
            self.by_map[map_idx] = Dual(player_name, time)
            return True
        return False

    def get_player_pb(self, map_idx, player_name):
        if player_name not in self.players.keys():
            return None
        return self.players[player_name].get_pb(map_idx)

    def get_server_record(self, map_idx):
        return self.by_map[map_idx].player_name, self.by_map[map_idx].time


class Dual:
    def __init__(self, player_name=None, time=None):
        self.player_name = player_name
        self.time = time

    def is_better(self, time):
        if self.time is None or int(time) < int(self.time):
            return True
        return False
