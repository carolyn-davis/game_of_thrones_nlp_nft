#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:41:32 2021

@author: carolyndavis
"""
import wordcloud as wc
import numpy as np ## Linear ALgebra
import pandas as pd ## For working with data
import plotly.express as px ## Visualization
import plotly.graph_objects as go ## Visualization
import matplotlib.pyplot as plt ## Visualization
import plotly as py ## Visualization
from wordcloud import WordCloud, STOPWORDS ## To create word clouds from script
import os



# =============================================================================
# Reading in the data
# =============================================================================

df = pd.read_csv('Game_of_Thrones_Script.csv')

df.shape

df.isnull().sum()



#there are 3 nulls so its cool to drop
df.dropna(inplace=True) 


# =============================================================================
# Grabbing the Dialogues
# =============================================================================

#first looking at the comparison of dialogue counts across the 8 seasons

#grabs the count groups of dialogue for each season
# dialogue_count = df['Season'].value_counts().reset_index()

# #renames the columns in the new df
# dialogue_count.columns=['Season', 'Counts']


# #sorts the seasons in ascending order
# dialogue_count.sort_values(by='Season', inplace=True)

# #visualizing the dialogue accounts for each season
# px.bar(dialogue_count, 'Season', 'Counts', title='Total Dialogue Counts Per Season.')

# =============================================================================
# Dialogue Grabs for Each Character 
# =============================================================================
# daenerys_targaryen = df[df['Name']=='daenerys targaryen']
# wordcloud = WordCloud(stopwords=STOPWORDS, min_font_size=10, background_color ='white', max_words=500).generate(
#     ' '.join(i for i in daenerys_targaryen['Sentence']))
# plt.figure(figsize = (10, 8), facecolor = None) 
# plt.imshow(wordcloud) 
# plt.axis("off") 
# # plt.tight_layout(pad = 0) 
# plt.show() 

df.Name.value_counts(normalize = True)
test = df[df['Name']=='daenerys targaryen']
test1= df[df['Sentence']].copy()

import nltk
import unicodedata
import re


def clean(text):
    '''Simplified text cleaning function'''
    text = text1
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return re.sub(r"[^a-z0-9\s]", '', text)

all_words = clean(' '.join(df.Sentence))



# Define the function to remove the punctuation
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text
# Apply to the DF series
text1['Sentence'] =text1.Sentence.apply(remove_punctuations)