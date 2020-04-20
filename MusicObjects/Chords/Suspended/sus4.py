from MusicObjects.Chords.chord import Chord


class SuspendedFourthChord(Chord):
    def __init__(self, root:int):
        notes = [root, root + 5, root + 7]
        super().__init__(notes)
