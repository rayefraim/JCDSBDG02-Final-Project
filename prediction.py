import pickle
from pandas import DataFrame, get_dummies, read_csv
from data import columns_regression, columns_cluster, dictGenre

### Import Spotipy API and authenticating
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = '9d6662eb9b5d4385a41336390cd9053e'
secret = 'd36d9e2db9fb4da8b4e15cf72a9835ae'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

model_regression = pickle.load(open("regression.sav",'rb'))
model_clustering = pickle.load(open("clustering.sav","rb"))
scaler = pickle.load(open('scaler.sav','rb'))
pca = pickle.load(open('pca.sav','rb'))
kmeans = pickle.load(open("kmeans.sav","rb"))

def prediction_regression(data):
    df = DataFrame(data,index=[0])
    df[["danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","duration_ms"]] = df[["danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","duration_ms"]].astype(float)
    df = get_dummies(data=df,columns=["mode","key",'time_signature'])
    df = df.reindex(columns=columns_regression, fill_value=0)
    result = model_regression.predict(df)
    return int(round(result[0]))

def prediction_clustering(data):
    df_cluster = DataFrame(data,index=[0])
    df_cluster[["danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","duration_ms"]] = df_cluster[["danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","duration_ms"]].astype(float)
    df_cluster = get_dummies(data=df_cluster,columns=["mode","key",'time_signature'])
    df_cluster = df_cluster.reindex(columns=columns_cluster, fill_value=0)
    step1 = scaler.transform(df_cluster)
    step2 = pca.transform(step1)
    result = kmeans.predict(step2)
    convert = dictGenre[result[0]]
    return convert

def get_recommendation(genre):
    df_rec = read_csv("Spotify Full Data with Genre.csv")
    index_song = df_rec[df_rec["genre"] == genre].sort_values(by="popularity",ascending=False).head(5).index

    track_name = []
    artist_name = []
    track_id = []
    cover_link = []
    spotify_link = []

    for item in index_song:
        song = df_rec.iloc[item]
        track_name.append(song["track_name"])
        artist_name.append(song["artist_name"])
        track_id.append(song["track_id"])
        spotify = "https://open.spotify.com/track/" + str(song["track_id"])
        spotify_link.append(spotify)
        cover_link.append(sp.track(song["track_id"])['album']['images'][1]['url'])
    
    return track_name, artist_name, track_id, cover_link, spotify_link

def prediction_song(data):
    id = sp.search(q="artist:{} track:{}".format(data["artist_name"],data["track_name"]),type="track",limit=1)['tracks']["items"][0]["id"]
    audio_features = sp.audio_features(id)[0]
    data1 = DataFrame(audio_features,index=[0])
    data1 = data1.drop(["type","id","uri","track_href","analysis_url"],axis=1)
    data1[["key","mode","time_signature"]] = data1[["key","mode","time_signature"]].astype('object')
    data1 = get_dummies(data=data1,columns=["mode","key",'time_signature'])
    data1 = data1.reindex(columns=columns_regression, fill_value=0)
    result = model_regression.predict(data1)
    result = int(round(result[0]))
    cover = sp.track(id)['album']['images'][1]['url']
    spotify = "https://open.spotify.com/track/" + str(id)
    name = data["artist_name"]
    track = data["track_name"]
    return result, cover, spotify, name, track

