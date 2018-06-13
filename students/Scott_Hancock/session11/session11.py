import pandas as pd

def sort_danceability_descending(my_tuple):
    return -my_tuple[1]

music = pd.read_csv("featuresdf.csv")

music.head()
music.describe()

songs = sorted([(w, x, y, z) for (w, x, y, z) in zip(music.artists, music.danceability, music.loudness, music.name) if x > 0.8 and y < -5.0], key=sort_danceability_descending)
songs

top_5_songs = songs[:5]

for i, j in enumerate(top_5_songs):
    print(i, j) #print them