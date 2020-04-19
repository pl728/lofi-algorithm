from typing import List

from MusicObjects.Chords.chord import Chord


class MajorChord(Chord):

    def __init__(self, root):
        notes = [root, root + 4, root + 7]
        super().__init__(notes)
