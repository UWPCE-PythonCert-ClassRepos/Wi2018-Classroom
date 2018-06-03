import pandas as pd

# I should mention here that Ed Sheeran is *NOT* my favorite artist.
# I chose him as the default.
music = pd.read_csv("featuresdf.csv")

dataframe_size = music.iloc[-1].name + 1


def generate_sheeran(artist_name):
    for i in range(dataframe_size):
        if artist_name in music.artists[i]:
            yield music.name[i]


eds_tracks = generate_sheeran("Sheeran")

for track in music.artists:
    try:
        print(next(eds_tracks))
    except StopIteration:
        break


def get_songs_based_on(song_property):
    if song_property not in music.columns:
        print("No such property: ", song_property)
        return
    for c in range(len(music.columns)):
        if music.columns[c] == song_property:
            col = music.columns[c]

    def above(n):
        pass


get_songs_based_on("Energy")