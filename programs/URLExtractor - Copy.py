# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 16:31:12 2018

@author: rajat13440
"""

def GetData():
    import json
    import pyodbc
    
    server = ''
    database = ''
    username = ''
    password = ''
    driver= ''
    
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    
    cursor.execute("Select ProspectName,SearchResult from ProspectData")
    urllist=[]
    bunch=[]
    prospect=[]
    row = cursor.fetchone()
    while row:
        prospect.append(str(row[0]))
        bunch.append(str(row[1]))
        row = cursor.fetchone()
    
    for prospect in bunch:
        data=json.loads(prospect)
        for each in data:
            urllist.append(each['url'])
    
    return urllist