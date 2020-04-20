from typing import List

from Players.wave_player_loop import WavePlayerLoop


class AudioPlayer:
    players: List[WavePlayerLoop]

    def __init__(self, players: List[WavePlayerLoop]):
        self.players = []
        for player in players:
            self.players.append(player)

    def play(self, event):
        for player in self.players:
            player.play()

    def stop(self, event):
        for player in self.players:
            player.stop()
