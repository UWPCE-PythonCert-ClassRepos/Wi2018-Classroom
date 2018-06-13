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

import pandas as pd
music = pd.read_csv("./data/featuresdf.csv")

LENGTH_OF_OUTPUT=5


def create_sexy_music_list():
    """Use a sorted list comprehension to create the return output"""
    ## return sorted([(z, n, x, y) for (n, x, y, z) in zip(music.name, music.artists, music.loudness, music.danceability) if y < -5.0 and z > 0.8], reverse=True)
    # return sorted([(danceability, name, artists, loudness)
    #                     for (name, artists, loudness, danceability) in zip(music.name, music.artists, music.loudness, music.danceability)
    #                     if loudness < -5.0 and danceability > 0.8],
    #                     reverse=True)
    import pdb; pdb.set_trace()
    musical_values=zip(music.name, music.artists, music.loudness, music.danceability)
    musical_preferred=[(z, n, x, y, broken) for (n, x, y, z) in  musical_values if y < -5.0 and z > 0.8]
    return sorted(musical_preferred, reverse=True)


def select_output(music_lc_ordered):
    """Select the length of the output to be used in the output"""

    while len(music_lc_ordered) > LENGTH_OF_OUTPUT:
        music_lc_ordered.pop()

    return (music_lc_ordered)


def output_selected(music_lc_ordered):
    """ Output all of the selected output"""

    print ('{:50s} | {:25s} | {:20s}'.format('Name', 'Artist', 'danceability'))
    print ('-' * 95)
    for i in sorted(music_lc_ordered, reverse=True):
        print ('{:50s} | {:25s} | {:20s}'.format(i[1], str(i[2]), str(i[0])))


if __name__ == '__main__':
    output_selected(select_output(create_sexy_music_list()))
