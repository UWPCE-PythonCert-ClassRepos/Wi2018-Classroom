#!/usr/bin/env python

"""
Write a generator to find and print all of your favorite artist’s tracks from the data set. 
Your favorite artist isn’t represented in that set? In that case, find Ed Sheeran’s tracks.
"""
import pandas as pd

class artist_generator:
    def __init__(self):
        self.music = pd.read_csv("featuresdf.csv")
        self.names = [name for name in self.music.name]
        self.artists = [artist for artist in self.music.artists]
        self.myList = zip(self.names, self.artists)	
    def __iter__(self):
        return self
    def __next__(self):
        for x in self.myList:
            if x[1] == 'Ed Sheeran':
                return x[0]			
				
def capture_high_energy_tracks(energy_level=0.8):
    def tracks():
        track =[]
        music = pd.read_csv("featuresdf.csv")
        names = [name for name in music.name]
        energy = [energy for energy in music.energy]
        myList = zip(names, energy)
        for x in myList:
            if x[1] > energy_level:
                track.append(x[0])
        print(track)
    return tracks				
				
if __name__ == '__main__':
    my_tracks = capture_high_energy_tracks(0.8)
    my_tracks()
    g = artist_generator()
    for index in range(5):
        val = next(g)
        if val != None:
            print(val)