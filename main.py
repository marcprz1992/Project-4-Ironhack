from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import tools1.sql_queries as esecuele
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# GET ENDPOINTS: SQL 
# SQL get everything
@app.route("/sql/")
def sql ():
    return jsonify(esecuele.get_everything())

@app.route("/sql/<title>", )
def everything_from_each_game (title):
    return jsonify(esecuele.get_everything_from_videogame(title))


#@app.route("/sa/<name>/", )
#def sa_from_character (name):
    everything = esecuele.get_just_dialogue(name)
    #return jsonify(everything)
    return jsonify([sia.polarity_scores(i["dialogue"])["compound"] for i in everything])



# 1) All info for those videogames rated more than 7
@app.route("/sql/reviews", )
def get_onñly_biggest_reviews ():
    return jsonify(esecuele.get_biggest_reviews ())

# QUERY 2: Average rating by developer when rating is bigger than 7
@app.route("/sql/average/by/developer", )
def get_only_avg_by_developer ():
    return jsonify(esecuele.get_average_by_developer ())

# QUERY 3: all titles with compound bigger than 0.5
@app.route("/sql/titles/compound", )
def get_only_all_titles_bigger_compound():
    return jsonify(esecuele.get_all_titles_bigger_compound())

# QUERY 4: all info where possitivity bigger than 0.2
@app.route("/sql/info/by/positivity", )
def get_only_all_info_where_bigger_positivity():
    return jsonify(esecuele.get_all_info_where_bigger_positivity())

# QUERY 5: all info for all videogames launched in a given year
@app.route("/sql/<year>/launches", )
def get_only_all_info_given_year(year):
    return jsonify(esecuele.get_all_info_given_year(year))

# QUERY 6: Number of titles launched by genre limit 20
@app.route("/sql/genre/launches", )
def get_only_count_titles_by_genre():
    return jsonify(esecuele.get_count_titles_by_genre())

# QUERY 7: Number of titles launched by publisher
@app.route("/sql/publisher/launches", )
def get_only_count_titles_by_publisher():
    return jsonify(esecuele.get_count_titles_by_publisher())

# QUERY 8: info for specific videogame (e.g. Mario games, passing a string)
@app.route("/sql/info/<title>", )
def get_only_info_of_videogame_s(title):
    return jsonify(esecuele.get_info_of_videogame_s(title))


# QUERY 9: Average negative sentiment by genre TOP 20
@app.route("/sql/genre/avgsentiment", )
def get_only_avg_negative_by_genre():
    return jsonify(esecuele.get_avg_negative_by_genre())

# QUERY 10: Key average info by developer (searching for it)
@app.route("/sql/developer/avginfo", )
def get_only_avg_info_by_developer(developer):
    return jsonify(esecuele.get_avg_info_by_developer(developer))

# QUERY 11: Key info by title
@app.route("/sql/title/keyinfo", )
def get_only_key_info_by_title():
    return jsonify(esecuele.get_key_info_by_title())

# QUERY 12: Key title info by specific searched developer
@app.route("/sql/keyinfo/<developer>", )
def get_only_all_titles_and_more_by_developer(developer):
    return jsonify(esecuele.get_all_titles_and_more_by_developer(developer))

# Change that one as equal to above!!!
# QUERY 13 Number of titles launched by searched developer by searched year
#@app.route("/sql/developer/year", )
#def get_only_all_titles_and_more_by_developer(developer,year):
    return jsonify(esecuele.get_all_titles_and_more_by_developer(developer,year))    

# QUERY 14 Top 10 games launched in searched year by negativity
@app.route("/sql/top10/<year>", ) 
def get_only_top_ten_games_by_negativity_by_given_year(year):
    return jsonify(esecuele.get_top_ten_games_by_negativity_by_given_year(year)) 

####### POST
@app.route("/insertrow", methods=["POST"])
def try_post ():
    # Decoding params
    my_params = request.args
    title = my_params["title"]
    game_url = my_params["game_url"]
    image_url = my_params["image_url"]
    system = my_params["system"]
    publisher = my_params["publisher"]
    developer = my_params["developer"]
    genre = my_params["genre"]
    release_date = my_params["release_date"]
    review = my_params["review"]
    review_conclusion = my_params["review_conclusion"]
    rating = my_params["rating"]
    neg = my_params["neg"]
    neu = my_params["neu"]
    pos = my_params["pos"]
    compound = my_params["compound"]
    index_pandas = my_params["index_pandas"]

    # Passing to my function: do the inserr
    esecuele.insert_one_row(title, game_url, image_url, system, publisher, developer, genre, release_date, review, review_conclusion, rating, neg, neu, pos, compound, index_pandas)
    return f"Query succesfully inserted"


if __name__ == "__main__":
    app.run(port=9000, debug=True)