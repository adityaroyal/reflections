# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:26:44 2016

@author: aditya royal
"""

import pandas as pd
import numpy as np
df = pd.read_csv('train.csv',header=0)
df['Age'][0:10]
print df['Age']
df[df['Age']>60][['Sex','Pclass','Age','Survived']]
print df[df['Age'].isnull()][['Sex','Pclass','Age']]
for i in range(1,4):
    print i, len(df[(df['Sex']=='male')&(df['Pclass']==i)])
df['Gender']=4
print df[df['Sex']=="female"]['Sex'].map(lambda x: x[0].upper())
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
median_ages=np.zeros((2,3))
print median_ages
for i in range(0,2):
    for j in range(0,3):
        ages=df[(df['Gender']==i)&(df['Pclass']==j+1)]['Age'].dropna()
        median_ages[i,j]=ages.median()
print median_ages
df['Agefill']=df['Age']
print df[df['Age'].isnull()][['Gender','Pclass','Age','Agefill']].head(10)
for i in range(0,2):
    for j in range(0,3):
        df.loc[(df['Age'].isnull())&(df['Gender']==i)&(df['Pclass']==j+1),'Agefill']=median_ages[i,j]
#print df[df['Agefill'].isnull()][['Gender','Pclass','Age','Agefill']].head(10)
df['FamilySize']=df['SibSp']+df['Parch']
df['Age*class']=df['Agefill']*df['Pclass']
import pylab as p
print df['Age*class'].hist()
p.show()
print df.dtypes[df.dtypes=='object']