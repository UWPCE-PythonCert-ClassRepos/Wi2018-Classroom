#!/usr/bin/env python

import pandas as pd

# Programming in python B Spring 2018
# April 15, 2018
# Lession 02 - saved in Session12 -
# Generators / closures - music tracks
# Tracy Allen - git repo https://github.com/tenoverpar/Wi2018-Classroom


# Assignment summary:
# 1) Write a generator to find and print all of Ed Sheeran’s tracks
#  from the data set. Submit your generator expression and the titles of
#  Ed’s tracks.
# 2) Write a closure to capture high energy tracks - anything over 8.0
#  Submit your code and the tracks it finds: artist name, track name and
#  energy value.

# Load data
music = pd.read_csv("featuresdf.csv")

# PART 1 -- generator expression
res = (name for name, artist in zip(music.name, music.artists)
       if artist == "Ed Sheeran")

print(list(res))
#  prints
# ['Shape of You', 'Castle on the Hill', 'Galway Girl', 'Perfect']


# PART 2 -- closure
def energy_music_factory(dataset):
    """A closure to create energy_music_function.

    Arg: dataset: a pandas dataset from .scv-file to close into the
    returned function.
    """
    def energy_music_function(energy_level):
        return [(artist, name, energy)
                for artist, name, energy in zip(dataset.artists,
                                                dataset.name,
                                                dataset.energy)
                if energy > energy_level]

    return energy_music_function


energy_music = energy_music_factory(music)
print(energy_music(0.8))


# Testing the closure
res2 = [(a, n, e) for a, n, e in zip(music.artists,
                                     music.name,
                                     music.energy)
        if e > 0.8]
assert energy_music(0.8) == res2
