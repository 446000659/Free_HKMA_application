#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:36:30 2019

@author: carol-cy
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

text = pd.read_csv('hkma_url.csv',dtype = 'str')
text.columns = ['Section','Sub-Category','Index','Numbering','Title','API_URL','Structure-type','Sub-Categry_cn','Title_cn']

urllist=text['API_URL']
filelist=text['Numbering']
filetitle=text['Title']
time_str_other=gettimemiss(0,130)


def savepic_month(n):
    """
    input a n number, it returns a set of pics saved and print done.
    适用end_of_month
    """
    file=filelist[n]
    data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
    data_attri=data.columns[1:]
    cols=len(data_attri)
    
    for num in range(0,cols):
        title = filetitle[n]+'\n'+str(num)+' - '+data_attri[num]
        x=data['end_of_month']
        y=data[data_attri[num]]
        plt.plot(x, y, 'b')
        plt.axis(fontsize=9)
        plt.locator_params(nbins=13)
        plt.title(title)
        plt.xticks(rotation=30)
        plt.savefig('img20190908214300/'+file+'_chart_'+str(num)+'.png')
        plt.show()
    return print('done'+str(n))

def savepic_day(n):
    """
    input a n number, it returns a set of pics saved and print done.
    适用end_of_day
    """
    file=filelist[n]
    data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
    data_attri=data.columns[1:]
    cols=len(data_attri)
    
    for num in range(0,cols):
        title = filetitle[n]+'\n'+str(num)+' - ' + data_attri[num]
        x=data['end_of_day']
        y=data[data_attri[num]]
        plt.plot(x, y, 'b')
        plt.axis(fontsize=9)
        plt.locator_params(nbins=31)
        plt.title(title)
        plt.xticks(rotation=90)
        plt.savefig('img20190908214300/'+file+'_chart_'+str(num)+'.png')
        plt.show()
    return print('done'+str(n))



def savepic_quarter(n):
    """
    input a n number, it returns a set of pics saved and print done.
    适用end_of_quarter
    """
    file=filelist[n]
    data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
    data_attri=data.columns[1:]
    cols=len(data_attri)
    
    for num in range(0,cols):
        title = filetitle[n]+'\n'+'Factor'+str(num)+' - '+data_attri[num]
        print(title)
        print(data)
        x=data['end_of_quarter']
        y=data[data_attri[num]]
        plt.plot(x, y, 'b')
        plt.axis(fontsize=9)
        plt.locator_params(nbins=5)
        plt.title(title)
        plt.xticks(rotation=30)
        plt.savefig('img20190908214300/'+file+'_chart_'+str(num)+'.png')
        plt.show()
    return print('done'+str(n))

def savepic_string(n,time_str,h):
    """
    input a n number, it returns a set of pics saved and print done.
    使用录入的t_str进行索引
    """
    file=filelist[n]
    data = pd.read_csv('csv20190903125300/'+file+'.csv',dtype='str')
    data_attri=data.columns[1:]
    cols=len(data_attri)
    
    for num in range(0,cols):
        title = filetitle[n]+'\n'+str(num)+' - '+data_attri[num]
        x=data[time_str]
        y=data[data_attri[num]]
        plt.plot(x, y, 'b')
        plt.axis(fontsize=9)
        plt.locator_params(nbins=h+1)
        plt.title(title)
        plt.xticks(rotation=90)
        plt.savefig('img20190908214300/'+file+'_chart_'+str(num)+'.png')
        plt.show()
    return print('done'+str(n))
"""
def export(a,b,time_str_other):
    输出(a,b)之间的所有图表
    
    for num in range(a,b):
        if num in time_str_other:
            print('exception'+str(num))
        else:
            savepic_month(num)
    return print('done'+ str(a) +'-'+ str(b))
"""
def exportothers(n):
    """输出其他类型的图表，每次一个,n必须为整数"""
    stringlist=[120,121,122,123,125]
    issue_datelist=[70,71,118,124]
    quarterlist=[26,62]
    daylist=[69,85,88,91,97,99,102,117]
    datelist=[126,127,129]
    otherlist=[119,128,92]
    if n in otherlist:
        if n==119:
            savepic_string(n,'expected_maturity_date',30)
        elif n==128:
            savepic_string(n,'end_date',30)
        else:
            """n==92"""
            savepic_string(n,'effect_day',30)            
    if n in stringlist:
        print('not fit for diagram')    
    if n in quarterlist:
        savepic_quarter(n)
    if n in daylist:
        savepic_day(n)
    if n in datelist:
        savepic_string(n,'date',30)
    if n in issue_datelist:
        savepic_string(n,'issue_date',30)
        
export(0,130,time_str_other)  

for num in time_str_other:
    exportothers(num)