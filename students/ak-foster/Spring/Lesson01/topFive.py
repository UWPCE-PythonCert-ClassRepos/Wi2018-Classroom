import pandas as pd

# Catch raw song data as music variable
music = pd.read_csv("featuresdf.csv")

# Get danceable songs
dance_music = [x for x in music.danceability if x > 0.8]

# Get artists and songs with dancability scores above 0.8 and low volume
print(sorted([(w, x, y, z) for (w, x, y, z) in zip(music.artists, music.danceability, music.loudness, music.name) if x > 0.8 and y < -5.0], key=lambda x: -x[1]))
