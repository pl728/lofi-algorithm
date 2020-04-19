from time import sleep

from mido import MidiFile
from pyo import Server, Notein, MidiAdsr, MToF, SineLoop, STRev, Sine, CrossFM, \
    Fader, Record, Clean_objects


class SinePlayer:
    def __init__(self):
        pass

    @staticmethod
    def play_midi_and_record_wav(mid_):
        # write mid_ to file
        with open("test.mid", "wb") as bin_file:
            mid_.writeFile(bin_file)

        s = Server().boot().start()

        # create audio synth
        midi_reader = Notein()
        amp = MidiAdsr(midi_reader['velocity'])
        pit = MToF(midi_reader['pitch'])
        osc = SineLoop(freq=pit, feedback=0, mul=amp).mix(1)
        rev = STRev(osc, revtime=1, cutoff=4000, bal=0.2).out()

        # create recorder
        rec = Record(rev, filename='beat.wav')
        clean = Clean_objects(12, rec)
        clean.start()

        midi_reader = MidiFile('test.mid')

        # makeshift infinite loop
        for message in midi_reader.play():
            s.addMidiEvent(*message.bytes())

        s.stop()

    def offline_render(self):
        pass
