from time import sleep

from pydub import AudioSegment

import Players.PySynth.pysynth_samp as pss  # a, b, e, and s variants available
from Composer.lofi_chord_generator import LofiChordGenerator
import wave, os
import Composer.wave_manager as wav_mgr
from MusicObjects.Chords.Sevenths.major_seventh import MajorSeventhChord


def cleanup_audio():
    for i in range(4):
        os.remove("chord_note"+ str(i+1) + ".wav")
    for i in range(8):
        os.remove("chord"+ str(i+1) + ".wav")


if __name__ == "__main__":

    number_of_chords = 8

    for i in range(16):

        lfcg = LofiChordGenerator(MajorSeventhChord(33+i))
        for j in range(number_of_chords):
            lfcg.set_chord().to_wav()
            auto_notes = ["chord_note1.wav", "chord_note2.wav", "chord_note3.wav", "chord_note4.wav"]
            wav_mgr.overlay_waves(auto_notes, 3000, j + 1)
        auto_chords = []
        for j in range(number_of_chords):
            auto_chords.append("chord" + str(j + 1) + ".wav")
        wav_mgr.add_waves(auto_chords, "output"+ str(i) +".wav")
        cleanup_audio()
