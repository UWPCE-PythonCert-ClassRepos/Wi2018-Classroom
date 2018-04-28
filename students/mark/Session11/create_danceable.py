#!/usr/bin/env python3

"""
Session 11:

Your job, now, is to:

* get artists
* get song names for for tracks
with:
* danceability scores over 0.8
* and loudness scores below -5.0.

In other words, quiet yet danceable tracks.

Also, these

* tracks should be sorted in descending order by danceability
    so that the
* most danceable tracks are up top.

You should be able to

* work your way there starting with the comprehension above.

And while you could use Pandas features along the way, you don’t need to.
To accomplish the objective you do not need to know anything more about Pandas than what
you can infer from the material herein. Standard library functions that could come in handy
include

* can use: zip() and sorted().

Submit your code and the top five tracks to complete the assignment.
"""


import pandas as pd
music = pd.read_csv("./data/featuresdf.csv")

### Take a look around to get a sense of the general shape of the data.
#### Uneeded after debugging (remove from production code / here only as example of looking around)
# print(music.head())
# print('#' * 3)
# music.describe()

### Now we are ready for the analytics. This first one is a gimme.
### We will use a comprehension to get danceability scores over 0.8.
# print([x for x in music.danceability if x > 0.8])
# print([x for x in music.loudness if x < -5.0])
# print([x for (x,y) in zip(music.loudness, music.danceability) if x < -5.0])
# print([(x,y) for (x,y) in zip(music.loudness, music.danceability) if x < -5.0 and y > 0.8])

def create_sexy_music_list():

    return [(z,n,x,y) for (n,x,y,z) in zip(music.name, music.artists, music.loudness, music.danceability) if y < -5.0 and z > 0.8]

music_lc_ordered=create_sexy_music_list()


def select_output():
    while len(sorted(music_lc_ordered, reverse=True)) > 5:
        music_lc_ordered.pop()

    return (music_lc_ordered)


def output_selected(music_lc_ordered):
    print ('{:50s} | {:25s} | {:20s}'.format('Name', 'Artist', 'danceability'))
    print ('-' * 95)
    for i in sorted(music_lc_ordered, reverse=True):
        print ('{:50s} | {:25s} | {:20s}'.format(i[1], str(i[2]), str(i[0])))

select_output()
output_selected(music_lc_ordered)
