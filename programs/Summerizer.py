# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:35:11 2018

@author: rajat13440
"""

from URLExtractor import GetData
from SentenceRank import Summary
import pandas as pd
import time

def Summarize():
    start_time = time.time()
    urls=GetData()
    summarylist=[]
    for url in urls:
        try:
            summary=Summary(url)
            summarylist.append(summary)
        except:
            print("error url- ",url)
            continue            
    df=pd.DataFrame({'urls':urls,'summary':summarylist})
    df.to_csv("Summaries.csv",sep=',',encoding='utf-8',index=None)
    print("--- %s seconds ---" % (time.time() - start_time))