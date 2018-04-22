import pandas as pd

music = pd.read_csv("featuresdf.csv")

def energyClosure(n):
    def energyReturn(music):
        high_energy_songs = [(x,y,z) for x, y, z in zip(music.artists, music.name, music.energy) if z > n]
        print(high_energy_songs)
    return energyReturn


energy8 = energyClosure(0.8)

energy8(music)


