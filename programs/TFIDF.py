# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:18:59 2018

@author: rajat13440
"""
#import pandas as pd
#import numpy as np
import nltk
import math

#import string, unicodedata
#import contractions
#import inflect

#from nltk.corpus import stopwords
#from nltk.stem import LancasterStemmer, WordNetLemmatizer
#pd.set_option('display.max_colwidth',1000)
#pd.set_option('display.max_columns', None)

class TFIDF:
    def tf(self,data,filename):
        fd=nltk.FreqDist(data[filename])
        return fd

    def idf(self,data,term):
        count=[term in row for row in data]
        inv_feq=math.log(len(count)/sum(count))
        return inv_feq

    def tfidf(self,data,row,n):
        term_scores={}
        file_fd=self.tf(data,row)
        for term in file_fd:
            print(term)
            if term.isalpha():
                idf_val=self.idf(data,term)
                tf_val=self.tf(data,row)[term]
                tfidf_val=tf_val*idf_val
                term_scores[term]=round(tfidf_val,2)
        return sorted(term_scores.items(),key=lambda x:-x[1])[:n]
    
    '''
    mylist=[]
    for index, row in articles.iterrows():
    mylist.append(tfidf2(articles["NormTokens"],index,5))
    '''