from typing import List

from midiutil import MIDIFile

from MusicObjects.Chords.Sevenths.major_dominant import MajorDominantChord
from MusicObjects.Chords.Sevenths.major_seventh import MajorSeventhChord
from MusicObjects.Chords.Sevenths.minor_dominant import MinorDominantChord
from MusicObjects.Chords.Triads.minor import MinorChord
from MusicObjects.Chords.Triads.major import MajorChord
from MusicObjects.Chords.chord_progression import ChordProgression
import random

from MusicObjects.note import Note


class ChordManager:

    def __init__(self):
        pass

    @staticmethod
    def generate_major_progression(root: int) -> ChordProgression:
        possible_steps = [2, 4, 5, 7, 9]
        root2 = random.choice(possible_steps)
        possible_steps.remove(root2)
        root3 = random.choice(possible_steps)

        chord1 = MajorChord(root)

        if root2 in [2, 4, 9]:
            chord2 = MinorChord(root + root2)
        else:
            chord2 = MajorChord(root + root2)

        if root3 in [2, 4, 9]:
            chord3 = MinorChord(root + root3)
        else:
            chord3 = MajorChord(root + root3)

        root4 = random.choice([5, 7])
        chord4 = MajorChord(root + root4)

        chords = [chord1, chord2, chord3, chord4]
        return ChordProgression(chords)

    @staticmethod
    def generate_lofi_progression(root: int) -> ChordProgression:
        possible_steps = [2, 4, 5]
        root2 = random.choice(possible_steps)
        possible_steps.remove(root2)
        possible_steps.append(7)
        root3 = random.choice(possible_steps)
        possible_steps.append(root2)
        possible_steps.append(0)
        possible_steps.append(0)
        root4 = random.choice(possible_steps)

        chord1 = MajorSeventhChord(root)
        if root2 in [2, 4, 9]:
            chord2 = MinorDominantChord(root + root2)
        else:
            chord2 = MajorSeventhChord(root + root2)

        if root3 in [2, 4, 9]:
            chord3 = MinorDominantChord(root + root3)
        else:
            chord3 = MajorSeventhChord(root + root3)

        if root4 in [2, 4, 9]:
            chord4 = MinorDominantChord(root + root4)
        else:
            chord4 = MajorSeventhChord(root + root4)

        chords = [chord1, chord2, chord3, chord4]
        return ChordProgression(chords)



    def add_to_midi(self, notes: List[Note], midi_file: MIDIFile) -> None:
        for note in notes:
            midi_file.addNote(0, 0, note.frequency, note.time_, note.duration,
                              note.velocity)
