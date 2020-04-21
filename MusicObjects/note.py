class Note:
    frequency: int  # 60 is C(4?)
    time_: int  # in audio
    duration: int  # in BPM
    velocity: int  # 0-127, as per the MIDI standard

    def __init__(self, frequency, time_, duration, velocity) -> None:
        self.frequency = frequency
        self.time_ = time_
        self.duration = duration
        self.velocity = velocity

