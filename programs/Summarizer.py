# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:35:11 2018

@author: rajat13440
"""

from URLExtractor import GetData
from TextExtractor import GetText
from SentenceRank import Summary
import pandas as pd
import datetime
import csv
import numpy as np
import pyodbc
import time

def Summarize():
    
    
    #import numpy as np
    server = 
    database = 
    username =
    password = 
    driver= 
    
    exclude=['twitter','glassdoor','youtube','wordpress','facebook','wikipedia','play.google','nasdaq']
    startTime_Main = datetime.datetime.now().strftime('%H:%M:%S')
    urls=GetData()
    notallowed=[]
    summarylist=[]
    summaryDict={}
    print("---START TIME %s ---" % startTime_Main)
    a=0
    for url in urls:
        a+=1
        if any (s in url[1] for s in exclude):
            #print("Not allowed -",url)
            notallowed.append(url)
        else:
            try:
                article=GetText(url[1])
            except:
                continue
            if not article.startswith("ERROR"):
                print("fetching summary for - ",url[1])
                summary=Summary(article)
            else:
                summary=article

            pdate=datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            suma=summary.replace('\'',' ')
            cs='DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
            cnInsert = pyodbc.connect(cs, autocommit=True)
            cursor1 = cnInsert.cursor()
            print(pdate)
            cursor1.execute("insert ProspectSummary(Summary,url,PROSPECTDATAID) values('"+str(suma)+"','"+str(url[1])+"','"+str(url[0])+"');")
            cursor1.execute("update ProspectData set IsProcessed='True', DATAPROCESSEDDATE='"+pdate+"' WHERE ID='"+str(url[0])+"';")
            
            summarylist.append(summary)
            summaryDict[url]=summary
            #print(a)
            print("---TIME %s ---" % (datetime.datetime.now().strftime('%H:%M:%S')))
            
    try:            
        df=pd.DataFrame(summaryDict,columns=["URL","SUMMARY"])
        df.to_csv("SummariesD11.csv",sep=',',encoding='utf-8',index=None)
    except:
        print("cant save")
    try:    
        np.savetxt("file_name11.csv", summarylist, delimiter=",", fmt='%s')    
    except:
        print("cant save file using np")
    try:    
        np.savetxt("notallowed.csv", notallowed, delimiter=",", fmt='%s')
    except:
        print("cant save not allowed using np")
        
    df=pd.DataFrame(summaryDict,columns=["URL","SUMMARY"])
    try: 
        with open('Summaries.csv', 'w',encoding='utf-8') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(summarylist)
    except:
        print("csv write not working")
        
        
    print("FINAL TIME --- %s  START TIME %s ---" % (datetime.datetime.now().strftime('%H:%M:%S') % startTime_Main))
    #del df
    return summarylist,summaryDict