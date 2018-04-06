import pandas as pd
import csv
import itertools

#------------------------------------------------------------------------
# Pandas
#------------------------------------------------------------------------
songs=pd.read_csv("featuresdf.csv")
result = songs[(songs.loudness < -5.0) & (songs.danceability > 0.8)]

#------------------------------------------------------------------------
# OO way
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

music=Songs().read_data("featuresdf.csv");





