# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 14:05:29 2016

@author: agoswami

Code from here : https://www.kaggle.com/c/titanic/details/getting-started-with-python
"""

import csv as csv
import numpy as np

train_file = open(r'F:\aghackerreborn\datasets\MLdatasets\titanic_train.csv', 'rb')
train_file_object = csv.reader(train_file)
    
header = train_file_object.next()
data = []
for row in train_file_object:
    data.append(row)
    
data = np.array(data)

number_passengers = np.size(data[0::,1].astype(np.float))
num_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = num_survived / number_passengers
print "proportion survivors : {0}".format(proportion_survivors)


women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"
women_onboard = data[women_only_stats, 1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)


proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)   
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived 
train_file.close()


#work with test file now
test_file = open(r'F:\aghackerreborn\datasets\MLdatasets\titanic_test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

prediction_file = open("genderbasedmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[3] == 'female':
        prediction_file_object.writerow([row[0], '1'])
    else:
        prediction_file_object.writerow([row[0], '0'])
        
test_file.close()
prediction_file.close()