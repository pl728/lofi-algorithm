from MusicObjects.Chords.chord import Chord


class MinorSeventhChord(Chord):

    def __init__(self, root):
        notes = [root, root + 3, root + 7, root + 10]
        super().__init__(notes)
        self.type = "minor seventh"
