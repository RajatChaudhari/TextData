# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:21:09 2018

@author: rajat13440
"""
from ProcessData import GetSentenceTokens, Normalize
#from TextExtractor import GetText

def _Frequency(wordslist):
    trimmeddictlist=[]
    freq={}
    for word in wordslist:
        freq[word]=wordslist.count(word)
    # gets only those words which are frequent than mean word frequency of that text
    trimmedfreq={k:v for (k,v) in freq.items() if v >(float(sum(freq.values())) / len(freq))}    
    trimmeddictlist.append(trimmedfreq)
    return trimmeddictlist

def Summary(article):
    #article=GetText(url)
    percent=(20/100)
    sentokens=GetSentenceTokens(article)
    tokens=Normalize(article)
    freqlist=_Frequency(tokens)
    #sentencerank=[]
    sentf={}
    for sentence in sentokens:
        msentence=sentence.lower().split(' ')
        a=0
        for word in freqlist[0]:
            if word.lower() in msentence:
                a+=1
                sentf[sentence]=a
	
    slength=percent*len(sentokens)
    sorteddict=sorted(sentf, key=sentf.get, reverse=True)[:int(slength)]
    #sentencerank.append(sorteddict)
    
    summary=str(' '.join(sorteddict))
    return summary


                