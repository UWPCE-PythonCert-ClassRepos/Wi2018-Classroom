import pandas as pd

# Catch raw song data as music variable
music = pd.read_csv("featuresdf.csv")

# GENERATOR
# Get Ed Sheeran songs by looping over list comprehension
for i in (song for artist, song in zip(music.artists, music.name) if 'Sheeran' in artist):
    print(i)

# CLOSURE
# High energy tracks (>0.8)
def get_energy(energy):

    def over_cuttoff(cuttoff):
        return energy > cuttoff

    return over_cuttoff(0.8)

# Get list of high energy song in list comprehension
e_songs = [(x, y, z) for (x, y, z) in zip(music.artists, music.name, music.energy) if get_energy(z)]
for song in e_songs:
    print(str(round(song[2], 2)) + " : " + song[0] + " - " + song[1])