from typing import List

from pydub import AudioSegment


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


def add_silence(file: str, export_file: str, silence_amount: int):
    """silence length: 3sec * silence amount"""
    before = AudioSegment.from_wav(file)
    output = before + AudioSegment.from_wav("vinyl-3s.wav")
    for i in range(silence_amount):
        output = output + AudioSegment.from_wav("silence-3sec.wav")
    output.export(export_file, format="wav")


def overlay_background(chord: str, background: List[str], file_number: int):
    c = AudioSegment.from_wav(chord)
    for bg in background:
        d = AudioSegment.from_wav(bg)
        c = c.overlay(d)
    c.export("c" + str(file_number) + ".wav", format="wav")
