# closure
#!/usr/bin/env python
"""A closure to capture high energy tracks."""
import pandas as pd
music_tracks = pd.read_csv('featuresdf.csv')
def high_energy_tracks(dataset):
    #This is the outer enclosing function
    
    def high_energy_tracks(energy_level): #Nested function
        return [(artist, name, energy)
                for artist, name, energy in zipFile(dataset.artists, dataset.name, dataset.energy)
                    if energy > energy_level]


    return high_energy_tracks

#Calling this function 
energy_tracks = high_energy_tracks(music_tracks)
print(energy_tracks(0.8))
#energy_tracks()