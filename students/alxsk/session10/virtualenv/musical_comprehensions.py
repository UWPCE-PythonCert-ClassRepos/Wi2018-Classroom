'''musical comprehensions
 Find top 5 artists and song name for track (sort desc) with danceability >.8 and loudness <5.0'''

import pandas as pd
music = pd.read_csv('music.csv')


print(music[music.loudness > -5].sort_values(by = 'danceability', ascending = False).head(5))



