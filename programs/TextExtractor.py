# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 15:08:09 2018

@author: rajat13440
"""

from bs4 import BeautifulSoup
import urllib.request

def GetText(link):
    
    try:
        with urllib.request.urlopen(link) as response:
            page = response.read()
        soup=BeautifulSoup(page, 'html.parser')
        ptag=soup.find_all('p')
        text=[]
        for tag in ptag:
            text.append(tag.get_text())
        texta=str(' '.join(text)).replace('\n',' ')
    except:
        print("error opening this link - %s, try accessing manually.", link)
        texta=['error','while','fetching','link']        
    
    return texta