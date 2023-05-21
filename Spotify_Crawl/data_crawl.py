import os 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd
import csv
import numpy as np

client_id = '89fc26a042194e2d959c8e81dd19ac52'
client_secret = 'ab695e82870c473faae2a1851247a392'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

tempo = []
speechiness= []
loudness = []
liveness = []
instrumentalness = []
energy = []
acousticness = []
valence = []
df = pd.read_csv(r'C:\Users\dungnvh\Desktop\big data\spotify.csv')
for i in range(10000,15000):
    artist = df.loc[i,'artist_name']
    track = df.loc[i,'track_name']
    print(track )
    track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    try:
        track_id = track_id['tracks']['items'][0]['id']
    except:
        pass
    try:
        result = sp.audio_features(track_id)[0]
        tempo.append(result['tempo'])
        speechiness.append(result['speechiness'])
        loudness.append(result['loudness'])
        liveness.append(result['liveness'])
        instrumentalness.append(result['instrumentalness'])
        energy.append(result['energy'])
        acousticness.append(result['acousticness'])
        valence.append(result['valence'])
        print(i)
    except:
        tempo.append("")
        speechiness.append("")
        loudness.append("")
        liveness.append("")
        instrumentalness.append("")
        energy.append("")
        acousticness.append("")
        valence.append("")
        print(i,'error')


df['tempo'] = pd.Series(tempo)
df['speechiness'] = pd.Series(speechiness)
df['loudness'] = pd.Series(loudness)
df['liveness'] = pd.Series(liveness)
df['instrumentalness'] = pd.Series(instrumentalness)
df['energy'] = pd.Series(energy)
df['acousticness'] = pd.Series(acousticness)
df['valence'] = pd.Series(valence)

df.to_csv('final_1.csv', index = False)
print(df.head(5))
# artist= 'Moses Sumney'
# track= 'Lonely World'

