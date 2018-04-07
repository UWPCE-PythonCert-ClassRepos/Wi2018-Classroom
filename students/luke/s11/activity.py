#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4189634?module_item_id=8331790

Your job, now, is to get artists and song names for for tracks with
danceability scores over 0.8 and loudness scores below -5.0. In other words,
quiet yet danceable tracks. Also, these tracks should be sorted in descending
order by danceability so that the most danceable tracks are up top.
"""

import pandas as pd


def make_list(dataframe):
    return \
        [x for idx, x
         in music.sort_values(by='danceability', ascending=False).iterrows()
         if x.danceability > 0.8 and x.loudness < -5]


if __name__ == "__main__":
    music = pd.read_csv("featuresdf.csv")
    dlist = make_list(music)
    print(dlist)
