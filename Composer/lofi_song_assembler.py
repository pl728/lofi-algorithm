import os
import random

import Composer.wave_manager as wave_manager
from Composer.lofi_chord_generator import LofiChordGenerator


class LofiSongAssembler:
    current_song: int

    def __init__(self):
        self.current_song = 0

    def create_playlist(self, num_songs, num_chords):
        counter = 0
        for i in range(num_songs):
            counter += 1
            self.render_all_chords(num_chords)
            print(str(counter) + " out of " + str(num_songs))

    def render_all_chords(self, num_chords):
        lfg = self.start_lfg()
        counter = 0
        chord_files = ["c" + str(i) + ".wav" for i in range(num_chords)]
        song_files = ["vinyl-3s.wav"] + chord_files
        for i in range(num_chords):
            lfg.render_next()
            counter += 1
            print(str((counter / num_chords) * 100) + "%")
        # song_date = datetime.now()
        # song_file = "C:\\Users\\linpa\\github\\pl728.github.io\\media\\audio\\" \
        #             "song" + song_date.strftime("%m-%d-%Y--%H-%M-%S") + ".wav"
        song_file = "C:\\Users\\linpa\\github\\pl728.github.io\\media\\audio\\z\\" \
                    "z" + str(self.current_song) + ".wav"
        wave_manager.add_waves(song_files, "d.wav")
        wave_manager.add_silence("d.wav", song_file, 1)
        for file in chord_files:
            os.remove(file)
        os.remove("d.wav")

        self.current_song += 1

    @staticmethod
    def start_lfg() -> LofiChordGenerator:
        root = random.randint(39, 51)
        major = bool(random.getrandbits(1))
        return LofiChordGenerator(root=root, major_minor=major)
