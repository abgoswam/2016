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

fare_ceiling = 40
data[data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size
number_of_classes = len(np.unique(data[0::,2]))

survival_table = np.zeros([2, number_of_classes, number_of_price_brackets], float)

for i in xrange(number_of_classes):
    for j in xrange(number_of_price_brackets):
        women_only_stats = data[ (data[0::,4] == "female") \
                                 & (data[0::,2].astype(np.float) == i+1 ) \
                                 & (data[0::,9].astype(np.float) >= j * fare_bracket_size) \
                                 & (data[0::,9].astype(np.float) < (j+1) * fare_bracket_size), 1]
                                 
        men_only_stats = data[ (data[0::,4] != "female") \
                                 & (data[0::,2].astype(np.float) == i+1 ) \
                                 & (data[0::,9].astype(np.float) >= j * fare_bracket_size) \
                                 & (data[0::,9].astype(np.float) < (j+1) * fare_bracket_size), 1]

                                 
        survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))
        survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))
        
        print women_only_stats
        print men_only_stats
        print "{0}:{1}:{2}:{3}".format(i, j, survival_table[0,i,j], survival_table[1,i,j])        
        
survival_table[ survival_table != survival_table ] = 0.        
survival_table[survival_table < 0.5] = 0
survival_table[survival_table >= 0.5] = 1

train_file.close()

#lets now work with the test file
test_file = open(r'F:\aghackerreborn\datasets\MLdatasets\titanic_test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

prediction_file = open("genderclasspricebasedmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)
prediction_file_object.writerow(["PassengerId", "Survived"])

# First thing to do is bin up the price file
for row in test_file_object:
    print row    
    for j in xrange(number_of_price_brackets):
        # If there is no fare then place the price of the ticket according to class
        try:
            row[8] = float(row[8])    # No fare recorded will come up as a string so
                                      # try to make it a float
        except:                       # If fails then just bin the fare according to the class
            bin_fare = 3 - float(row[1])
            break                     # Break from the loop and move to the next row
        if row[8] > fare_ceiling:     # Otherwise now test to see if it is higher
                                      # than the fare ceiling we set earlier
            bin_fare = number_of_price_brackets - 1
            break                     # And then break to the next row

        if row[8] >= j*fare_bracket_size\
            and row[8] < (j+1)*fare_bracket_size:     # If passed these tests then loop through
                                                      # each bin until you find the right one
                                                      # append it to the bin_fare
                                                      # and move to the next loop
            bin_fare = j
            break
        # Now I have the binned fare, passenger class, and whether female or male, we can
        # just cross ref their details with our survival table
    if row[3] == 'female':
        print "{0},{1},{2}".format(row[1], 
            bin_fare, 
            survival_table[ 1, float(row[1]) - 1, bin_fare])
            
        prediction_file_object.writerow([row[0], "%d" % int(survival_table[ 0, float(row[1]) - 1, bin_fare ])])
    else:
        print "{0},{1},{2}".format(row[1], 
            bin_fare, 
            survival_table[ 1, float(row[1]) - 1, bin_fare])
            
        prediction_file_object.writerow([row[0], "%d" % int(survival_table[ 1, float(row[1]) - 1, bin_fare])])



# Close out the files
test_file.close()
prediction_file.close()

