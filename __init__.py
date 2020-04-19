from time import sleep
from tkinter import *

from GUI.beat_editor import BeatEditor
from MusicObjects.Chords.Triads.major import MajorChord
from MusicObjects.Chords.Triads.minor import MinorChord
from MusicObjects.Chords.Triads.diminished import DiminishedChord
from MusicObjects.Chords.Triads.suspended_second import SuspendedSecondChord
from MusicObjects.Chords.Triads.suspended_fourth import SuspendedFourthChord
from MusicObjects.Chords.Sevenths.major_dominant import MajorDominantChord
from MusicObjects.Chords.Sevenths.major_seventh import MajorSeventhChord
from MusicObjects.Chords.Sevenths.minor_seventh import MinorSeventhChord
from Managers.chord_manager import ChordManager

from midiutil import MIDIFile
from mido import MidiFile
from pyo import *

from Players.sine_player import SinePlayer

if __name__ == "__main__":
    root = Tk()
    be = BeatEditor(root)
    be.set_title(root, "Lo-fi Beat Generator")
    root.mainloop()
