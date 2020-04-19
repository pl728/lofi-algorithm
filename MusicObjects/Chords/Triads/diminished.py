from MusicObjects.Chords.chord import Chord


class DiminishedChord(Chord):

    def __init__(self, root):
        notes = [root, root + 3, root + 6]
        super().__init__(notes)
