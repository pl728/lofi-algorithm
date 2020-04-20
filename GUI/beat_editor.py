import random
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from typing import List

from midiutil import MIDIFile

from Managers.chord_manager import ChordManager
from Players.sine_player import SinePlayer
from Players.wave_player_loop import WavePlayerLoop
from pydub import AudioSegment


def combine_sound_file():
    sounds = [AudioSegment.from_wav(
        r'/Users/linpa/PycharmProjects/beats/drum1.wav'),
        AudioSegment.from_wav(
            r'/Users/linpa/PycharmProjects/beats/beat.wav')]
    output = sounds[0].overlay(sounds[1])
    output.export('output.wav', format="wav")


class BeatEditor:
    current_drum_rhythm: int

    def __init__(self, master):
        self.combined_loop = WavePlayerLoop(r'drum.wav')
        self.current_drum_rhythm = 0

        frame = Frame(master)
        frame.grid()
        button_generate = Button(master, text="Generate & Play")
        button_generate.bind("<Button-1>", self.generate)
        button_generate.grid(column=0, row=0)

        button_play = Button(master, text="Loop")
        button_play.bind("<Button-1>", self.play_all_button)
        button_play.grid(column=0, row=1)

        button_stop = Button(master, text="Stop")
        button_stop.bind("<Button-1>", self.stop_all_button)
        button_stop.grid(column=0, row=2)


        drum_rhythm_label = Label(master, text="Drum Rhythm")
        drum_rhythm_label.grid(column=2, row=0)

        button_rhythm_left = Button(master, text="<")
        button_rhythm_left.bind("<Button-1>",
                                self.left_rhythm)
        button_rhythm_left.grid(column=1, row=0)

        button_rhythm_right = Button(master, text=">")
        button_rhythm_right.bind("<Button-1>",
                                 self.right_rhythm)
        button_rhythm_right.grid(column=3, row=0)

    def left_rhythm(self, event):
        if self.current_drum_rhythm == 0:
            self.current_drum_rhythm = 2
        else:
            self.current_drum_rhythm -= 1
        print(self.current_drum_rhythm)
        self.select_export_drum_rhythm()

    def right_rhythm(self, event):
        if self.current_drum_rhythm == 2:
            self.current_drum_rhythm = 0
        else:
            self.current_drum_rhythm += 1
        print(self.current_drum_rhythm)
        self.select_export_drum_rhythm()

    def select_export_drum_rhythm(self):
        drum_segment = AudioSegment.from_wav(
            r'/Users/linpa/PycharmProjects/beats/drum1.wav')
        if self.current_drum_rhythm == 1:
            drum_segment = AudioSegment.from_wav(
                r'/Users/linpa/PycharmProjects/beats/drum2.wav')
        elif self.current_drum_rhythm == 2:
            drum_segment = AudioSegment.from_wav(
                r'/Users/linpa/PycharmProjects/beats/drum3.wav')
        beat_segment = AudioSegment.from_wav(
            r'/Users/linpa/PycharmProjects/beats/beat.wav')
        sounds = [beat_segment, drum_segment]
        output = sounds[0].overlay(sounds[1])
        output.export('output.wav', format="wav")
        self.combined_loop.stop()
        self.combined_loop = WavePlayerLoop(r'output.wav')
        self.combined_loop.play()


    def play_all_button(self, event):
        self.combined_loop.stop()
        self.combined_loop = WavePlayerLoop(r'output.wav')
        self.combined_loop.play()

    def stop_all_button(self, event):
        self.combined_loop.stop()

    def generate(self, event):
        self.combined_loop.stop()
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


