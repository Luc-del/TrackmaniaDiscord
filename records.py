import player


class Records:
    def __init__(self):
        self.players = {}

    def add_player(self, player_name):
        p = player.Player(player_name)
        self.players[p.name] = p

    def add_pb(self, player_name, map_idx, time):
        if player_name not in self.players.keys():
            self.add_player(player_name)
        return self.players[player_name].pb(map_idx, time)
