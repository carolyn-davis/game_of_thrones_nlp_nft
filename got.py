#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:41:32 2021

@author: carolyndavis
"""


# =============================================================================
# Imports Utilized
# =============================================================================
import wordcloud as wc
import numpy as np ## Linear ALgebra
import pandas as pd ## For working with data
import plotly.express as px ## Visualization
import plotly.graph_objects as go ## Visualization
import matplotlib.pyplot as plt ## Visualization
import plotly as py ## Visualization
from wordcloud import WordCloud, STOPWORDS ## To create word clouds from script
import os
import io
from io import StringIO

from PIL import Image

# =============================================================================
# Reading in the data
# =============================================================================

df = pd.read_csv('Game_of_Thrones_Script.csv')

df.shape

df.isnull().sum()



#there are 3 nulls so its cool to drop
df.dropna(inplace=True) 

# =============================================================================
# Removing the Punctuation
# =============================================================================


#Need to remove thepunctuation for real semantic analysis...
df["Sentence"] = df['Sentence'].str.replace('[^\w\s]','')
df.head()

# =============================================================================
# Getting all the rows together for each designated character
# =============================================================================
# word_seperator = df.Sentence.str.cat(sep=' ')
#test worked now all words are divided correctly

# =============================================================================
# #Looking at the characters present in the data 
# =============================================================================
df.Name.value_counts().head(50)
#Takeaway:
    #over 50 total characters possibly more, so lets focus on prominent
    #protagonists and antagonists in the series 

# =============================================================================
# Characters Chosen--------------
# =============================================================================

# tyrion lannister      1760
# jon snow              1133
# daenerys targaryen    1048
# cersei lannister      1005
# jaime lannister        945
# sansa stark            784
# arya stark             783

# =============================================================================
# Grabbing the Dialogues
# =============================================================================
#Make new dfs for each characters relevant dialogue in the script data



# =============================================================================
# Tyrion Lannister 
# =============================================================================
tyrion_lannister = df[df['Name']=='tyrion lannister']

wordcloud = WordCloud(stopwords=STOPWORDS,background_color ='white',max_words=500,relative_scaling=0,collocations=True,colormap=('binary')).generate(
    ' '.join(i for i in tyrion_lannister['Sentence']))
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 
#Takeaways:
# TODO: ATP can only get the text to read in black/grey appearance with colormap->'binary'

# =============================================================================
# Jon Snow
# =============================================================================
jon_snow = df[df['Name']=='jon snow']

wordcloud = WordCloud(stopwords=STOPWORDS,background_color ='white',max_words=500,relative_scaling=0,collocations=True,colormap=('binary')).generate(
    ' '.join(i for i in jon_snow['Sentence']))
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 

# =============================================================================
# Daenerys Targaryen 
# =============================================================================

daenerys_targaryen = df[df['Name']=='daenerys targaryen']

wordcloud = WordCloud(stopwords=STOPWORDS,background_color ='white',max_words=500,relative_scaling=0,collocations=True,colormap=('binary')).generate(
    ' '.join(i for i in daenerys_targaryen['Sentence']))
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 


# =============================================================================
# cersei lannister
# =============================================================================
cersei_lannister = df[df['Name']=='cersei lannister']

wordcloud = WordCloud(stopwords=STOPWORDS,background_color ='white',max_words=500,relative_scaling=0,collocations=True,colormap=('binary')).generate(
    ' '.join(i for i in cersei_lannister['Sentence']))
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 


# =============================================================================
# jaime lannister 
# =============================================================================
jaime_lannister = df[df['Name']=='jaime lannister']

wordcloud = WordCloud(stopwords=STOPWORDS,background_color ='white',max_words=500,relative_scaling=0,collocations=True,colormap=('binary')).generate(
    ' '.join(i for i in jaime_lannister['Sentence']))
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 

# =============================================================================
# sansa stark
# =============================================================================
sansa_stark = df[df['Name']=='sansa stark']

wordcloud = WordCloud(stopwords=STOPWORDS,background_color ='white',max_words=500,relative_scaling=0,collocations=True,colormap=('binary')).generate(
    ' '.join(i for i in sansa_stark['Sentence']))
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 


# =============================================================================
#  arya stark
# =============================================================================
arya_stark = df[df['Name']=='arya stark']

wordcloud = WordCloud(stopwords=STOPWORDS,background_color ='white',max_words=500,relative_scaling=0,collocations=True,colormap=('binary')).generate(
    ' '.join(i for i in arya_stark['Sentence']))
# specify the custom font to use
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show() 


# =============================================================================
# Creating the Mask 
# =============================================================================
# Create an array from the image you want to use as a mask
## Your file path will look different

import cv2   #image reader import
image = cv2.imread("/Users/carolyndavis/Desktop/Side-Projects/game_of_thrones_nlp_nft/snatch.jpg")


# =============================================================================
# path!!!!
# =============================================================================
# /Users/carolyndavis/Desktop/Side-Projects/game_of_thrones_nlp_nft/dan.jpeg


# =============================================================================
# Testing the Mask on Danaerys
# =============================================================================

wordcloud = WordCloud(background_color='black', mask=image,mode="RGB",color_func=lambda *args,**kwargs: "white", 
width=1000 , max_words=1500, height=1000, random_state=1,relative_scaling=0,collocations=True).generate(' '.join(i for i in daenerys_targaryen['Sentence']))
plt.figure(figsize = (25, 25)) 
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.axis("off")
plt.show() 

