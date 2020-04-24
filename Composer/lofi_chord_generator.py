import os
import random
from typing import List

import Composer.wave_manager as wave_manager
import Players.PySynth.pysynth_b as pss  # a, b, e, and s variants available
from MusicObjects.Chords.Sevenths.major_seventh import MajorSeventhChord
from MusicObjects.Chords.Sevenths.minor_seventh import MinorSeventhChord
from MusicObjects.Chords.chord import Chord


class LofiChordGenerator:
    """Generates lo-fi chord, audio"""

    current_chord: Chord
    tonic: Chord
    chord_number: int
    current_beat: int  # 0-3
    current_measure: int  # 0-3
    current_position: int  # 0-15

    def __init__(self, root: int, major_minor: bool):
        self.chord_scale = self.get_tonic_scale(root, major_minor)
        # self.chord_scale = self.chord_scale.insert_substitutons()
        self.major = major_minor
        self.chord_number = 0
        self.tonic = self.chord_scale[0]
        self.current_chord = self.tonic
        self.previous_chord = None

        self.current_beat = 0
        self.current_measure = 0
        self.current_position = 0
        self.gravity = 0  # 0-100, chance of going home
        # self.momentum = random.getrandbits(1)  # True/False, true - up, false - down

        self.note0, self.note1, self.note2, self.note3 = [], [], [], []

    def set_next_chord(self):
        """ todo: needs anti repetitiveness, i.e. a reset if things are too repetitive"""
        self.previous_chord = self.current_chord

        # excludes current chord
        home, tension = self.get_close_home(), self.get_close_tension()

        current_tension = self.current_chord in tension
        previous_tension = self.previous_chord in tension

        if self.current_beat == 3 and random.randint(0, 3) == 1:
            return

        # if current_tension:
        #     # want a higher chance to go home
        #     if random.randint(1, 100) > 25:
        #         self.current_chord = self.get_smooth_transitions(home)
        #     else:
        #         self.current_chord = self.get_smooth_transitions(tension)
        # else:
        #
        #     if random.randint(1, 100) > 50:
        #         self.current_chord = self.get_smooth_transitions(tension)
        #     else:
        #         self.current_chord = self.get_smooth_transitions(home)

        if self.current_beat == 0:
            self.current_chord = self.get_smooth_transitions(home)

        elif self.current_beat == 1:
            if random.randint(1, 100) < 80:
                self.current_chord = self.get_smooth_transitions(tension)
            else:
                self.current_chord = self.get_smooth_transitions(home)
        elif self.current_beat == 2:
            if random.randint(1, 100) < 50:
                self.current_chord = self.get_smooth_transitions(tension)
            else:
                self.current_chord = self.get_smooth_transitions(home)
        else:
            if random.randint(1, 100) < 20:
                return
            else:
                if random.randint(1, 100) < 20:
                    self.current_chord = self.get_smooth_transitions(tension)
                else:
                    self.current_chord = self.get_smooth_transitions(home)

        return self

    def render_next(self, bpm: int = 80):
        """chooses a chord and converts this chord to a wav file with one chord
        a-notes
        b-chord
        c-chord+drum
        """
        self.set_next_chord()
        chord_letters = self.current_chord.convert_to_letter()
        for elem in enumerate(chord_letters):
            pss.make_wav([(elem[1], 1)], fn="a" + str(elem[0]) + ".wav", bpm=bpm)
        note_files = ["a" + str(i) + ".wav" for i in range(4)]
        wave_manager.overlay_waves(note_files, 3000, self.chord_number)
        if self.chord_number > 3:
            wave_manager.overlay_background("b" + str(self.chord_number) + ".wav",
                                            ["lofi-drums-1-3s.wav", "vinyl-3s.wav"],
                                            self.chord_number)
        else:
            wave_manager.overlay_background("b" + str(self.chord_number) + ".wav",
                                            ["vinyl-3s.wav"],
                                            self.chord_number)

        os.remove("b" + str(self.chord_number) + '.wav')
        for i in range(4):
            os.remove("a" + str(i) + ".wav")
        self.update_beat_position()
        return self

    def update_beat_position(self):
        self.chord_number += 1
        if self.current_beat == 3:
            self.current_beat = 0
            self.current_measure += 1
        else:
            self.current_beat += 1

        self.current_position += 1

    def get_close_tension(self):
        """returns random close tension chord excluding current chord"""
        close_home = []
        for chord in self.get_close_chords():
            if chord in self.get_tension_chords():
                close_home.append(chord)
        return close_home

    def get_close_home(self):
        """returns random close home chord, excluding current chord"""
        close_home = []
        for chord in self.get_close_chords():
            if chord in self.get_home_chords():
                close_home.append(chord)
        return close_home

    def get_home_chords(self):
        """gets all chords that are considered to be a HOME chord,
                based on the scale generated by the current root"""
        home_chords = []
        if self.major:
            for i in range(len(self.chord_scale)):
                if i in [2, 3, 6, 9, 10]:
                    home_chords.append(self.chord_scale[i])
        else:
            for i in range(len(self.chord_scale)):
                if i in [0, 2, 5]:  # fix this later
                    home_chords.append(self.chord_scale[i])
        return home_chords

    def get_tension_chords(self):
        """gets all chords that are considered to be a TENSION chord,
        based on the scale generated by the current root"""
        tension_chords = []
        if self.major:
            for i in range(len(self.chord_scale)):
                if i in [0, 1, 4, 5, 7, 8, 11, 12]:  # can adjust later
                    tension_chords.append(self.chord_scale[i])
        else:
            for i in range(len(self.chord_scale)):
                if i in [1, 3, 4, 6]:  # todo: find real minor tensions
                    tension_chords.append(self.chord_scale[i])
        return tension_chords

    @staticmethod
    def get_tonic_scale(root: int, major: bool) -> List[Chord]:
        """Takes a root as the tonic root and returns all chords in its scale depending on
        major/minor.

        Works for homogeneous M7, m7 chord scales (without chord substitutions) """
        if major:
            return [
                MinorSeventhChord(root - 10),
                MinorSeventhChord(root - 8),
                MajorSeventhChord(root - 7),
                # MajorSeventhChord(root - 5),
                MinorSeventhChord(root - 3),
                # MinorSeventhChord(root - 1),

                MajorSeventhChord(root),

                MinorSeventhChord(root + 2),
                MinorSeventhChord(root + 4),
                MajorSeventhChord(root + 5),
                # MajorSeventhChord(root + 7),
                MinorSeventhChord(root + 9),
                # MinorSeventhChord(root + 11)
            ]
        else:
            return [
                # dim MinorSeventhChord(root - 10),
                MajorSeventhChord(root - 9),
                MinorSeventhChord(root - 7),
                MinorSeventhChord(root - 5),
                MajorSeventhChord(root - 4),
                MajorSeventhChord(root - 2),

                MinorSeventhChord(root),

                # dim MinorSeventhChord(root + 2),
                MajorSeventhChord(root + 3),
                MinorSeventhChord(root + 5),
                MinorSeventhChord(root + 7),
                MajorSeventhChord(root + 8),
                MajorSeventhChord(root + 10)
            ]

    def insert_substitutions(self) -> None:
        ...

    def get_close_chords(self) -> List[Chord]:
        """Returns all chords (excluding current chord) that are within
         3 steps away from the current chord
        and within the current chord scale (chord space)."""
        diameter = []
        index = self.chord_scale.index(self.current_chord)
        for i in range(index - 3, index + 3):
            if -1 < i < len(self.chord_scale) and not self.chord_scale[i] == self.current_chord:
                diameter.append(self.chord_scale[i])
        return diameter

    def get_tonic_index(self) -> int:
        """returns the index of the tonic (middle) chord."""
        return len(self.chord_scale) // 2

    def get_current_index(self) -> int:
        """returns the index of the current chord."""
        return self.chord_scale.index(self.current_chord)

    def get_chord_index(self, chord: Chord) -> int:
        """returns the index of the specified chord."""
        return self.chord_scale.index(chord)

    # def set_chord_gravity(self):
    #     self.gravity = (abs((self.get_current_index() - self.get_tonic_index())
    #                         // self.get_tonic_index()) * 100)

    def get_smooth_transitions(self, chords: List[Chord]) -> Chord:
        """returns chord in the list that is most similar to current chord"""
        count = 0
        common_chords = []

        for chord in chords:
            for note1 in chord.get_notes():
                for note2 in self.current_chord.get_notes():
                    # if same note (letter)
                    if note1 % 12 == note2 % 12:
                        count += 1

            if count > 0:
                common_chords.append(chord)
            count = 0
        if len(common_chords) == 0:
            return random.choice(chords)
        return random.choice(common_chords)

    def get_all_substitutions(self) -> List[Chord]:
        ...
