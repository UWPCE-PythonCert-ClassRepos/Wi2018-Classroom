import pandas as pd

music = pd.read_csv("featuresdf.csv")


fav_artist = "Ed Sheeran"
favorite_songs = (y for x, y in zip(music.artists, music.name) if x == fav_artist)

for s in favorite_songs:
    print(s)



