# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:25:49 2018

@author: rajat13440
"""

import pandas as pd
#import nltk
#import contractions
#import inflect

pd.set_option('display.max_colwidth',1000)
pd.set_option('display.max_columns', None)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
pos_word_list=[]
neg_word_list=[]
neu_word_list=[]

def GetSentiment(text):
    temp=[]
    ncount=0
    pcount=0
    for word in text:
    
        if (sid.polarity_scores(word)['compound']) >= 0.5:
            pcount+=1
            if word not in pos_word_list:
                pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.5:
            ncount+=1
            if word not in neg_word_list:
                neg_word_list.append(word)
        else:
            if word not in neu_word_list: 
                neu_word_list.append(word)
    if(pcount>0 and ncount==0):
        temp.append(1)
    elif(ncount%2>0):
        temp.append(-1)
    elif(ncount%2==0 and ncount==0):
        temp.append(1)
    else:
        temp.append(0)            
    #sentiment="Pos: "+ str(pcount) +" Neg: "+ str(ncount) #unused
    return temp[0]

'''#articles["Sentiments"]=articles["NormTokens"].apply(lambda x:GetSentiment(x))'''