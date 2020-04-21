from typing import List

from pydub import AudioSegment

def overlay_waves(files: List[str], chord_length: int, file_number: int):
    """bpm = 80 -> chord_length = 3000"""
    audio_segments = [AudioSegment.from_wav(file)[:chord_length] for file in files]
    output = audio_segments[0].overlay(audio_segments[1])
    for i in range(2, len(audio_segments)):
        output = output.overlay(audio_segments[i])
    output.export("chord" + str(file_number) + ".wav", format="wav")

def add_waves(files: List[str], export_file: str):
    audio_segments = [AudioSegment.from_wav(file) for file in files]
    output = sum(audio_segments)
    output.export(export_file, format='wav')


