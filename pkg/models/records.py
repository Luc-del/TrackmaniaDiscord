from pkg.models import player
import pkg.models.map as vmap
from utils.json import marshall_json_dict


class Records:
    def __init__(self):
        self.__players = {}
        self.__by_map = {k: None for k in vmap.get_list()}

    def add_player(self, player_name):
        p = player.Player(player_name)
        self.__players[p.name] = p

    def add_pb(self, player_name, map_idx, time):
        if player_name not in self.__players.keys():
            self.add_player(player_name)
        is_pb = self.__players[player_name].pb(map_idx, time)
        is_server_record = self.pb_by_map(map_idx, player_name, time)
        return is_pb, is_server_record

    def pb_by_map(self, map_idx, player_name, time):
        if self.__by_map[map_idx] is None or self.__by_map[map_idx].beats(time):
            self.__by_map[map_idx] = Dual(player_name, time)
            return True
        return False

    def get_player_pb(self, map_idx, player_name):
        if player_name not in self.__players.keys():
            return None
        return self.__players[player_name].get_pb(map_idx)

    def get_server_record(self, map_idx):
        if self.__by_map[map_idx] is None:
            return None, None, False
        return self.__by_map[map_idx].player_name, self.__by_map[map_idx].time, True

    def player_exists(self, player_name):
        return player_name in self.__players.keys()

    def marshall_json(self):
        return {
            "players": marshall_json_dict(self.__players),
            "by_map": marshall_json_dict(self.__by_map)
        }


class Dual:
    def __init__(self, player_name=None, time=None):
        self.player_name = player_name
        self.time = time

    def beats(self, time):
        if self.time is None or int(time) < int(self.time):
            return True
        return False

    def marshall_json(self):
        if self.player_name is None:
            return

        return {
            "player_name": self.player_name,
            "time": self.time.marshall_json()
        }
