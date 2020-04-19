import random
from tkinter import *

from midiutil import MIDIFile

from Managers.chord_manager import ChordManager
from Players.sine_player import SinePlayer


def play(event):
    chord_manager = ChordManager()
    chord_progression = chord_manager.generate_lofi_progression(random.randint(52, 65))
    chord_progression_notes = chord_progression.convert_to_notes()
    midi_file = MIDIFile()
    midi_file.addTempo(0, 0, 80)
    chord_manager.add_to_midi(chord_progression_notes, midi_file)
    player = SinePlayer()
    player.play_midi_and_record_wav(midi_file)


class BeatEditor:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        button1 = Button(master, text="Generate & Play")
        button1.bind("<Button-1>", play)
        button1.pack()

    @staticmethod
    def set_title(master, title: str):
        master.title(title)


