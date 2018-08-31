# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 16:31:12 2018

@author: rajat13440
"""

def GetData():
    import json
    import pyodbc
    #import numpy as np
	server = ''
    database = ''
    username = ''
    password = ''
    driver= ''
    
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    
    cursor.execute("Select Id,ProspectName,SearchResult from ProspectData Where IsProcessed='False' and  BINGSEARCHUPDATES='True'")
    urllist=[]
    bunch=[]
    pid=[]
    row = cursor.fetchone()
    while row:
        bunch.append(str(row[2]))
        for prospect in bunch:
            data=json.loads(prospect)
        for each in data:
            urllist.append(each['url'])
            pid.append(row[0])
        row = cursor.fetchone()
   	 
    d=[]
    e=[]
    for c in zip(pid,urllist):
        if c[1] not in d:
            d.append(c[0])
            e.append(c[1])
    return zip(d,e)