#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:18:10 2019

@author: carol-cy
"""

import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
import time

text = pd.read_csv('hkma_url.csv',dtype = 'str')
text.columns = ['Section','Sub-Category','Numbering','Title','API_URL','Sub-Categry_cn','Title_cn']

urllist=text['API_URL']
filelist=text['Numbering']
n=130
"""
def extractdata(url):
    resp=requests.get(url)
    data=resp.json()
    result=data['result']
    record=result['records']
    return(json_normalize(record))
    
for num in range(118,n):
    data=extractdata(urllist[num])
    print('done',num)
    exportfilename=filelist[num]+'.csv'
    data.to_csv(exportfilename,encoding='utf-8',index=True,header=True)
    print('export done',num)
    time.sleep(20)
"""
def extractjson(url):
    resp=requests.get(url)
    data=resp.json()
    result=data['result']
    record=result['records']
    return(record)

for num in range(0,1):
    data=extractjson(urllist[num])
    print('done',num)
    exportfilename=filelist[num]+'.json'
    data.to_csv(exportfilename,encoding='utf-8',index=True,header=True)
    print('export done',num)
    time.sleep(20)
