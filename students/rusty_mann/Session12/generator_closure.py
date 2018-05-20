
import pandas as pd
music = pd.read_csv("featuresdf.csv")


#generates tracks by Ed Sheeran 
good_music = [(yield name, artists) for name, artists in zip(music.name, music.artists) if artists == "Ed Sheeran"]

next(good_music)
#Tracks generated:
#Shape of You
#Castle on the Hill
#Galway Girl
#Perfect



def high_energy(df):
    def find_high_energy(energy_level1=0.8, energy_level2=1.0):
        for artists, name, energy in zip(df.artists, df.name, df.energy):
            if energy_level2 > energy > energy_level1:
                line = (artists, name, energy)
                print(line)
    return find_high_energy

high_energy_songs = high_energy(music)
high_energy_songs()

#Tracks returned:
#('Luis Fonsi', 'Despacito - Remix', 0.815)
#('Post Malone', 'Congratulations', 0.812)
#('Jason Derulo', 'Swalla (feat. Nicki Minaj & Ty Dolla $ign)', 0.8170000000000001)
#('Ed Sheeran', 'Castle on the Hill', 0.8340000000000001)
#('Imagine Dragons', 'Thunder', 0.81)
#('Danny Ocean', 'Me Rehúso', 0.804)
#('Ed Sheeran', 'Galway Girl', 0.8759999999999999)
#('The Weeknd', 'I Feel It Coming', 0.813)
#('Starley', 'Call On Me - Ryan Riback Extended Remix', 0.843)
#('Martin Jensen', 'Solo Dance', 0.836)
#('Enrique Iglesias', 'SUBEME LA RADIO', 0.823)
#('Maggie Lindemann', 'Pretty Girl - Cheat Codes X CADE Remix', 0.868)
#('Bruno Mars', '24K Magic', 0.8029999999999999)
#('Katy Perry', 'Chained To The Rhythm', 0.8009999999999999)
#('Wisin', 'Escápate Conmigo', 0.8640000000000001)
#('Steve Aoki', 'Just Hold On', 0.932)
#('CNCO', 'Reggaetón Lento (Bailemos)', 0.838)
#('The Vamps', 'All Night', 0.809)
#('The Chainsmokers', "Don't Let Me Down", 0.8590000000000001)