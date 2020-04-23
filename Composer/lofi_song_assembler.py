import os
import random

from datetime import datetime

import Composer.wave_manager as wave_manager
from Composer.lofi_chord_generator import LofiChordGenerator


class LofiSongAssember:
    current_song: int

    def __init__(self):
        self.current_song = 0

    def create_playlist(self, num_songs, num_chords):
        for i in range(num_songs):
            self.render_song(num_chords)

    def render_song(self, num_chords):
        lfg = self.create_random_lfg()
        chord_files = ["c" + str(i) + ".wav" for i in range(num_chords)]
        for i in range(num_chords):
            lfg.render_next()
        song_date = datetime.now()
        song_file = "C:\\Users\\linpa\\github\\pl728.github.io\\media\\audio\\" \
                    "song" + song_date.strftime("%m-%d-%Y--%H-%M-%S") + ".wav"
        wave_manager.add_waves(chord_files,
                               song_file)
        for file in chord_files:
            os.remove(file)

        self.current_song += 1

    @staticmethod
    def create_random_lfg() -> LofiChordGenerator:
        root = random.randint(33, 45)
        major = bool(random.getrandbits(1))
        return LofiChordGenerator(root, major)
