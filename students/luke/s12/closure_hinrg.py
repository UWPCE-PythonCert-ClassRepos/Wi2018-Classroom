#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4189637

Closures
Using the same data set, write a closure to capture high energy tracks. We will
define high energy tracks as anything over 0.8. Submit your code and the tracks
it finds, artist name, track name and energy value.
"""

import pandas as pd

def make_nrg_closure(nrg):
    """ Partial function for filtering dataframe on energy field """
    def filter_on_nrg(dataframe):
        """ Filter input on stored energy value """
        # XXX TODO filter dataframe where energy > nrg
        # Raise StopIteration at end of data
        pass
    return filter_on_nrg


def make_list(dataframe):
    """ Add filtered name/artists to list """
    return \
        [f"{x.get('name')} by {x.get('artists')}"
         for idx, x
         in music.sort_values(by='danceability', ascending=False).iterrows()
         if x.danceability > 0.8 and x.loudness < -5]


if __name__ == '__main__':
    music = pd.read_csv('featuresdf.csv')
    hi_nrg = make_nrg_closure(0.8)
    try:
        while True:
            print(hi_nrg(music))
    except StopIteration:
        pass

    return
