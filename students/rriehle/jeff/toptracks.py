#!/usr/bin/env python3
import os
import pandas as pd

file_to_copy = os.path.normpath("featuresdf.csv") #for Mac
music = pd.read_csv(file_to_copy)

def get_music(a,n,d,l):
    good_music = []
    for artist,name,danceability,loudness in zip(music.artists,music.name,music.danceability,music.loudness):
        if danceability > 0.8 and loudness < -5.0:
            line = (artist, name, danceability, loudness)
            good_music.append(line)
    return good_music

def music_key(good_music):
    return good_music[2]

good_music = get_music(music.artists,music.name,music.danceability,music.loudness)
music_key(good_music)

#list comp way from for loop above
quiet_yet_dancey = [(artist,name,danceability,loudness) for (artist,name,danceability,loudness) in zip(music.artists,music.name,music.danceability,music.loudness) if danceability > 0.8 and loudness < -5.0]

"""
Top songs based on criteria:
Headers: Artist, Song, Danceability, Loudness
[('Migos', 'Bad and Boujee (feat. Lil Uzi Vert)', 0.927, -5.313),
('Drake', 'Fake Love', 0.927, -9.433),
('Kendrick Lamar', 'HUMBLE.', 0.904, -6.8420000000000005),
('21 Savage', 'Bank Account', 0.884, -8.228),
('Jax Jones', "You Don't Know Me - Radio Edit", 0.8759999999999999, -6.053999999999999),
('Liam Payne', 'Strip That Down', 0.8690000000000001, -5.595),
('Future', 'Mask Off', 0.833, -8.795),
('Zion & Lennox', 'Otra Vez (feat. J Balvin)', 0.8320000000000001, -5.428999999999999),
('Drake', 'Passionfruit', 0.809, -11.377)]
"""

#generator comp using Ed Sheeran tracks
ed_sheeran_tracks = [name for (artist,name) in zip(music.artists,music.name) if artist == 'Ed Sheeran']
ed_sheeran_tracks_2 = (name for (artist,name) in zip(music.artists,music.name) if artist == 'Ed Sheeran')

def track_list_generator(track_list):
    for track in track_list:
        yield track

# def track_list_generator_2(track_list):
#     # num_of_tracks = 0
#     # while num_of_tracks < len(track_list):
#         for track in track_list:
#             print(track)
#             # num_of_tracks +=1


def track_list_generator_2(track_list):
    for track in track_list:
        return track


track_list_generator(ed_sheeran_tracks)
track_list_generator(ed_sheeran_tracks_2) #can call next on this to iterate

track_list_generator_2(ed_sheeran_tracks)
track_list_generator_2(ed_sheeran_tracks_2)

"""
These are all the Ed Sheeran tracks:
Shape of You
Castle on the Hill
Galway Girl
Perfect
"""


#find high energy tracks with closure , energy > 0.8
track_list = [(artist,name,energy) for (artist,name,energy) in zip(music.artists,music.name,music.energy)]
#the list below was used for testing
post_malone_tracks = [(artist,name,energy) for (artist,name,energy) in zip(music.artists,music.name,music.energy) if artist == 'Post Malone']


def track_energy_closure(energy):
    def get_tracks(track_list):
        # return [x for x in track_list if x[2] > energy]
        return list(filter(lambda x: x[2] > energy, track_list))  # can't get this to print the string value
    return get_tracks


#print sorted list of songs with energy > 0.8
high_energy_tracks = track_energy_closure(0.8)


print(sorted(high_energy_tracks(track_list),key=lambda x: x[2],reverse=True))
# l = [sorted(high_energy_tracks(track_list),key=lambda x: x[2],reverse=True)]

#print sorted list of songs with energy > 0.5, done for testing
# high_energy_tracks = track_energy_closure(0.5)
# print(sorted(high_energy_tracks(track_list),key=lambda x: x[2],reverse=False))
# l2 = [sorted(high_energy_tracks(track_list),key=lambda x: x[2],reverse=False)]

#print sorted list of post malone songs with energy > 0.5, done for testing
# high_energy_tracks = track_energy_closure(0.5)
# print(sorted(high_energy_tracks(post_malone_tracks),key=lambda x: x[2],reverse=True))
# l3 = [sorted(high_energy_tracks(post_malone_tracks),key=lambda x: x[2],reverse=True)]

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

