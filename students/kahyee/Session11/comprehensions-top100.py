import pandas as pd

music = pd.read_csv("featuresdf.csv")

possible_songs = [(x,y,z) for x, y, z in zip(music.name, music.danceability, music.loudness) if y > 0.8 and z < 5.0]

def dance_key(item):
    return item[1]
    
sorted_songs = sorted(possible_songs, key= dance_key, reverse=True)

#print(sorted_songs)

answer = [sorted_songs[x][0] for x in range(5)]

print(answer)

