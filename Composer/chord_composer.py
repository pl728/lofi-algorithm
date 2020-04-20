from typing import List

from midiutil import MIDIFile

from MusicObjects.Chords.Sevenths.major_dominant import MajorDominantChord
from MusicObjects.Chords.Sevenths.major_seventh import MajorSeventhChord
from MusicObjects.Chords.Sevenths.minor_dominant import MinorDominantChord
from MusicObjects.Chords.Sevenths.minor_seventh import MinorSeventhChord
from MusicObjects.Chords.chord import Chord
from MusicObjects.Chords.chord_progression import ChordProgression
import random

from MusicObjects.note import Note

# MAJOR_SEVENTH_LANDING =


class ChordGenerator:
    """Generates chord progressions."""

    def __init__(self):
        pass

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

    def sevenths_get_random_dominant(self, direction: bool,
                                     major: bool, root: int) -> Chord:
        if direction:
            step = random.choice([7, 11])
            if major:
                return MajorSeventhChord(root + step)
            else:
                return MinorDominantChord(root + step)
        else:
            step = random.choice([-1, -5])
            if major:
                return MajorSeventhChord(root + step)
            else:
                return MinorDominantChord(root + step)

    def sevenths_get_random_subdominant(self, direction: bool,
                                        major: bool, root: int) -> Chord:
        if direction:
            step = random.choice([2, 5])
            if major:
                return MajorSeventhChord(root + step)
            else:
                return MinorDominantChord(root + step)
        else:
            step = random.choice([-7, -10])
            if major:
                return MajorSeventhChord(root + step)
            else:
                return MinorDominantChord(root + step)

    @staticmethod
    def get_major_seventh_chord_scale(root: int) -> ChordProgression:
        scale = [MajorSeventhChord(root),
                 MinorDominantChord(root + 2),
                 MinorDominantChord(root + 4),
                 MajorSeventhChord(root + 5),
                 MajorSeventhChord(root + 7),
                 MinorDominantChord(root + 9),
                 MinorDominantChord(root + 11)]
        return ChordProgression(scale)

    @staticmethod
    def get_minor_seventh_chord_scale(root: int) -> ChordProgression:
        scale = [MinorSeventhChord(root),
                 MinorDominantChord(root + 2),
                 MajorDominantChord(root + 3),
                 MajorDominantChord(root + 5),
                 MinorDominantChord(root + 7),
                 MajorSeventhChord(root + 8),
                 MinorDominantChord(root + 11)]
        return ChordProgression(scale)

    def get_matching_chords(self, scale: List[Chord]):
        """
        >>> chord_manager = ChordGenerator(60)
        >>> major_seventh_scale = chord_manager.get_minor_seventh_chord_scale()
        >>> chord_manager.get_matching_chords(major_seventh_scale.chords)
        [1, 3, 4, 6, 7]
        """
        tonic = scale.pop(0)
        matching = []
        for chord in scale:
            matching.append(self.get_chord_similarity(tonic, chord))
        scale.insert(0, tonic)
        return matching

    def get_chord_similarity(self, chord1: Chord, chord2: Chord) -> int:
        """
        >>> c1 = Chord([0, 15, 4, 6])
        >>> c2 = Chord([1, 3, 5, 6])
        >>> cm = ChordGenerator(60)
        >>> cm.get_chord_similarity(c1, c2)
        2
        """
        matching = 0
        for note1 in chord1.notes:
            for note2 in chord2.notes:
                if note1 % 12 == note2 % 12:
                    matching += 1
        return matching

    @staticmethod
    def add_to_midi(notes: List[Note], midi_file: MIDIFile) -> None:
        for note in notes:
            midi_file.addNote(0, 0, note.frequency, note.time_, note.duration,
                              note.velocity)
