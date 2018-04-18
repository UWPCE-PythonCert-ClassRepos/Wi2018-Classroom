#!/usr/bin/env python3

import pandas as pd
music = pd.read_csv('./data/featuresdf.csv')


print(music[music.loudness > -5].sort_values(by = 'danceability', ascending = False).head(5))
