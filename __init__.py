from Composer.lofi_song_assembler import LofiSongAssembler

if __name__ == "__main__":
    lsa = LofiSongAssembler()
    lsa.create_playlist(num_songs=4, num_chords=32)
