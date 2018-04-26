import pandas as pd

class artist_track:
    def __init__(self):
        self.music = pd.read_csv("featuresdf.csv")
        self.names = [name for name in self.music.name]
        self.artists = [artist for artist in self.music.artists]
        self.myList = zip(self.names, self.artists)	
    def __iter__(self):
        return self
    def __next__(self):
        for val in self.myList:
            if val[1] == 'Ed Sheeran':
                return val[0]			
				
				
				
if __name__ == '__main__':
    a = artist_track()
    for i in range(5):
        favorite_artists_track = next(a)
        if favorite_artists_track != None:
        	print(favorite_artists_track)