#!/usr/bin/env python
import pandas as pd
"""
Objective: Use comprehension, featuresdf.csv and pandas

Get artists and song names for for tracks with danceability
scores over 0.8 and loudness scores below -5.0.

Also, these tracks should be sorted in descending order by danceability
so that the most danceable tracks are up top.
"""


def print_all_features():
    print(music.head())
    print(music.describe())


def filter_dancability(music):
    list1 = sorted([(w, x, y, z) for (w, x, y, z)
                   in zip(music.name, music.artists,
                          music.danceability, music.loudness)
                    if y > 0.8 and z < -5.0], reverse=False)
    return(list1)


if __name__ == "__main__":

    print("Load the featuresdf.csv file for all the data")
    music = pd.read_csv("featuresdf.csv")
    good_music = filter_dancability(music)
    print("Most danceable songs are as follows")
    print("NAME, ARTIST, DANCEABILITY, LOUDNESS")
    print("*****************************************")
    for i in good_music:
        print(i)
