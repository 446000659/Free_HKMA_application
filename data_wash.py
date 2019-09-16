#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:53:54 2019

@author: carol-cy
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

text = pd.read_csv('hkma_url.csv',dtype = 'str')
text.columns = ['Section','Sub-Category','Index','Numbering','Title','API_URL','Structure-type','Sub-Categry_cn','Title_cn']

urllist=text['API_URL']
filelist=text['Numbering']
filetitle=text['Title']
n=len(filelist)

def getattrlist(a,b):    
    """
    在(a,b-1)的范围内，获取这一范围内所有csv的表头，输出单个list（排重）
    通常默认a=0,b=n
    """
    
    attr_list=[]
    attr_duplicate=[]
    for num in range(a,b):
        file=filelist[num]
        data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
        data_attri=data.columns[1:]
        for item in data_attri:            
            """attr_list.append(item) """           
            if item not in attr_list:
                attr_list.append(item)
            else:
                attr_duplicate.append(item+' in '+file+'('+str(num)+')')
           
    return attr_list

def getattrduplicate(a,b):    
    """
    在(a,b-1)的范围内，获取这一范围内所有csv的表头，输出所有重复column
    通常默认a=0,b=n
    """
    
    attr_list=[]
    attr_duplicate=[]
    for num in range(a,b):
        file=filelist[num]
        data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
        data_attri=data.columns[1:]
        for item in data_attri:            
            """attr_list.append(item) """           
            if item not in attr_list:
                attr_list.append(item)
            else:
                attr_duplicate.append(item+' in '+file+'['+str(num)+']')
           
    return attr_duplicate

def gettime(a,b):    
    """
    在(a,b-1)的范围内，获取这一范围内所有csv的表头，返回所有以’end of month'为时间索引的csv
    通常默认a=0,b=n
    """
    
    time_tf_list=[]
    time_miss_list=[]
    for num in range(a,b):
        file=filelist[num]
        data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
        data_attri=data.columns[1:]
        time1='end_of_month'
        if time1 in data_attri:
            time_tf_list.append(num)
        else:
            time_miss_list.append(num)
           
    return time_tf_list

def gettimemiss(a,b):    
    """
    在(a,b-1)的范围内，获取这一范围内所有csv的表头，返回所有以’end of month'为时间索引的csv
    通常默认a=0,b=n
    """
    
    time_tf_list=[]
    time_miss_list=[]
    for num in range(a,b):
        file=filelist[num]
        data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
        data_attri=data.columns[1:]
        time1='end_of_month'
        if time1 in data_attri:
            time_tf_list.append(num)
        else:
            time_miss_list.append(num)
           
    return time_miss_list

def findattr(str):
    """
    在全部csv范围内，获取所有具有这一表头的位置并打印
    """
    locator=[]
    for num in range(0,130):
        file=filelist[num]
        data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
        data_attri=data.columns[1:]
        if str in data_attri:
            locator.append('found in '+ file+'.csv')
    return locator      

asstl=findattr('asst_negodebt_gov_fc')    
print()   
    
"""
def getattrivalue(attr_list,a,b):
    
    在（a,b)的范围内，获取这一范围内所有csv对表头的响应，1，0表达
    默认，attr_list,0,n

    attr_value=[]
    attr_list=getattrlist(a,b)
    return attr_list
    for num in range(a,b):
        file=filelist[num]
        data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
        for item in data:
            if item attr_list.append(0)
        else:
"""
duplicate=getattrduplicate(0,130)