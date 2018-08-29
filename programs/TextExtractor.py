# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 15:08:09 2018

@author: rajat13440
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from socket import timeout
import http
import gc

def GetText(link):
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