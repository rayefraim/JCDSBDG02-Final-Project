# JCDSBDG02-Final-Project
Final project for Job Connector Data Science Bandung batch 2 program in Purwadhika Startup and Coding School.


## Objective
- Find out what creates a song popular in Spotify
- Find out the chance of a song to be popular based on audio features or existing songs in Spotify
- Evaluate a plan or draft for a song before releasing it based on what makes song popular in Spotify
- Find new talents for the label company or endorse or any business project related

## Data Gathering
The data for the training was taken from Spotify API using Spotipy library for Python. The training data had 2,000 songs per year from 2010-2019. 
Features on this dataset are:

> - Year - Year the song was published
> - duration_ms - The duration of the track in milliseconds.
> - key - The estimated overall key of the track. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. (Range 0-11)
> - mode - Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
> - time_signature - An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).
> - acousticness - A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
> - danceability - Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
> - energy - Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
> - instrumentalness - Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
> - liveness - Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
> - loudness - The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
> - speechiness - Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
> - valence - A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
> - tempo - The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
> - popularity - The popularity of the track. The value will be between 0 and 100, with 100 being the most popular. The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are. Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity.

The example for the dataset are as follow:


## Model
#### Predicting Popularity Score
This model used Random Forest Regressor to predict the prediction of the popularity score


#### Clustering Song to Genres
The songs were clustered using KMeans clustering method. Before the features get predicted by the model, the data was normalized using Standard Scaler and then reduce the feature dimensionality using PCA with n-components = 4.



#### Simple Recommender System for Reference
To help user with real songs based on the audio features they have inputted, simple recommender system model will show 5 similar song based on their genre for user reference



## Result

### Regression Model

Using KFold to search for the best model:

| | MAE	| RMSE |	R2 Score |
|------------------|--------|------|------ |
|Linear Regression |	7.074 |	8.736 |	0.084|
|Lasso |	7.280 |	8.996 |	0.028 |
|Ridge |	7.072 |	8.734 |	0.084 |
|DecisionTreeRegressor |	9.402 |	11.890 |	-0.698 |
|RandomForestRegressor |	6.746 |	8.432  |	0.146  |
|GradientBoostingRegressor |	6.800 |	8.438  |	0.144  |
|XGBRegressor |	6.944 |	8.646 |	0.102 |
|KNeighborsRegressor	7.870	9.782	-0.148

The model with the best error score is Random Forest Regressor, and using the hyperparameter (RandomSearchCV) i decided to continue to use the default parameter since the tuning didn't show better result

The result was

|Error | Error Rate|
|---|---|
|Mean Average Error | 6.75%|
|Root Mean Square Error | 8.41%|

The model is able to predict the songs from 50-70 score, but cannot predict well for songs with more than 70. Need to explore other features to improve the score prediction


### KMeans
Clustered to 8 different genres.
The KMeans results were labelled based on their audio features and manually listen and search for the genre online.
The genres are: 
- Pop Disco Electronics
- Alternative
- Hip Hop Electronics
- Ballad
- Instrumental
- Pop Rock
- Hip Hop Disco
- R&B



## Dashboard
![Home Screen](https://i.imgur.com/VfWwyVH.jpg)
Home Screen for User

![Prediction by Audio Feature](https://i.imgur.com/kJ0N2by.jpg)
Prediction by inputting the audio features

![Result1](https://i.imgur.com/YhHAoKg.jpg)
Result from prediction by audio features

![Prediction by Existing Song](https://i.imgur.com/3dcmyO8.jpg)
Prediction from existing song in Spotify library

![Result2](https://i.imgur.com/7Jn93L0.jpg)
Result from prediction by existing song

![Visualization](https://i.imgur.com/tE64LzA.jpg)
Data Visualization for User

![About](https://i.imgur.com/5NTzed6.jpg)
About the project


