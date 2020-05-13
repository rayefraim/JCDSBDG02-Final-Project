keys = ["C","C#","D","D#","E","F","F#",'G',"G#","A","A#","B"]
columns_regression = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
       'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms',
       'mode_1.0', 'key_1.0', 'key_2.0', 'key_3.0', 'key_4.0', 'key_5.0',
       'key_6.0', 'key_7.0', 'key_8.0', 'key_9.0', 'key_10.0', 'key_11.0',
       'time_signature_4.0']
columns_cluster = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
       'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms',
       'key_0.0', 'key_1.0', 'key_2.0', 'key_3.0', 'key_4.0', 'key_5.0',
       'key_6.0', 'key_7.0', 'key_8.0', 'key_9.0', 'key_10.0', 'key_11.0',
       'mode_0.0', 'mode_1.0', 'time_signature_3.0', 'time_signature_4.0']
dictGenre = {0 : "Pop Disco Electronics",
    1 : "Alternative",
    2 : "HipHop Electronics",
    3 : "Ballad",
    4 : "Instrumental",
    5 : "Instrumental",
    6 : "Pop Rock",
    7 : "HipHop Disco",
    8 : "R&B"}
messages_score = [
    "Your song have a high probability to be a popular or have lot of audio feature similarity with hit songs.",
    "Your song have the average audio features with most songs out there in Spotify. ",
    "Your song are popularity score are far below the average score. Maybe your song is very unique or just not the preference of spotify's user.If you want to get more popularity, according to the data, dance song and high energy song usually are more popular in Spotify."
]

