from pkg.models import player
import pkg.models.time as time
from utils.json import marshal_json_dict, unmarshal_json_dict


class Records:
    def __init__(self):
        self.__players = {}

    def add_player(self, player_name):
        self.__players[player_name] = player.Player()

    def register_player_time(self, player_name, map_idx, t):
        if player_name not in self.__players.keys():
            self.add_player(player_name)
        return self.__players[player_name].register_time(map_idx, t)

    def get_player_pb(self, player_name, map_idx):
        if player_name not in self.__players.keys():
            return None
        return self.__players[player_name].get_pb(map_idx)

    def delete_player_pb(self, player_name, map_idx):
        return self.__players[player_name].delete_pb(map_idx)

    def get_server_record(self, map_idx):
        best_player_name, best_player_time = None, None
        for player_name in self.__players.keys():
            player_time = self.__players[player_name].get_pb(map_idx)
            if player_time is not None:
                if best_player_name is None or best_player_time > player_time:
                    best_player_name, best_player_time = player_name, player_time

        return best_player_name, best_player_time

    def player_exists(self, player_name):
        return player_name in self.__players.keys()

    def marshal_json(self):
        return {
            "players": marshal_json_dict(self.__players),
        }

