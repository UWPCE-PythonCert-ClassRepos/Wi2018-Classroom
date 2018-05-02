#!/usr/bin/env python3
import os
import pandas as pd

file_to_copy = os.path.normpath("/Users/jchristo/Desktop/PythonProjects/Wi2018-Classroom/students/jchristo/session11/featuresdf.csv") #for Mac
music = pd.read_csv(file_to_copy)

#Assignment 2:
# generator comp using Ed Sheeran tracks
track_list = zip(music.artists,music.name)
ed_sheeran_tracks_1 = list(filter(lambda x: x[0] == 'Ed Sheeran', track_list))
ed_sheeran_tracks_2 = [name for (artist, name) in track_list if artist == 'Ed Sheeran']
ed_sheeran_tracks_3 = (name for (artist, name) in track_list if artist == 'Ed Sheeran')

def track_list_generator(ed_sheeran_tracks_1):
    for track in ed_sheeran_tracks_1:
        yield track

def track_list_generator_2(ed_sheeran_tracks_2):
    for track in ed_sheeran_tracks_2:
        yield track

def track_list_generator_3(ed_sheeran_tracks_3):
    for track in ed_sheeran_tracks_3:
        print(track)

#testing the first list
songs = track_list_generator(ed_sheeran_tracks_1)
for song in songs:
    print(song)

#testing the second list
songs2 = track_list_generator_2(ed_sheeran_tracks_2)
for song in songs2:
    print(song)

#testing the third list
songs3 = track_list_generator_3(ed_sheeran_tracks_3)
for song in songs3:
    print(song)

"""
These are all the Ed Sheeran tracks:
Shape of You
Castle on the Hill
Galway Girl
Perfect
"""


#find high energy tracks with closure , energy > 0.8
music_list = zip(music.artists, music.name, music.energy)
high_energy_tracks = [(artist, name, energy) for (artist, name, energy) in music_list]
#the list below was used for testing
post_malone_tracks = [(artist, name, energy) for (artist, name, energy) in music_list if artist == 'Post Malone']

def track_energy_closure(energy=0):
    def get_tracks(track_list):
        #return [x for x in track_list if x[2] > energy]
        return list(filter(lambda x: x[2] > energy, track_list))
    return get_tracks

#print sorted list of songs with energy > 0.8
high_energy = track_energy_closure(0.8)
print(sorted(high_energy(track_list2), key=lambda x: x[2], reverse=True))
l = [sorted(high_energy(track_list2), key=lambda x: x[2], reverse=True)]

#print sorted list of post malone songs with energy > 0.5, done for testing
high_energy2 = track_energy_closure(0.5)
print(sorted(high_energy2(post_malone_tracks),key=lambda x: x[2],reverse=True))
l2 = [sorted(high_energy2(post_malone_tracks),key=lambda x: x[2],reverse=True)]

#Below is the output from the sorted list with energy > 0.8
"""
('Steve Aoki', 'Just Hold On', 0.932),
('Ed Sheeran', 'Galway Girl', 0.8759999999999999),
('Maggie Lindemann', 'Pretty Girl - Cheat Codes X CADE Remix', 0.868),
('Wisin', 'Escápate Conmigo', 0.8640000000000001),
('The Chainsmokers', "Don't Let Me Down", 0.8590000000000001),
('Starley', 'Call On Me - Ryan Riback Extended Remix', 0.843),
('CNCO', 'Reggaetón Lento (Bailemos)', 0.838),
('Martin Jensen', 'Solo Dance', 0.836),
('Ed Sheeran', 'Castle on the Hill', 0.8340000000000001),
('Enrique Iglesias', 'SUBEME LA RADIO', 0.823),
('Jason Derulo', 'Swalla (feat. Nicki Minaj & Ty Dolla $ign)', 0.8170000000000001),
('Luis Fonsi', 'Despacito - Remix', 0.815),
('The Weeknd', 'I Feel It Coming', 0.813),
('Post Malone', 'Congratulations', 0.812),
('Imagine Dragons', 'Thunder', 0.81),
('The Vamps', 'All Night', 0.809),
('Danny Ocean', 'Me Rehúso', 0.804),
('Bruno Mars', '24K Magic', 0.8029999999999999),
('Katy Perry', 'Chained To The Rhythm', 0.8009999999999999)]
"""