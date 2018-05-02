#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4189637

Closures
Using the same data set, write a closure to capture high energy tracks. We will
define high energy tracks as anything over 0.8. Submit your code and the tracks
it finds, artist name, track name and energy value.
"""

import pandas as pd

def make_nrg_df_filter(energy):
    """ Partial function for filtering dataframe on energy field """
    nrg = energy

    def filter_on_nrg(df):
        """ Filter input on stored energy value """
        return df[df['energy'] > nrg]

    return filter_on_nrg


if __name__ == '__main__':
    music = pd.read_csv('featuresdf.csv')
    hi_nrg_df_filter = make_nrg_df_filter(0.8)
    print(hi_nrg_df_filter(music)\
            [['name', 'artists', 'energy']].to_string(index=False))
