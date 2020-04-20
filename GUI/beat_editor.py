import random
from tkinter import *
from typing import List

from midiutil import MIDIFile

from Managers.chord_manager import ChordManager
from Players.audio_player import AudioPlayer
from Players.sine_player import SinePlayer
from Players.wave_player_loop import WavePlayerLoop
from pydub import AudioSegment


def generate(event):
    chord_manager = ChordManager()
    chord_progression = chord_manager.generate_lofi_progression(
        random.randint(52, 65))
    chord_progression_notes = chord_progression.convert_to_notes()
    midi_file = MIDIFile()
    midi_file.addTempo(0, 0, 80)
    chord_manager.add_to_midi(chord_progression_notes, midi_file)
    player = SinePlayer()
    player.play_midi_and_record_wav(midi_file)
    combine_sound_file()


def combine_sound_file():
    sounds = [AudioSegment.from_wav(
        r'/Users/linpa/PycharmProjects/beats/drum.wav'),
        AudioSegment.from_wav(
            r'/Users/linpa/PycharmProjects/beats/beat.wav')]
    output = sounds[0].overlay(sounds[1])
    output.export('output.wav', format="wav")


class BeatEditor:

    def __init__(self, master):
        self.combined_loop = None

        frame = Frame(master)
        frame.grid()
        button_generate = Button(master, text="Generate & Play")
        button_generate.bind("<Button-1>", generate)
        button_generate.grid(column=0, row=0)

        button_play = Button(master, text="play")
        button_play.bind("<Button-1>", self.play_all)
        button_play.grid(column=0, row=1)

        button_stop = Button(master, text="stop")
        button_stop.bind("<Button-1>", self.stop_all)
        button_stop.grid(column=0, row=2)

    def play_all(self, event):
        self.combined_loop = WavePlayerLoop(r'output.wav')
        self.combined_loop.play()

    def stop_all(self, event):
        self.combined_loop.stop()

    @staticmethod
    def generate(self, event):
        chord_manager = ChordManager()
        chord_progression = chord_manager.generate_lofi_progression(
            random.randint(52, 65))
        chord_progression_notes = chord_progression.convert_to_notes()
        midi_file = MIDIFile()
        midi_file.addTempo(0, 0, 80)
        chord_manager.add_to_midi(chord_progression_notes, midi_file)
        player = SinePlayer()
        player.play_midi_and_record_wav(midi_file)
        combine_sound_file()
