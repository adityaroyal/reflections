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
data= np.array(data)
number_of_passengers=np.size(data[0::,1].astype(np.float))
number_survived=np.sum(data[0::,1].astype(np.float))
proportion=number_survived/number_of_passengers
women=data[0::,4]=='female'
men=data[0::,4]=='male'
women_on_board=data[women,1].astype(np.float)
men_on_board=data[men,1].astype(np.float)
women_survived=np.sum(women_on_board)/np.size(women_on_board)
men_survived=np.sum(men_on_board)/np.size(men_on_board)
prediction_file_object=csv.writer(open('genderbasedmodel.csv','wb'))
prediction_file_object.writerow(["passengerid","surviverid"])
test_file_object=csv.reader(open('test.csv','rb'))
for row in test_file_object:
    if row[3]=='female':
        prediction_file_object.writerow([row[0],'1'])
    else:
        prediction_file_object.writerow([row[0],'0'])