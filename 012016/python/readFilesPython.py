# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:06:55 2016

@author: agoswami
"""

filename = r'E:\hackerreborn\012016\_resources\coffee.csv'

with open(filename, 'rb') as f:
    line = f.read()
    print line

#Python’s “readlines” reads everything in the text file and has them in a list of lines. 
#Here is how to use Python’s “readlines”
with open(filename, 'rb') as f:
    lines = f.readlines()
    print lines

print "-------------"
    
#A better way to read a text file that is memory-friendly is to read the file line by line, that is one line at a time. 
#Python has (at least) two ways to read a text file line by line easily.    
with open(filename, 'rb') as f:
    line = f.readline()
    
    ## If the file is not empty keep reading line one at a time
    ## till the file is empty
    while line:
        print line
        line = f.readline()

print "-------------"
  
#One can also use an iterator to read a text file one line at time.        
with open(filename, 'rb') as f:
    for line in f:
        print line
    
print "-------------"

#CSV
import csv
with open(filename, 'rb') as f:
    header = f.readline().strip()
    print header
    
    line1 = f.next().strip()
    print "line1 : {0}".format(line1)
    
#    creaating the csv reader
    csvreader = csv.reader(f)

    line2 = csvreader.next()
    print "line2 : {0}".format(line2)
    
#    iterate over the csvreader
    for line in csvreader:
        print line
        
print "-"*40

import pandas as pd
df = pd.read_csv(filename)