from MusicObjects.Chords.chord import Chord


class SuspendedSecondChord(Chord):

    def __init__(self, root):
        notes = [root, root + 2, root + 7]
        super().__init__(notes)
