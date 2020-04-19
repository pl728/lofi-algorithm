from typing import List

from MusicObjects.Chords.chord import Chord
from MusicObjects.note import Note


class ChordProgression:
    chords: List[Chord]

    def __init__(self, chords: List[Chord]):
        self.chords = chords

    def __str__(self):
        progression_string = ""
        for chord in self.chords:
            progression_string += chord.__str__()
            progression_string += "\n"
        return progression_string

    def convert_to_notes(self) -> List[Note]:
        notes = []
        for i in range(len(self.chords)):
            notes += self.chords[i].convert_to_notes(i if i == 0 else i * 4, 4, 96)
        return notes



