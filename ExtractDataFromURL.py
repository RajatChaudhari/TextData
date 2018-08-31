
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import re
import csv
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import math

import string, unicodedata
#import contractions
#import inflect

#from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
pd.set_option('display.max_colwidth',1000)
pd.set_option('display.max_columns', None) 


# In[2]:

#we can fetch this from a csv as well, so this need not be hard coded.
page=requests.get("http://www.dailymail.co.uk/sport/index.html")


# In[3]:


soup=BeautifulSoup(page.content, 'html.parser')
links=[a['href'].split('#')[0] for a in soup.find_all('a',attrs={'href':re.compile("^http://www.dailymail.co.uk/sport")})]


# In[4]:


len(links)


# In[5]:


sportsarticles=[]

for link in links:
    body=requests.get(link)
    article=BeautifulSoup(body.content,'html.parser')
    paras=article.find_all('p',class_="mol-para-with-font")
    if paras:
        one=[]
        for text in paras:
            one.append(text.get_text())
    sportsarticles.append(one)


# In[6]:


#removing nested list, converting each article as a big string instead
newlist=[]
for a in sportsarticles:
    b= ' '.join(a)
    newlist.append(b)


# In[7]:


#removing duplicate articles
final_list = []
for num in newlist:
    if num not in final_list:
        final_list.append(num)


# In[8]:


with open("articles8Aug.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in final_list:
        writer.writerow([val])