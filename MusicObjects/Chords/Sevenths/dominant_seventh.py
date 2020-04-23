from MusicObjects.Chords.chord import Chord


class MajorDominantChord(Chord):

    def __init__(self, root):
        notes = [root, root + 4, root + 7, root + 10]
        super().__init__(notes)
        self.type = "seventh"
