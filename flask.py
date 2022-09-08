from flask import Flask,jsonify,requests
import csv

all_articles = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]


liked_articles = []
disliked_articles = []
did_not_read_articles = []


app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })


@app.route("/liked-article",methods = ["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)

    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked-article",methods = ["POST"])
def disliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)

    return jsonify({
        "status":"success"
    }),205

@app.route("/did-not-read-article",methods = ["POST"])
def did_not_watch_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    did_not_read_articles.append(article)
    
    return jsonify({
        "status":"success"
    }),210

