from time import sleep
from tkinter import *
from GUI.beat_editor import BeatEditor
from Players.wave_player_loop import WavePlayerLoop

if __name__ == "__main__":
    root = Tk()
    root.title("Lo-fi Beat Generator")
    root.geometry('350x200')
    be = BeatEditor(root)
    root.mainloop()
