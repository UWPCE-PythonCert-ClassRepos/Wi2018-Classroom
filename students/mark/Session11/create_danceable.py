#!/usr/bin/env python3

import pandas as pd
music = pd.read_csv("./data/featuresdf.csv")

### Take a look around to get a sense of the general shape of the data.

print(music.head())
print('#' * 3)
music.describe()

### Now we are ready for the analytics. This first one is a gimme.
### We will use a comprehension to get danceability scores over 0.8.

print([x for x in music.danceability if x > 0.8])

print([x for x in music.loudness if x < -5.0])
print([x for (x,y) in zip(music.loudness, music.danceability) if x < -5.0])
print([(x,y) for (x,y) in zip(music.loudness, music.danceability) if x < -5.0 and y > 0.8])
print([(z,x,y) for (z,x,y) in zip(music.artists, music.loudness, music.danceability) if x < -5.0 and y > 0.8])


#Use pandas location to create a hash table
print(music.iloc[0][1], music.iloc[0][2], music.iloc[0][6])
# 0 = id (assumption: ID is unique)
# 1 = name
# 2 = artist
# 3 = danceability
# 6 = loudness
print(music.iloc[0][1], music.iloc[0][2], music.iloc[0][3], music.iloc[0][6])


print("[+] NEXT DATA: ")

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

data_sorted_dance=[]
for i in sexy_music.keys():
    print(i, " ", sexy_music[i][2])
    data_sorted_dance.append(sexy_music[i][2])
print("DATA SORTED")
print(data_sorted_dance)

### try this
print("[+] Try this")

def score_danceable():
    return sorted({(v[2], k) for k, v in sexy_music.items()}, reverse=True)

def print_dancable():
    for i in score_danceable():
        print(sexy_music[i[1]][0])

print ('[+] running print dancable')
print_dancable()

### TODO: sort the hash based on value of key music.loc[i][3]
#print (sexy_music) # debug

# for key in sorted(sexy_music.iterkeys()):
#     print "%s: %s" % (key, mydict[key])

### create a list with the values



# if music.danceability > 0.8:
#     print(music.loudness)


#import pdb; pdb.set_trace()
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
