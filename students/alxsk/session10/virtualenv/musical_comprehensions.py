'''musical comprehensions
 Find top 5 artists and song name for track (sort desc) with danceability >.8 and loudness <5.0'''

import pandas as pd
music = pd.read_csv('music.csv')


print(music[music.loudness > -5].sort_values(by = 'danceability', ascending = False).head(5))

print(music.nlargest('danceability', n = 5,))

#selection = pd.select('music', where 'danceability > 0.8')
#print(selection)
#print([x for x  in list(zip(music.danceability,  music.loudness)) if x > 0.8 and x < -5.0])

#panda way
#music.describe.t 
#music.query(' ').sorted(' ')
