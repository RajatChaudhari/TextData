# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:12:11 2018

@author: rajat13440
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from socket import timeout
import http
import gc
import nltk
import unicodedata
import re

summaryDict={}

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/words')
except LookupError:
     nltk.download('words')

#try:
#    nltk.data.find('sentiment/vader_lexicon')
#except LookupError:
#    nltk.download('vader_lexicon')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

#try:
#    nltk.data.find('tokenizers/punkt')
#except LookupError:
#    nltk.download('wordnet')

#class ProcessData:
#    
#    def __init__(self,x):
#        
#        self.GetSentenceTokens(x)
#        self.Normalize(x)

class Extract:
    def GetText(self,link):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        try:
            req = Request(link, headers=headers)
            with urlopen(req) as response:
                page = response.read()
                soup=BeautifulSoup(page, 'html.parser')
                ptag=soup.find_all('p')
                ''' Analysis
                 #if len(ptag)<5:
                  #print("VERY LOW P TAGS, STUDY THIS - %s - %d" %(link, len(ptag)))
                  #texta=link + "  **VERY LOW P TAGS, STUDY THIS " '''
            text=[]
            for tag in ptag:
                text.append(tag.get_text())
                texta=str(' '.join(text)).replace('\n',' ')

            #print("processed {} {} \n".format(link,b))
            #b+=1
        except http.client.IncompleteRead:
            #print("INCOMPLETE READ - {}".format(link))
            texta="ERROR: "+link + "  **INCOMPLETE READ"
        except WindowsError as e:
            #print("WINDOWS ERROR {} {}".format(e,link))
            texta="ERROR: "+link + "  **WINDOWS ERROR {}".format(e)
        except BaseException as error:
            #print("SOME OTHER ERROR {}".format(link))
            texta="ERROR: "+link + "  **SOME OTHER ERROR  {}".format(error)
        except timeout:
            #print("LINK {} TIMED OUT \n".format(link))
            #timedout.append(link)
            texta="ERROR: "+link + "  **TIMED OUT"
        del text,headers
        gc.collect    
        return texta
    
    def _Frequency(self,wordslist):
        trimmeddictlist=[]
        freq={}
        for word in wordslist:
            freq[word]=wordslist.count(word)
            # gets only those words which are frequent than mean word frequency of that text
            trimmedfreq={k:v for (k,v) in freq.items() if v >(float(sum(freq.values())) / len(freq))}    
            trimmeddictlist.append(trimmedfreq)
        return trimmedfreq

    def Summary(self,article):
        #article=GetText(url)
        percent=(20/100)
        sentokens=self.GetSentenceTokens(article)
        tokens=self.Normalize(article)
        freqlist=self._Frequency(tokens)
        #sentencerank=[]
        sentf={}
        for sentence in sentokens:
            msentence=sentence.lower().split(' ')
            a=0
            for word in freqlist:
                if word.lower() in msentence:
                    a+=1
                    sentf[sentence]=a
        slength=percent*len(sentokens)
        sorteddict=sorted(sentf, key=sentf.get, reverse=True)[:int(slength)]
        #sentencerank.append(sorteddict)
    
        summary=str(' '.join(sorteddict))
        return summary
    

        
    def GetSentenceTokens(self,x):
        y=nltk.sent_tokenize(x)
        return y    
        
    def _remove_stopwords(self,words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in nltk.corpus.stopwords.words('english'):
                new_words.append(word)
        return new_words
    
    def _lower(self,x):
        norm=[word.lower() for word in x]
        return norm

    def _remove_non_ascii(self,words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words

    def _remove_punctuation(self,words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words

    def Normalize(self,x):
        x1=nltk.word_tokenize(x)
        x2=self._remove_stopwords(x1)
        x3=self._remove_punctuation(x2)
        x4=self._remove_non_ascii(x3)
        x5=self._lower(x4)
        return x5
    
    def Summarize(self,url):
        import pandas as pd
        import datetime
        #import csv
        import numpy as np
        import time
        starttime=time.time()
        exclude=['twitter','glassdoor','youtube','wordpress','facebook','wikipedia','play.google','nasdaq']
        startTime_Main = datetime.datetime.now().strftime('%H:%M:%S')
        summarylist=[]
        summary1=""
        #print("---START TIME %s ---" % startTime_Main)
        if any (s in url for s in exclude):
            #print("Not allowed -",url)
            summary1="Not Allowed {}".format(url)
        else:
            try:
                article=self.GetText(url)
            except BaseException as e:
                article="ERROR {} {}".format(e,url)
            
            if not article.startswith("ERROR"):
                print("fetching summary for - ",url)
                summary1=self.Summary(article)
            else:
                summary1=article
        
        summaryDict[url]=summary1
        #print("{:.2f}".format((time.time()-starttime)))
        return summary1
        