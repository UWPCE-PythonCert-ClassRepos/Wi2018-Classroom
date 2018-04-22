#!/usr/bin/env python3

"""
https://canvas.uw.edu/courses/1188584/assignments/4189637

Generators
Last week we looked at Spotify’s top tracks from 2017. We used comprehensions
and perhaps a lambda to find tracks we might like. Having recovered from last
week’s adventure in pop music we’re ready to venture back.

Write a generator to find and print all of your favorite artist’s tracks from
the data set. Your favorite artist isn’t represented in that set? In that case,
find Ed Sheeran’s tracks.

Load the data set following the instructions from last week. Submit your
generator expression and the titles of Ed’s tracks.
"""

import pandas as pd

def make_ed_gen(dataframe):
    """ Provide generator producing Ed Sheeran's tracks from dataframe """
    def gen_ed(dataframe):
        """ Generator producing Ed Sheeran's tracks from dataframe """
        # XXX TODO Write generator
        # Raise StopIteration at end of data
        pass
    return gen_ed

def make_list(dataframe):
    eds = []
    my_gen_ed = make_ed_gen();
    try:
        while True:
            x = my_gen_ed()
            eds += (f"{x.get('name')}")
    except StopIteration:
        pass

    return

if __name__ == '__main__':
    music = pd.read_csv('featuresdf.csv')
    edlist = make_list(music)
    print(edlist)
