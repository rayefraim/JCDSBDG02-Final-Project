from flask import Flask, render_template, request
from data import keys,messages_score, dataSpotify
from prediction import prediction_regression, prediction_clustering, get_recommendation, prediction_song

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('Home_Screen.html')

@app.route('/Song_Popularity_and_Genre_Predictor_with_Reference_Recommender', methods=["GET","POST"])
def prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        popularity_score = prediction_regression(data)
        cluster_genre = prediction_clustering(data)
        list_recommendation = get_recommendation(cluster_genre)
        if popularity_score >= 60:
            message = messages_score[0]
        elif popularity_score <=50:
            message = messages_score[2]
        else:
            message = messages_score[1]
        return render_template("Predicted_popularity.html", data_dict = data, score = popularity_score, genre=cluster_genre,message_popularity = message, recommendation= list_recommendation)
    return render_template('Song_Popularity_and_Genre_Predictor_with_Reference_Recommender.html', data_keys=keys)

@app.route('/visualization')
def visualization():
    return render_template('Data_Visualisation.html', data_spotify = dataSpotify)

@app.route('/Input_Song_Name_and_Artist_Name', methods=["GET","POST"])
def prediction2():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        popularity_score2 = prediction_song(data)
        return render_template("Input_Song_Name_and_Artist_Name___Result.html", score2 = popularity_score2, title = data["track_name"], artist = data["artist_name"])
    return render_template('Input_Song_Name_and_Artist_Name.html')

@app.route('/about')
def about():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(debug=True,port=1234)
