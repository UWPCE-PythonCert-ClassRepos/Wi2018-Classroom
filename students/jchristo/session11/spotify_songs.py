#!/usr/bin/env python3
import os
import pandas as pd

file_to_copy = os.path.normpath("/Users/jchristo/Desktop/PythonCert/Wi2018-Classroom/students/jchristo/session11/featuresdf.csv") #for Mac
music = pd.read_csv(file_to_copy)

def get_music(a,n,d,l):
    good_music = []
    for artist,name,danceability,loudness in zip(music.artists,music.name,music.danceability,music.loudness):
        if danceability > 0.8 and loudness > -5.0:
            line = (artist, name, danceability, loudness)
            good_music.append(line)
    return good_music

def music_key(good_music):
    return good_music[2]

good_music = get_music(music.artists,music.name,music.danceability,music.loudness)
music_key(good_music)

#list comp way from for loop above
l = [(artist,name,danceability,loudness) for (artist,name,danceability,loudness) in zip(music.artists,music.name,music.danceability,music.loudness) if danceability > 0.8 and loudness > -5.0]

from timeit import default_timer as timer
# START MY TIMER
for_start = timer()
print(sorted(good_music,key=music_key,reverse=True))
# STOP MY TIMER
for_end = timer() - for_start # in seconds
print(f"{for_end} for loop")

# START MY TIMER
comp_start = timer()
print(sorted(l,key=music_key,reverse=True))
# STOP MY TIMER
comp_end = timer() - comp_start # in seconds
print(f"{comp_end} list comp")

"""
Top songs based on criteria:
Headers: Artist, Song, Danceability, Loudness
[('Calvin Harris', 'Feels', 0.893, -3.105),
 ('Shawn Mendes', "There's Nothing Holdin' Me Back", 0.857, -4.035),
 ('Rita Ora', 'Your Song', 0.855, -4.093),
 ('Bruno Mars', "That's What I Like", 0.853, -4.961),
 ('Shakira', 'Chantaje', 0.852, -2.9210000000000003),
 ('Travis Scott', 'goosebumps', 0.841, -3.37),
 ('Ed Sheeran', 'Shape of You', 0.825, -3.1830000000000003),
 ('Bruno Mars', '24K Magic', 0.818, -4.282)]
"""
