import pandas as pd

music = pd.read_csv("featuresdf.csv")

print("Here are the artists in the spotify list: ")
print(music.artists)

def hasNext(index):
    if index < len(music):
        return True
    else:
        return False

def favorite_artist(name):
    index = 0
    while hasNext(index):
        if name == music.artists[index].lower():
            yield music.name[index]
        index +=1

def get_name():
    artist_name = input("Enter name for musical artist: ").strip().lower()
    return artist_name

artist = get_name()
artist_gen = favorite_artist(artist)
print("\nThe song names for {}:".format(artist.title()))

for i in range(0,len(music)):
    try:
        print(next(artist_gen))
    except StopIteration as e:
        print("\nEnd of music database")
        break
