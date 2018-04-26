#!/usr/bin/env python 3
"""
Bring up an interpreter and loading the data

"""
import pandas as pd 
music = pd.read_csv("featuresdf.csv")

music.head()
music.describe()

dlist = [x for idx, x 
		in music.sort_values(by='danceability', ascending=False).iterrows()
		if x.danceability > 0.8 and x.loudness < -5.0]
print(dlist)

#python pandas_activity.py
"""[id                                4Km5HrUvYTaSUfiSGPJeQ
name                Bad and Boujee (feat. Lil Uzi Vert)
artists                                           Migos
danceability                                      0.927
energy                                            0.665
key                                                  11
loudness                                         -5.313
mode                                                  1
speechiness                                       0.244
acousticness                                      0.061
instrumentalness                                      0
liveness                                          0.123
valence                                           0.175
tempo                                           127.076
duration_ms                                      343150
time_signature                                        4
Name: 48, dtype: object, id                  343YBumqHu19cGoGARUTs
name                            Fake Love
artists                             Drake
danceability                        0.927
energy                              0.488
key                                     9
loudness                           -9.433
mode                                    0
speechiness                          0.42
acousticness                        0.108
instrumentalness                        0
liveness                            0.196
valence                             0.605
tempo                             133.987
duration_ms                        210937
time_signature                          4
Name: 51, dtype: object, id                  7KXjTSCq5nL1LoYtL7XAw
name                              HUMBLE.
artists                    Kendrick Lamar
danceability                        0.904
energy                              0.611
key                                     1
loudness                           -6.842
mode                                    0
speechiness                        0.0888
acousticness                     0.000259
instrumentalness                 2.03e-05
liveness                           0.0976
valence                               0.4
tempo                              150.02
duration_ms                        177000
time_signature                          4
Name: 5, dtype: object, id                  2fQrGHiQOvpL9UgPvtYy6
name                         Bank Account
artists                         21 Savage
danceability                        0.884
energy                              0.346
key                                     8
loudness                           -8.228
mode                                    0
speechiness                         0.351
acousticness                       0.0151
instrumentalness                 7.04e-06
liveness                           0.0871
valence                             0.376
tempo                              75.016
duration_ms                        220307
time_signature                          4
Name: 94, dtype: object, id                           00lNx0OcTJrS3MKHcB80H
name                You Don't Know Me - Radio Edit
artists                                  Jax Jones
danceability                                 0.876
energy                                       0.669
key                                             11
loudness                                    -6.054
mode                                             0
speechiness                                  0.138
acousticness                                 0.163
instrumentalness                                 0
liveness                                     0.185
valence                                      0.682
tempo                                      124.007
duration_ms                                 213947
time_signature                                   4
Name: 62, dtype: object, id                  6EpRaXYhGOB3fj4V2uDkM
name                      Strip That Down
artists                        Liam Payne
danceability                        0.869
energy                              0.485
key                                     6
loudness                           -5.595
mode                                    1
speechiness                        0.0545
acousticness                        0.246
instrumentalness                        0
liveness                           0.0765
valence                             0.527
tempo                             106.028
duration_ms                        204502
time_signature                          4
Name: 38, dtype: object, id                  0VgkVdmE4gld66l8iyGjg
name                             Mask Off
artists                            Future
danceability                        0.833
energy                              0.434
key                                     2
loudness                           -8.795
mode                                    1
speechiness                         0.431
acousticness                       0.0102
instrumentalness                   0.0219
liveness                            0.165
valence                             0.281
tempo                             150.062
duration_ms                        204600
time_signature                          4
Name: 14, dtype: object, id                      3QwBODjSEzelZyVjxPOHd
name                Otra Vez (feat. J Balvin)
artists                         Zion & Lennox
danceability                            0.832
energy                                  0.772
key                                        10
loudness                               -5.429
mode                                        1
speechiness                               0.1
acousticness                           0.0559
instrumentalness                     0.000486
liveness                                 0.44
valence                                 0.704
tempo                                  96.016
duration_ms                            209453
time_signature                              4
Name: 84, dtype: object, id                  7hDc8b7IXETo14hHIHdnh
name                         Passionfruit
artists                             Drake
danceability                        0.809
energy                              0.463
key                                    11
loudness                          -11.377
mode                                    1
speechiness                        0.0396
acousticness                        0.256
instrumentalness                    0.085
liveness                            0.109
valence                             0.364
tempo                              111.98
duration_ms                        298941
time_signature                          4
Name: 36, dtype: object] """


