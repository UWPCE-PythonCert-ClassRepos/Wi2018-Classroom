import pandas as pd 

music = pd.read_csv("featuresdf.csv")

def energy():
	def getValues(level = 0.0):
		filtered_list =  [(artist, song, energy) for (artist, song, energy) in zip(music.artists, music.name, music.energy) if energy > level]
		return filtered_list
	return getValues


print("Tracks with energy greater than 0.8")
eng_close = energy()

for music_entry in eng_close(0.8):
	print(music_entry)

print("\nTracks with energy greater than 0.9")
eng_close2 = energy()

for music_entry in eng_close2(0.9):
	print(music_entry)
