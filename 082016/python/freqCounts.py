# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:21:34 2016

@author: agoswami
"""

import pandas as pd
import numpy as np
from collections import defaultdict
from collections import Counter
from scipy.stats import itemfreq

mylist = [1,1,1,2,2,2,5,25,1,1]

#using python collections: Counter and Defaultdict
c = Counter(mylist)
print(c)

d = defaultdict(int)
for item in mylist:
    d[item] += 1
    
print(d)

# numpy : Usage 1. using numpy.unique, with return_counts argument
x = np.array([1,1,1,2,2,2,5,25,1,1])
unique, counts = np.unique(x, return_counts=True)
print(np.asarray((unique, counts)).T)

# numpy : Usage 2. using methods bincount, nonzero, zip / vstack
x = np.array([1,1,1,2,2,2,5,25,1,1])
y = np.bincount(x)
ii = np.nonzero(y)[0]

fc = zip(ii,y[ii]) # [(1, 5), (2, 3), (5, 1), (25, 1)]
for item in fc:
    print(item)
    
np.vstack((ii,y[ii])).T

#using pandas
s = pd.Series(mylist)
s2 = s.value_counts()
print(s2)

#Using Scipy
itemfreq(mylist)
