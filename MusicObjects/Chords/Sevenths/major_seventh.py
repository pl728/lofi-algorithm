from MusicObjects.Chords.chord import Chord


class MajorSeventhChord(Chord):

    def __init__(self, root):
        notes = [root, root + 4, root + 7, root + 11]
        super().__init__(notes)
        self.type = "major seventh"
