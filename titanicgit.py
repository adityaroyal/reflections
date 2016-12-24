# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:54:47 2016

@author: aditya royal
"""
import csv as csv
import numpy as np
csv_file_object=csv.reader(open('train.csv','rb'))
header=csv_file_object.next()
data=[]
for row in csv_file_object:
    data.append(row)
print np.array(data)