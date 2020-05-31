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
![](https://i.imgur.com/5hKd9do.png)

## Data Pre-Processing

There are few problems from the dataset :
1. What does time_signature 0, 1, and 5 means?
2. There are tracks with long duration than most usual song
3. The data seems to include podcast/talkshow, which shouldn't be count as music. While instrumental should be okay
4. There are binaural sounds in the data, which people may listen for therapic purpose. We'll try to filter out those

The solutions:
1. Dropping the data with time signature 0,1,5 since it doesn't make sense, it seems there is issue with the time signature recognition from several forum. Even after manual check, the time signature were combination of 4/4 or even 3/4.
2. Create a range for duration that make sense for a music duration using outlier from upper limit.
3. Using "speechiness" features to filter out the talkshow/podcast with the speechiness score above 0.66
4. Using "tempo" features to filter out the binaural recording. Song under lower limit were dropped


## Model
#### Predicting Popularity Score
This model used Random Forest Regressor to predict the prediction of the popularity score


#### Clustering Song to Genres
The songs were clustered using KMeans clustering method. Before the features get predicted by the model, the data was normalized using Standard Scaler and then reduce the feature dimensionality using PCA with n-components = 4 from the variance drop-off point.



#### Simple Recommender System for Reference
To help user with real songs based on the audio features they have inputted, simple recommender system model will show 5 similar song based on their genre for user reference



## Result

### Regression Model

Using KFold to search for the best model with 5 fold CV:

| | MAE	| RMSE |	R2 Score |
|------------------|--------|------|------ |
|Linear Regression |	7.074 |	8.736 |	0.084|
|Lasso |	7.280 |	8.996 |	0.028 |
|Ridge |	7.072 |	8.734 |	0.084 |
|DecisionTreeRegressor |	9.402 |	11.890 |	-0.698 |
|RandomForestRegressor |	6.746 |	8.432  |	0.146  |
|GradientBoostingRegressor |	6.800 |	8.438  |	0.144  |
|XGBRegressor |	6.944 |	8.646 |	0.102 |
|KNeighborsRegressor	|	7.870	|	9.782	|	-0.148	|

The model with the best error score is Random Forest Regressor, and using the hyperparameter (RandomSearchCV) i decided to continue to use the default parameter since the tuning didn't show better result

The result was

|Error | Error Rate|
|---|---|
|Mean Average Error | 6.75%|
|Root Mean Square Error | 8.41%|

The model is able to predict the songs from 50-70 score, but cannot predict well for songs with more than 70. Need to explore other features to improve the score prediction


### KMeans
Clustered to 9 different genres.
The KMeans results were labelled based on their audio features and manually listen and search for the genre online.
The result from the clustering with features average as the parameter

|	|danceability	|	energy	|	loudness	|	acousticness	|	instrumentalness	|	liveness	|	valence	|	tempo	|	speechiness	|
|---	|-------	|-------	|-------	|-------	|--------	|-------	|-------	|--------	|--------	|
|cat0	|	0.7038	|	0.7011	|	-5.6968	|	0.1268	|	0.0000	|	0.1291	|	0.6201	|	119.4799	|	0.0872	|
|cat1	|	0.5702	|	0.3968	|	-9.6268	|	0.5918	|	0.0011	|	0.1120	|	0.3152	|	109.5219	|	0.0398	|
|cat2	|	0.7299	|	0.6890	|	-5.7839	|	0.1317	|	0.0000	|	0.1282	|	0.6010	|	117.7829	|	0.1287	|
|cat3	|	0.5296	|	0.5455	|	-6.8413	|	0.3893	|	0.0000	|	0.1326	|	0.4351	|	131.9123	|	0.0454	|
|cat4	|	0.2937	|	0.0872	|	-23.3402	|	0.9578	|	0.9118	|	0.1040	|	0.1010	|	94.9623	|	0.0423	|
|cat5	|	0.2813	|	0.1250	|	-21.5246	|	0.9377	|	0.8544	|	0.1045	|	0.1115	|	102.4899	|	0.0437	|
|cat6	|	0.5215	|	0.7536	|	-5.4285	|	0.0553	|	0.0000	|	0.1955	|	0.3824	|	129.9244	|	0.0501	|
|cat7	|	0.5404	|	0.7725	|	-5.2470		|0.0457	|	0.0001	|	0.2112	|	0.3775	|	129.9971	|	0.0655	|
|cat8	|	0.5910	|	0.4296	|	-9.5420	|	0.5084	|	0.0080	|	0.1136	|	0.2814	|	106.1739	|	0.0532	|
  
The genres are: 
| Category | Genre |
| ------- | ------ |
| cat0 | Pop Disco Electronics |
| cat1 | Alternative |
| cat2 | Hip Hop Electronics |
| cat3 | Ballad |
| cat4 | Instrumental |
| cat5 | Intstrumental |
| cat6 | Pop Rock |
| cat7 | Hip Hop Disco |
| cat8 | R&B |



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


