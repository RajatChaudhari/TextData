# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:35:11 2018

@author: rajat13440
"""

class Summerization:
    
    def __init__(self,x,x1):
        self.Summerize(x,x1)
    '''# This method will call a function to process data from another class and
    pass it on to other function'''    
    def WordFrequency():
        t=ProcessData()
        NormTokens=t.
        dictlist=[]
        trimmeddictlist=[]
        for wordslist in NormTokens:
            freq={}
            for word in wordslist:
                freq[word]=wordslist.count(word)
                trimmedfreq={k:v for (k,v) in freq.items() if v >(float(sum(freq.values())) / len(freq))}    
            dictlist.append(freq)
            trimmeddictlist.append(trimmedfreq)        