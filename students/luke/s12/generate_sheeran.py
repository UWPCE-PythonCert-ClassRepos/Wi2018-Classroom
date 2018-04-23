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
    df = dataframe 
    def ed_gen():
        """ Generator producing Ed Sheeran's tracks from dataframe """
        for idx, row in df.iterrows():
            if row['artists'] != 'Ed Sheeran':
                continue
            yield row['name']
        raise StopIteration

    return ed_gen

def make_list(df):
    eds = []
    my_ed_gen = make_ed_gen(df);
    i = 0
    while True:
        try:
            eds += my_ed_gen()
        except StopIteration:
            break
        finally:
            break

    return eds

if __name__ == '__main__':
    music = pd.read_csv('featuresdf.csv')
    edlist = make_list(music)
    print(edlist)
