#!/usr/bin/env python

'''Write a generator to find and print all of Ed Sheeran’s tracks.'''


#use a generator to yeild values from an infinite data set, read data off disk by loading parts of it at a time, or need a way to facilate values before you know them.


import pandas as pd

read_music = pd.read_csv("featuresdf.csv")

def sheeran_gen():
    for artists, name in zip(read_music.artists, read_music.name):
         if 'Sheeran' in artists:
            yield name

for track in sheeran_gen():
    print(track)