import pandas as pd


#-----------------------------------------------------------------------
# Generator to yield song name from artist
#------------------------------------------------------------------------
def get_song(csv,artist):
    songs=pd.read_csv(csv)
    yield songs[(songs.artists==artist)]

songs=get_song("featuresdf.csv","Ed Sheeran")

while True:
    print(next(songs)["name"])

#-----------------------------------------------------------------------
# Generator to yield song name from artist
#------------------------------------------------------------------------
def music(csv):
    songs=pd.read_csv(csv)
    def get_track(energy):
        nonlocal  songs
        return songs[(songs.energy>energy)]
    return get_track

songs_by_energy=music("featuresdf.csv")
hi_song=songs_by_energy(0.8)
[print(f"'{j[1]}' by '{j[2]}' at energy of '{j[4]}'") for j in hi_song.sort_values("energy",ascending=False).values]
