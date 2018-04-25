import pandas as pd

music = pd.read_csv("featuresdf.csv")

#Pandas native method
dance_vol = music[(music.danceability >= 0.8) & (music.loudness > -5)]

sorted_dance_vol = dance_vol.sort_values(by = ['danceability'], ascending=False)

final_df = sorted_dance_vol[['artists', 'name', 'danceability', 'loudness']]

final_df


#for loop method
def dance_vol(df):
    good_music = []
    for artists, name, danceability, loudness in zip(music.artists, music.name, music.danceability, music.loudness):
        if danceability >= 0.8 and loudness > -5:
            line = (artists, name, danceability, loudness)  
            good_music.append(line)
    return good_music

all_good_music = dance_vol(music)
sorted_music = sorted(all_good_music, key=lambda x: x[2], reverse=True)

sorted_music


#Comprehension method
good_music = [(artists, name, danceability, loudness) for artists, name, danceability, loudness 
in zip(music.artists, music.name, music.danceability, music.loudness) if danceability >= 0.8 and loudness > -5]

def sort_by_danceability(item):
    return item[2]
good_music.sort(key = sort_by_danceability, reverse=True)

good_music