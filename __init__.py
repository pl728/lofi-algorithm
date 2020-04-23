from Composer.lofi_song_assembler import LofiSongAssember

if __name__ == "__main__":
    lsa = LofiSongAssember()
    lsa.create_playlist(num_songs=1, num_chords=32)
