import pandas as pd

music = pd.read_csv("featuresdf.csv")

music.head()
music.describe()

''' generator for songs by Halsey '''
songs = (x for x in list(zip(music.artists, music.name, music.danceability, music.loudness, music.energy)) if x[0] == 'Halsey')

for i in songs:
    print(i)

''' closure for songs with energy over 0.8 '''
def closure(energy):
    def inner(music):
        songs = [(x, y, z) for x, y, z in zip(music.artists, music.name, music.energy) if z > energy]
        return songs
    return inner

highenergyfunc = closure(0.8)
print(highenergyfunc(music))
