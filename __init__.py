from time import sleep

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


def play_midi(mid_):
    s = Server().boot().start()

    midi_reader = Notein()
    amp = MidiAdsr(midi_reader['velocity'])
    pit = MToF(midi_reader['pitch'])
    osc = SineLoop(freq=pit, feedback=0.05, mul=amp).mix(1)
    rev = STRev(osc, revtime=1, cutoff=4000, bal=0.2).out()

    with open("test.mid", 'wb') as bin_file:
        mid_.writeFile(bin_file)
    midi_reader = MidiFile('test.mid')

    for msg in midi_reader.play():
        for message in midi_reader.play():
            # For each message, we convert it to integer data with the bytes()
            # method and send the values to pyo's Server with the addMidiEvent()
            # method. This method programmatically adds a MIDI message to the
            # server's internal MIDI event buffer.
            print(*message.bytes())
            # for byte in message.bytes():
            #     s.addMidiEvent(byte)
            s.addMidiEvent(*message.bytes())


    sleep(1)
    s.stop()


if __name__ == "__main__":
    cm = ChordManager()
    root = random.randint(52, 65)
    cp = cm.generate_lofi_progression(root)
    # cp = cm.generate_major_progression(60)
    for chord in cp.chords:
        print(chord)
    cp_notes = cp.convert_to_notes()
    midi_file = MIDIFile(1)
    midi_file.addTempo(0, 0, 80)
    cm.add_to_midi(cp_notes, midi_file)
    play_midi(midi_file)
