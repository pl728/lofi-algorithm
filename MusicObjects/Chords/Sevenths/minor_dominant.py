from MusicObjects.Chords.chord import Chord


class MinorDominantChord(Chord):

    def __init__(self, root):
        notes = [root, root + 3, root + 7, root + 10]
        super().__init__(notes)
