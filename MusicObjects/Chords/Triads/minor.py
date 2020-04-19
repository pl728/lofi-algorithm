from MusicObjects.Chords.chord import Chord


class MinorChord(Chord):

    def __init__(self, root):
        notes = [root, root + 3, root + 7]
        super().__init__(notes)
