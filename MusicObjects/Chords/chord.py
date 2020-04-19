from typing import List
from MusicObjects.note import Note


class Chord:
    """
    A musical chord that contains notes.
    """
    notes: List[int]

    def __init__(self, notes: List[int]):
        self.notes = notes

    def __str__(self):
        note_letters = []
        for note in self.notes:
            if note % 12 == 0:
                note_letters.append("C")
            elif note % 12 == 1:
                note_letters.append("C#/D♭")
            elif note % 12 == 2:
                note_letters.append("D")
            elif note % 12 == 3:
                note_letters.append("D#/E♭")
            elif note % 12 == 4:
                note_letters.append("E")
            elif note % 12 == 5:
                note_letters.append("F")
            elif note % 12 == 6:
                note_letters.append("F#/G♭")
            elif note % 12 == 7:
                note_letters.append("G")
            elif note % 12 == 8:
                note_letters.append("G#/A♭")
            elif note % 12 == 9:
                note_letters.append("A")
            elif note % 12 == 10:
                note_letters.append("A#/B♭")
            elif note % 12 == 11:
                note_letters.append("B")
        return ', '.join(note_letters) + " "

    def invert(self, number_of_times: int = 1):
        for i in range(number_of_times):
            first_note = self.notes.pop(0)
            self.notes.append(first_note)

    def convert_to_notes(self, time_: int, duration: int, volume: int) -> List[Note]:
        notes = []
        for note in self.notes:
            notes.append(Note(note, time_, duration, volume))
        return notes
