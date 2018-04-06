import pandas as pd
import csv
import operator


#------------------------------------------------------------------------
# Pandas
#------------------------------------------------------------------------
def read_songs(csv):
    songs=pd.read_csv(csv)
    return songs[(songs.loudness < -5.0) & (songs.danceability > 0.8)]

#------------------------------------------------------------------------
# OO
#------------------------------------------------------------------------
class Song():

    def __init__(self,id, name, artists, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness,
                liveness, valence, tempo, duration_ms, time_signature):
        self.id=id
        self.name=name
        self.artists=artists
        self.danceability=float(danceability)
        self.energy=float(energy)
        self.key=float(key)
        self.loudness=float(loudness)
        self.mode=float(mode)
        self.speechiness=float(speechiness)
        self.acousticness=float(acousticness)
        self.instrumentalness=float(instrumentalness)
        self.liveness=float(liveness)
        self.valence=float(valence)
        self.tempo=float(tempo)
        self.duration_ms=float(duration_ms)
        self.time_signature=float(time_signature)

class Songs():

    def __init__(self):
        self.songs=[]


    def add(self, other):
        self.songs.append(other)

    def read_data(self,file):
        with open(file,'rU') as f:
            reader = csv.reader(f)
            next(reader,None)
            [self.add(s) for s in [Song(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15]) for r in reader]]
            return self

#------------------------------------------------------------------------
# Compare  OO version with pandas
#------------------------------------------------------------------------
#print OO
music = sorted([i for i in Songs().read_data("featuresdf.csv").songs if i.danceability > 0.8 and i.loudness < -5.0],key=operator.attrgetter('danceability'),reverse=True)
print(f"\n{'='*50}\nOO\n{'='*50}")
for i in music:
    print(f"'{i.artists}' singing '{i.name}' at danceability of '{i.danceability}'" )

print(f"\n{'='*50}\nPandas\n{'='*50}")

#print pandas
[print(f"'{j[2]}' singing '{j[1]}' at danceability of '{j[3]}'") for j in read_songs("featuresdf.csv").sort_values("danceability",ascending=False).values]


   


