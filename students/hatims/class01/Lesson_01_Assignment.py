#!/usr/bin/env python

"""
get artists and song names for for tracks with danceability scores over 0.8 and loudness scores below -5.0. In other words, quiet yet danceable tracks. 
Also, these tracks should be sorted in descending order by danceability so that the most danceable tracks are up top
"""
import pandas as pd
music = pd.read_csv("featuresdf.csv")


names = [name for name in music.name]
artists = [artist for artist in music.artists]
danceability = [danceability for danceability in music.danceability]
loudness = [loudness for loudness in music.loudness]

myList = zip(names, artists, danceability, loudness)
print(sorted([('Song: ' + x[0], 'Artist:  ' + x[1]) for x in myList if x[2] > (0.8) and x[3] < (-5.0)])) 		


