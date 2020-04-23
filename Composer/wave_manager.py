from pydub import AudioSegment
from typing import List


def overlay_waves(files: List[str], chord_length_time: int, file_number: int):
    """bpm = 80 -> chord_length = 3000"""
    audio_segments = [AudioSegment.from_wav(file)[:chord_length_time] for file in files]
    output = audio_segments[0].overlay(audio_segments[1])
    for i in range(2, len(audio_segments)):
        output = output.overlay(audio_segments[i])
    output.export("b" + str(file_number) + ".wav", format="wav")

def add_waves(files: List[str], export_file: str):
    audio_segments = [AudioSegment.from_wav(file) for file in files]
    output = sum(audio_segments)
    output.export(export_file, format='wav')


def overlay_drums(chord: str, drum: str, file_number: int):
    c = AudioSegment.from_wav(chord)
    d = AudioSegment.from_wav(drum)
    c.overlay(d).export("c" + str(file_number) + ".wav", format="wav")
