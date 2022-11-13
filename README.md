# Nintendo Switch Videogames Sentiment Review

## Objective
As part of our fourth project in the Data Analytics bootcamp, we have been tasked the following objectives:

1) Find or create a database with reviews, comments, actual text where we can do some sentiment analysis using the different methods we have learned in class

2) Upload the final database we end up with to MySQL Workbench

3) Create Python functions that run SQL queries in order to serve the data we want to see

4) Create an API through Flask and use our terminal and the functions we created so we can practice some "get" and some "post" requests as if we wanted to access our own API as a external user - i.e. understand how the API works from inside


## Database chosen

The database that has been used for this project is a public database from Kaggle (add link) about Nintendo Switch videogames and the official review about each of them that has been done by ADD LINK to their website.

SCREENSHOT1 and 2 OF KAGGLE

## Data cleaning & Sentiment Analysis

The database itself was pretty clean already, but some extra data that was not very useful for this project has been removed in order to make the final output simpler.

With regards to the sentiment analysis, the Sentiment Intensity Analyzer (sia) from Vader has been applied to all the videogames review in order to get how positive, negative, neutral as well as the compound of each game review is.

This is an example of what the final database with the sentiment analysis included looks like:

SCREENSHOT3 and 4

## Uploading the database into MySQL

Once we have got all the data to use for this project, we were tasked to upload this information to MySQL so we can self-serve the data as much as we want.

There were some barriers to this part of the process given the way the information was initially collated vs. the requirements from MySQL to get all the information in a specific format, but after some challenges the information was uploaded properly! This is an example of what the database looked like in MySQL:

SCREENSHOT5


## Python functions running SQL queries

Now that the data is also available in MySQL, I decided to run some SQL queries through Python - by establishing the connection to SQL accordingly - so I could serve the SQL data in Python. An example of one of the functions I used would be the following:

SCREENSHOT6


## API creation

Once the queries have been created, I did set up an API using Flask through my own terminal so I could test whether the API could work publicly - as long as you have access to it - and that all the queries that were initially created in Python could be executed by external users if accessing the API with the right accesses.

The way the data is visualised in both Google Chrome and Mozilla Firefox is slightly different, so the following two screenshots are just showing the differences:

If accessing the API via Chrome:

SCREENSHOT7

If accessing the API via Firefox:

SCREENSHOT8

The way external users could access this - test - API is the following:

a) Get actual access to the API / url

b) Read the documentation - that has not been pulled together for this project given it is only a test - so users know what information this API can retrieve as well as how they need to access to it by playing with the url (e.g. searching for specific information of a videogame publisher).

c) The list of queries, which include the information users can retrieve, is in the sql_queries.py file

## Examples: Getting some data as 'users'




## Conclusions

## Key documents/deliverables








