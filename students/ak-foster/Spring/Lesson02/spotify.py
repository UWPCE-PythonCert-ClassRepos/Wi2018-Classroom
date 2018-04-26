import pandas as pd

# Catch raw song data as music variable
music = pd.read_csv("featuresdf.csv")

# Get Ed Sheeran songs by looping over list comprehension
for track in (song for artist, song in zip(music.artists, music.name) if 'Sheeran' in artist):
    print(track)

# High energy tracks (>0.8)
def get_energy(cuttoff):
    def over_cuttoff(energy):
        return energy > cuttoff
    return over_cuttoff

# Set cutt off
cuttoff = get_energy(0.8)

# Get list of high energy song in list comprehension
print([(x, y, z) for (x, y, z) in zip(music.artists, music.name, music.energy) if get_energy(z)])