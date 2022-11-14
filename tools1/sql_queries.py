from config.sql_connection import engine
import pandas as pd

def get_everything ():
    query = """SELECT * FROM reviews;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_videogame (title):
    query = f"""SELECT * 
    FROM reviews
    WHERE title = '{title}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_review (title):
    query = f"""SELECT review 
    FROM reviews
    WHERE title = '{title}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# 1) All info for those videogames rated more than 7
def get_biggest_reviews ():
    query = f"""SELECT * 
    FROM nintendo_switch_reviews.reviews
    WHERE rating > 7
    ORDER BY rating DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# QUERY 2: Average rating by developer when rating is bigger than 7
def get_average_by_developer ():
    query = f"""SELECT developer, ROUND(AVG(rating),1) as 'Average Rating' 
    FROM reviews
    WHERE rating > 7
    GROUP BY developer
    ORDER BY ROUND(AVG(rating),1) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")



# QUERY 3: all titles with compound bigger than 0.5
def get_all_titles_bigger_compound():
    query = f"""SELECT title,compound
    FROM reviews
    WHERE compound > 0.5
    ORDER BY compound DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# QUERY 4: all info where possitivity bigger than 0.2
def get_all_info_where_bigger_positivity():
    query = f"""SELECT *
    FROM reviews
    WHERE pos > 0.2
    ORDER BY pos DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# QUERY 5: all info for all videogames launched in a given year
def get_all_info_given_year(year):
    query = f"""SELECT *
    FROM reviews
    WHERE release_date LIKE '%%{year}%%'
    ORDER BY title DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


# QUERY 6: Number of titles launched by genre limit 20
def get_count_titles_by_genre():
    query = f"""SELECT genre, count(title) as 'Number of titles launched'
    FROM reviews
    GROUP BY genre
    ORDER BY count(title) DESC
    LIMIT 20;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# QUERY 7: Number of titles launched by publisher
def get_count_titles_by_publisher():
    query = f"""SELECT publisher, count(title) as 'Number of titles launched'
    FROM reviews
    GROUP BY publisher
    ORDER BY count(title) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# QUERY 8: info for specific videogame (e.g. Mario games, passing a string)
def get_info_of_videogame_s(title):
    query = f"""SELECT title, developer, release_date, rating, compound
    FROM reviews
    WHERE title LIKE '%%{title}%%'
    ORDER BY rating DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# QUERY 9: Average negative sentiment by genre
def get_avg_negative_by_genre():
    query = f"""SELECT genre, AVG(neg) as 'Average negative sentiment'
    FROM reviews
    GROUP BY genre
    ORDER BY AVG(neg) ASC
    LIMIT 20;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# QUERY 10: Key average info by developer (searching for it)
def get_avg_info_by_developer(developer):
    query = f"""SELECT developer, AVG(neg) as 'Average negative sentiment', AVG(pos) as 'Average positive sentiment', AVG(compound) as 'Average compound'
    FROM reviews
    WHERE developer LIKE '%%{developer}%%'
    GROUP BY developer
    ORDER BY AVG(neg) ASC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# QUERY 11: Key info by title
def get_key_info_by_title():
    query = f"""SELECT title, developer, neg, pos, compound
    FROM reviews
    ORDER BY compound ASC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# QUERY 12: Key title info by specific searched developer
def get_all_titles_and_more_by_developer(developer):
    query = f"""SELECT title, developer, rating, neg, pos, compound
    FROM reviews
    WHERE developer LIKE '%%{developer}%%'
    ORDER BY rating DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# QUERY 13 Number of titles launched by searched developer by searched year
def get_all_titles_and_more_by_developer_and_year(developer,year):
    query = f"""SELECT developer,COUNT(title) as 'Number of titles launched'
    FROM reviews
    WHERE release_date LIKE '%%{year}%%'
    AND developer LIKE '%%{developer}%%'
    GROUP BY developer
    ORDER BY count(title) DESC;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

# QUERY 14 Top 10 games launched in searched year by negativity 
def get_top_ten_games_by_negativity_by_given_year(year):
    query = f"""SELECT title, neg, pos, compound
    FROM reviews
    WHERE release_date LIKE '%%{year}%%'
    ORDER BY neg DESC
    LIMIT 10;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def insert_one_row (id,title, game_url, image_url, system, publisher, developer, genre, release_date, review, review_conclusion, rating, neg, neu, pos, compound, index_pandas):
    query = f"""INSERT INTO reviews
     (id, title, game_url, image_url, `system`, publisher, developer, genre, release_date, review, review_conclusion, rating, `neg`, neu, pos, compound, index_pandas) 
        VALUES ('{id}','{title}', '{game_url}','{image_url}','{system}','{publisher}','{developer}','{genre}','{release_date}','{review}','{review_conclusion}',{rating},{neg},{neu},{pos},{compound},'{index_pandas}');
    """
    engine.execute(query)
    return f"Correctly introduced!"