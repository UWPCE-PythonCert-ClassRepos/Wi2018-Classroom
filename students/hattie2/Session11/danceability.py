#!/usr/bin/env python3

import pandas as pd
music = pd.read_csv("featuresdf.csv")

stuff = music.loc[music['danceability'] > 0.8]

sorted_stuff = stuff.sort_values(['danceability'], ascending=False)

quiet_stuff = sorted_stuff.loc[music['loudness'] < -5]
song_list = quiet_stuff.name + ' by ' + quiet_stuff.artists
#print(dir(song_list))
print(song_list.values[0:5])
