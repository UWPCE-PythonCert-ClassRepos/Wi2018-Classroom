
"""Instructions
Generators
Last week we looked at Spotify’s top tracks from 2017. We used comprehensions and perhaps a lambda to find tracks
we might like. Having recovered from last week’s adventure in pop music we’re ready to venture back.

Write a generator to find and print all of your favorite artist’s tracks from the data set. Your favorite artist
isn’t represented in that set? In that case, find Ed Sheeran’s tracks.

Load the data set following the instructions from last week. Submit your generator expression and the titles of
Ed’s tracks.

Closures
Using the same data set, write a closure to capture high energy tracks. We will define high energy tracks as anything
over 0.8. Submit your code and the tracks it finds, artist name, track name and energy value."""


#!/usr/bin/env python3

import pandas as pd
music = pd.read_csv("featuresdf.csv")


#generator I hate working with DF like this
def drake_songs(music):
    for i in range(0, len(music)):
            if music.iloc[i].artists == 'Drake':
                yield music.name.iloc[i]


drake_generator = drake_songs(music)

print(next(drake_generator))
print(next(drake_generator))
print(next(drake_generator))
#print(next(drake_generator))


#closure - this is a better closure

def artist_finder(data_set):  # line 1
    def return_function(drake ='Drake'):  # line 2
        songlist = []
        for i in range(0, len(data_set)):
                if data_set.iloc[i].artists == str(drake):
                    songlist.append(music.name.iloc[i])
        return songlist
    return return_function


spotify_artist_finder = artist_finder(music)

drake_finder = spotify_artist_finder()
print(drake_finder)

ed_finder = spotify_artist_finder('Ed Sheeran')
print(ed_finder)