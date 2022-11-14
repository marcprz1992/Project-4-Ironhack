import pandas as pd
import sqlalchemy as alch
from getpass import getpass
import re
import numpy as np
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import stylecloud
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from IPython.display import Image
import wordcloud as wc

# Function 1: Getting the wordcloud for a given txt file in a given location
def get_a_cool_gamepad_visual(a,b):  
    path_txt = a
    path_visual = b
    stylecloud.gen_stylecloud(file_path=f"{path_txt}",
                              icon_name='fas fa-gamepad',
                              colors=['#ffdb4d', '#ff0000', '#e74c3c'],
                              background_color='black',
                              output_name = f"{path_visual}")
    return Image(filename=f"{path_visual}") 



# Function 2: Getting the wordcloud for a given dataframe in a given location
def get_a_cool_gamepad_visual_from_df(df,index,path_visual):  
    df2 = df["review"][f"{index}"]
    stylecloud.gen_stylecloud(file_path=f"{df2}",
                              icon_name='fas fa-gamepad',
                              colors=['#ffdb4d', '#ff0000', '#e74c3c'],
                              background_color='black',
                              output_name = f"{path_visual}")
    return Image(filename=f"{path_visual}") 

# Function 3: Getting the wordcloud for a given videogame in a given location (and a given dataframe, in my case the videogame dataframe)
def get_a_cool_gamepad_visual_from_df(df,title,path_visual):  
    stylecloud.gen_stylecloud(text=df.loc[df["title"] == f"{title}"]["review"].values[0],
                              icon_name='fas fa-gamepad',
                              colors=['#ffdb4d', '#ff0000', '#e74c3c'],
                              background_color='black',
                              output_name = f"{path_visual}")
    return Image(filename=f"{path_visual}")