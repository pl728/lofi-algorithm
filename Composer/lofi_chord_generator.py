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
        self.chord_scale = self.get_chord_scale(root, major_minor)
        self.major = major_minor
        self.chord_number = 0
        self.tonic = self.chord_scale[0]
        self.current_chord = self.tonic

        self.current_beat = 0
        self.current_measure = 0
        self.current_position = 0

        self.note0 = []
        self.note1 = []
        self.note2 = []
        self.note3 = []

    def set_next_chord(self):
        # todo: previous chords, sequence
        if self.current_beat == 3:
            if random.randint(0, 20) < 15:
                self.current_chord = self.current_chord
            else:
                self.current_chord = random.choice(self.get_close_tension())
        elif self.current_measure % 2 == 1 and (self.current_beat == 2 or self.current_beat == 3):
            self.current_chord = random.choice(self.get_close_home())
        elif self.current_chord in self.get_tension_chords():
            if random.randint(0, 10) < 7:
                self.current_chord = random.choice(self.get_close_home())
            else:
                self.current_chord = random.choice(self.get_close_tension())
        else:
            if random.randint(0, 10) < 3:
                self.current_chord = random.choice(self.get_close_home())
            else:
                self.current_chord = random.choice(self.get_close_tension())

        return self

    def render_next(self):
        """chooses a chord and converts this chord to a wav file with one chord
        a-notes
        b-chord
        c-chord+drum """
        self.set_next_chord()
        chord_letters = self.current_chord.convert_to_letter()
        for elem in enumerate(chord_letters):
            pss.make_wav([(elem[1], 1)], fn="a" + str(elem[0]) + ".wav", bpm=80)
        note_files = ["a" + str(i) + ".wav" for i in range(4)]
        wave_manager.overlay_waves(note_files, 3000, self.chord_number)
        wave_manager.overlay_drums("b" + str(self.chord_number) + ".wav",
                                   "lofi-drums-1-3s.wav",
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

    def separate_chord_notes(self) -> None:
        self.note0.append(self.current_chord.convert_to_letter()[0])
        self.note1.append(self.current_chord.convert_to_letter()[1])
        self.note2.append(self.current_chord.convert_to_letter()[2])
        self.note3.append(self.current_chord.convert_to_letter()[3])

    @staticmethod
    def get_chord_scale(root: int, major: bool) -> List[Chord]:
        """Takes a root as the tonic root and returns all chords in its scale depending on
        major/minor.

        Works for homogeneous M7, m7 chord scales (without chord substitutions) """
        if major:
            return [MajorSeventhChord(root - 5),
                    MinorSeventhChord(root - 3),
                    MinorSeventhChord(root - 1),
                    MajorSeventhChord(root),
                    MinorSeventhChord(root + 2),
                    MinorSeventhChord(root + 4),
                    MajorSeventhChord(root + 5)]
        else:
            return [
                #         MinorSeventhChord(root - 10),
                #         MajorSeventhChord(root - 9),
                #         MinorSeventhChord(root - 7),
                MinorSeventhChord(root - 5),
                MajorSeventhChord(root - 4),
                MinorSeventhChord(root - 2),
                MinorSeventhChord(root),
                MinorSeventhChord(root + 2),
                MajorSeventhChord(root + 3),
                MinorSeventhChord(root + 5)]
            # MinorSeventhChord(root + 7),
            # MajorSeventhChord(root + 8),
            # MinorSeventhChord(root + 10)]

    def get_close_tension(self):
        """returns random close tension chord """
        index = self.chord_scale.index(self.current_chord)
        close_tension = []
        for i in range(index - 4, index + 4):
            if -1 < i < len(self.chord_scale):
                if self.chord_scale[i] in self.get_tension_chords():
                    close_tension.append(self.chord_scale[i])
        return close_tension

    def get_close_home(self):
        """returns random close home chord"""
        index = self.chord_scale.index(self.current_chord)
        close_home = []
        for i in range(index - 4, index + 4):
            if -1 < i < len(self.chord_scale):
                if self.chord_scale[i] in self.get_home_chords():
                    close_home.append(self.chord_scale[i])
        return close_home

    def get_home_chords(self):
        home_chords = []
        if self.major:
            for i in range(len(self.chord_scale)):
                if i in [0, 3, 4]:
                    home_chords.append(self.chord_scale[i])
        else:
            for i in range(len(self.chord_scale)):
                if i in [0, 2, 5]:
                    home_chords.append(self.chord_scale[i])
        return home_chords

    def get_tension_chords(self):
        tension_chords = []
        if self.major:
            for i in range(len(self.chord_scale)):
                if i in [1, 2, 5, 6]:
                    tension_chords.append(self.chord_scale[i])
        else:
            for i in range(len(self.chord_scale)):
                if i in [1, 3, 4, 6]:
                    tension_chords.append(self.chord_scale[i])
        return tension_chords
