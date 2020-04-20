import Players.PySynth.pysynth_s as pss  # a, b, e, and s variants available

if __name__ == "__main__":
    # root = Tk()
    # root.title("Lo-fi Beat Generator")
    # root.geometry('350x200')
    # be = BeatEditor(root)
    # root.mainloop()


    ''' (note, duration)
    Note name (a to g), then optionally a '#' for sharp or
    'b' for flat, then optionally the octave (defaults to 4).
    An asterisk at the end means to play the note a little 
    louder.  Duration: 4 is a quarter note, -4 is a dotted 
    quarter note, etc.'''
    song = (
        ('c', 4), ('c*', 4), ('eb', 4),
        ('g#', 4), ('g*', 2), ('g5', 4),
        ('g5*', 4), ('r', 4), ('e5', 16),
        ('f5', 16), ('e5', 16), ('d5', 16),
        ('e5*', 4)
    )

    # Beats per minute (bpm) is really quarters per minute here
    pss.make_wav(song, fn="danube.wav", bpm=180)
