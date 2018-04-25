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
				
				
				
if __name__ == '__main__':
    g = artist_generator()
    for index in range(5):
        val = next(g)
        if val != None:
            print(val)