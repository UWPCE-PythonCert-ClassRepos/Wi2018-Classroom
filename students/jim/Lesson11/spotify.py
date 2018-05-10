import pandas as pd

music = pd.read_csv("featuresdf.csv")

songs_we_want = [music.iloc[x] for x in range(len(music.index))
                 if music.iloc[x].danceability > 0.8 and
                 music.iloc[x].loudness < -5.0]

songs_we_want.sort(key=lambda song: song.danceability, reverse=True)

for i in songs_we_want:
    print(i.artists, "--", i[1])


# Why does i.name give the index number instead of the field value?
# Anyway I can get it with i[1] but... why?