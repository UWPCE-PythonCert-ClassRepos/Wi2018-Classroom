#!/usr/bin/env python3

"""
Session 11:

### Attempt at doing this some other way than a straight list comprehension
#Use pandas location to create a hash table
"""


"""
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

LENGTH_OF_OUTPUT=5

### Attempt at doing this some other way than a straight list comprehension
#Use pandas location to create a hash table
# 0 = id (assumption: ID is unique)
# 1 = name
# 2 = artist
# 3 = danceability
# 6 = loudness
## debug output: print(music.iloc[0][1], music.iloc[0][2], music.iloc[0][3], music.iloc[0][6])

def create_dict_data():
    """Create the dict containing the data

    returns: dict(key, (list)) / sexy_music """

    i=0
    sexy_music={}
    while i < len(music):
        if music.iloc[i][3] > 0.8 and music.iloc[i][6] < -5.0:
            sexy_music.update({music.iloc[i][0]:
                                [music.iloc[i][1],
                                music.iloc[i][2],
                                music.iloc[i][3],
                                music.iloc[0][6]]})
        i += 1

    return sexy_music


def score_danceable(sexy_music):
    """ use a dict comprehension to create the list of sorted items
    and truncate the list to the desired length

    returns: list / sexy_music_stuff
    """
    sexy_music_stuff = sorted({(v[2], k) for k, v in sexy_music.items()}, reverse=True)

    # truncate the list at 5 items
    while len(sexy_music_stuff) > LENGTH_OF_OUTPUT:
        sexy_music_stuff.pop()

    return sexy_music_stuff


def print_dancable(danceability_scored):
    """Print output of the items after danceability (or required sorting value) has been selected"""

    print ('{:50s} | {:25s} | {:20s}'.format('Name', 'Artist', 'danceability'))
    print ('-' * 95)
    for i in danceability_scored:
        print('{:50s} | {:25s} | {:20s}'.format(str(sexy_music[i[1]][0]),str(sexy_music[i[1]][1]),str(sexy_music[i[1]][2])))



if __name__ == '__main__':
    sexy_music=create_dict_data()
    print_dancable(score_danceable(sexy_music))
