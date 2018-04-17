import pandas as pd

music = pd.read_csv("featuresdf.csv")

print(music.head())
print(music.describe())

def zip_music():
	dance_zip = [(artists, name, danceability, loudness) for (artists, name, danceability, loudness) in zip(music.artists, music.name, music.danceability, music.loudness) if danceability > 0.8 and loudness < -5.0]
	#print(dance_zip)
	return dance_zip

def sort_zip():
	music_zip = zip_music()
	music_zip_sorted = sorted(music_zip, key = lambda x: x[2], reverse = True)
	return music_zip_sorted 

for music_entry in sort_zip():
	print(music_entry)

print("Top 5 Songs:")
for i in range(0, 6):
	print(sort_zip())

