#!/usr/bin/env python3
import os
import pandas as pd

file_to_copy = os.path.normpath("/Users/jchristo/Desktop/PythonCert/Wi2018-Classroom/students/jchristo/session11/featuresdf.csv") #for Mac
music = pd.read_csv(file_to_copy)

def get_music(a,n,d,l):
    good_music = []
    for artist,name,danceability,loudness in zip(music.artists,music.name,music.danceability,music.loudness):
        if danceability > 0.8 and loudness < -5.0:
            line = (artist, name, danceability, loudness)
            good_music.append(line)
    return good_music

def music_key(good_music):
    return good_music[2]

good_music = get_music(music.artists,music.name,music.danceability,music.loudness)
music_key(good_music)

#list comp way from for loop above
l = [(artist,name,danceability,loudness) for (artist,name,danceability,loudness) in zip(music.artists,music.name,music.danceability,music.loudness) if danceability > 0.8 and loudness < -5.0]

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
[('Migos', 'Bad and Boujee (feat. Lil Uzi Vert)', 0.927, -5.313), 
('Drake', 'Fake Love', 0.927, -9.433), 
('Kendrick Lamar', 'HUMBLE.', 0.904, -6.8420000000000005), 
('21 Savage', 'Bank Account', 0.884, -8.228), 
('Jax Jones', "You Don't Know Me - Radio Edit", 0.8759999999999999, -6.053999999999999), 
('Liam Payne', 'Strip That Down', 0.8690000000000001, -5.595), 
('Future', 'Mask Off', 0.833, -8.795), 
('Zion & Lennox', 'Otra Vez (feat. J Balvin)', 0.8320000000000001, -5.428999999999999), 
('Drake', 'Passionfruit', 0.809, -11.377)]
"""
